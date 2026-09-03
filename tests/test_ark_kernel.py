import pytest
import math
from ark_kernel import (
    HEBREW_LETTERS,
    ARCHITECTURE_CONFIG,
    CHAZAKA_PRIORS,
    WeightDomain,
    HolographicStringNode,
    IterationEngine,
    StructuralBlocksRegistry,
    Processor21Registry,
    DualRingArchitecture,
    run_tests
)

def test_constants_and_config():
    assert len(HEBREW_LETTERS) == 22
    assert HEBREW_LETTERS[0] == "א"
    assert HEBREW_LETTERS[-1] == "ת"
    assert ARCHITECTURE_CONFIG["logic_base_lock"] == 441
    assert ARCHITECTURE_CONFIG["volume_base"] == 9261
    assert ARCHITECTURE_CONFIG["ai231_gate_count"] == 231
    assert ARCHITECTURE_CONFIG["crystallographic_space_groups"] == 230
    assert CHAZAKA_PRIORS["chazakat_hashta"] == 0.99995
    assert len(WeightDomain) == 6

def test_holographic_string_node_canonical():
    node = HolographicStringNode.create_canonical("א", 0)
    assert node.letter == "א"
    assert node.index == 0
    assert node.radius == 1.0
    assert node.bulk_energy == 100.0
    assert node.chaos_energy == 5.0

def test_t_duality_transformation():
    node = HolographicStringNode.create_canonical("א", 0)
    initial_radius = node.radius
    initial_bulk = node.bulk_energy
    initial_chaos = node.chaos_energy

    scale = 1.618
    node.apply_t_duality(scale)

    expected_radius = (scale ** 2) / initial_radius
    assert math.isclose(node.radius, expected_radius)
    assert math.isclose(node.bulk_energy, initial_chaos * (expected_radius / initial_radius))
    assert math.isclose(node.chaos_energy, initial_bulk * (initial_radius / expected_radius))

def test_t_duality_invalid_radius():
    node = HolographicStringNode.create_canonical("א", 0)
    node.radius = 0.0
    with pytest.raises(ValueError, match="Radius cannot be non-positive or non-finite"):
        node.apply_t_duality()

def test_holographic_transform():
    node = HolographicStringNode.create_canonical("א", 0)
    node.apply_t_duality()
    node.apply_holographic_transform()

    assert 0.0 <= node.coherence <= 1.0
    assert node.surface_tension > 0.0
    assert node.entropy < 0.5
    d = node.to_dict()
    assert d["letter"] == "א"
    assert d["node_index"] == 0
    assert "topological_state" in d

def test_iteration_engine_step():
    engine = IterationEngine()
    state = engine.step()

    assert state["meta"]["iteration"] == 1
    assert state["meta"]["node_count"] == 22
    assert state["meta"]["protocol"] == "T-DUALITY_HOLOGRAPHIC_V1"
    assert len(state["nodes"]) == 22

def test_iteration_engine_determinism():
    engine_a = IterationEngine()
    engine_b = IterationEngine()

    state_a = engine_a.step()
    state_b = engine_b.step()

    assert state_a == state_b

def test_registries_and_scaffolding():
    assert StructuralBlocksRegistry.verify_involution()
    assert len(Processor21Registry.PHASES) == 21
    ring = DualRingArchitecture()
    assert ring.validate_boundaries()

def test_run_tests_utility():
    results = run_tests()
    for test_name, outcome in results.items():
        assert outcome == "PASS"


def test_jules_network_reporter():
    from ark_kernel import JulesNetworkReporter, NetworkMetrics
    reporter = JulesNetworkReporter()
    metrics = reporter.get_runtime_metrics()
    assert isinstance(metrics, NetworkMetrics)
    assert metrics.total_nodes == 100000
    assert metrics.active_connections == 100000

    comparison = reporter.runtime_comparison()
    assert "Jules_Deterministic_Network" in comparison
    assert "Standard_Probabilistic_NN" in comparison

    report_str = reporter.generate_report()
    import json
    parsed = json.loads(report_str)
    assert "architecture" in parsed
    assert "runtime_analysis" in parsed
