from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
from typing import Any, Callable, Dict, Iterable, List
import json


@dataclass(frozen=True)
class Task:
    request_id: str
    task_id: str
    role: str
    input: Any
    constraints: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceRecord:
    stage: str
    status: str
    digest: str
    detail: Dict[str, Any] = field(default_factory=dict)


class WangaRuntime:
    """Deterministic local runtime for the first executable WANGA POC.

    This is deliberately provider-neutral: it proves routing, state transitions,
    verification and evidence emission without claiming production model quality.
    """

    def __init__(self, handlers: Dict[str, Callable[[Task], Dict[str, Any]]] | None = None):
        self.handlers = handlers or {
            "planner": self._default_handler,
            "implementer": self._default_handler,
            "verifier": self._default_handler,
        }

    @staticmethod
    def _digest(value: Any) -> str:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        return sha256(payload.encode("utf-8")).hexdigest()

    @classmethod
    def _request_id(cls, user_input: Any) -> str:
        return f"req-{cls._digest(user_input)[:16]}"

    @classmethod
    def _task_id(cls, request_id: str, role: str) -> str:
        return f"task-{cls._digest({'request_id': request_id, 'role': role})[:16]}"

    @staticmethod
    def _default_handler(task: Task) -> Dict[str, Any]:
        return {
            "role": task.role,
            "task_id": task.task_id,
            "input": task.input,
            "status": "COMPLETED",
        }

    def run(self, user_input: Any, roles: Iterable[str] = ("planner", "implementer", "verifier")) -> Dict[str, Any]:
        request_id = self._request_id(user_input)
        state: List[str] = ["INGESTED"]
        evidence: List[EvidenceRecord] = []
        results: List[Dict[str, Any]] = []

        for role in roles:
            if role not in self.handlers:
                state.append("FAILED")
                evidence.append(EvidenceRecord("ROUTE", "FAIL", self._digest(role), {"unknown_role": role}))
                return self._report(request_id, state, results, evidence)
            state.append(f"ROUTED:{role}")
            task = Task(request_id, self._task_id(request_id, role), role, user_input)
            result = self.handlers[role](task)
            results.append(result)
            digest = self._digest(result)
            status = result.get("status", "UNKNOWN")
            evidence.append(EvidenceRecord(role.upper(), status, digest, {"task_id": task.task_id}))
            if status != "COMPLETED":
                state.append("FAILED")
                return self._report(request_id, state, results, evidence)
            state.append(f"COMPLETED:{role}")

        verification_input = {"request_id": request_id, "results": results}
        verification_digest = self._digest(verification_input)
        state.extend(["VERIFIED", "EVIDENCE_EMITTED", "COMPLETED"])
        evidence.append(EvidenceRecord("VERIFY", "PASS", verification_digest, {"result_count": len(results)}))
        return self._report(request_id, state, results, evidence)

    @staticmethod
    def _report(request_id: str, state: List[str], results: List[Dict[str, Any]], evidence: List[EvidenceRecord]) -> Dict[str, Any]:
        return {
            "request_id": request_id,
            "state": state,
            "results": results,
            "evidence": [asdict(item) for item in evidence],
            "verification_status": "PASSED" if state[-1] == "COMPLETED" else "FAILED",
        }
