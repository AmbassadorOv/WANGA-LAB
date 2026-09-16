# Task Queue Protocol

The queue is the execution boundary between the Orchestrator and Workers.

## Lifecycle

PENDING -> CLAIMED -> RUNNING -> SUCCEEDED
                         |-> RETRY -> PENDING
                         |-> DEAD_LETTER

## Required properties

- Every task has a stable task_id and run_id.
- Every task has an idempotency_key derived from its logical operation and input snapshot.
- Claiming must be atomic.
- Running tasks use a lease with an expiration timestamp.
- Workers must emit a result reference; they do not mutate RunState directly.
- Retries must increment attempt and preserve the previous failure record.
- A dead-letter task blocks any dependent publication step.

## Queue priority

Priority is configuration, not scientific significance. It determines execution order only.

## Dependency rule

A task may execute only when all declared dependency task_ids have SUCCEEDED. A failed or dead-letter dependency prevents downstream execution.

## Persistence rule

The first implementation may use SQLite for a single runner. The production implementation should use a transactional persistent store that supports atomic claim/lease operations. Queue state must not depend on process memory.

## Forensic rule

Queue events are audit events. They must be retained with timestamps and linked to the corresponding run and snapshot.