from pathlib import Path
from tempfile import TemporaryDirectory

from queue import TaskQueue


def main() -> None:
    with TemporaryDirectory() as tmp:
        q = TaskQueue(Path(tmp) / "queue.sqlite")
        q.enqueue({
            "task_id": "SMOKE-001",
            "run_id": "RUN-SMOKE",
            "worker": "observation",
            "operation": "collect_control_set",
        })
        task = q.claim(60)
        assert task and task["status"] == "CLAIMED"
        q.start(task["task_id"])
        q.complete(task["task_id"], "result://SMOKE-001")
        print("QUEUE_SMOKE_TEST: PASS")


if __name__ == "__main__":
    main()
