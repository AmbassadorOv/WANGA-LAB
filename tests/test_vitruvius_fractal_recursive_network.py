import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vitruvius_fractal_recursive_network as m

def test_recursive_family_extraction():
    report={"candidates":[{"repo":"x/y","path":"a/b/c.py","architectures":["A"],"score":9}],"integrations":[]}
    g=m.build(report)
    kinds=[n["kind"] for n in g["nodes"]]
    assert "REPOSITORY" in kinds
    assert "FAMILY" in kinds
    assert "ARTIFACT" in kinds
    assert g["node_count"] >= 5

def test_branch_folds_into_global_network():
    report={"candidates":[],"integrations":[{"branch":"agent/vitruvius/integrate-a","architecture":"A"}]}
    g=m.build(report)
    assert any(e["relation"]=="MAPS_TO" for e in g["edges"])
    assert any(n["kind"]=="INTEGRATION_BRANCH" for n in g["nodes"])
