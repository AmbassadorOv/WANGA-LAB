import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import wanga_neural_architecture_network as nan

def test_network_loads_manifest():
    manifest = json.loads((ROOT / "vitruvius" / "ARCHITECTURE_GRAPH_MANIFEST_V1.json").read_text())
    net = nan.NeuralArchitectureNetwork(manifest)
    assert len(net.nodes) >= 15
    assert len(net.edges) >= 29

def test_propagation_is_deterministic_and_unverified():
    manifest = json.loads((ROOT / "vitruvius" / "ARCHITECTURE_GRAPH_MANIFEST_V1.json").read_text())
    a = nan.NeuralArchitectureNetwork(manifest).propagate("VITRUVIUS", {"event":"test"})
    b = nan.NeuralArchitectureNetwork(manifest).propagate("VITRUVIUS", {"event":"test"})
    assert [x.__dict__ for x in a] == [x.__dict__ for x in b]
    assert all(x.evidence_state == "UNVERIFIED" for x in a)
