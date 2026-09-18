"""Independent verification of audit integrity and external evidence."""

from __future__ import annotations

from typing import Any

from ..crypto.sha256_chain import verify_chain


def verify_audit(
    audit: dict[str, Any],
    *,
    external_timestamp_verified: bool | None,
    external_anchor_verified: bool | None,
) -> dict[str, Any]:
    """Return PASS/FAIL/UNKNOWN without treating missing external evidence as success."""
    required = ("timestamp_utc", "chain", "S1", "S2", "S3")
    if any(k not in audit for k in required):
        return {"status": "FAIL", "errors": ["AUDIT_SCHEMA_INCOMPLETE"]}
    try:
        local_ok = verify_chain(audit["S1"], audit["S2"], audit["S3"], audit["timestamp_utc"], audit["chain"].get("LEGAL_CONTRACT_HASH", "")) == audit["chain"]
    except Exception as exc:
        return {"status": "FAIL", "errors": [f"INTEGRITY_EXCEPTION:{type(exc).__name__}"]}
    if not local_ok:
        return {"status": "FAIL", "errors": ["HASH_CHAIN_MISMATCH"]}
    errors=[]
    if external_timestamp_verified is not True:
        errors.append("TIMESTAMP_UNVERIFIED")
    if external_anchor_verified is not True:
        errors.append("ANCHOR_UNVERIFIED")
    return {"status": "UNKNOWN", "errors": errors} if errors else {"status": "PASS", "errors": []}
