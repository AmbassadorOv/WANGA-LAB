from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .model import HolographicStringNode, LetterGroup, SephirahLine


class CollapseDecision(str, Enum):
    COLLAPSE = "COLLAPSE"
    HOLD = "HOLD_SUPERPOSITION"
    SEARCH_FRONTIER = "SEARCH_FRONTIER"


@dataclass(frozen=True)
class CollapsePolicy:
    """Deterministic collapse gate.

    The examples in the specification resolve an ambiguity in the prose:
    Simple letters remain Search Frontier even when coherence is high;
    Doubles may close only on the middle line; Mothers may close when
    coherence is stable. This preserves the stated operational examples.
    """

    coherence_threshold: float = 0.95

    def __post_init__(self) -> None:
        if not 0.0 <= self.coherence_threshold <= 1.0:
            raise ValueError("coherence_threshold must be in [0, 1]")

    def decide(self, node: HolographicStringNode) -> CollapseDecision:
        stable = node.coherence >= self.coherence_threshold

        if node.group is LetterGroup.SIMPLE:
            return CollapseDecision.SEARCH_FRONTIER

        if not stable:
            return CollapseDecision.HOLD

        if node.group is LetterGroup.MOTHERS:
            return CollapseDecision.COLLAPSE

        if (
            node.group is LetterGroup.DOUBLES
            and node.sephirah_line is SephirahLine.MIDDLE
        ):
            return CollapseDecision.COLLAPSE

        return CollapseDecision.HOLD

    def apply(self, node: HolographicStringNode) -> CollapseDecision:
        decision = self.decide(node)
        if decision is CollapseDecision.COLLAPSE:
            node.collapse()
        else:
            node.hold_superposition()
        return decision
