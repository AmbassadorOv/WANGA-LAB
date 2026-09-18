from __future__ import annotations
from typing import Any
from src.crypto.sha256_chain import build_chain, canonical_json
SCHEMA_VERSION = "8.0"

def build_audit(exposure: Any, screw: Any, recovery: Any, contract_hash: str | None = None, timestamp: str | None = None) -> dict[str, Any]:
    return {"schema_version": SCHEMA_VERSION, "audit": {"exposure":exposure,"screw":screw,"recovery":recovery},
            "integrity": build_chain(exposure,screw,recovery,timestamp),
            "legal_binding": {"contract_sha256":contract_hash} if contract_hash else None}

def canonical_bytes(package: dict[str, Any]) -> bytes:
    return canonical_json(package)
