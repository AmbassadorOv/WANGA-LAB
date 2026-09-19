# WANGA-X — Requirement-Driven, Evolving Dynamic Computational Architecture

WANGA-X defines the computational architecture as a requirement-derived and time-addressable object.

## Core paradigm

The architecture is not the first computational object. The process begins with the user's query or system request:

```
USER QUERY / SYSTEM REQUEST
        ↓
REQUIREMENT
        ↓
REQUIRED NEURAL COMPUTATION
        ↓
NEURAL COMPUTATIONAL STRUCTURE
        ↓
BLUEPRINT
        ↓
NEURAL COMPUTER
        ↓
EXECUTION
```

The central thesis is that the **required neural computation** is the determinant between the requirement and the Blueprint. The Blueprint then specifies the neural computer that performs that computation.

This is the WANGA-X architectural direction:

**Do not fit the required computation into a fixed neural architecture; derive the Blueprint of the neural computer from the neural computation required by the user's request.**

When the requirement changes, the neural computation is reconsidered and a new or changed Blueprint may be generated:

```
CHANGED REQUIREMENT
        ↓
NEW REQUIRED NEURAL COMPUTATION
        ↓
NEW / CHANGED COMPUTATIONAL STRUCTURE
        ↓
NEW BLUEPRINT
        ↓
EVOLVED NEURAL COMPUTER
```

The evolving neural system may include changes to architecture, topology, modules, connections, routing, parameters/weights, resources, and state representation as required by the computation.

## Core loop

```
HUMAN / SYSTEM DISCOVERY
        ↓
USER / SYSTEM REQUIREMENT
        ↓
REQUIRED NEURAL COMPUTATION
        ↓
ARCHITECTURE BLUEPRINT
        ↓
FRAME-BY-FRAME MATERIALIZATION
        ↓
EXECUTION
        ↓
OBSERVE / VERIFY
        ↓
NEW OR CHANGED REQUIREMENT
        ↓
NEW NEURAL COMPUTATION
        ↓
NEW BLUEPRINT
        ↓
REBUILD / RECOMPOSE / REPLACE
```

## Human discovery is an input trigger

A human researcher may identify a missing architectural assumption or mechanism during sustained work, including through a dream or other internal discovery process.

WANGA-X does not classify the origin as evidence. It records the researcher's explicit report as a **Discovery Trigger**, converts it into a testable hypothesis, and routes it through the normal evidence and verification pipeline.

`DISCOVERY -> HYPOTHESIS -> REQUIREMENT CHANGE -> NEURAL COMPUTATION -> BLUEPRINT -> BUILD -> TEST -> VERIFY`

## Architecture as an editable construction timeline

A WANGA-X build is represented as an ordered sequence of recoverable construction states ("frames").

Each frame records the architectural state reached at that point. A frame can be inspected before construction continues.

```
F0 → F1 → F2 → F3 → F4 → ARCHITECTURE-A
          ↑
        PAUSE
          ↓
     INSPECT / VERIFY
          ↓
   ROLLBACK TO F2
          ↓
   CHANGE REQUIREMENT
          ↓
 NEW NEURAL COMPUTATION
          ↓
   NEW BLUEPRINT
          ↓
 F2' → F3' → F4' → ARCHITECTURE-B
```

## Dynamic construction primitives

- **DISCOVER** — record a human-identified candidate insight or requirement change.
- **PAUSE** — stop materialization at a defined frame.
- **SNAPSHOT** — preserve the exact architectural state.
- **INSPECT** — evaluate the state and its evidence.
- **ROLLBACK** — restore a previous verified state.
- **FORMALIZE** — convert a discovery into a testable hypothesis and explicit requirements.
- **DERIVE** — determine the neural computation required by the requirement.
- **EDIT** — modify the requirement, Blueprint, or selected architectural components.
- **RECOMPOSE** — assemble a revised architecture from reusable compatible parts.
- **REBUILD** — materialize the revised Blueprint.
- **VERIFY** — validate the new state before continuation or activation.
- **COMMIT** — designate a verified state as an executable architecture version.

## Why this is architectural, not an auxiliary layer

Evolution during work is part of the construction model itself. The system does not merely execute a static architecture and keep external logs about it. The architecture-generation process has a state history that can be traversed, inspected, corrected, and continued.

The resulting abstraction is:

**Query/Requirement → Required Neural Computation → Blueprint → Neural Computer**

rather than:

**Fixed Neural Architecture → Workload → Adaptation**

## Relation to WANGA-LAB

WANGA-X is intended to become the architectural principle connecting:

- Human Discovery Input — supplies candidate research changes.
- Rational Logic — formalizes and constrains the required computation.
- Neural Thinking Machine — reasons over candidate neural computational structures.
- Model Fabric — supplies models and computational resources.
- Evidence / Provenance — preserves construction and execution state.
- Drift Forensics — detects meaningful changes in behavior or requirements.
- Verification — validates architectural states and transitions.

WANGA-X is therefore not treated as an additional bolt-on layer. It changes the architectural assumption under which the other WANGA-LAB components operate.

## Research status

This document defines the architectural hypothesis and target mechanism.

It does not claim that the complete mechanism has already been implemented or experimentally validated.

The next technical milestone is a minimal virtual-processor prototype demonstrating:

1. query/requirement input;
2. required neural-computation derivation;
3. Blueprint generation;
4. frame-based architecture materialization;
5. pause/snapshot;
6. controlled requirement change;
7. revised neural computation;
8. revised Blueprint;
9. replacement or recomposition;
10. independent verification.
