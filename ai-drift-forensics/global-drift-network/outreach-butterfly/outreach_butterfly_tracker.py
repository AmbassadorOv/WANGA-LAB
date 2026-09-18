"""WANGA outreach-to-network propagation tracker.

This module is intentionally descriptive: it records outreach events, joins
observations by time windows, compares observed change with a declared
baseline, and emits reproducible relationship candidates. It does not infer
causality and never promotes an unverified relationship to evidence.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from math import sqrt
from typing import Iterable, Optional


@dataclass(frozen=True)
class OutreachEvent:
    event_id: str
    sender: str
    recipient: str
    timestamp: datetime
    subject_class: str
    requested_action: str
    target_sector: str


@dataclass(frozen=True)
class Observation:
    observation_id: str
    entity: str
    timestamp: datetime
    move_type: str
    asset_or_domain: str
    counterparty: Optional[str] = None
    direction: Optional[str] = None
    magnitude: Optional[float] = None
    confidence: float = 1.0


@dataclass(frozen=True)
class Baseline:
    expected_rate: float
    expected_mean: float = 0.0
    expected_std: float = 1.0


@dataclass(frozen=True)
class ButterflySignal:
    event_id: str
    recipient: str
    observation_id: str
    time_delta_hours: float
    temporal_overlap: float
    action_similarity: float
    counterparty_overlap: float
    asset_overlap: float
    sequence_similarity: float
    baseline_deviation: float
    propagation_depth: int
    propagation_width: int
    evidence_confidence: float
    status: str


class OutreachButterflyTracker:
    """Deterministic first-pass tracker for outreach-linked propagation."""

    def __init__(
        self,
        *,
        pre_window_hours: int = 168,
        post_window_hours: int = 168,
        temporal_half_life_hours: float = 48.0,
        minimum_confidence: float = 0.70,
        butterfly_threshold: float = 0.65,
    ) -> None:
        if pre_window_hours < 0 or post_window_hours < 0:
            raise ValueError("windows must be non-negative")
        if temporal_half_life_hours <= 0:
            raise ValueError("temporal_half_life_hours must be positive")
        if not 0 <= minimum_confidence <= 1:
            raise ValueError("minimum_confidence must be in [0,1]")
        if not 0 <= butterfly_threshold <= 1:
            raise ValueError("butterfly_threshold must be in [0,1]")
        self.pre_window_hours = pre_window_hours
        self.post_window_hours = post_window_hours
        self.temporal_half_life_hours = temporal_half_life_hours
        self.minimum_confidence = minimum_confidence
        self.butterfly_threshold = butterfly_threshold

    @staticmethod
    def _similarity(a: Optional[str], b: Optional[str]) -> float:
        if not a or not b:
            return 0.0
        return 1.0 if a.casefold() == b.casefold() else 0.0

    def _temporal_overlap(self, delta_hours: float) -> float:
        if delta_hours < 0 or delta_hours > self.post_window_hours:
            return 0.0
        return 2 ** (-delta_hours / self.temporal_half_life_hours)

    def _baseline_deviation(self, observation: Observation, baseline: Baseline) -> float:
        if observation.magnitude is None:
            return 0.0
        z = abs(observation.magnitude - baseline.expected_mean) / max(
            abs(baseline.expected_std), 1e-12
        )
        return min(z / 3.0, 1.0)

    def evaluate(
        self,
        event: OutreachEvent,
        observation: Observation,
        *,
        baseline: Baseline,
        previous_observations: Iterable[Observation] = (),
    ) -> ButterflySignal:
        delta_hours = (
            observation.timestamp - event.timestamp
        ).total_seconds() / 3600.0
        temporal = self._temporal_overlap(delta_hours)

        action_similarity = self._similarity(
            event.requested_action, observation.move_type
        )
        asset_similarity = self._similarity(event.target_sector, observation.asset_or_domain)
        counterparty_similarity = self._similarity(event.recipient, observation.entity)

        prior = list(previous_observations)
        prior_same_entity = [
            x for x in prior
            if x.entity.casefold() == observation.entity.casefold()
            and x.timestamp < observation.timestamp
        ]
        sequence_similarity = 1.0 if prior_same_entity else 0.0

        baseline_deviation = self._baseline_deviation(observation, baseline)

        raw = (
            0.25 * temporal
            + 0.15 * action_similarity
            + 0.15 * counterparty_similarity
            + 0.15 * asset_similarity
            + 0.10 * sequence_similarity
            + 0.20 * baseline_deviation
        )
        evidence_confidence = min(
            observation.confidence,
            1.0 if baseline.expected_std != 0 else 0.0,
        )

        score = raw * evidence_confidence
        if evidence_confidence < self.minimum_confidence:
            status = "INSUFFICIENT_EVIDENCE"
        elif score >= self.butterfly_threshold:
            status = "BUTTERFLY_SIGNAL"
        elif score >= 0.40:
            status = "POSSIBLE_PROPAGATION"
        else:
            status = "NORMAL_OR_UNRELATED"

        return ButterflySignal(
            event_id=event.event_id,
            recipient=event.recipient,
            observation_id=observation.observation_id,
            time_delta_hours=delta_hours,
            temporal_overlap=round(temporal, 6),
            action_similarity=action_similarity,
            counterparty_overlap=counterparty_similarity,
            asset_overlap=asset_similarity,
            sequence_similarity=sequence_similarity,
            baseline_deviation=round(baseline_deviation, 6),
            propagation_depth=1 if temporal > 0 else 0,
            propagation_width=1 if temporal > 0 else 0,
            evidence_confidence=round(evidence_confidence, 6),
            status=status,
        )

    @staticmethod
    def to_record(signal: ButterflySignal) -> dict:
        return asdict(signal)
