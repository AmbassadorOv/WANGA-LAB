#!/usr/bin/env python3
"""Autonomous, review-deferred architecture integrator for WANGA-LAB.

Safety model:
- never pushes to main
- never deletes or disables source branches
- integrates only an explicit allowlist
- aborts a conflicting integration instead of guessing
- records every action as evidence
- reattempts previously conflicting sources on later runs
"""
from __future__ import annotations
import json, os, re, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "ARCHITECTURE_BUILD_MANIFEST.yml"
STATE = ROOT / "docs" / "AUTOBUILD_STATE.json"
BUILD_BRANCH = os.environ.get("BUILD_BRANCH", "autobuild/architecture-construction")

FOUNDATION_COMMITS = [
    "08723b895359eef5e20b04057bb447395827ed0e",
    "4247577198628e478e012255bc0c0db009c0aac1",
    "82a748d1113b8cc3bee6ab7a1fbae4453f3df3be",
    "3169eb854d1f92f45b08451d33bfd5529cd4d94f",
    "bdd9f33aa2eb1f433b5310dac0ab404c4963d315",
]

def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check)

def sh(*args: str) -> str:
    return run(*args).stdout.strip()

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def parse_sources(text: str):
    return re.findall(r"^\s*- id: ([^\n]+)\n\s+branch: ([^\n]+)\n\s+layer: ([^\n]+)", text, re.M)

def assert_build_branch():
    """Fail closed unless the builder is running on the dedicated build branch."""
    actual = sh("git", "branch", "--show-current")
    if actual != BUILD_BRANCH:
        raise SystemExit(
            f"refusing architecture build on unexpected branch: {actual!r}; expected {BUILD_BRANCH!r}"
        )
    if BUILD_BRANCH == "main":
        raise SystemExit("refusing architecture build on main")

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"build_branch": BUILD_BRANCH, "started_at": now(), "integrated": [], "conflicts": [], "foundation": [], "runs": []}

def save_state(state):
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def is_ancestor(commit: str) -> bool:
    return run("git", "merge-base", "--is-ancestor", commit, "HEAD", check=False).returncode == 0

def integrate_commit(commit: str, state):
    if is_ancestor(commit):
        if commit not in state["foundation"]:
            state["foundation"].append(commit)
        return "already-present"
    r = run("git", "cherry-pick", commit, check=False)
    if r.returncode:
        run("git", "cherry-pick", "--abort", check=False)
        state["conflicts"].append({"kind":"foundation", "ref":commit, "time":now(), "stderr":r.stderr[-3000:]})
        return "conflict"
    state["foundation"].append(commit)
    return "integrated"

def integrate_branch(item, state):
    bid, branch, layer = item
    run("git", "fetch", "origin", f"{branch}:refs/remotes/origin/{branch}", check=False)
    if run("git", "rev-parse", f"origin/{branch}", check=False).returncode:
        state["conflicts"].append({"kind":"missing-branch","id":bid,"branch":branch,"layer":layer,"time":now()})
        return "missing"
    if run("git", "merge-base", "--is-ancestor", f"origin/{branch}", "HEAD", check=False).returncode == 0:
        return "already-present"
    r = run("git", "merge", "--squash", f"origin/{branch}", check=False)
    if r.returncode:
        run("git", "merge", "--abort", check=False)
        state["conflicts"].append({"kind":"branch","id":bid,"branch":branch,"layer":layer,"time":now(),"stderr":r.stderr[-3000:]})
        return "conflict"
    run("git", "commit", "-m", f"autobuild: integrate {layer} / {bid}")
    state["integrated"].append({"id":bid,"branch":branch,"layer":layer,"time":now(),"sha":sh("git","rev-parse","HEAD")})
    return "integrated"

def write_wix_snapshot():
    text = MANIFEST.read_text(encoding="utf-8")
    names = re.findall(r"^\s+- name: ([^\n]+)\n\s+site_id: ([^\n]+)\n\s+role: ([^\n]+)\n\s+status: ([^\n]+)", text, re.M)
    snapshot = {
        "generated_at": now(),
        "source": "docs/ARCHITECTURE_BUILD_MANIFEST.yml",
        "purpose": "Wix publication/integration surfaces; GitHub remains source of code and architecture contracts.",
        "sites": [{"name":n,"site_id":sid,"role":role,"status":status} for n,sid,role,status in names],
    }
    (ROOT/"docs"/"WIX_ARCHITECTURE_SNAPSHOT.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False)+"\n", encoding="utf-8"
    )

def main():
    assert_build_branch()
    state = load_state()
    state["runs"].append({"started_at": now(), "head_before": sh("git","rev-parse","HEAD")})
    for c in FOUNDATION_COMMITS:
        integrate_commit(c, state)
    sources = parse_sources(MANIFEST.read_text(encoding="utf-8"))
    for item in sources:
        integrate_branch(item, state)
    write_wix_snapshot()
    state["runs"][-1]["head_after"] = sh("git","rev-parse","HEAD")
    state["runs"][-1]["working_tree"] = sh("git","status","--porcelain")
    save_state(state)
    print(json.dumps({
        "build_branch": BUILD_BRANCH,
        "head": sh("git","rev-parse","HEAD"),
        "integrated_count": len(state["integrated"]),
        "conflict_count": len(state["conflicts"]),
        "foundation_count": len(state["foundation"]),
    }, indent=2))

if __name__ == "__main__":
    main()
