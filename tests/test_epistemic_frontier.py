import pytest

from epistemic_frontier import (
    EpistemicFrontierEngine,
    EpistemicState,
    FrontierConfig,
    Proposition,
)


def test_possible_is_active_propagation_state():
    engine = EpistemicFrontierEngine()
    result = engine.evaluate([
        Proposition("must", EpistemicState.MUST),
        Proposition("possible", EpistemicState.POSSIBLE),
        Proposition("forbidden", EpistemicState.FORBIDDEN),
    ])

    assert result.closed_ids == ["must", "forbidden"]
    assert result.propagated_ids == ["possible"]
    assert "possible" in result.preserved_ids


def test_provisional_and_unresolved_are_not_closed():
    engine = EpistemicFrontierEngine()
    result = engine.evaluate([
        Proposition("p", EpistemicState.PROVISIONAL),
        Proposition("u", EpistemicState.UNRESOLVED),
    ])

    assert result.closed_ids == []
    assert set(result.preserved_ids) == {"p", "u"}
    assert result.provisional_ids == ["p"]
    assert result.search_frontiers == ["u"]
    assert engine.final_state(result) is EpistemicState.SEARCH_FRONTIER


def test_contradiction_creates_third_unresolved_state_without_inventing_x():
    engine = EpistemicFrontierEngine()
    a = Proposition("A", EpistemicState.KNOWN, category=3)
    b = Proposition("B", EpistemicState.KNOWN, category=8)

    mapped = engine.map_contradiction(a, b)

    assert mapped.left_id == "A"
    assert mapped.right_id == "B"
    assert mapped.third_state is EpistemicState.UNRESOLVED
    assert mapped.relation == "incompatible_descriptions"


def test_cognitive_preservation_matches_retained_relevant_options():
    engine = EpistemicFrontierEngine()
    result = engine.evaluate([
        Proposition("m1", EpistemicState.MUST),
        Proposition("m2", EpistemicState.MUST),
        Proposition("f1", EpistemicState.FORBIDDEN),
        Proposition("p1", EpistemicState.POSSIBLE),
        Proposition("p2", EpistemicState.POSSIBLE),
        Proposition("u1", EpistemicState.UNRESOLVED),
        Proposition("q1", EpistemicState.PROVISIONAL),
    ])

    assert result.cognitive_preservation == pytest.approx(4 / 7)
    assert result.closure_efficiency == pytest.approx(3 / 7)


def test_cross_perspective_keeps_common_and_different_projections():
    engine = EpistemicFrontierEngine()
    result = engine.cross_perspective({
        "view_a": [Proposition("shared", EpistemicState.KNOWN), Proposition("a", EpistemicState.KNOWN)],
        "view_b": [Proposition("shared", EpistemicState.KNOWN), Proposition("b", EpistemicState.KNOWN)],
    })

    assert result["invariant_ids"] == ["shared"]
    assert result["difference_ids"] == ["a", "b"]
    assert result["view_count"] == 2


def test_baseline_rejects_automatic_closure_of_open_states():
    with pytest.raises(ValueError):
        FrontierConfig(close_unresolved=True).validate()

    with pytest.raises(ValueError):
        FrontierConfig(close_provisional=True).validate()


def test_deterministic_replay():
    propositions = [
        Proposition("A", EpistemicState.POSSIBLE, category=1),
        Proposition("B", EpistemicState.UNRESOLVED, category=2),
        Proposition("C", EpistemicState.FORBIDDEN, category=3),
    ]
    engine_a = EpistemicFrontierEngine()
    engine_b = EpistemicFrontierEngine()

    assert engine_a.evaluate(propositions).to_dict() == engine_b.evaluate(propositions).to_dict()
