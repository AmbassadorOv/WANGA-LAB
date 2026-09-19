#!/usr/bin/env python3
"""Create a deterministic daily-run manifest and state snapshot.

This runner does not perform scientific analysis. It establishes the execution
record that later observation/verification workers populate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/daily-run")
    parser.add_argument("--run-id", default=None)
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    run_id = args.run_id or now.strftime("RUN-%Y%m%dT%H%M%SZ")
    out = Path(args.output) / run_id
    out.mkdir(parents=True, exist_ok=True)

    state = {
        "run_id": run_id,
        "status": "CREATED",
        "created_at": now.isoformat(),
        "program": "global-drift-network-whitepaper-30-day-evidence",
        "protocol_version": "1.0.0",
        "baseline_id": "BASELINE-001",
        "task_ids": [],
        "evidence_ids": [],
        "quality_gate": "PENDING",
    }

    snapshot = {
        "snapshot_id": f"SNAP-{run_id}",
        "run_id": run_id,
        "parent_snapshot_id": None,
        "created_at": now.isoformat(),
        "schema_version": "1.0.0",
        "state": state,
        "event_ids": [],
    }
    snapshot["state_hash"] = sha256(snapshot["state"])
    snapshot["snapshot_hash"] = sha256(snapshot)

    manifest = {
        "run_id": run_id,
        "status": "CREATED",
        "created_at": now.isoformat(),
        "schedule_source": "schedule.json",
        "baseline_id": "BASELINE-001",
        "snapshot_id": snapshot["snapshot_id"],
        "snapshot_hash": snapshot["snapshot_hash"],
        "runner": "daily_run.py",
        "analysis_status": "NOT_STARTED",
        "note": "Execution scaffold only; no scientific finding is produced by this runner.",
    }

    (out / "run.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "snapshot.json").write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"run_id": run_id, "snapshot_id": snapshot["snapshot_id"], "snapshot_hash": snapshot["snapshot_hash"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
