from src.crypto.sha256_chain import build_chain, verify_chain


def test_chain_verifies():
    chain = build_chain(
        {"x": 1},
        {"y": 2},
        {"z": 3},
        "2026-01-01T00:00:00Z",
    )
    assert verify_chain(
        {"x": 1},
        {"y": 2},
        {"z": 3},
        "2026-01-01T00:00:00Z",
        chain,
    )


def test_single_byte_change_changes_hash():
    a = build_chain({"x": 1}, {"y": 2}, {"z": 3}, "2026-01-01T00:00:00Z")
    b = build_chain({"x": 1}, {"y": 2}, {"z": 4}, "2026-01-01T00:00:00Z")
    assert a["S3"] != b["S3"]
    assert a["MASTER_CHAIN_HASH"] != b["MASTER_CHAIN_HASH"]
