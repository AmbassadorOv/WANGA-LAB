"""Public sandbox seam for the three-layer SY-NeuroKernel logic model.

This module deliberately does not implement the protected Rational Logic core.
It exposes a deterministic interface between:
1. CrystalSymmetricLogic — fixed K22 / 231-pair topology.
2. LetterContractionExpansionLogic — state contraction/expansion over the same 22 addresses.
3. FractalRationalLogic — composition + structured communication packets.

Status: PROTOTYPED until repository tests and independent verification are complete.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import tanh
from typing import Sequence


N = 22


class Provenance(str, Enum):
    STRUCTURAL_SOURCE = "STRUCTURAL_SOURCE"
    COMPUTED = "COMPUTED"
    GENERATED_MESSAGE = "GENERATED_MESSAGE"


@dataclass(frozen=True)
class LogicMessage:
    kind: str
    depth: int
    source: str
    payload: tuple[float, ...]
    provenance: Provenance


def _check_state(state: Sequence[float]) -> tuple[float, ...]:
    values = tuple(float(x) for x in state)
    if len(values) != N:
        raise ValueError("state must contain exactly 22 values")
    return values


class CrystalSymmetricLogic:
    """Scores the immutable unordered K22 gate space."""

    def __init__(self) -> None:
        self.gates = tuple(
            (a, b) for a in range(N) for b in range(a + 1, N)
        )
        if len(self.gates) != 231:
            raise AssertionError("K22 must contain exactly 231 unordered gates")

    def evaluate(self, state: Sequence[float]) -> tuple[float, ...]:
        values = _check_state(state)
        # Symmetric gate response: swapping endpoints cannot change the score.
        return tuple((values[a] + values[b]) / 2.0 for a, b in self.gates)


class LetterContractionExpansionLogic:
    """Deterministic contraction/expansion state transform over 22 addresses."""

    def transform(
        self,
        state: Sequence[float],
        contraction: float,
        expansion: float,
    ) -> tuple[float, ...]:
        values = _check_state(state)
        if not 0.0 <= contraction <= 1.0:
            raise ValueError("contraction must be in [0, 1]")
        if not 0.0 <= expansion <= 1.0:
            raise ValueError("expansion must be in [0, 1]")

        center = sum(values) / N
        contracted = tuple(
            center + (value - center) * (1.0 - contraction)
            for value in values
        )
        mean_abs = sum(abs(x - center) for x in contracted) / N
        if mean_abs == 0.0 or expansion == 0.0:
            return contracted

        # Expansion restores contrast around the same center without creating
        # new addresses or relations.
        gain = 1.0 + expansion
        return tuple(
            center + (value - center) * gain for value in contracted
        )


class FractalRationalLogic:
    """Composition layer that turns two deterministic views into communication."""

    def __init__(self) -> None:
        self.crystal = CrystalSymmetricLogic()
        self.letters = LetterContractionExpansionLogic()

    def step(
        self,
        state: Sequence[float],
        contraction: float,
        expansion: float,
        depth: int = 0,
    ) -> LogicMessage:
        values = _check_state(state)
        transformed = self.letters.transform(values, contraction, expansion)
        gate_scores = self.crystal.evaluate(transformed)

        # Collapse 231 gate scores back to 22 address signals by deterministic
        # incidence averaging. This is an architectural bridge, not the
        # protected Rational Logic implementation.
        accum = [0.0] * N
        counts = [0] * N
        for score, (a, b) in zip(gate_scores, self.crystal.gates):
            accum[a] += score
            accum[b] += score
            counts[a] += 1
            counts[b] += 1
        fused = tuple(
            tanh(accum[i] / counts[i]) for i in range(N)
        )

        return LogicMessage(
            kind="NEURAL_DIALOGUE_STATE",
            depth=depth,
            source="FractalRationalLogic",
            payload=fused,
            provenance=Provenance.GENERATED_MESSAGE,
        )

    def speak(
        self,
        state: Sequence[float],
        contraction: float,
        expansion: float,
        depth: int = 0,
    ) -> LogicMessage:
        """Emit a structured message instead of returning an untyped score."""
        return self.step(state, contraction, expansion, depth)
