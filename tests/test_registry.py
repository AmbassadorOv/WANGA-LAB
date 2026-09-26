from holographic_string_nn import HEBREW_LETTERS, LETTER_REGISTRY


def test_registry_has_all_22_letters():
    assert len(HEBREW_LETTERS) == 22
    assert set(HEBREW_LETTERS) == set(LETTER_REGISTRY)


def test_group_counts_are_3_7_12():
    counts = {}
    for metadata in LETTER_REGISTRY.values():
        counts[metadata.group] = counts.get(metadata.group, 0) + 1
    assert counts[metadata.group.__class__.MOTHERS] == 3
    assert counts[metadata.group.__class__.DOUBLES] == 7
    assert counts[metadata.group.__class__.SIMPLE] == 12
