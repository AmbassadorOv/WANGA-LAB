import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("fold",ROOT/"scripts/vitruvius_global_github_neural_network.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_source_exists():
    assert (ROOT/"vitruvius/THREE_FAMILY_BRANCH_TREE_V1.json").exists()
    assert (ROOT/"vitruvius/GITHUB_BRANCH_FABRIC_MANIFEST_V1.json").exists()
