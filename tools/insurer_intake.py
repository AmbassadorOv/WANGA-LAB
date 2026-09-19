"""Deterministic insurer intake triage for WANGA-LAB."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

VALID_STATUSES = {"READY_FOR_REPLAY","NEEDS_EVIDENCE","NEEDS_SCOPE","OUT_OF_SCOPE","PENDING_CLIENT_ACCESS"}

REQUIRED = ("case_ref","business_domain","system_model","claimed_or_observed_drift","requested_deliverable")

@dataclass(frozen=True)
class TriageResult:
    case_ref: str
    status: str
    missing: tuple[str, ...]
    blockers: tuple[str, ...]

def triage(record: Mapping[str, Any]) -> TriageResult:
    case_ref = str(record.get("case_ref", "")).strip() or "UNASSIGNED"
    missing = tuple(k for k in REQUIRED if not str(record.get(k, "")).strip())
    if missing:
        return TriageResult(case_ref, "NEEDS_SCOPE", missing, ("required_intake_fields",))
    if record.get("out_of_scope") is True:
        return TriageResult(case_ref, "OUT_OF_SCOPE", (), ("scope_boundary",))
    if record.get("client_access_required") is True and record.get("client_access_granted") is not True:
        return TriageResult(case_ref, "PENDING_CLIENT_ACCESS", (), ("client_access",))
    evidence = record.get("evidence", {})
    if not isinstance(evidence, Mapping):
        evidence = {}
    missing_evidence = tuple(k for k in ("baseline","outputs","provenance") if not evidence.get(k))
    if missing_evidence:
        return TriageResult(case_ref, "NEEDS_EVIDENCE", missing_evidence, ("evidence_package",))
    return TriageResult(case_ref, "READY_FOR_REPLAY", (), ())

def load_records(records: list[Mapping[str, Any]], active_limit: int) -> list[dict[str, Any]]:
    if active_limit < 0:
        raise ValueError("active_limit must be non-negative")
    results, active = [], 0
    for record in records:
        result = triage(record)
        status = result.status
        if status == "READY_FOR_REPLAY" and active >= active_limit:
            status = "QUEUED_FOR_REPLAY"
        elif status == "READY_FOR_REPLAY":
            active += 1
        results.append({"case_ref": result.case_ref, "status": status,
                        "missing": list(result.missing), "blockers": list(result.blockers)})
    return results
