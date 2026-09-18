import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "scripts" / "vitruvius_automation_engine.py"

def test_engine_dry_run_is_deterministically_structured():
    result = subprocess.run(
        [sys.executable, str(ENGINE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    assert payload["mode"] == "dry-run"
    assert payload["index_nodes"] >= 5
    assert payload["index_edges"] >= 7
    assert payload["work_items"] >= 1

def test_engine_does_not_write_by_default():
    index = ROOT / "vitruvius" / "VITRUVIUS_INDEX.json"
    queue = ROOT / "vitruvius" / "VITRUVIUS_WORK_QUEUE.json"
    if index.exists():
        index.unlink()
    if queue.exists():
        queue.unlink()
    subprocess.run(
        [sys.executable, str(ENGINE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert not index.exists()
    assert not queue.exists()
