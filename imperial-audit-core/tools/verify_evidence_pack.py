#!/usr/bin/env python3
"""Verify an imperial-audit-core portable evidence pack offline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.evidence.offline_court import OfflineEvidenceCourt


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify an imperial-audit-core evidence pack without its issuer server."
    )
    parser.add_argument("pack", type=Path)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the verification report as JSON.",
    )
    args = parser.parse_args()

    report = OfflineEvidenceCourt(args.pack).verify()

    if args.json:
        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(f"PACK: {report.pack_id}")
        print(f"MASTER: {report.master_hash or 'MISSING'}")
        print(f"STATUS: {report.overall_status}")
        for finding in report.findings:
            print(f"[{finding.status}] {finding.code}: {finding.detail}")

    return 0 if report.overall_status in {"VERIFIED", "PARTIAL"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
