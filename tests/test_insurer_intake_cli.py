import json
import subprocess
import sys
from pathlib import Path

FIXTURE = Path("artifacts/insurer-intake-demo/intake.json")

def test_cli_reads_machine_intake_and_emits_pipeline_json(tmp_path):
    output = tmp_path / "pipeline.json"
    subprocess.run(
        [sys.executable, "tools/insurer_intake_cli.py", str(FIXTURE), "-o", str(output)],
        check=True,
    )
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["active_limit"] == 2
    assert len(data["results"]) == 10
    assert sum(x["execution_state"] == "REPLAY" for x in data["results"]) == 2
    assert sum(x["execution_state"] == "QUEUED" for x in data["results"]) == 5
