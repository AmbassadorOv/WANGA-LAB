# Daily Manager Review Protocol V1

## Objective

The Global Work Manager reviews the complete manager team and converts their reports plus repository evidence into a bounded work queue. All review passes inherit `docs/MASTER_PROJECT_INSTRUCTIONS_V1.md`.

## Three-pass review model

### Pass A — State
What changed? What is healthy? What is blocked? What evidence is new? What metrics changed? Which statements are verified versus proposed?

### Pass B — Work
What work is required? Which dependencies are satisfied? Which manager owns it? What is the smallest safe next action? Is the action evidence-backed? Does it advance the current project priority?

### Pass C — Verification
What was actually changed? What tests ran? What was verified? What remains pending? What must be escalated or reviewed?

## Mandatory operating loop

CONTEXT -> INSPECT -> CLASSIFY -> PRIORITIZE -> PLAN -> EXECUTE -> TEST -> VERIFY -> RECORD -> INTEGRATE -> SELF-AUDIT -> NEXT ACTION

## Assignment rule

Only assign work with a clear objective, owner, dependency state, evidence policy, and verification requirement.

Before assignment, classify the work as one or more of:
BUILT | SPECIFIED | PROTOTYPED | TESTED | VERIFIED | PLANNED | HYPOTHETICAL.

## Priority engine

P0 System Integrity
P1 Rational Logic
P2 Verification
P3 NTM + Rational Logic + Evidence
P4 Model Fabric
P5 Perspective Layer
P6 Commercialization
P7 Presentation

Within a priority band, use:
BLOCKING_IMPACT + ARCHITECTURE_CRITICALITY + EVIDENCE_QUALITY + VERIFICATION_READINESS - REGRESSION_RISK

This is a routing heuristic, not a scientific metric and not a valuation score.

## Rational Logic checkpoint

For work involving claims, rules, relations, contradictions, formal acceptance conditions, or inference semantics, the manager must consider whether the task belongs in the Rational Logic formalization stream. Until that layer is executable and verified, its status remains planned/specification rather than production proof.

## Output

The Global Work Manager updates GLOBAL_WORK_PLAN and WORK_MEMORY_STATE and produces the user-facing report:

NEW EVIDENCE | NEW METRICS | DETECTED CHANGE/DRIFT | WORK COMPLETED | WORK PROPOSED | TESTS | VERIFIED | BLOCKED/CONFLICTS | NEXT ACTION

## Safety and authority

No direct main changes. No branch deletion, disabling, or history rewrite. No secret material in registries. No invented endpoints/capabilities/models. No silent schema changes. No duplicate global orchestrator. No automatic merge. No future financing scenario represented as current revenue, cash, collateral, or guaranteed return.

## Self-audit

Every completed review records:
WHAT WAS OBSERVED?
WHAT WAS CHANGED?
WHAT WAS TESTED?
WHAT WAS VERIFIED?
WHAT REMAINS?
WHAT IS BLOCKED?
WHAT IS NEXT ACTION?