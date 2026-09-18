# WANGA Work Memory Protocol V1

Status: ACTIVE BUILD CONTROL PLANE

## Master instruction inheritance

Work Memory records and enforces the continuity requirements of `docs/MASTER_PROJECT_INSTRUCTIONS_V1.md`. It is bookkeeping and resume state; it does not override repository evidence or create an independent authority.

## Purpose

Maintain a durable, machine-readable record of architecture decisions, verified repository state, completed construction, unresolved conflicts, and the next deterministic build actions.

This persistent work-memory layer is the resume point for autonomous construction. Git remains the implementation history; this layer records current operational state and intent.

## Memory classes

- FACT: verified repository or architecture fact.
- DECISION: accepted construction rule or boundary.
- CONSTRAINT: must-not-violate condition.
- OBSERVATION: observed but not yet interpreted.
- PROPOSAL: candidate next change.
- VERIFIED_RESULT: completed and checked result.
- BLOCKED: work that cannot safely proceed.
- CONFLICT: incompatible source or implementation state.
- NEXT_ACTION: deterministic pending construction step.

## Required continuity fields

For every substantive build step, record:
- context
- observed state
- classification
- selected priority
- dependencies
- action
- changed artifacts
- tests
- verification result
- pending/blocked/conflict state
- next action

## Update rule

Every substantive autonomous build step MUST record what was observed, what changed, what was verified, what remains pending, and the next deterministic action.

A slot must never be reported as a live model connection merely because an architectural identity exists.

## Authority

- Git history: implementation history.
- Schemas/contracts: machine interfaces.
- Work memory: current build-state bookkeeping and continuity.
- Master Project Instructions: common project operating contract.
- Wix: architecture/publication evidence.
- Final review: outside autonomous construction.

## Invariants

- Never push autonomous construction directly to main.
- Never delete, disable, or rewrite preserved source branches.
- Never store provider credentials in model registries.
- Never enable a model without capability and health verification.
- Never resolve a source conflict by guessing.
- Never replace the existing global Work Manager/Orchestrator with a competing orchestrator.
- Never silently change an agent identity or evidence chain.
- Never represent vision, valuation scenarios, or future financing scenarios as verified facts.
- Preserve initial versions as historical references for recovering original intent when needed.