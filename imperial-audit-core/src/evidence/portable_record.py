"""Platform-neutral Imperial Evidence Record (IER) package builder."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

IER_VERSION = "1.0"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_ier_manifest(root: str | Path) -> dict[str, Any]:
    root = Path(root)
    audit_path = root / "audit_output.json"
    if not audit_path.is_file():
        raise FileNotFoundError("audit_output.json is required")

    files: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel == "manifest.json":
            continue
        files[rel] = sha256_file(path)

    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    hashes = audit.get("cryptographic_integrity", {}).get("hashes", {})

    return {
        "format": "IMPERIAL-EVIDENCE-RECORD",
        "format_version": IER_VERSION,
        "record_type": "portable-evidence-package",
        "pack_id": audit.get("pack_id", "UNSPECIFIED"),
        "master_hash": hashes.get("MASTER_CHAIN_HASH"),
        "hash_algorithm": "SHA-256",
        "encoding": "UTF-8",
        "platform_dependencies": [],
        "files": files,
    }


def write_ier_manifest(root: str | Path) -> Path:
    root = Path(root)
    manifest = build_ier_manifest(root)
    target = root / "manifest.json"
    target.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
