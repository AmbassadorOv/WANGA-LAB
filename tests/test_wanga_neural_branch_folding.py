import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("fold",ROOT/"scripts/wanga_neural_branch_folding.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_one_endpoint_per_logical_branch():
    fabric={"counts":{"seed":57,"recursive":116736,"micro":3735552,"total":3852345},"sample":[{"node_id":"BRANCH-x"}]}
    architecture={"architectures":[{"id":"VITRUVIUS"},{"id":"NTM"}]}
    out=m.build(fabric,architecture)
    assert out["logical_branch_nodes"] == 3852345
    assert out["neural_endpoint_nodes"] == 3852345
    assert out["parametric_relations"][0]["cardinality"] == "1:1"
    assert out["sample_edges"][0]["relation"] == "BRANCH_TO_NEURAL_ENDPOINT"
