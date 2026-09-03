"""ARK cognitive propagation / epistemic frontier engine.

This is a domain-agnostic computational model. It does not modify or expose
foundation-model weights; it operates on explicit states and configuration.

Core semantics:
    MUST        -> constrain / close branch
    FORBIDDEN   -> block / close branch
    POSSIBLE    -> propagate to the next cognitive node
    PROVISIONAL -> report without closure
    UNRESOLVED  -> preserve and expose a search frontier
    CONTRADICTION -> map the tension instead of selecting a winner

The engine deliberately does not manufacture an explanation for an
unrepresented X. It records a search frontier instead.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import product
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
class CategoryAddress:
    """A validated 3-axis address in the 21-category space."""

    x: int
    y: int
    z: int
    category_count: int = 21

    def __post_init__(self) -> None:
        for value in (self.x, self.y, self.z):
            if not 1 <= value <= self.category_count:
                raise ValueError(
                    f"category coordinate must be in 1..{self.category_count}"
                )

    @property
    def index(self) -> int:
        """Stable zero-based index for the 21^3 address space."""
        n = self.category_count
        return ((self.x - 1) * n + (self.y - 1)) * n + (self.z - 1)

    @property
    def cardinality(self) -> int:
        return self.category_count ** 3


@dataclass(frozen=True)
class Proposition:
    id: str
    state: EpistemicState
    category: int = 1
    source: str = "synthetic"
    address: Optional[CategoryAddress] = None

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("proposition id cannot be empty")
        if not 1 <= self.category <= 21:
            raise ValueError("category must be in 1..21")


@dataclass(frozen=True)
class ContradictionMap:
    left_id: str
    right_id: str
    relation: str
    third_state: EpistemicState = EpistemicState.UNRESOLVED


@dataclass(frozen=True)
class CognitiveTransition:
    """One explicit edge in the recursive cognitive path."""

    source_id: str
    target_id: str
    state: EpistemicState
    reason: str


@dataclass
class FrontierResult:
    input_count: int
    closed_ids: List[str]
    preserved_ids: List[str]
    propagated_ids: List[str]
    contradiction_maps: List[ContradictionMap]
    search_frontiers: List[str]
    provisional_ids: List[str]
    transitions: List[CognitiveTransition]

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

    @property
    def frontier_depth(self) -> int:
        if not self.transitions:
            return 0
        return max(
            max((index for index, _ in enumerate(self.transitions, start=1)), default=0),
            0,
        )

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
            "transitions": [
                {
                    "source_id": item.source_id,
                    "target_id": item.target_id,
                    "state": item.state.value,
                    "reason": item.reason,
                }
                for item in self.transitions
            ],
            "cognitive_preservation": self.cognitive_preservation,
            "closure_efficiency": self.closure_efficiency,
            "frontier_depth": self.frontier_depth,
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
        transitions: List[CognitiveTransition] = []

        for proposition in propositions:
            action = self._classify(proposition.state)
            if action == "close":
                closed.append(proposition.id)
            elif action == "propagate":
                propagated.append(proposition.id)
                preserved.append(proposition.id)
                transitions.append(
                    CognitiveTransition(
                        proposition.id,
                        proposition.id,
                        EpistemicState.POSSIBLE,
                        "POSSIBLE -> PROPAGATE",
                    )
                )
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
            transitions=transitions,
        )

    def propagate(self, propositions: Sequence[Proposition]) -> List[Proposition]:
        """Emit only active POSSIBLE nodes as candidates for the next node."""
        return [p for p in propositions if p.state is EpistemicState.POSSIBLE]

    def build_cognitive_path(
        self,
        propositions: Sequence[Proposition],
        next_state: EpistemicState = EpistemicState.PROVISIONAL,
    ) -> List[CognitiveTransition]:
        """Build a deterministic path without collapsing the source options."""
        path: List[CognitiveTransition] = []
        for proposition in self.propagate(propositions):
            target = f"{proposition.id}::next"
            path.append(
                CognitiveTransition(
                    proposition.id,
                    target,
                    next_state,
                    "propagated active possibility",
                )
            )
        return path

    def map_contradiction(
        self,
        left: Proposition,
        right: Proposition,
        relation: str = "incompatible_descriptions",
    ) -> ContradictionMap:
        """Record tension without selecting A or B as the truth by default."""
        if left.id == right.id:
            raise ValueError("a contradiction requires two distinct propositions")
        return ContradictionMap(left.id, right.id, relation)

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

    def category_addresses(self) -> Iterable[CategoryAddress]:
        """Enumerate the complete 21^3 routing space deterministically."""
        n = self.config.category_count
        return (
            CategoryAddress(x, y, z, n)
            for x, y, z in product(range(1, n + 1), repeat=3)
        )

    def final_state(self, result: FrontierResult) -> EpistemicState:
        """Return an aggregate state; never collapse an unresolved frontier."""
        if result.search_frontiers:
            return EpistemicState.SEARCH_FRONTIER
        if result.provisional_ids:
            return EpistemicState.PROVISIONAL
        if result.propagated_ids:
            return EpistemicState.POSSIBLE
        return EpistemicState.KNOWN if result.closed_ids else EpistemicState.UNRESOLVED


__all__ = [
    "CategoryAddress",
    "CognitiveTransition",
    "ContradictionMap",
    "EpistemicFrontierEngine",
    "EpistemicState",
    "FrontierConfig",
    "FrontierResult",
    "Proposition",
]
