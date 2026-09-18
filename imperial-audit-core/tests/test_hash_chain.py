from src.crypto.sha256_chain import build_chain, verify_chain


def test_chain_verifies():
    chain = build_chain({"x": 1}, {"y": 2}, {"z": 3}, "2026-01-01T00:00:00Z")
    assert verify_chain({"x": 1}, {"y": 2}, {"z": 3}, "2026-01-01T00:00:00Z", chain)


def test_single_byte_change_changes_hash():
    a = build_chain({"x": 1}, {"y": 2}, {"z": 3}, "2026-01-01T00:00:00Z")
    b = build_chain({"x": 1}, {"y": 2}, {"z": 4}, "2026-01-01T00:00:00Z")
    assert a["S3"] != b["S3"]
    assert a["MASTER_CHAIN_HASH"] != b["MASTER_CHAIN_HASH"]


def test_rfc3161_missing_token_is_unknown():
    from src.crypto.rfc3161_timestamp import verify_rfc3161_token
    assert verify_rfc3161_token(None)["status"] == "UNKNOWN" if isinstance(verify_rfc3161_token(None), dict) else verify_rfc3161_token(None).status == "UNKNOWN"


def test_ots_missing_proof_is_unknown():
    from src.crypto.bitcoin_anchor import verify_ots_proof
    assert verify_ots_proof(None)["status"] == "UNKNOWN"
