# Immutable State Snapshots

Snapshots preserve the complete research state at defined checkpoints.

Minimum metadata:

- `snapshot_id`
- `run_id`
- `parent_snapshot_id`
- `created_at`
- `schema_version`
- `state`
- `event_ids`
- `content_hash`

Expected chain:

`S0 → S1 → S2 → ... → S30`

The snapshot hash should be calculated from a canonical representation of the snapshot content. Historical snapshots should not be overwritten as part of normal operation.
