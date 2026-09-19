import json, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("m",ROOT/"scripts/vitruvius_family_atom_mapper.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_manifest_defines_three_root_families_and_atoms():
    d=json.loads((ROOT/"vitruvius/FAMILY_ATOM_GOVERNANCE_ONTOLOGY_V1.json").read_text())
    assert len(d["root_families"])==3
    assert len(d["atoms"])>=30
def test_multi_family_atom_exists():
    d=json.loads((ROOT/"vitruvius/FAMILY_ATOM_GOVERNANCE_ONTOLOGY_V1.json").read_text())
    assert any(len(x[2])>=2 for x in d["atoms"])
