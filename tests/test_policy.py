from holographic_string_nn import (
    CollapseDecision,
    CollapsePolicy,
    HolographicStringNode,
    LetterGroup,
    SephirahLine,
)


def node(letter: str, group: LetterGroup, line: SephirahLine, coherence: float):
    return HolographicStringNode(letter, group, line, coherence)


def test_mother_can_collapse_at_stable_coherence():
    decision = CollapsePolicy().decide(
        node("א", LetterGroup.MOTHERS, SephirahLine.RIGHT_LEFT, 0.96)
    )
    assert decision is CollapseDecision.COLLAPSE


def test_double_stays_open_off_middle_line():
    decision = CollapsePolicy().decide(
        node("ב", LetterGroup.DOUBLES, SephirahLine.RIGHT_LEFT, 0.99)
    )
    assert decision is CollapseDecision.HOLD


def test_double_can_collapse_on_middle_line():
    decision = CollapsePolicy().decide(
        node("ת", LetterGroup.DOUBLES, SephirahLine.MIDDLE, 0.99)
    )
    assert decision is CollapseDecision.COLLAPSE


def test_simple_is_search_frontier_even_at_high_coherence():
    decision = CollapsePolicy().decide(
        node("ה", LetterGroup.SIMPLE, SephirahLine.MIDDLE, 1.0)
    )
    assert decision is CollapseDecision.SEARCH_FRONTIER


def test_low_coherence_blocks_mother():
    decision = CollapsePolicy().decide(
        node("ש", LetterGroup.MOTHERS, SephirahLine.MIDDLE, 0.50)
    )
    assert decision is CollapseDecision.HOLD
