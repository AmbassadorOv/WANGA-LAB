from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


STATUSES = {"PENDING", "CLAIMED", "RUNNING", "SUCCEEDED", "RETRY", "FAILED", "DEAD_LETTER", "CANCELLED"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_idempotency_key(run_id: str, operation: str, input_snapshot_id: str | None) -> str:
    raw = f"{run_id}|{operation}|{input_snapshot_id or ''}"
    return hashlib.sha256(raw.encode()).hexdigest()


class TaskQueue:
    """Small persistent queue for the first single-runner implementation."""

    def __init__(self, db_path: str | Path):
        self.db = sqlite3.connect(db_path, timeout=30, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            run_id TEXT NOT NULL,
            worker TEXT NOT NULL,
            operation TEXT NOT NULL,
            status TEXT NOT NULL,
            attempt INTEGER NOT NULL DEFAULT 0,
            max_attempts INTEGER NOT NULL DEFAULT 3,
            priority INTEGER NOT NULL DEFAULT 50,
            idempotency_key TEXT NOT NULL UNIQUE,
            input_snapshot_id TEXT,
            dependencies TEXT NOT NULL DEFAULT '[]',
            lease_expires_at TEXT,
            created_at TEXT NOT NULL,
            started_at TEXT,
            finished_at TEXT,
            result_ref TEXT,
            error TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_tasks_claim ON tasks(status, priority DESC, created_at);
        CREATE TABLE IF NOT EXISTS queue_events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id TEXT NOT NULL,
            from_status TEXT,
            to_status TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            detail TEXT
        );
        """)

    def enqueue(self, task: dict[str, Any]) -> str:
        status = task.get("status", "PENDING")
        if status not in STATUSES:
            raise ValueError(f"invalid status: {status}")
        task_id = task["task_id"]
        idem = task.get("idempotency_key") or make_idempotency_key(
            task["run_id"], task["operation"], task.get("input_snapshot_id")
        )
        created = task.get("created_at", now())
        self.db.execute(
            """INSERT OR IGNORE INTO tasks
            (task_id,run_id,worker,operation,status,attempt,max_attempts,priority,idempotency_key,input_snapshot_id,dependencies,created_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (task_id, task["run_id"], task["worker"], task["operation"], status,
             task.get("attempt", 0), task.get("max_attempts", 3), task.get("priority", 50),
             idem, task.get("input_snapshot_id"), json.dumps(task.get("dependencies", [])), created),
        )
        return task_id

    def claim(self, lease_seconds: int = 900) -> dict[str, Any] | None:
        """Atomically claim the highest-priority task whose dependencies succeeded."""
        with self.db:
            candidates = self.db.execute(
                "SELECT * FROM tasks WHERE status IN ('PENDING','RETRY') ORDER BY priority DESC, created_at LIMIT 50"
            ).fetchall()
            for row in candidates:
                deps = json.loads(row["dependencies"])
                if deps:
                    marks = ",".join("?" for _ in deps)
                    ok = self.db.execute(
                        f"SELECT COUNT(*) FROM tasks WHERE task_id IN ({marks}) AND status='SUCCEEDED'", deps
                    ).fetchone()[0] == len(deps)
                    if not ok:
                        continue
                old = row["status"]
                expires = (datetime.now(timezone.utc) + timedelta(seconds=lease_seconds)).isoformat()
                updated = self.db.execute(
                    "UPDATE tasks SET status='CLAIMED',attempt=attempt+1,lease_expires_at=?,started_at=? WHERE task_id=? AND status IN ('PENDING','RETRY')",
                    (expires, now(), row["task_id"]),
                ).rowcount
                if updated:
                    self._event(row["task_id"], old, "CLAIMED")
                    return dict(self.db.execute("SELECT * FROM tasks WHERE task_id=?", (row["task_id"],)).fetchone())
        return None

    def start(self, task_id: str) -> None:
        self._transition(task_id, "CLAIMED", "RUNNING")

    def heartbeat(self, task_id: str, lease_seconds: int = 900) -> None:
        expires = (datetime.now(timezone.utc) + timedelta(seconds=lease_seconds)).isoformat()
        self.db.execute("UPDATE tasks SET lease_expires_at=? WHERE task_id=? AND status='RUNNING'", (expires, task_id))

    def complete(self, task_id: str, result_ref: str) -> None:
        with self.db:
            self._transition(task_id, "RUNNING", "SUCCEEDED", result_ref=result_ref, finished_at=now(), lease_expires_at=None)

    def fail(self, task_id: str, error: str) -> None:
        row = self.db.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        if not row:
            raise KeyError(task_id)
        target = "RETRY" if row["attempt"] < row["max_attempts"] else "DEAD_LETTER"
        with self.db:
            self._transition(task_id, row["status"], target, error=error, finished_at=now(), lease_expires_at=None)

    def recover_expired(self) -> int:
        current = now()
        rows = self.db.execute("SELECT task_id FROM tasks WHERE status IN ('CLAIMED','RUNNING') AND lease_expires_at < ?", (current,)).fetchall()
        for row in rows:
            self._transition(row["task_id"], None, "RETRY", error="lease_expired", lease_expires_at=None)
        return len(rows)

    def _transition(self, task_id: str, expected: str | None, target: str, **fields: Any) -> None:
        if target not in STATUSES:
            raise ValueError(target)
        row = self.db.execute("SELECT status FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        if not row:
            raise KeyError(task_id)
        if expected is not None and row["status"] != expected:
            raise RuntimeError(f"task {task_id}: expected {expected}, got {row['status']}")
        sets = ["status=?"]
        values: list[Any] = [target]
        for key, value in fields.items():
            sets.append(f"{key}=?")
            values.append(value)
        values.append(task_id)
        self.db.execute(f"UPDATE tasks SET {','.join(sets)} WHERE task_id=?", values)
        self._event(task_id, row["status"], target)

    def _event(self, task_id: str, old: str | None, new: str, detail: str | None = None) -> None:
        self.db.execute(
            "INSERT INTO queue_events(task_id,from_status,to_status,timestamp,detail) VALUES(?,?,?,?,?)",
            (task_id, old, new, now(), detail),
        )
