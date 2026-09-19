import json
from pathlib import Path

DATA = Path("research-architecture/external-projects/copernicus/proteus_101296397.json")

def test_proteus_record_is_valid_and_traceable():
    record = json.loads(DATA.read_text())
    assert record["record_type"] == "external_research_project"
    assert record["source_system"] == "European Commission CORDIS"
    assert record["project"]["grant_agreement_id"] == "101296397"
    assert record["project"]["acronym"] == "PROTEUS"
    assert record["project"]["start_date"] == "2026-09-01"
    assert record["project"]["end_date"] == "2030-02-28"
    assert len(record["participants"]) == 18
    assert record["technical_scope"]["causal_reasoning"] is True
    assert record["technical_scope"]["agentic_orchestration"] is True
    assert record["technical_scope"]["transparent_traceable_outputs"] is True
    assert record["wanga_integration"]["status"] == "OBSERVED_EXTERNAL_PROJECT"
