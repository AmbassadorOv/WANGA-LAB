"""Create and execute a deterministic daily preparation run.

This first implementation uses mock worker operations. Real observation,
verification, and synthesis workers can be attached behind the same queue API.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RUNTIME = Path(__file__).resolve().parent
sys.path.insert(0, str(RUNTIME))
from state import connect, init_db, create_run, snapshot, enqueue, claim, complete, fail, append_event

SCHEDULE = RUNTIME.parent / "schedule.json"


def load_schedule():
    return json.loads(SCHEDULE.read_text(encoding="utf-8"))


def mock_worker(task):
    return {
        "task_id": task["task_id"],
        "worker": task["worker"],
        "operation": task["operation"],
        "status": "MOCK_SUCCESS",
        "note": "Runtime plumbing verified; replace with evidence-producing worker."
    }


def main():
    schedule = load_schedule()
    if not schedule.get("enabled", True):
        print("schedule disabled")
        return

    db = connect()
    init_db(db)
    run_id = create_run(db, schedule["schedule_id"])
    state = {"status": "SNAPSHOTTED", "stage": "snapshot", "tasks": [], "results": []}
    snap = snapshot(db, run_id, state)

    for spec in [
        ("observation", "change_scan", 70),
        ("relationship", "cross_surface_scan", 60),
        ("verification", "evidence_check", 90),
        ("publication", "whitepaper_synthesis", 40),
    ]:
        task_id = enqueue(db, run_id, spec[0], spec[1],
                          {"run_id": run_id, "snapshot_id": snap, "operation": spec[1]}, spec[2])
        state["tasks"].append(task_id)

    state["status"] = "EXECUTING"
    state["stage"] = "worker_execution"
    snap = snapshot(db, run_id, state, snap)

    while True:
        task = claim(db, "daily-runner")
        if task is None or task["run_id"] != run_id:
            break
        try:
            result = mock_worker(task)
            result_path = RUNTIME.parent / "state" / f"{task['task_id']}.json"
            result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            complete(db, task["task_id"], str(result_path))
            state["results"].append(result)
            append_event(db, run_id, "TASK_SUCCEEDED", result)
        except Exception as exc:
            fail(db, task["task_id"], repr(exc))
            append_event(db, run_id, "TASK_FAILED", {"task_id": task["task_id"], "error": repr(exc)})

    state["status"] = "QUALITY_CHECKED"
    state["stage"] = "quality_gate"
    state["quality_gate"] = {
        "status": "REVIEW_REQUIRED",
        "reason": "Mock workers produced no evidentiary findings. No publication permitted."
    }
    snapshot(db, run_id, state, snap)
    db.execute("UPDATE runs SET status=?, updated_at=? WHERE run_id=?", ("COMPLETED", __import__('state').now(), run_id))
    db.commit()
    print(json.dumps({"run_id": run_id, "status": "COMPLETED", "quality_gate": state["quality_gate"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
