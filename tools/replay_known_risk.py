"""Deterministic synthetic replay fixture for the first known-risk case."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

CASE_REF = "CASE_REF_2026_DRIFT_KNOWN_RISK_001"
ROOT = Path(__file__).resolve().parents[1] / "artifacts" / "drift-known-risk-001"

def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()

def replay() -> dict[str, object]:
    baseline = {"policy_version":"synthetic-v1","answer_class":"BASELINE","score":1.0}
    observed = {"policy_version":"synthetic-v1","answer_class":"DRIFTED","score":0.5}
    return {"case_ref":CASE_REF,"fixture":"synthetic","baseline":baseline,"observed":observed,
            "deviation_detected":baseline != observed,
            "baseline_sha256":canonical_hash(baseline),"observed_sha256":canonical_hash(observed)}

def main() -> None:
    result = replay()
    out = ROOT / "outputs" / "replay-result.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()
