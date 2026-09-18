"""Canonical SHA-256 evidence chain.

The chain is deterministic: callers supply the UTC timestamp that is being
committed. No wall-clock value is generated inside the hash function.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_chain(
    s1: Any,
    s2: Any,
    s3: Any,
    timestamp: str,
    legal_contract_hash: str = "",
) -> dict[str, str]:
    """Build S1/S2/S3 and the master commitment.

    legal_contract_hash is optional for backward compatibility. New
    evidence packages should always provide it when a contract is in scope.
    """
    s1_hash = sha256_hex(canonical_bytes(s1))
    s2_hash = sha256_hex(canonical_bytes(s2))
    s3_hash = sha256_hex(canonical_bytes(s3))

    master_payload = (
        f"S1={s1_hash}\n"
        f"S2={s2_hash}\n"
        f"S3={s3_hash}\n"
        f"TIMESTAMP={timestamp}\n"
        f"LEGAL_CONTRACT_HASH={legal_contract_hash}"
    ).encode("utf-8")

    return {
        "S1": s1_hash,
        "S2": s2_hash,
        "S3": s3_hash,
        "TIMESTAMP_UTC": timestamp,
        "LEGAL_CONTRACT_HASH": legal_contract_hash,
        "MASTER_CHAIN_HASH": sha256_hex(master_payload),
    }


def verify_chain(
    s1: Any,
    s2: Any,
    s3: Any,
    timestamp: str,
    chain: dict[str, str],
    legal_contract_hash: str = "",
) -> bool:
    expected = build_chain(
        s1,
        s2,
        s3,
        timestamp,
        legal_contract_hash,
    )
    return expected == chain
