"""Minimal deterministic audit generator."""

from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from ..crypto.sha256_chain import build_chain

def generate_audit(s1: Any, s2: Any, s3: Any) -> dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()
    return {"timestamp_utc": timestamp, "chain": build_chain(s1, s2, s3, timestamp), "S1": s1, "S2": s2, "S3": s3}
