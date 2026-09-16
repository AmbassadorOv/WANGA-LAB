"""Persistent run state, task queue, events, and immutable snapshots.

The runtime is intentionally dependency-light: Python stdlib + SQLite.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = ROOT / "state"
DB_PATH = STATE_DIR / "pipeline.db"
SNAPSHOT_DIR = STATE_DIR / "snapshots"


def now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    return db


def init_db(db):
    db.executescript("""
    CREATE TABLE IF NOT EXISTS runs (
      run_id TEXT PRIMARY KEY,
      schedule_id TEXT NOT NULL,
      status TEXT NOT NULL,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      current_snapshot_id TEXT
    );
    CREATE TABLE IF NOT EXISTS tasks (
      task_id TEXT PRIMARY KEY,
      run_id TEXT NOT NULL REFERENCES runs(run_id),
      worker TEXT NOT NULL,
      operation TEXT NOT NULL,
      input_hash TEXT NOT NULL,
      status TEXT NOT NULL,
      priority INTEGER NOT NULL DEFAULT 50,
      attempt INTEGER NOT NULL DEFAULT 0,
      lease_until TEXT,
      result_ref TEXT,
      error TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      UNIQUE(run_id, operation, input_hash)
    );
    CREATE TABLE IF NOT EXISTS events (
      event_id TEXT PRIMARY KEY,
      run_id TEXT NOT NULL REFERENCES runs(run_id),
      event_type TEXT NOT NULL,
      payload_json TEXT NOT NULL,
      created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS snapshots (
      snapshot_id TEXT PRIMARY KEY,
      run_id TEXT NOT NULL REFERENCES runs(run_id),
      parent_snapshot_id TEXT,
      schema_version TEXT NOT NULL,
      content_hash TEXT NOT NULL,
      path TEXT NOT NULL,
      created_at TEXT NOT NULL
    );
    """)
    db.commit()


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def create_run(db, schedule_id):
    run_id = "run-" + uuid.uuid4().hex[:16]
    ts = now()
    db.execute("INSERT INTO runs VALUES (?, ?, ?, ?, ?, ?)",
               (run_id, schedule_id, "CREATED", ts, ts, None))
    db.commit()
    append_event(db, run_id, "RUN_CREATED", {"schedule_id": schedule_id})
    return run_id


def append_event(db, run_id, event_type, payload):
    event_id = "evt-" + uuid.uuid4().hex[:16]
    db.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?)",
               (event_id, run_id, event_type, canonical(payload), now()))
    db.commit()
    return event_id


def snapshot(db, run_id, state, parent_snapshot_id=None):
    snapshot_id = "snap-" + uuid.uuid4().hex[:16]
    payload = {"snapshot_id": snapshot_id, "run_id": run_id, "state": state}
    raw = canonical(payload).encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    path = SNAPSHOT_DIR / f"{run_id}-{snapshot_id}.json"
    path.write_bytes(raw)
    db.execute("INSERT INTO snapshots VALUES (?, ?, ?, ?, ?, ?)",
               (snapshot_id, run_id, parent_snapshot_id, "1.0", digest, str(path), now()))
    db.execute("UPDATE runs SET current_snapshot_id=?, updated_at=? WHERE run_id=?",
               (snapshot_id, now(), run_id))
    db.commit()
    return snapshot_id


def enqueue(db, run_id, worker, operation, input_payload, priority=50):
    input_hash = hashlib.sha256(canonical(input_payload).encode()).hexdigest()
    task_id = "task-" + uuid.uuid4().hex[:16]
    ts = now()
    try:
        db.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (task_id, run_id, worker, operation, input_hash, "PENDING", priority,
                    0, None, None, None, ts, ts))
        db.commit()
    except sqlite3.IntegrityError:
        row = db.execute("SELECT task_id FROM tasks WHERE run_id=? AND operation=? AND input_hash=?",
                         (run_id, operation, input_hash)).fetchone()
        return row[0]
    append_event(db, run_id, "TASK_ENQUEUED", {"task_id": task_id, "worker": worker, "operation": operation})
    return task_id


def recover_expired(db):
    ts = now()
    rows = db.execute("SELECT task_id FROM tasks WHERE status='RUNNING' AND lease_until < ?", (ts,)).fetchall()
    for row in rows:
        db.execute("UPDATE tasks SET status='PENDING', lease_until=NULL, updated_at=? WHERE task_id=?",
                   (ts, row[0]))
    db.commit()
    return len(rows)


def claim(db, worker, lease_minutes=20):
    recover_expired(db)
    # SQLite serializes the short write transaction, making this claim atomic.
    db.execute("BEGIN IMMEDIATE")
    row = db.execute("SELECT task_id FROM tasks WHERE status='PENDING' ORDER BY priority DESC, created_at LIMIT 1").fetchone()
    if not row:
        db.commit()
        return None
    task_id = row[0]
    lease = (datetime.now(timezone.utc) + timedelta(minutes=lease_minutes)).isoformat()
    db.execute("UPDATE tasks SET status='RUNNING', attempt=attempt+1, lease_until=?, updated_at=? WHERE task_id=?",
               (lease, now(), task_id))
    db.commit()
    return db.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchone()


def complete(db, task_id, result_ref):
    db.execute("UPDATE tasks SET status='SUCCEEDED', result_ref=?, lease_until=NULL, updated_at=? WHERE task_id=?",
               (result_ref, now(), task_id))
    db.commit()


def fail(db, task_id, error, max_attempts=3):
    row = db.execute("SELECT attempt, run_id FROM tasks WHERE task_id=?", (task_id,)).fetchone()
    status = "DEAD_LETTER" if row[0] >= max_attempts else "PENDING"
    db.execute("UPDATE tasks SET status=?, error=?, lease_until=NULL, updated_at=? WHERE task_id=?",
               (status, error[:2000], now(), task_id))
    db.commit()


if __name__ == "__main__":
    db = connect()
    init_db(db)
    print(f"initialized {DB_PATH}")
