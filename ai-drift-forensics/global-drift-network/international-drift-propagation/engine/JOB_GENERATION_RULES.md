# Job Generation Rules

## Goal

Turn one Event Instance into deterministic observation work without embedding scientific conclusions in the scheduler.

## Cartesian coverage

For each event instance, generate jobs for every declared combination of:

`WINDOW × TARGET × PROBE`

where TARGET is:

`REGION × LANGUAGE × SURFACE × SYSTEM`

The scheduler must preserve the declared coverage. It must not silently substitute another region, language, surface or system.

## Worker routing

- `BASELINE`, `PRE_EVENT`, `HIGH_RESOLUTION`, `POST_EVENT`, `PERSISTENCE` → `WORKER_OBSERVATION`
- `RELATIONSHIP_SCAN` → `WORKER_RELATIONSHIP`
- `REPRODUCTION`, `ATTRIBUTION`, `VERIFICATION` → `WORKER_VERIFICATION`
- `DIGEST` → `WORKER_PUBLICATION`

## Deterministic job identity

A job identity should be derived from:

`event_instance_id + phase + region + language + surface + system_id + probe_id + window`

The same inputs must produce the same logical job identity so retries do not create duplicate scientific observations.

## Retry rule

A failed collection attempt may be retried, but each attempt must retain its own provenance. A retry must never overwrite the original evidence record.

## Missing-data rule

If a target cannot be observed, the queue records `UNRESOLVED` or `BLOCKED` with a reason. It does not synthesize a measurement.

## Relationship generation

Relationship jobs are created only after sufficient observations exist to compare time-aligned signatures. Candidate generation may identify:

- cross-region relationships
- cross-language relationships
- cross-surface relationships
- combined relationships

Candidate generation is not attribution.

## Verification handoff

Every candidate edge entering verification carries its source observations, baseline references, temporal alignment information and uncertainty notes.
