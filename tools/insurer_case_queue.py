"""Insurer case queue state machine.

The queue governs operational routing only. It never promotes evidence to VERIFIED.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

STATES = (
    "INTAKE",
    "SCOPED",
    "READY_FOR_REPLAY",
    "QUEUED",
    "REPLAY",
    "VERIFY",
    "HUMAN_GATE",
    "REPORT",
    "BLOCKED",
    "CLOSED",
)

TRANSITIONS = {
    "INTAKE": {"SCOPED", "BLOCKED"},
    "SCOPED": {"READY_FOR_REPLAY", "BLOCKED"},
    "READY_FOR_REPLAY": {"QUEUED", "REPLAY", "BLOCKED"},
    "QUEUED": {"REPLAY", "BLOCKED"},
    "REPLAY": {"VERIFY", "BLOCKED"},
    "VERIFY": {"HUMAN_GATE", "BLOCKED"},
    "HUMAN_GATE": {"REPORT", "BLOCKED"},
    "REPORT": {"CLOSED", "BLOCKED"},
    "BLOCKED": {"INTAKE", "SCOPED", "READY_FOR_REPLAY", "QUEUED", "REPLAY", "VERIFY", "HUMAN_GATE"},
    "CLOSED": set(),
}

@dataclass(frozen=True)
class CaseState:
    case_ref: str
    state: str
    history: tuple[str, ...] = ()

    def transition(self, next_state: str) -> "CaseState":
        if next_state not in STATES:
            raise ValueError(f"unknown state: {next_state}")
        if next_state not in TRANSITIONS[self.state]:
            raise ValueError(f"invalid transition: {self.state} -> {next_state}")
        return CaseState(
            case_ref=self.case_ref,
            state=next_state,
            history=self.history + (next_state,),
        )

def plan_activation(cases: Iterable[CaseState], active_limit: int) -> list[CaseState]:
    """Move READY_FOR_REPLAY cases into REPLAY up to active_limit; queue the rest."""
    if active_limit < 0:
        raise ValueError("active_limit must be non-negative")
    active = 0
    planned = []
    for case in cases:
        if case.state != "READY_FOR_REPLAY":
            planned.append(case)
            continue
        if active < active_limit:
            planned.append(case.transition("REPLAY"))
            active += 1
        else:
            planned.append(case.transition("QUEUED"))
    return planned
