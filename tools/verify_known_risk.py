"""Independent repository-level verifier for CASE_REF_2026_DRIFT_KNOWN_RISK_001."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "artifacts" / "drift-known-risk-001"
CASE_REF = "CASE_REF_2026_DRIFT_KNOWN_RISK_001"

def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify() -> dict[str, object]:
    manifest = json.loads((ROOT / "evidence-manifest.json").read_text(encoding="utf-8"))
    replay = json.loads((ROOT / "outputs" / "replay-result.json").read_text(encoding="utf-8"))

    checks = [
        ("case_ref", replay["case_ref"] == CASE_REF),
        ("fixture", replay["fixture"] == "synthetic"),
        ("model_output_unchanged", replay["model_output_changed"] is False),
        ("criterion_changed", replay["criterion_changed"] is True),
        ("deviation_detected", replay["deviation_detected"] is True),
        ("drift_type", replay["drift_type"] == "CRITERION_DRIFT"),
        ("baseline_decision", replay["baseline_evaluation"]["decision"] == "REJECT"),
        ("observed_decision", replay["observed_evaluation"]["decision"] == "ACCEPT"),
        ("same_score", replay["baseline_evaluation"]["score"] == replay["observed_evaluation"]["score"]),
        ("manifest_algorithm", manifest["hash_algorithm"] == "SHA-256"),
    ]

    for item in manifest["artifacts"]:
        path = ROOT / item["path"]
        checks.append((f"hash:{item['path']}", path.exists() and sha_file(path) == item["sha256"]))

    passed = all(ok for _, ok in checks)
    return {
        "case_ref": CASE_REF,
        "verification_status": "VERIFIED" if passed else "FAILED",
        "verification_scope": "repository-level independent recheck",
        "third_party_audit": False,
        "external_timestamp": "PENDING",
        "external_anchor": "PENDING",
        "checks": [{"name": name, "passed": ok} for name, ok in checks],
        "all_required_checks_passed": passed,
    }

def main() -> None:
    result = verify()
    out = ROOT / "verification" / "verification-result.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["all_required_checks_passed"] else 1)

if __name__ == "__main__":
    main()
