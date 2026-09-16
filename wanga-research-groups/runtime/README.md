# WANGA Research Group Runtime

This directory defines the first executable boundary for research groups.

The runtime is intentionally model-agnostic. A worker receives a bounded task, reads declared inputs, produces declared artifacts, and returns a worker-contract result. A model may later be attached as a compute runtime; it is not the operating system, orchestrator, or authority.

Execution contract:

`LOAD GROUP → LOAD QUEUE → CLAIM TASK → EXECUTE → WRITE ARTIFACT → RUN ACCEPTANCE CHECKS → RETURN RESULT → REVIEW/PROMOTE`

Integrity rules:

- No synthetic observations may be promoted as evidence.
- Workers cannot silently change schemas, thresholds, historical observations, or evidence classifications.
- Failed, blocked, negative, and inconclusive work remains recorded.
- Every output must identify its task and input references.
- Verification is a separate stage from generation whenever the task is scientific evidence.

Phase 1 provides queue and contract infrastructure. Phase 2 can attach real Python workers and model adapters without changing the research-group contract.
