"""Build a self-contained portable evidence package."""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

from .offline_court import OfflineEvidenceCourt


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def export_pack(source_dir: str | Path, output_zip: str | Path) -> Path:
    source = Path(source_dir)
    output = Path(output_zip)
    if not (source / 'audit_output.json').is_file():
        raise FileNotFoundError('audit_output.json is required')

    with tempfile.TemporaryDirectory() as temp_name:
        staging = Path(temp_name) / 'evidence-pack'
        shutil.copytree(source, staging)
        report = OfflineEvidenceCourt(staging).verify()
        (staging / 'verification_report.json').write_text(
            json.dumps(report.to_dict(), indent=2, ensure_ascii=False),
            encoding='utf-8',
        )

        manifest = {}
        for path in sorted(staging.rglob('*')):
            if path.is_file() and path.name != 'manifest.json':
                manifest[str(path.relative_to(staging))] = _sha256(path)
        (staging / 'manifest.json').write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True),
            encoding='utf-8',
        )

        output.parent.mkdir(parents=True, exist_ok=True)
        archive_base = output.with_suffix('')
        archive = Path(shutil.make_archive(str(archive_base), 'zip', staging))
        if archive != output:
            archive.replace(output)
    return output