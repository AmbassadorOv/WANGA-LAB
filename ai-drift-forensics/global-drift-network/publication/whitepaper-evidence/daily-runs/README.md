# Daily Run Records

One record per measurement day.

Required fields:

- `run_id`
- `date`
- `started_at`
- `completed_at`
- `baseline_id`
- `config_hash`
- `code_commit`
- `source_ids`
- `task_ids`
- `worker_versions`
- `observations`
- `anomalies`
- `quality_gate`
- `snapshot_id`
- `snapshot_hash`
- `status`

A daily run should be append-only after completion. Corrections should create a new record or correction event rather than silently rewriting the historical record.
