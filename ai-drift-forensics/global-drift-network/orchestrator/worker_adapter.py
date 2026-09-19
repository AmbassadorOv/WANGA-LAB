"""Stable adapter contract between the Orchestrator and workers.

Workers receive immutable task input and return a serializable result.
They must not mutate run state or publish externally.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Protocol


@dataclass(frozen=True)
class WorkerContext:
    run_id: str
    task_id: str
    input_snapshot_id: str
    attempt: int
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkerResult:
    status: str
    output: Dict[str, Any]
    evidence_ids: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


class Worker(Protocol):
    name: str

    def execute(self, context: WorkerContext, payload: Dict[str, Any]) -> WorkerResult:
        ...


def validate_result(result: WorkerResult) -> None:
    """Reject malformed worker results before they enter run state."""
    if result.status not in {"SUCCEEDED", "REVIEW", "BLOCKED", "FAILED"}:
        raise ValueError(f"Invalid worker status: {result.status}")
    if not isinstance(result.output, dict):
        raise TypeError("Worker output must be a dictionary")
    if not isinstance(result.evidence_ids, tuple):
        raise TypeError("evidence_ids must be a tuple")
