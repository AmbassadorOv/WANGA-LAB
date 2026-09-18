"""Deterministic audit artifact generator."""

from __future__ import annotations

from typing import Any

from ..crypto.sha256_chain import build_chain


def generate_audit(s1: Any, s2: Any, s3: Any, *, captured_at: str) -> dict[str, Any]:
    """Generate an artifact using explicit capture metadata; never read wall-clock time."""
    return {
        "timestamp_utc": captured_at,
        "chain": build_chain(s1, s2, s3, captured_at),
        "S1": s1,
        "S2": s2,
        "S3": s3,
    }
