"""Generate a compact remote-oversight summary from the insurer pipeline."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
from tools.insurer_pipeline import build_pipeline

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "artifacts" / "insurer-intake-demo" / "intake.json"

def build_oversight() -> dict[str, object]:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    results = build_pipeline(data["records"], int(data["active_limit"]))
    execution = Counter(x["execution_state"] for x in results)
    intake = Counter(x["intake_status"] for x in results)
    return {
        "scenario": data["scenario"],
        "active_limit": data["active_limit"],
        "total_cases": len(results),
        "active_replay": execution.get("REPLAY", 0),
        "queued": execution.get("QUEUED", 0),
        "blocked_or_pending": sum(
            1 for x in results if x["execution_state"] == "BLOCKED"
        ),
        "human_gate": sum(
            1 for x in results if x["execution_state"] == "HUMAN_GATE"
        ),
        "intake_status_counts": dict(sorted(intake.items())),
        "requires_architect_attention": [
            x["case_ref"] for x in results
            if x["execution_state"] in {"BLOCKED", "HUMAN_GATE"}
        ],
    }

def main() -> None:
    print(json.dumps(build_oversight(), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
