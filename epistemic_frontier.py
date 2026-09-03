"""Epistemic Frontier Engine

A domain-agnostic decision layer for preserving unresolved alternatives.
This is a computational model; it does not modify or expose foundation-model
weights.  It operates on an explicit configuration supplied by the caller.

Core semantics:
    MUST       -> constrain
    FORBIDDEN  -> eliminate
    POSSIBLE   -> propagate
    PROVISIONAL-> report without closing
    UNRESOLVED -> preserve / continue
    CONTRADICTION -> investigate

The engine deliberately does not manufacture an explanation for an
unrepresented X.  It records a search frontier instead.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


class EpistemicState(str, Enum):
    MUST = "MUST"
    POSSIBLE = "POSSIBLE"
    FORBIDDEN = "FORBIDDEN"
    PROVISIONAL = "PROVISIONAL"
    UNRESOLVED = "UNRESOLVED"
    CONTRADICTION = "CONTRADICTION"
    KNOWN = "KNOWN"
    INFERRED = "INFERRED"
    SEARCH_FRONTIER = "SEARCH_FRONTIER"


@dataclass(frozen=True)
class FrontierConfig:
    """Explicit policy parameters for the decision layer."""

    category_count: int = 21
    possible_weight: float = 1.0
    contradiction_weight: float = 1.0
    preservation_floor: float = 0.0
    close_provisional: bool = False
    close_unresolved: bool = False

    def validate(self) -> None:
        if self.category_count <= 0:
            raise ValueError("category_count must be positive")
        if self.possible_weight < 0 or self.contradiction_weight < 0:
            raise ValueError("weights must be non-negative")
        if not 0.0 <= self.preservation_floor <= 1.0:
            raise ValueError("preservation_floor must be in [0, 1]")
        if self.close_provisional or self.close_unresolved:
            raise ValueError(
                "Baseline safety policy forbids automatic closure of "
                "PROVISIONAL or UNRESOLVED states"
            )


@dataclass(frozen=True)
class Proposition:
    id: str
    state: EpistemicState
    category: int = 0
    source: str = "synthetic"

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("proposition id cannot be empty")
        if self.category < 0:
            raise ValueError("category cannot be negative")


@dataclass(frozen=True)
class ContradictionMap:
    left_id: str
    right_id: str
    relation: str
    third_state: EpistemicState = EpistemicState.UNRESOLVED


@dataclass
class FrontierResult:
    input_count: int
    closed_ids: List[str]
    preserved_ids: List[str]
    propagated_ids: List[str]
    contradiction_maps: List[ContradictionMap]
    search_frontiers: List[str]
    provisional_ids: List[str]

    @property
    def cognitive_preservation(self) -> float:
        if self.input_count == 0:
            return 1.0
        return len(set(self.preserved_ids)) / self.input_count

    @property
    def closure_efficiency(self) -> float:
        if self.input_count == 0:
            return 0.0
        return len(set(self.closed_ids)) / self.input_count

    def to_dict(self) -> Dict[str, object]:
        return {
            "input_count": self.input_count,
            "closed_ids": list(self.closed_ids),
            "preserved_ids": list(self.preserved_ids),
            "propagated_ids": list(self.propagated_ids),
            "provisional_ids": list(self.provisional_ids),
            "search_frontiers": list(self.search_frontiers),
            "contradiction_maps": [
                {
                    "left_id": item.left_id,
                    "right_id": item.right_id,
                    "relation": item.relation,
                    "third_state": item.third_state.value,
                }
                for item in self.contradiction_maps
            ],
            "cognitive_preservation": self.cognitive_preservation,
            "closure_efficiency": self.closure_efficiency,
        }


class EpistemicFrontierEngine:
    """Deterministic state transition engine for an explicit candidate set."""

    def __init__(self, config: Optional[FrontierConfig] = None):
        self.config = config or FrontierConfig()
        self.config.validate()

    @staticmethod
    def _classify(state: EpistemicState) -> str:
        if state is EpistemicState.MUST:
            return "close"
        if state is EpistemicState.FORBIDDEN:
            return "close"
        if state is EpistemicState.POSSIBLE:
            return "propagate"
        if state is EpistemicState.PROVISIONAL:
            return "preserve"
        if state is EpistemicState.UNRESOLVED:
            return "preserve"
        if state is EpistemicState.CONTRADICTION:
            return "investigate"
        return "preserve"

    def evaluate(self, propositions: Sequence[Proposition]) -> FrontierResult:
        closed: List[str] = []
        preserved: List[str] = []
        propagated: List[str] = []
        provisional: List[str] = []
        frontiers: List[str] = []

        for proposition in propositions:
            action = self._classify(proposition.state)
            if action == "close":
                closed.append(proposition.id)
            elif action == "propagate":
                propagated.append(proposition.id)
                preserved.append(proposition.id)
            elif action == "investigate":
                preserved.append(proposition.id)
                frontiers.append(proposition.id)
            else:
                preserved.append(proposition.id)
                if proposition.state is EpistemicState.PROVISIONAL:
                    provisional.append(proposition.id)
                if proposition.state is EpistemicState.UNRESOLVED:
                    frontiers.append(proposition.id)

        return FrontierResult(
            input_count=len(propositions),
            closed_ids=closed,
            preserved_ids=preserved,
            propagated_ids=propagated,
            contradiction_maps=[],
            search_frontiers=frontiers,
            provisional_ids=provisional,
        )

    def map_contradiction(
        self,
        left: Proposition,
        right: Proposition,
        relation: str = "incompatible_descriptions",
    ) -> ContradictionMap:
        """Record tension without selecting A or B as the truth by default."""
        if left.id == right.id:
            raise ValueError("a contradiction requires two distinct propositions")
        if left.state is EpistemicState.FORBIDDEN and right.state is EpistemicState.FORBIDDEN:
            third = EpistemicState.UNRESOLVED
        else:
            third = EpistemicState.UNRESOLVED
        return ContradictionMap(left.id, right.id, relation, third)

    def investigate_contradictions(
        self,
        contradictions: Iterable[Tuple[Proposition, Proposition]],
    ) -> List[ContradictionMap]:
        return [self.map_contradiction(left, right) for left, right in contradictions]

    def cross_perspective(
        self,
        views: Mapping[str, Sequence[Proposition]],
    ) -> Dict[str, object]:
        """Compare representations without assuming they share one ontology."""
        all_props = [p for props in views.values() for p in props]
        by_id: Dict[str, List[Tuple[str, Proposition]]] = {}
        for view_name, props in views.items():
            for prop in props:
                by_id.setdefault(prop.id, []).append((view_name, prop))

        invariants = [pid for pid, occurrences in by_id.items() if len(occurrences) > 1]
        differences = [pid for pid, occurrences in by_id.items() if len(occurrences) == 1]
        return {
            "view_count": len(views),
            "invariant_ids": sorted(invariants),
            "difference_ids": sorted(differences),
            "unresolved_view_count": len(views),
            "candidate_count": len(all_props),
        }

    def final_state(self, result: FrontierResult) -> EpistemicState:
        """Return a provisional aggregate; never collapse an unresolved frontier."""
        if result.search_frontiers:
            return EpistemicState.SEARCH_FRONTIER
        if result.provisional_ids:
            return EpistemicState.PROVISIONAL
        if result.propagated_ids:
            return EpistemicState.POSSIBLE
        return EpistemicState.KNOWN if result.closed_ids else EpistemicState.UNRESOLVED


__all__ = [
    "ContradictionMap",
    "EpistemicFrontierEngine",
    "EpistemicState",
    "FrontierConfig",
    "FrontierResult",
    "Proposition",
]
