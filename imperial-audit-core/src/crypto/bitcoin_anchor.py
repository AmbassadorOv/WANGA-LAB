"""Public-anchor boundary; no fabricated external confirmation."""
from __future__ import annotations


def create_ots_submission(digest_hex: str) -> dict[str, str]:
    if len(digest_hex) != 64:
        raise ValueError("Expected SHA-256 digest")
    int(digest_hex, 16)
    return {"digest": digest_hex, "status": "PENDING_EXTERNAL_ANCHOR"}


def verify_ots_proof(proof: bytes | None) -> dict[str, str]:
    if not proof:
        return {"status": "UNKNOWN", "reason": "ANCHOR_PROOF_MISSING"}
    return {"status": "UNKNOWN", "reason": "EXTERNAL_ANCHOR_PARSER_NOT_CONFIGURED"}
