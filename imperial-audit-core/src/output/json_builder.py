"""Canonical JSON builder."""

from __future__ import annotations
import json
from typing import Any

def build_audit_json(audit: dict[str, Any]) -> str:
    return json.dumps(audit, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
