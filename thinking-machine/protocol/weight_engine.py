"""
Contradiction Weight Engine
----------------------------
Structural signals regulate investigation/communication priority.
They are NOT truth probabilities and do not certify correctness.

Signals are aligned with the review protocol's distinction between
source, dependency, contradiction, depth, evidence, and resolution.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class WeightFactors:
    source: float = 0.0
    dependency: float = 0.0
    contradiction: float = 0.0
    depth: float = 0.0
    evidence: float = 0.0
    resolution: float = 0.0

def clamp(x: float) -> float:
    return max(0.0, min(1.0, float(x)))

def structural_weight(f: WeightFactors) -> float:
    value = (
        0.15 * clamp(f.source)
        + 0.20 * clamp(f.dependency)
        + 0.25 * clamp(f.contradiction)
        + 0.15 * clamp(f.depth)
        + 0.15 * clamp(f.evidence)
        + 0.10 * clamp(f.resolution)
    )
    return round(clamp(value), 6)

def access_weight_required(f: WeightFactors) -> float:
    return round(0.35 + 0.50 * structural_weight(f), 6)
