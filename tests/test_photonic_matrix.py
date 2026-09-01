"""
WANGA-NANO-21 Photonic Neuromorphic Matrix Test Suite
"""

import pytest
from wanga.blueprint import BlueprintRegistry
from wanga.vnp_fabric import VirtualGPU
from wanga.vgpu import VirtualNanoProcessor, VNPConfig


def test_configuration_loading():
    reg = BlueprintRegistry("config/photonic_neuromorphic_matrix.json")
    assert len(reg.get_nodes()) == 21
    assert reg.topology.gate_count == 231
    assert reg.rule_system.get("rule_count") == 32
    assert len(reg.receptors.get("inner", [])) + len(reg.receptors.get("outer", [])) == 4
    assert len(reg.list_blueprints()) == 7


def test_node_integrity():
    reg = BlueprintRegistry("config/photonic_neuromorphic_matrix.json")
    nodes = reg.get_nodes()
    node_ids = [n.id for n in nodes]
    assert sorted(node_ids) == list(range(1, 22))
    assert len(set(node_ids)) == 21

    for n in nodes:
        assert n.role
        assert n.recommended_processor
        assert n.category
        assert n.rationale


def test_processor_mapping():
    reg = BlueprintRegistry("config/photonic_neuromorphic_matrix.json")
    node1 = reg.get_node(1)
    profile1 = reg.map_node_to_processor_profile(node1)
    assert profile1.family == "photonic"
    assert "phase_compute" in profile1.capabilities

    node2 = reg.get_node(2)
    profile2 = reg.map_node_to_processor_profile(node2)
    assert profile2.family == "quantum_morphic"


def test_virtual_gpu_instantiation():
    gpu = VirtualGPU("vgpu-photonic")
    registry = gpu.load_blueprint("config/photonic_neuromorphic_matrix.json")
    vnps = gpu.instantiate_blueprint(registry)

    assert len(vnps) == 21
    assert len(gpu.list_processors()) == 21
    assert gpu.get_processor("VNP-001").blueprint_node_id == 1
    assert gpu.get_processor("VNP-021").blueprint_node_id == 21

    status = gpu.status()
    assert status["processor_count"] == 21
    assert status["blueprint"]["total_vertices"] == 21
    assert status["blueprint"]["epicyclic_gates"] == 231


def test_fabric_nodes():
    gpu = VirtualGPU("vgpu-fabric-test")
    gpu.instantiate_blueprint(gpu.load_blueprint("config/photonic_neuromorphic_matrix.json"))
    assert gpu.fabric.get_topology_info()["node_count"] == 21


@pytest.mark.parametrize("scale", [32, 50])
def test_scalability_beyond_blueprint(scale):
    gpu = VirtualGPU(f"vgpu-scale-{scale}")
    # Load and instantiate blueprint (21 VNPs)
    gpu.instantiate_blueprint(gpu.load_blueprint("config/photonic_neuromorphic_matrix.json"))

    # Dynamically register additional generic VNPs up to scale without modifying blueprint
    for i in range(22, scale + 1):
        vnp = VirtualNanoProcessor(VNPConfig(id=f"VNP-{i:03d}"))
        gpu.register_processor(vnp)

    assert len(gpu.list_processors()) == scale
