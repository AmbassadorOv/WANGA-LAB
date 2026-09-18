"""Canonical SHA-256 chain for S1/S2/S3 and MASTER."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    )


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_chain(s1: Any, s2: Any, s3: Any, timestamp: str) -> dict[str, str]:
    s1_hash = sha256_hex(canonical_bytes(s1))
    s2_hash = sha256_hex(canonical_bytes(s2))
    s3_hash = sha256_hex(canonical_bytes(s3))
    master_payload = (
        f"S1={s1_hash}\n"
        f"S2={s2_hash}\n"
        f"S3={s3_hash}\n"
        f"TIMESTAMP={timestamp}"
    ).encode("utf-8")
    return {
        "S1": s1_hash,
        "S2": s2_hash,
        "S3": s3_hash,
        "MASTER_CHAIN_HASH": sha256_hex(master_payload),
    }


def verify_chain(
    s1: Any,
    s2: Any,
    s3: Any,
    timestamp: str,
    chain: dict[str, str],
) -> bool:
    expected = build_chain(s1, s2, s3, timestamp)
    return expected == chain
