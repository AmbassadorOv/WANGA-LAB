import json, subprocess, sys

def test_daily_operations_report_is_read_only_and_machine_readable():
    result=subprocess.run([sys.executable,"scripts/daily_operations_report.py"],capture_output=True,text=True,check=True)
    data=json.loads(result.stdout)
    assert data["operation_status"]=="READ_ONLY_REPORT"
    assert data["known_risk_case"]["status"]=="PLANNED"
    assert "Real client evidence" in " ".join(data["human_attention"])
