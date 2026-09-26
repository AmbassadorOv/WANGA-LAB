from __future__ import annotations

from dataclasses import dataclass

from .model import HolographicStringNode
from .policy import CollapseDecision, CollapsePolicy


@dataclass(frozen=True)
class NodeEvaluation:
    letter: str
    group: str
    sephirah_line: str
    coherence: float
    decision: str
    state: str


class HolographicStringEngine:
    """Minimal execution engine for the symbolic collapse policy."""

    def __init__(self, policy: CollapsePolicy | None = None) -> None:
        self.policy = policy or CollapsePolicy()

    def evaluate(self, node: HolographicStringNode) -> NodeEvaluation:
        decision = self.policy.apply(node)
        return NodeEvaluation(
            letter=node.letter,
            group=node.group.value,
            sephirah_line=node.sephirah_line.value,
            coherence=node.coherence,
            decision=decision.value,
            state=node.state,
        )

    def evaluate_many(
        self, nodes: list[HolographicStringNode]
    ) -> list[NodeEvaluation]:
        return [self.evaluate(node) for node in nodes]
