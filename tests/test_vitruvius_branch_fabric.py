import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vitruvius_branch_fabric as m

def test_fabric_exceeds_one_million_nodes():
    c=m.counts(57,2048,32)
    assert c["total"] >= 1_048_576
    assert c == {"seed":57,"recursive":116736,"micro":3735552,"total":3852345}

def test_ids_are_deterministic_and_neural_bound():
    a=m.branch_node("seed","parent",1,7,"RECURSIVE")
    b=m.branch_node("seed","parent",1,7,"RECURSIVE")
    assert a.node_id == b.node_id
    assert a.neural_endpoint.startswith("NEURAL-ENDPOINT-")
