"""Generate a bounded daily operations report from repository state."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    insurer=read_json(ROOT/"artifacts/insurer-intake-demo/intake.json") or {}
    case=read_json(ROOT/"artifacts/drift-known-risk-001/evidence-manifest.json") or {}
    wm=read_json(ROOT/"docs/WORK_MEMORY_STATE.json") or {}
    report={
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "repository":"AmbassadorOv/WANGA-LAB",
        "operation_status":"READ_ONLY_REPORT",
        "architecture": {
            "global_work_manager": "documented" if (ROOT/"docs/GLOBAL_WORK_MANAGER.schema.json").exists() else "missing",
            "model_fabric": "documented" if (ROOT/"docs/MODEL_AGENT_ARCHITECTURE_V1.md").exists() else "missing",
            "global_drift_network": "present" if (ROOT/"ai-drift-forensics/global-drift-network").exists() else "missing",
        },
        "insurer_intake": {
            "demo_records":len(insurer.get("records",[])),
            "demo_active_limit":insurer.get("active_limit"),
        },
        "known_risk_case": {
            "status":"PLANNED",
            "evidence_manifest_status":case.get("status"),
            "verification":"PENDING_REAL_EVIDENCE",
        },
        "work_memory": {
            "status":wm.get("status"),
            "main_branch":wm.get("main_branch"),
        },
        "human_attention": [
            "Only cases in HUMAN_GATE or explicit BLOCKED state require architectural intervention.",
            "Real client evidence is not implied by synthetic fixtures.",
            "External timestamp/anchor status remains pending until proof is actually checked.",
        ],
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
