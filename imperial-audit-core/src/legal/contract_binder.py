"""Bind a legal-agreement digest to an audit artifact."""

from __future__ import annotations
import hashlib
from pathlib import Path

def sha256_file(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def bind_contract(audit_hash: str, contract_hash: str) -> str:
    if len(audit_hash) != 64 or len(contract_hash) != 64:
        raise ValueError("Expected SHA-256 hashes")
    return hashlib.sha256(f"AUDIT={audit_hash}\nCONTRACT={contract_hash}".encode()).hexdigest()
