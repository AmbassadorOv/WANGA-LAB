import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "scripts" / "vitruvius_automation_engine.py"

def run_engine():
    return subprocess.run(
        [sys.executable, str(ENGINE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

def test_engine_dry_run_is_deterministically_structured():
    result = run_engine()
    payload = json.loads(result.stdout)
    assert payload["mode"] == "dry-run"
    assert payload["index_nodes"] >= 5
    assert payload["index_edges"] >= 7
    assert payload["work_items"] >= 1
    assert payload["architecture_nodes"] >= 10
    assert payload["architecture_relationships"] >= 10
    assert payload["branch_patterns"] >= 10

def test_engine_does_not_write_by_default():
    paths = [
        ROOT / "vitruvius" / "VITRUVIUS_INDEX.json",
        ROOT / "vitruvius" / "VITRUVIUS_WORK_QUEUE.json",
        ROOT / "vitruvius" / "ARCHITECTURE_GRAPH.json",
        ROOT / "vitruvius" / "ARCHITECTURE_RELATIONSHIP_REGISTRY.json",
    ]
    for path in paths:
        if path.exists():
            path.unlink()
    run_engine()
    assert all(not path.exists() for path in paths)

def test_engine_write_produces_graph_and_relationship_registry():
    subprocess.run(
        [sys.executable, str(ENGINE), "--write"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    graph = json.loads((ROOT / "vitruvius" / "ARCHITECTURE_GRAPH.json").read_text())
    registry = json.loads((ROOT / "vitruvius" / "ARCHITECTURE_RELATIONSHIP_REGISTRY.json").read_text())
    assert graph["authority"] == "VITRUVIUS"
    assert registry["authority"] == "VITRUVIUS"
    assert all(r["discovered_by"] == "VITRUVIUS" for r in graph["relationships"])
    assert all(r["verification_status"] == "NOT_VERIFIED" for r in graph["relationships"])
