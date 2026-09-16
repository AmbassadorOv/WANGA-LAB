#!/usr/bin/env python3
"""Audit WANGA research-group queues without executing research claims."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "task_queue.schema.json"
GROUPS = [
    "neural-core",
    "neural-os",
    "model-runtime",
    "node-network",
    "memory-knowledge",
    "architect-interface",
]


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema["required"])
    errors: list[str] = []
    total = 0
    for group in GROUPS:
        path = ROOT / group / "WORK_QUEUE.json"
        if not path.exists():
            errors.append(f"missing queue: {path}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        missing = required - set(data)
        if missing:
            errors.append(f"{path}: missing {sorted(missing)}")
            continue
        if data["group_id"] != "RG-" + group.upper().replace("-", "-"):
            errors.append(f"{path}: group_id mismatch")
        for task in data["tasks"]:
            total += 1
            for field in ("task_id", "objective", "status", "acceptance_checks"):
                if field not in task:
                    errors.append(f"{path}: task missing {field}")
            if not task.get("acceptance_checks"):
                errors.append(f"{path}: task has no acceptance checks")

    print(f"WANGA queue audit: groups={len(GROUPS)} tasks={total}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: queue structure is internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
