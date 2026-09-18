# Daily Manager Review Protocol V1

## Objective

The Global Work Manager reviews the complete manager team and converts their reports plus repository evidence into a bounded work queue.

## Three-pass review model

### Pass A — State
What changed? What is healthy? What is blocked? What evidence is new? What metrics changed?

### Pass B — Work
What work is required? Which dependencies are satisfied? Which manager owns it? What is the smallest safe next action? Is the action evidence-backed?

### Pass C — Verification
What was actually changed? What tests ran? What was verified? What remains pending? What must be escalated or reviewed?

## Assignment rule

Only assign work with a clear objective, owner, dependency state, evidence policy, and verification requirement.

## Priority heuristic

BLOCKING_IMPACT + ARCHITECTURE_CRITICALITY + EVIDENCE_QUALITY + VERIFICATION_READINESS - REGRESSION_RISK

This is a routing heuristic, not a scientific metric.

## Output

The Global Work Manager updates GLOBAL_WORK_PLAN and WORK_MEMORY_STATE and produces the user-facing report:

NEW EVIDENCE | NEW METRICS | DETECTED CHANGE/DRIFT | WORK COMPLETED | WORK PROPOSED | TESTS | VERIFIED | BLOCKED/CONFLICTS | NEXT ACTION

## Safety

No direct main changes. No branch deletion. No secret material in registries. No invented endpoints/capabilities. No silent schema changes. No duplicate global orchestrator. No automatic merge.
