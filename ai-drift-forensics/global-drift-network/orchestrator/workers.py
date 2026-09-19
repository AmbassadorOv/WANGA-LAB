"""Initial deterministic worker implementations for pipeline integration tests."""

from typing import Any, Dict
from worker_adapter import WorkerContext, WorkerResult, validate_result


class ObservationWorker:
    name = "observation"

    def execute(self, context: WorkerContext, payload: Dict[str, Any]) -> WorkerResult:
        result = WorkerResult(
            status="SUCCEEDED",
            output={
                "worker": self.name,
                "run_id": context.run_id,
                "input_hash": payload.get("input_hash"),
                "observation_status": "RECORDED",
            },
        )
        validate_result(result)
        return result


class RelationshipWorker:
    name = "relationship"

    def execute(self, context: WorkerContext, payload: Dict[str, Any]) -> WorkerResult:
        result = WorkerResult(
            status="SUCCEEDED",
            output={
                "worker": self.name,
                "run_id": context.run_id,
                "relationship_status": "RECORDED",
            },
        )
        validate_result(result)
        return result


class VerificationWorker:
    name = "verification"

    def execute(self, context: WorkerContext, payload: Dict[str, Any]) -> WorkerResult:
        result = WorkerResult(
            status="REVIEW",
            output={
                "worker": self.name,
                "run_id": context.run_id,
                "verification_status": "REQUIRES_EVIDENCE_REVIEW",
            },
            warnings=("No external evidence source attached in baseline mode.",),
        )
        validate_result(result)
        return result


class PublicationWorker:
    name = "publication"

    def execute(self, context: WorkerContext, payload: Dict[str, Any]) -> WorkerResult:
        # Publication is deliberately gated; this adapter never publishes itself.
        result = WorkerResult(
            status="BLOCKED",
            output={
                "worker": self.name,
                "run_id": context.run_id,
                "publication_status": "QUALITY_GATE_REQUIRED",
            },
        )
        validate_result(result)
        return result
