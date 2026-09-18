# WANGA Architecture Owner Boundaries

## Purpose

This document defines the division between architecture ownership and engineering implementation so the system does not require the architecture owner to perform engineering operations manually.

## Architecture Owner

The architecture owner defines:
- system goals and scope
- concepts, entities, events, moves, baselines and relationships
- required capabilities and acceptance criteria
- research questions and monitoring priorities
- governance constraints
- interpretation rules
- what the system must and must not infer

The architecture owner does **not** need to:
- edit repository files manually
- create branches manually
- wire integrations manually
- run repetitive tests manually
- maintain CI/CD manually
- perform routine GitHub operations manually

## Engineering / Agent Execution Layer

Engineering agents and hired engineers are responsible for:
- implementation
- repository changes
- branch management
- tests and validation
- CI/CD
- data ingestion
- integrations
- deployment
- observability
- bug fixing
- technical documentation
- reporting implementation status and blockers

## Automatic Outreach Rule

Every outbound institutional email that is actually sent should create an Outreach Event with:
- event identifier
- sender
- recipient
- timestamp (T0)
- subject/action class
- target sector

The event should then enter the Butterfly Effect tracking pipeline automatically.

The system must never automatically resend the email unless explicitly authorized.

## GitHub Rule

When an outbound email is recorded as a real Outreach Event, the corresponding tracking state and implementation artifacts should be updated in the designated WANGA GitHub workflow without requiring the architecture owner to perform routine repository operations manually.

## Butterfly Effect Rule

Post-T0 observations are compared against the relevant baseline. Temporal order alone is not treated as causality.

Statuses:
- NORMAL_OR_UNRELATED
- POSSIBLE_PROPAGATION
- BUTTERFLY_SIGNAL
- INSUFFICIENT_EVIDENCE

## Architecture Completion Gate

The architecture is considered ready for engineering handoff when:
1. interfaces between modules are defined;
2. event schemas are defined;
3. evidence/provenance requirements are defined;
4. baseline and drift rules are defined;
5. outreach/T0 lifecycle is defined;
6. propagation analysis rules are defined;
7. automation responsibilities are assigned;
8. acceptance tests are specified.

The architecture owner should receive concise results, exceptions and decisions required from them—not a list of routine engineering buttons to press.
