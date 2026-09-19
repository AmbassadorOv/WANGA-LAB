"""Deterministic continuity planning engine.

This module models exposure, reserve, coverage and stress-test relationships.
It does not issue insurance, price policies, or make underwriting decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import json


@dataclass(frozen=True)
class Exposure:
    exposure_id: str
    amount: float
    currency: str
    verified: bool = False

    def __post_init__(self) -> None:
        if not self.exposure_id:
            raise ValueError("exposure_id is required")
        if self.amount < 0:
            raise ValueError("amount must be non-negative")
        if not self.currency:
            raise ValueError("currency is required")


@dataclass(frozen=True)
class Coverage:
    coverage_id: str
    capacity: float
    retention: float = 0.0
    status: str = "PLANNED"

    def __post_init__(self) -> None:
        if not self.coverage_id:
            raise ValueError("coverage_id is required")
        if self.capacity < 0 or self.retention < 0:
            raise ValueError("capacity and retention must be non-negative")
        if self.status not in {"PLANNED", "QUOTED", "BOUND", "ACTIVE", "EXPIRED"}:
            raise ValueError("unsupported coverage status")


@dataclass(frozen=True)
class StressScenario:
    scenario_id: str
    loss_factor: float

    def __post_init__(self) -> None:
        if not self.scenario_id:
            raise ValueError("scenario_id is required")
        if not 0 <= self.loss_factor <= 1:
            raise ValueError("loss_factor must be between 0 and 1")


@dataclass
class ContinuityPlan:
    plan_id: str
    exposures: list[Exposure] = field(default_factory=list)
    coverages: list[Coverage] = field(default_factory=list)
    scenarios: list[StressScenario] = field(default_factory=list)

    def total_exposure(self) -> float:
        return sum(item.amount for item in self.exposures)

    def verified_exposure(self) -> float:
        return sum(item.amount for item in self.exposures if item.verified)

    def active_capacity(self) -> float:
        return sum(
            item.capacity
            for item in self.coverages
            if item.status == "ACTIVE"
        )

    def coverage_gap(self) -> float:
        return max(0.0, self.verified_exposure() - self.active_capacity())

    def stress_result(self, scenario_id: str) -> dict[str, float | str]:
        scenario = next(
            (item for item in self.scenarios if item.scenario_id == scenario_id),
            None,
        )
        if scenario is None:
            raise KeyError(f"unknown scenario: {scenario_id}")

        stressed_loss = self.verified_exposure() * scenario.loss_factor
        uncovered_loss = max(0.0, stressed_loss - self.active_capacity())
        return {
            "scenario_id": scenario.scenario_id,
            "stressed_loss": stressed_loss,
            "active_capacity": self.active_capacity(),
            "uncovered_loss": uncovered_loss,
        }

    def audit_digest(self) -> str:
        payload = {
            "plan_id": self.plan_id,
            "exposures": [
                {
                    "id": item.exposure_id,
                    "amount": item.amount,
                    "currency": item.currency,
                    "verified": item.verified,
                }
                for item in sorted(self.exposures, key=lambda x: x.exposure_id)
            ],
            "coverages": [
                {
                    "id": item.coverage_id,
                    "capacity": item.capacity,
                    "retention": item.retention,
                    "status": item.status,
                }
                for item in sorted(self.coverages, key=lambda x: x.coverage_id)
            ],
            "scenarios": [
                {
                    "id": item.scenario_id,
                    "loss_factor": item.loss_factor,
                }
                for item in sorted(self.scenarios, key=lambda x: x.scenario_id)
            ],
        }
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        return sha256(encoded).hexdigest()
