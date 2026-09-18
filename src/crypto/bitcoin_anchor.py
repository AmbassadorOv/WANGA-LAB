from __future__ import annotations
import hashlib
from pathlib import Path

def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def build_anchor_manifest(path: str | Path) -> dict[str, str]:
    return {"file":Path(path).name,"sha256":sha256_file(path),"anchoring_system":"OpenTimestamps/Bitcoin","status":"NOT_SUBMITTED"}
