from .model import LetterGroup, LetterMetadata, SephirahLine


LETTER_REGISTRY: dict[str, LetterMetadata] = {
    # Sefer Yetzirah-style three Mothers / seven Doubles / twelve Simples.
    "א": LetterMetadata("א", LetterGroup.MOTHERS, "יסוד"),
    "מ": LetterMetadata("מ", LetterGroup.MOTHERS, "יסוד"),
    "ש": LetterMetadata("ש", LetterGroup.MOTHERS, "יסוד"),

    "ב": LetterMetadata("ב", LetterGroup.DOUBLES, "כפילות"),
    "ג": LetterMetadata("ג", LetterGroup.DOUBLES, "כפילות"),
    "ד": LetterMetadata("ד", LetterGroup.DOUBLES, "כפילות"),
    "כ": LetterMetadata("כ", LetterGroup.DOUBLES, "כפילות"),
    "פ": LetterMetadata("פ", LetterGroup.DOUBLES, "כפילות"),
    "ר": LetterMetadata("ר", LetterGroup.DOUBLES, "כפילות"),
    "ת": LetterMetadata("ת", LetterGroup.DOUBLES, "כפילות"),

    "ה": LetterMetadata("ה", LetterGroup.SIMPLE, "התפשטות"),
    "ו": LetterMetadata("ו", LetterGroup.SIMPLE, "התפשטות"),
    "ז": LetterMetadata("ז", LetterGroup.SIMPLE, "התפשטות"),
    "ח": LetterMetadata("ח", LetterGroup.SIMPLE, "התפשטות"),
    "ט": LetterMetadata("ט", LetterGroup.SIMPLE, "התפשטות"),
    "י": LetterMetadata("י", LetterGroup.SIMPLE, "התפשטות"),
    "ל": LetterMetadata("ל", LetterGroup.SIMPLE, "התפשטות"),
    "נ": LetterMetadata("נ", LetterGroup.SIMPLE, "התפשטות"),
    "ס": LetterMetadata("ס", LetterGroup.SIMPLE, "התפשטות"),
    "ע": LetterMetadata("ע", LetterGroup.SIMPLE, "התפשטות"),
    "צ": LetterMetadata("צ", LetterGroup.SIMPLE, "התפשטות"),
    "ק": LetterMetadata("ק", LetterGroup.SIMPLE, "התפשטות"),
}


SEPHIROTIC_REGISTRY: dict[str, SephirahLine] = {
    "כתר": SephirahLine.MIDDLE,
    "תפארת": SephirahLine.MIDDLE,
    "יסוד": SephirahLine.MIDDLE,
    "מלכות": SephirahLine.MIDDLE,
    "חכמה": SephirahLine.RIGHT_LEFT,
    "בינה": SephirahLine.RIGHT_LEFT,
    "חסד": SephirahLine.RIGHT_LEFT,
    "גבורה": SephirahLine.RIGHT_LEFT,
    "נצח": SephirahLine.RIGHT_LEFT,
    "הוד": SephirahLine.RIGHT_LEFT,
}
