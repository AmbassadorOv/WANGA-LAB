"""ARK Holographic String Neural Network.

A deterministic research implementation of the 22-letter alphabetic/
Sephirotic weighting model described in the ARK-Kernel specification.
"""

from .model import (
    HEBREW_LETTERS,
    LetterGroup,
    SephirahLine,
    HolographicStringNode,
)
from .policy import CollapsePolicy, CollapseDecision
from .registry import LETTER_REGISTRY, SEPHIROTIC_REGISTRY

__all__ = [
    "HEBREW_LETTERS",
    "LetterGroup",
    "SephirahLine",
    "HolographicStringNode",
    "CollapsePolicy",
    "CollapseDecision",
    "LETTER_REGISTRY",
    "SEPHIROTIC_REGISTRY",
]

__version__ = "0.1.0"
