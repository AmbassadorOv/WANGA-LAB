from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from typing import Any

def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def build_chain(exposure: Any, screw: Any, recovery: Any, timestamp: str | None = None) -> dict[str, str]:
    ts = timestamp or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    s1, s2, s3 = (sha256_hex(canonical_json(x)) for x in (exposure, screw, recovery))
    return {"S1": s1, "S2": s2, "S3": s3, "timestamp": ts,
            "MASTER_CHAIN_HASH": sha256_hex(canonical_json({"S1":s1,"S2":s2,"S3":s3,"timestamp":ts}))}

def verify_chain(evidence: dict[str, Any]) -> bool:
    if not all(k in evidence for k in ("exposure","screw","recovery","chain")): return False
    return build_chain(evidence["exposure"], evidence["screw"], evidence["recovery"], evidence["chain"]["timestamp"]) == evidence["chain"]
