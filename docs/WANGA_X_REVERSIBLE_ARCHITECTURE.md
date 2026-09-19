# WANGA-X — Requirement-Driven, Evolving Dynamic Computational Architecture

WANGA-X defines the computational architecture as a requirement-derived and time-addressable object.

The system does not begin with a fixed computational architecture and force changing requirements into it. The current computational requirements determine the architecture that should be constructed.

## Core loop

```
HUMAN / SYSTEM DISCOVERY
        ↓
REQUIREMENT
        ↓
REASON / SPECIFY COMPUTATION
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
NEW BLUEPRINT
        ↓
REBUILD / RECOMPOSE / REPLACE
```

## Human discovery is an input trigger

A human researcher may identify a missing architectural assumption or mechanism during sustained work, including through a dream or other internal discovery process.

WANGA-X does not classify the origin as evidence. It records the researcher's explicit report as a **Discovery Trigger**, converts it into a testable hypothesis, and routes it through the normal evidence and verification pipeline.

`DISCOVERY -> HYPOTHESIS -> REQUIREMENT CHANGE -> BLUEPRINT -> BUILD -> TEST -> VERIFY`

The system does not encode the proposition that a dream is true. It encodes the operational fact that a researcher has identified a candidate change worth formalizing and testing.

## Architecture as an editable construction timeline

A WANGA-X build is represented as an ordered sequence of recoverable construction states ("frames").

Each frame records the architectural state reached at that point. A frame can be inspected before construction continues.

Conceptually:

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
   NEW BLUEPRINT
          ↓
   F2' → F3' → F4' → ARCHITECTURE-B
```

The film analogy is intentional: the construction process is a sequence of editable computational states. Stopping at a frame permits inspection and, where required, a change of the construction trajectory rather than forcing completion of an obsolete architecture.

## Dynamic construction primitives

- **DISCOVER** — record a human-identified candidate insight or requirement change.
- **PAUSE** — stop materialization at a defined frame.
- **SNAPSHOT** — preserve the exact architectural state.
- **INSPECT** — evaluate the state and its evidence.
- **ROLLBACK** — restore a previous verified state.
- **FORMALIZE** — convert a discovery into a testable hypothesis and explicit requirements.
- **EDIT** — modify the requirement, Blueprint, or selected architectural components.
- **RECOMPOSE** — assemble a revised architecture from reusable compatible parts.
- **REBUILD** — materialize the revised Blueprint.
- **VERIFY** — validate the new state before continuation or activation.
- **COMMIT** — designate a verified state as an executable architecture version.

## Why this is architectural, not an auxiliary layer

Evolution during work is part of the construction model itself. The system does not merely execute a static architecture and keep external logs about it. The architecture-generation process has a state history that can be traversed, inspected, corrected, and continued.

The resulting abstraction is:

**Discovery/Requirement → Architecture State Sequence → Executable Architecture**

rather than:

**Fixed Architecture → Workload → Adaptation**

## Relation to WANGA-LAB

WANGA-X is intended to become the architectural principle connecting:

- Human Discovery Input — supplies candidate research changes.
- Rational Logic — formalizes and constrains computational requirements.
- Neural Thinking Machine — explores and reasons over candidate computational structures.
- Model Fabric — supplies models and computational resources.
- Evidence / Provenance — preserves construction and execution state.
- Drift Forensics — detects meaningful changes in behavior or requirements.
- Verification — validates architectural states and transitions.

WANGA-X is therefore not treated as an additional bolt-on layer. It changes the architectural assumption under which the other WANGA-LAB components operate.

## Research status

This document defines the architectural hypothesis and target mechanism.

It does not claim that the complete mechanism has already been implemented or experimentally validated.

The next technical milestone is a minimal virtual-processor prototype demonstrating:

1. discovery/requirement input;
2. hypothesis formalization;
3. Blueprint generation;
4. frame-based architecture materialization;
5. pause/snapshot;
6. rollback;
7. requirement change;
8. revised Blueprint;
9. replacement or recomposition;
10. independent verification of the resulting architecture.
