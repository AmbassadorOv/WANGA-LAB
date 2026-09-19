"""Deterministic replay for CASE_REF_2026_DRIFT_KNOWN_RISK_001."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / "artifacts" / "drift-known-risk-001"
CASE_REF = "CASE_REF_2026_DRIFT_KNOWN_RISK_001"

def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()

def load_inputs() -> dict[str, object]:
    return json.loads((ROOT / "replay" / "inputs.json").read_text(encoding="utf-8"))

def build_replay(inputs: dict[str, object]) -> dict[str, object]:
    model_output = inputs["model_output"]
    baseline = inputs["baseline_criterion"]
    observed = inputs["observed_criterion"]
    score = float(model_output["score"])

    def evaluate(criterion: dict[str, object]) -> dict[str, object]:
        threshold = float(criterion["pass_threshold"])
        return {
            "criterion_id": criterion["criterion_id"],
            "criterion_version": criterion["criterion_version"],
            "pass_threshold": threshold,
            "score": score,
            "decision": "ACCEPT" if score >= threshold else "REJECT",
        }

    baseline_eval = evaluate(baseline)
    observed_eval = evaluate(observed)

    return {
        "case_ref": CASE_REF,
        "fixture": "synthetic",
        "model_output_changed": False,
        "criterion_changed": baseline != observed,
        "deviation_detected": baseline_eval != observed_eval,
        "drift_type": "CRITERION_DRIFT",
        "baseline_evaluation": baseline_eval,
        "observed_evaluation": observed_eval,
        "hashes": {
            "model_output_sha256": canonical_hash(model_output),
            "baseline_criterion_sha256": canonical_hash(baseline),
            "observed_criterion_sha256": canonical_hash(observed),
            "baseline_evaluation_sha256": canonical_hash(baseline_eval),
            "observed_evaluation_sha256": canonical_hash(observed_eval),
        },
    }

def main() -> None:
    result = build_replay(load_inputs())
    out = ROOT / "outputs" / "replay-result.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()
