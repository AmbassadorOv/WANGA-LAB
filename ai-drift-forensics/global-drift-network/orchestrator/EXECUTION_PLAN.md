# Executable Pipeline — Next Milestones

## Current milestone

The evidence layer and daily-run shell exist on branch `whitepaper-evidence-infrastructure`. The next executable boundary is the persistent task queue.

## Run lifecycle

1. Scheduler starts a run.
2. Orchestrator creates the initial run record and snapshot.
3. Orchestrator enqueues tasks derived from routing policy.
4. Queue claims tasks atomically and assigns leases.
5. Workers execute against an immutable input snapshot.
6. Worker results are stored as evidence-linked outputs.
7. Orchestrator reduces results into the next state snapshot.
8. Verification evaluates claims and evidence.
9. Quality Gate decides PASS, REVIEW, or BLOCK.
10. Only PASS enters the publication queue.

## Implementation order

- Queue persistence and smoke tests.
- Lease expiry and retry recovery.
- Worker adapter interface.
- Observation worker using a fixed control set.
- Verification worker and evidence-chain linkage.
- Snapshot reducer.
- Quality Gate checks.
- Daily end-to-end test run.
- Only then connect real external data sources.

## Non-negotiable controls

- No worker may publish directly.
- No observation may overwrite the baseline.
- Every derived claim must reference evidence IDs.
- Failed verification cannot be represented as verified evidence.
- Retries must be idempotent.
- Every state transition must be auditable.
