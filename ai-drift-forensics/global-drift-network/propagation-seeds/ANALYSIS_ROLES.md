# Propagation Analysis Roles

These are logical analysis lanes in the repository. They are not claims that human staff or external teams have been assigned.

| Lane | Responsibility | Output |
|---|---|---|
| SEED-INTAKE | Capture unique public weekend signals | Seed records |
| PROVENANCE | Preserve source, timestamp, baseline and evidence links | Evidence receipts |
| DRIFT-EXTRACT | Measure deviation from baseline | Candidate Drift records |
| PROPAGATION | Compare independent points for shared signatures | Propagation events |
| PERSISTENCE | Track continuation, recovery, return and reversal | Persistence records |
| SYNTHESIS | Build the Monday network picture | Monday report |
| CLOSURE | Recheck Tuesday and resolve open observations | Closure report |

## Routing rule

No observation skips provenance. No propagation event is accepted from a single point. No private-person inference is used. Public observations are kept separate from hypotheses about causality.

## Required handoff

`seed -> evidence receipt -> candidate drift -> verification -> propagation event -> Monday synthesis -> Tuesday closure`
