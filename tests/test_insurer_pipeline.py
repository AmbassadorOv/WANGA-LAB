import json
from pathlib import Path
from tools.insurer_pipeline import build_pipeline

FIXTURE = Path("artifacts/insurer-intake-demo/intake.json")

def test_ten_prospect_pipeline_routes_without_overactivation():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    result = build_pipeline(data["records"], data["active_limit"])
    assert sum(x["execution_state"] == "REPLAY" for x in result) == 2
    assert sum(x["intake_status"] == "NEEDS_EVIDENCE" for x in result) == 1
    assert sum(x["intake_status"] == "PENDING_CLIENT_ACCESS" for x in result) == 1
    assert sum(x["intake_status"] == "OUT_OF_SCOPE" for x in result) == 1
    assert sum(x["execution_state"] == "QUEUED" for x in result) == 5
