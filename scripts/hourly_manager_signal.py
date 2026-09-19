"""Hourly signal helper for the WANGA Global Work Manager.

The GitHub Actions workflow owns scheduling and state checkpointing.
This module keeps the decision rule deterministic and side-effect free.
"""

from __future__ import annotations

import json
from pathlib import Path


def actionable_tasks(plan_path: str = "docs/GLOBAL_WORK_PLAN.json") -> list[dict]:
    path = Path(plan_path)
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [
        task for task in data.get("tasks", [])
        if task.get("status") in {"READY", "RUNNING", "REVIEW_REQUIRED", "BLOCKED", "CONFLICT"}
    ]


if __name__ == "__main__":
    tasks = actionable_tasks()
    print(json.dumps({"actionable": bool(tasks), "count": len(tasks)}, indent=2))
