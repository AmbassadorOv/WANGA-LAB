"""End-to-end deterministic insurer intake router.

Triage is followed by bounded activation. Only replay-ready cases can enter the
forensic execution queue. Verification and reporting remain downstream gates.
"""
from __future__ import annotations
from typing import Any, Mapping
from tools.insurer_intake import triage
from tools.insurer_case_queue import CaseState, plan_activation

def build_pipeline(records: list[Mapping[str, Any]], active_limit: int) -> list[dict[str, Any]]:
    triaged = [triage(r) for r in records]
    states = [
        CaseState(t.case_ref, "READY_FOR_REPLAY") if t.status == "READY_FOR_REPLAY"
        else CaseState(t.case_ref, "BLOCKED")
        for t in triaged
    ]
    activated = plan_activation(states, active_limit)
    result = []
    for t, s in zip(triaged, activated):
        if t.status != "READY_FOR_REPLAY":
            result.append({
                "case_ref": t.case_ref,
                "intake_status": t.status,
                "execution_state": "BLOCKED",
                "missing": list(t.missing),
                "blockers": list(t.blockers),
            })
        else:
            result.append({
                "case_ref": t.case_ref,
                "intake_status": t.status,
                "execution_state": s.state,
                "missing": [],
                "blockers": [],
            })
    return result
