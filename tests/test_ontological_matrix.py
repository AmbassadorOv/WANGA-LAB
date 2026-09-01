"""
WANGA Ontological Matrix & State Transition Test Suite
"""

import pytest
from wanga.matrix import OntologicalMatrix, OntologicalNode, OntologicalRelation, OntologicalLayerType
from wanga.state import OntologicalStateEngine, StateStage


def test_ontological_matrix_layers():
    m = OntologicalMatrix()
    node_src = m.add_node(OntologicalNode(
        node_id="n-source",
        layer=OntologicalLayerType.SOURCE,
        label="Tanakh Source Text"
    ))
    node_cfg = m.add_node(OntologicalNode(
        node_id="n-config",
        layer=OntologicalLayerType.CONFIGURATION,
        label="Kabbalistic Relational Matrix"
    ))

    rel = m.add_relation(OntologicalRelation(
        relation_id="r-1",
        source_node_id="n-source",
        target_node_id="n-config",
        relation_type="STRUCTURES",
        layer_provenance=OntologicalLayerType.CONFIGURATION
    ))

    assert len(m.get_nodes_by_layer(OntologicalLayerType.SOURCE)) == 1
    assert len(m.get_nodes_by_layer(OntologicalLayerType.CONFIGURATION)) == 1
    assert len(m.get_relations_for_node("n-source")) == 1


def test_ontological_state_lifecycle():
    engine = OntologicalStateEngine()
    assert engine.current_stage == StateStage.POTENTIAL

    # 1. Transition to CONFIGURED
    engine.transition_to_configured({"active_blueprint": "Photonic Matrix"})
    assert engine.current_stage == StateStage.CONFIGURED

    # 2. Generate CANDIDATEs
    engine.generate_candidates([
        {"id": "cand-a", "score": 90, "valid_flag": True},
        {"id": "cand-b", "score": 30, "valid_flag": False}
    ])
    assert engine.current_stage == StateStage.CANDIDATE
    assert len(engine.candidates) == 2

    # 3. Birur Clarification
    valid_cands = engine.run_birur_clarification([
        {"required_key": "valid_flag"}
    ])
    assert engine.current_stage == StateStage.BIRUR
    assert len(valid_cands) == 2

    # 4. Resolve State
    resolved = engine.resolve_state()
    assert engine.current_stage == StateStage.RESOLVED
    assert resolved.candidate_id == "cand-1"

    # 5. Actualize State
    actualized = engine.actualize_state()
    assert engine.current_stage == StateStage.ACTUALIZED
    assert actualized["stage"] == "ACTUALIZED"
    assert "state_witness_hash" in actualized


def test_birur_constraint_rejection():
    engine = OntologicalStateEngine()
    engine.transition_to_configured({})
    engine.generate_candidates([
        {"val": 10},
        {"val": 5}
    ])
    valid = engine.run_birur_clarification([{"required_key": "val", "min_value": 8}])
    assert len(valid) == 1
    assert valid[0].payload["val"] == 10
