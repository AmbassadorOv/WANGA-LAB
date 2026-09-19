import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("mapper",ROOT/"scripts/vitruvius_ten_architecture_family_mapper.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_manifest_has_ten_sources():
    import json
    d=json.loads((ROOT/"vitruvius/TEN_ARCHITECTURE_FAMILY_GOVERNANCE_MAP_V1.json").read_text())
    assert len(d["source_files"])==10
    assert len(d["architecture_bindings"])==10
def test_all_bindings_have_governance_and_root():
    import json
    d=json.loads((ROOT/"vitruvius/TEN_ARCHITECTURE_FAMILY_GOVERNANCE_MAP_V1.json").read_text())
    assert all(x["root"] in d["family_roots"] and x["governance"] for x in d["architecture_bindings"])
