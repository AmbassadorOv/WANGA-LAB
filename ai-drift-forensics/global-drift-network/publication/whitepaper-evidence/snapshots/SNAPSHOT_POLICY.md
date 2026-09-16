# Snapshot Policy

Snapshots are immutable records of the Orchestrator state at a defined point in a run.

## Required fields

- `snapshot_id`
- `run_id`
- `parent_snapshot_id` (null only for the first snapshot)
- `created_at`
- `schema_version`
- `state_hash`
- `event_ids`
- `task_ids`
- `evidence_ids`
- `quality_gate_status`

## Rules

1. Never overwrite an existing snapshot.
2. Every new snapshot references its immediate parent.
3. Hash the canonical state representation, not a presentation format.
4. Store raw evidence separately; snapshots contain references and state, not destructive replacements of source material.
5. A failed run still receives a final snapshot describing its failure state.
6. A retry creates a new run/attempt record and references the prior failed run.
7. Any protocol change receives a new `schema_version` or `protocol_version` as appropriate.

## State chain

`S0 -> S1 -> S2 -> ... -> Sn`

The chain must permit reconstruction of the state transitions that produced a White Paper claim.

## Publication rule

A claim cannot be promoted to publication solely because a snapshot exists. Publication requires evidence references and successful verification/quality-gate status.
