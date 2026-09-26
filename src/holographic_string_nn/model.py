from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final


HEBREW_LETTERS: Final[tuple[str, ...]] = (
    "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ",
    "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת",
)


class LetterGroup(str, Enum):
    MOTHERS = "אמות"
    DOUBLES = "כפולות"
    SIMPLE = "פשוטות"


class SephirahLine(str, Enum):
    MIDDLE = "קו האמצע"
    RIGHT_LEFT = "ימין-שמאל"
    ABOVE_BELOW = "מעל-מתחת"


@dataclass(frozen=True)
class LetterMetadata:
    letter: str
    group: LetterGroup
    name_weight: str


@dataclass
class HolographicStringNode:
    """One of the 22 symbolic nodes.

    No numeric neural weight is assigned to the letter itself.  The
    node carries symbolic identity plus a measured coherence value.
    """

    letter: str
    group: LetterGroup
    sephirah_line: SephirahLine
    coherence: float = 0.0
    state: str = "SUPERPOSITION"

    def __post_init__(self) -> None:
        if self.letter not in HEBREW_LETTERS:
            raise ValueError(f"Unknown Hebrew letter: {self.letter!r}")
        if not 0.0 <= self.coherence <= 1.0:
            raise ValueError("coherence must be in [0, 1]")

    @property
    def symbolic_weight(self) -> tuple[LetterGroup, SephirahLine]:
        """The non-numeric weight: letter identity + Sephirotic location."""
        return self.group, self.sephirah_line

    def update_coherence(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError("coherence must be in [0, 1]")
        self.coherence = value

    def hold_superposition(self) -> None:
        self.state = "SUPERPOSITION"

    def collapse(self) -> None:
        self.state = "GROUNDED_CONCLUSION"
