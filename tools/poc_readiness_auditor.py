#!/usr/bin/env python3
"""WANGA-LAB POC readiness audit: structure, imports, tests and executable smoke checks."""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def find_files(patterns):
    out = []
    for pattern in patterns:
        if isinstance(pattern, (list, tuple)):
            pattern = pattern[0]
        out.extend(str(p.relative_to(ROOT)) for p in ROOT.rglob(pattern))
    return sorted(set(out))

def run(cmd):
    try:
        p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=180)
        return p.returncode == 0, (p.stdout + "\n" + p.stderr).strip()[-5000:]
    except Exception as exc:
        return False, str(exc)

def add(checks, name, category, ok, evidence, weight):
    checks.append({
        "name": name, "category": category,
        "status": "VERIFIED" if ok else "MISSING/FAILED",
        "score": 1.0 if ok else 0.0, "weight": weight,
        "evidence": evidence
    })

checks = []

ntm = ROOT / "wanga-research-groups" / "neural_thinking_machine" / "ntm_core.py"
add(checks, "NTM executable core", "implementation", ntm.exists(),
    find_files(["*ntm*.py", "*orchestrat*.py", "*router*.py"]), .20)

ark = ROOT / "ark_kernel.py"
add(checks, "ARK Kernel", "implementation", ark.exists(),
    ["ark_kernel.py"] if ark.exists() else [], .10)

verification = ROOT / "ai-drift-forensics" / "VERIFICATION_PROTOCOL.md"
add(checks, "Verification protocol", "verification", verification.exists(),
    ["ai-drift-forensics/VERIFICATION_PROTOCOL.md"] if verification.exists() else [], .10)

drift = ROOT / "ai-drift-forensics"
add(checks, "Drift Forensics", "drift", drift.exists(),
    find_files(["*drift*.py", "*forensic*.py", "*DRIFT*.md"]), .15)

memory_files = find_files(["*memory*.py", "*audit*.py", "*persistence*.py", "*MEMORY*.md", "*AUDIT*.md"])
add(checks, "Memory/Audit", "memory", bool(memory_files), memory_files, .10)

research_files = find_files(["*research*.py", "*vitruvius*.py", "*cluster*.py", "*graph*.py", "*RESEARCH*.md", "*VITRUVIUS*.md"])
add(checks, "Research/Vitruvius", "research", bool(research_files), research_files, .10)

api_files = find_files(["*api*.py", "*fastapi*.py", "main.py"])
add(checks, "API", "api", bool(api_files), api_files, .05)

ok, out = run([sys.executable, "-m", "compileall", "-q", "."])
add(checks, "Python compilation", "testing", ok, [out] if out else [], .10)

ok, out = run([sys.executable, "-m", "pytest", "-q"])
add(checks, "Automated tests", "testing", ok, [out] if out else [], .10)

# Actual executable smoke test. Passing this is stronger evidence than file existence.
if ntm.exists():
    smoke = [
        sys.executable, "-c",
        "from wanga_research_groups.neural_thinking_machine.ntm_core import NTMOrchestrator; "
        "r=NTMOrchestrator().run('readiness smoke test'); "
        "assert r['verification_status']=='PASSED'; "
        "assert r['reasoning_status']=='VERIFIED_FINDING'; "
        "print(r['request_id'])"
    ]
    ok, out = run(smoke)
else:
    ok, out = False, "NTM core not present"
add(checks, "NTM executable smoke test", "execution", ok, [out] if out else [], .10)

weight_total = sum(c["weight"] for c in checks)
weighted = sum(c["score"] * c["weight"] for c in checks) / weight_total if weight_total else 0.0
hard = [c["name"] for c in checks
        if c["name"] in ("Python compilation", "Automated tests", "NTM executable smoke test")
        and c["score"] < 1.0]

verdict = "NOT_READY" if hard else ("POC_PARTIAL" if weighted < .85 else "POC_READY")
report = {
    "project": "WANGA-LAB",
    "readiness_score_percent": round(weighted * 100, 2),
    "verdict": verdict,
    "hard_failures": hard,
    "checks": checks,
}
print(json.dumps(report, indent=2, ensure_ascii=False))
(ROOT / "POC_READINESS_REPORT.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
)
sys.exit(0 if verdict == "POC_READY" else 1)
