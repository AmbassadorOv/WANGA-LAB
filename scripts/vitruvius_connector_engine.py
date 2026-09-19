#!/usr/bin/env python3
"""Vitruvius Connector Engine.

Discovers candidate architecture-compatible files across accessible GitHub repositories,
maps them to WANGA architecture nodes, and creates bounded integration proposals.

The engine NEVER merges automatically and NEVER copies protected Rational Logic
implementation. It creates a dedicated branch and pull request for each proposal.
"""

from __future__ import annotations
import argparse, base64, fnmatch, json, os, re
from dataclasses import dataclass
from urllib.parse import quote
from urllib.request import Request, urlopen

API = "https://api.github.com"
PROTECTED = ("rational-logic", "rational_logic", "wanga-native-rational-logic")


@dataclass
class Candidate:
    repo: str
    path: str
    html_url: str
    score: int
    architectures: list[str]
    reason: list[str]


def api(path: str, token: str, method: str = "GET", body=None):
    data = None if body is None else json.dumps(body).encode()
    req = Request(API + path, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def get_json(path: str, token: str):
    return api(path, token)


def search_code(query: str, token: str, per_page: int = 30):
    q = quote(query)
    return get_json(f"/search/code?q={q}&per_page={per_page}", token).get("items", [])


def get_file(repo: str, path: str, ref: str, token: str):
    p = quote(path, safe="/")
    return get_json(f"/repos/{repo}/contents/{p}?ref={quote(ref)}", token)


def protected(path: str) -> bool:
    x = path.lower()
    return any(p in x for p in PROTECTED)


def score(item: dict, architecture: dict) -> tuple[int, list[str]]:
    path = item.get("path", "").lower()
    name = item.get("name", "").lower()
    hay = f"{path} {name}"
    points, reasons = 0, []
    keywords = architecture.get("keywords", [])
    for kw in keywords:
        if kw.lower() in hay:
            points += 3
            reasons.append(f"keyword:{kw}")
    for pattern in architecture.get("file_patterns", []):
        if fnmatch.fnmatch(path, pattern.lower()):
            points += 5
            reasons.append(f"pattern:{pattern}")
    return points, reasons


def discover(architectures: list[dict], token: str, per_query: int):
    out = []
    for arch in architectures:
        for query in arch.get("search_queries", []):
            for item in search_code(query, token, per_query):
                repo = item.get("repository", {}).get("full_name", "")
                path = item.get("path", "")
                if not repo or not path or protected(path):
                    continue
                s, reasons = score(item, arch)
                if s:
                    out.append(Candidate(
                        repo, path, item.get("html_url", ""),
                        s, [arch["id"]], reasons
                    ))
    # Merge duplicate files and architecture matches.
    merged = {}
    for c in out:
        key = (c.repo, c.path)
        if key not in merged:
            merged[key] = c
        else:
            merged[key].score += c.score
            merged[key].architectures = sorted(set(merged[key].architectures + c.architectures))
            merged[key].reason = sorted(set(merged[key].reason + c.reason))
    return sorted(merged.values(), key=lambda x: (-x.score, x.repo, x.path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="vitruvius/CONNECTOR_ENGINE_MANIFEST_V1.json")
    ap.add_argument("--min-score", type=int, default=6)
    ap.add_argument("--per-query", type=int, default=10)
    ap.add_argument("--target-repo", default=os.getenv("GITHUB_REPOSITORY", "AmbassadorOv/WANGA-LAB"))
    ap.add_argument("--target-branch", default=os.getenv("GITHUB_BASE_REF", "main"))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--integrate", action="append", default=[], help="repo:path:target_path:architecture_id")
    ap.add_argument("--integration-branch", default="", help="Base branch for integration proposals")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required")

    manifest = json.load(open(args.manifest, encoding="utf-8"))
    candidates = [c for c in discover(manifest["architectures"], token, args.per_query)
                  if c.score >= args.min_score]

    report = {
        "engine": "VITRUVIUS_CONNECTOR_ENGINE",
        "mode": "write" if args.write else "dry-run",
        "target_repo": args.target_repo,
        "target_branch": args.target_branch,
        "candidate_count": len(candidates),
        "candidates": [c.__dict__ for c in candidates],
        "rules": {
            "auto_merge": False,
            "protected_implementation_copy": False,
            "promotion_to_verified": False,
            "integration_requires_pull_request": True,
        },
    }

    os.makedirs("vitruvius", exist_ok=True)
    with open("vitruvius/CONNECTOR_DISCOVERY_REPORT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    if not args.write:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    integrations = []
    for spec in args.integrate:
        parts = spec.split(":", 3)
        if len(parts) != 4:
            raise SystemExit("Integration format: repo:path:target_path:architecture_id")
        src_repo, src_path, target_path, arch_id = parts
        if protected(src_path) or protected(target_path):
            raise SystemExit("Protected implementation cannot be copied")
        repo_meta = get_json(f"/repos/{src_repo}", token)
        src_ref = repo_meta["default_branch"]
        source = get_file(src_repo, src_path, src_ref, token)
        if not isinstance(source, dict) or "content" not in source:
            raise SystemExit(f"Source file not readable: {src_repo}:{src_path}")
        content = base64.b64decode(source["content"]).decode("utf-8")
        base = args.integration_branch or args.target_branch
        suffix = re.sub(r"[^a-z0-9-]+", "-", f"{arch_id}-{src_repo.split('/')[-1]}-{src_path.split('/')[-1]}".lower()).strip("-")
        head = f"agent/vitruvius/integrate-{suffix}"[:120]
        base_ref = get_json(f"/repos/{args.target_repo}/git/ref/heads/{quote(base, safe='')}", token)
        base_sha = base_ref["object"]["sha"]
        api(f"/repos/{args.target_repo}/git/refs", token, "POST", {"ref": f"refs/heads/{head}", "sha": base_sha})
        blob = api(f"/repos/{args.target_repo}/git/blobs", token, "POST", {"content": base64.b64encode(content.encode()).decode(), "encoding": "base64"})
        base_tree = get_json(f"/repos/{args.target_repo}/git/commits/{base_sha}", token)["tree"]["sha"]
        tree = api(f"/repos/{args.target_repo}/git/trees", token, "POST", {"base_tree": base_tree, "tree": [{"path": target_path, "mode": "100644", "type": "blob", "sha": blob["sha"]}]})
        commit = api(f"/repos/{args.target_repo}/git/commits", token, "POST", {"message": f"vitruvius: integrate {src_repo}:{src_path}", "tree": tree["sha"], "parents": [base_sha]})
        api(f"/repos/{args.target_repo}/git/refs/heads/{quote(head, safe='')}", token, "PATCH", {"sha": commit["sha"], "force": False})
        pr = api(f"/repos/{args.target_repo}/pulls", token, "POST", {"title": f"vitruvius: integrate {arch_id} artifact", "head": head, "base": base, "body": f"Vitruvius integration proposal. Source: {src_repo}:{src_path}. Target architecture: {arch_id}. Target path: {target_path}. Requires review and verification; no automatic merge."})
        integrations.append({"source":f"{src_repo}:{src_path}","target":target_path,"architecture":arch_id,"branch":head,"pull_request":pr.get("html_url"),"status":"PROPOSED"})
    report["integrations"] = integrations
    with open("vitruvius/CONNECTOR_DISCOVERY_REPORT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
