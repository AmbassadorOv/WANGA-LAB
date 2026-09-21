"""Deterministic governance mediation boundary.

The mediation layer is a buffer between heterogeneous actors/systems.
It does not decide substantive truth or exercise authority over recipients.
It normalizes claims, preserves provenance, detects conflicts, and produces
a stable hand-off packet for human/institutional decision processes.
"""

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Any


class MediationState(str, Enum):
    RECEIVED = "RECEIVED"
    BUFFERED = "BUFFERED"
    CONFLICT = "CONFLICT"
    STABILIZED = "STABILIZED"
    QUARANTINED = "QUARANTINED"


@dataclass(frozen=True)
class GovernanceClaim:
    actor_id: str
    domain: str
    statement: str
    evidence_ref: str
    provenance_ref: str


@dataclass(frozen=True)
class MediationPacket:
    state: MediationState
    claims: tuple[GovernanceClaim, ...]
    conflicts: tuple[tuple[str, str], ...]
    common_frame: dict[str, Any]
    integrity_sha256: str


class GovernanceMediator:
    """Create auditable mediation packets without resolving disputed substance."""

    def mediate(self, claims: list[GovernanceClaim]) -> MediationPacket:
        if not claims:
            raise ValueError("at least one claim is required")

        canonical = sorted(
            claims,
            key=lambda c: (c.domain, c.actor_id, c.statement, c.evidence_ref),
        )

        conflicts: list[tuple[str, str]] = []
        for i, left in enumerate(canonical):
            for right in canonical[i + 1 :]:
                if left.domain == right.domain and left.statement != right.statement:
                    conflicts.append((left.actor_id, right.actor_id))

        common_frame = {
            "domains": sorted({c.domain for c in canonical}),
            "actors": sorted({c.actor_id for c in canonical}),
            "evidence_refs": sorted({c.evidence_ref for c in canonical}),
            "provenance_refs": sorted({c.provenance_ref for c in canonical}),
            "substantive_resolution": False,
        }

        payload = {
            "claims": [c.__dict__ for c in canonical],
            "conflicts": conflicts,
            "common_frame": common_frame,
        }
        digest = sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()

        state = (
            MediationState.CONFLICT
            if conflicts
            else MediationState.STABILIZED
        )
        return MediationPacket(
            state=state,
            claims=tuple(canonical),
            conflicts=tuple(conflicts),
            common_frame=common_frame,
            integrity_sha256=digest,
        )
