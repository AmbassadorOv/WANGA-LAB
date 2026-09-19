# WANGA-X — Human Discovery Trigger Protocol

Status: DESIGN / RESEARCH

## Purpose

WANGA-X recognizes a practical source of research change: a human researcher may notice a missing relationship, constraint, mechanism, or architectural possibility through sustained work, including during sleep or dreams.

The system does not need to determine the origin of that insight. It treats the researcher's explicit report of the insight as a **Discovery Trigger**.

The trigger is not scientific evidence and is not treated as evidence. It is an input that can cause the research system to create a hypothesis, change a requirement, generate a new Blueprint, and begin a controlled verification path.

## Classification

`HUMAN DISCOVERY -> HYPOTHESIS -> REQUIREMENT CHANGE -> BLUEPRINT -> MATERIALIZATION -> EXPERIMENT -> EVIDENCE -> VERIFICATION`

A Discovery Trigger is therefore:

- **source:** human researcher;
- **type:** discovery trigger;
- **epistemic status:** unverified hypothesis/input;
- **authority:** may initiate research work, but cannot establish truth by itself;
- **required next step:** formalization and test.

Whether the discovery occurred during waking work, reflection, sleep, or a dream is metadata about its origin, not a scientific validity class.

## Operational effect

When a researcher declares that an insight changes the architecture assumption, WANGA-X may:

1. preserve the current architecture snapshot;
2. record the discovery trigger;
3. translate the insight into an explicit hypothesis;
4. derive candidate changed requirements;
5. generate one or more Blueprints;
6. materialize candidate architectures;
7. execute controlled experiments;
8. compare against the previous architecture;
9. preserve all observations and failures;
10. verify the result before activation or commit.

## Reversible research loop

`DISCOVERY -> SNAPSHOT -> FORMALIZE -> BRANCH -> BLUEPRINT -> BUILD -> TEST -> VERIFY -> COMMIT / ROLLBACK`

The original state remains recoverable. A discovery therefore changes the research trajectory without destroying the evidence of the previous trajectory.

## Important distinction

The system must never encode:

`DREAM -> TRUE`

It encodes:

`DREAM/INSIGHT -> RESEARCH TRIGGER -> TESTABLE HYPOTHESIS`

The scientific claim begins only when the resulting mechanism can be specified, implemented, measured, reproduced, and independently checked.

## WANGA-X consequence

This makes the human researcher an explicit source of architectural hypothesis generation without making the human insight itself part of the computational evidence chain.

The architecture can therefore evolve from a human-discovered requirement change while retaining a strict separation between:

- discovery;
- specification;
- implementation;
- observation;
- evidence;
- verification.
