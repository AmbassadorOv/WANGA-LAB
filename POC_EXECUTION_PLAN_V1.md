# WANGA-LAB — POC Execution Plan V1

Status: ACTIVE BUILD PLAN

## Objective

Turn the existing architecture documents into a reproducible, provider-neutral operational POC.

## Definition of Done

A local run must be able to execute:

TASK
-> INTENT/CLASSIFICATION
-> ROUTING
-> REASONING NODE(S)
-> CRITIQUE
-> VERIFICATION
-> SYNTHESIS
-> AUDIT RECORD

The run must preserve request_id/task_id, node roles, evidence references, verification state, latency/usage when available, failures, and final status.

## Workstreams

### A. NTM Core
- typed task envelope
- model registry
- provider-neutral ModelAdapter
- router
- execution state
- failure/retry routing
- synthesis

### B. Verification
- schema validation
- deterministic checks
- evidence/provenance record
- verification gates
- explicit unresolved state

### C. Drift Forensics
- baseline/current representation
- structural diff
- semantic-drift hooks
- drift classification
- repair candidate record
- audit trail

### D. Memory
- run state
- episodic records
- verification history
- retrieval interface

### E. Research Intelligence
- ingestion interface
- normalization
- deduplication
- classification
- clustering
- capability/evidence graph

### F. API
- health endpoint
- task submission
- run retrieval
- audit retrieval
- deterministic local demo

## First POC Principle

Do not fake model calls or verification. The first POC may use deterministic local adapters and synthetic tasks, but every result must identify what was actually executed.

## Acceptance Tests

1. Same input + same deterministic adapter => reproducible output.
2. Malformed node output => captured failure and no silent promotion.
3. Verification failure => result remains unverified.
4. Node disagreement => preserved, not hidden.
5. Drift case => classification and evidence references are emitted.
6. Full run => machine-readable audit record is written.
7. No credentials are committed to Git.
