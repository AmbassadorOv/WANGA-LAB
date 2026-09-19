import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("tree",ROOT/"scripts/vitruvius_three_family_branch_tree.py")
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def test_every_branch_gets_exactly_one_family_and_neural_wrapper():
    branches=[{"name":"agent/codex/neural-architecture-network","sha":"a"},{"name":"drift/global-network/evidence-infrastructure","sha":"b"},{"name":"agent/research/composition-fractals-2026-09-19","sha":"c"}]
    nodes=m.classify(branches)
    assert len(nodes)==3
    assert all(n["family"] in m.FAMILIES for n in nodes)
    assert all(n["neural_endpoint"].startswith("NEURAL-ENDPOINT-") for n in nodes)
def test_family_partition_is_total():
    branches=[{"name":"main","sha":"x"},{"name":"agent/codex/fractal-github-neural-network","sha":"y"}]
    nodes=m.classify(branches)
    assert len({n["family"] for n in nodes})>=1
