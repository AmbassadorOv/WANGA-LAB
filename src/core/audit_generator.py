from __future__ import annotations
from typing import Any
from src.output.json_builder import build_audit

def generate(exposure: Any, screw: Any, recovery: Any, contract_hash: str | None = None, timestamp: str | None = None):
    return build_audit(exposure, screw, recovery, contract_hash, timestamp)
