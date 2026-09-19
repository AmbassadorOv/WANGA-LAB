# WANGA-X — Research Foundations for Evolving Dynamic Architecture

Status: RESEARCH FOUNDATION / DESIGN

## Purpose

WANGA-X will not begin by inventing every mechanism from first principles. It will use established research directions as technical starting points and add a dynamic architectural layer that connects them into one requirement-driven construction loop.

The initial foundation is organized around four research families:

1. High-Level Synthesis (HLS)
2. Software-Defined Accelerators (SODA)
3. Requirement-to-Architecture synthesis
4. Runtime / adaptive architecture

The objective is not to claim that any of these projects already implement WANGA-X. They provide reusable starting mechanisms.

## Research foundation A — High-Level Synthesis

HLS demonstrates a direct path from high-level algorithmic descriptions to generated hardware designs.

Google XLS is particularly useful as a starting reference because it provides a high-level hardware synthesis toolchain, a central IR, simulation/execution paths, and generation of synthesizable Verilog/SystemVerilog.

WANGA-X research extraction:

`COMPUTATION DESCRIPTION → IR → GENERATED ARCHITECTURE → EXECUTION / VERIFICATION`

Potential reuse:
- intermediate representation;
- graph/dataflow representation;
- lowering pipeline;
- generated architecture;
- execution at multiple abstraction levels;
- formal/correctness checking.

## Research foundation B — SODA

SODA demonstrates automated generation of specialized accelerators from high-level programming frameworks and supports design-space exploration.

WANGA-X research extraction:

`HIGH-LEVEL COMPUTATION → SPECIALIZED ARCHITECTURE → DESIGN-SPACE EXPLORATION → GENERATED IMPLEMENTATION`

Potential reuse:
- architecture templates;
- reusable hardware components;
- automated synthesis;
- design-space exploration;
- optimization loops;
- modular composition.

## Research foundation C — Requirement-to-Architecture synthesis

Recent LLM-based software-architecture research investigates mapping requirements to architectural decisions and alternatives.

ARLO, for example, maps architecturally relevant natural-language requirements to architectural choices and uses optimization to select among alternatives.

WANGA-X research extraction:

`REQUIREMENT → ARCHITECTURAL CONSTRAINTS / CHOICES → ARCHITECTURE CANDIDATE`

Potential reuse:
- requirement formalization;
- architectural decision representation;
- traceability from requirement to architectural choice;
- candidate comparison;
- constraint-based selection.

## Research foundation D — Runtime architectural adaptation

Adaptive architecture research provides mechanisms for changing system structure when runtime conditions or requirements change.

WANGA-X research extraction:

`OBSERVE → DETECT CHANGE → RECONFIGURE / RECOMPOSE`

The WANGA-X research question extends this:

`CHANGED REQUIREMENT → NEW COMPUTATIONAL SPECIFICATION → NEW BLUEPRINT → NEW ARCHITECTURE`

The target is not merely parameter adaptation. The architecture itself becomes a generated object that can be replaced or recomposed.

## Dynamic synthesis layer

WANGA-X places a common dynamic layer over these research directions:

```
                RATIONAL LOGIC
                     ↓
          COMPUTATIONAL REQUIREMENT
                     ↓
             ARCHITECTURE REASONING
                     ↓
              BLUEPRINT / IR
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
     HLS/SODA    SOFTWARE       VIRTUAL
     MATERIAL.   ARCHITECTURE   MATERIALIZER
       ↓             ↓             ↓
       └─────────────┼─────────────┘
                     ↓
                 EXECUTION
                     ↓
             EVIDENCE / VERIFY
                     ↓
             REQUIREMENT CHANGE
                     ↓
              NEW BLUEPRINT
                     ↓
       RECOMPOSE / REBUILD / REPLACE
```

The central research hypothesis is that these capabilities can be unified around a persistent Blueprint/IR and a controlled architecture-state sequence.

## Architecture-state model

Each generated architecture is treated as a versioned computational state:

`A0 → A1 → A2 → ... → An`

A requirement change produces a new candidate trajectory:

`Ak → Requirement' → Blueprint' → Ak+1'`

The system must preserve enough state to inspect, compare, verify, and, when necessary, restore a previously verified state.

Rollback is a mechanism. The architectural principle is **evolving dynamic architecture**.

## First prototype

The first prototype should remain virtual/software-defined rather than attempting physical hardware reconfiguration.

Minimum experiment:

1. define two materially different computational requirements;
2. express each requirement in a common representation;
3. generate at least two architecture Blueprints;
4. materialize each as an executable graph;
5. execute identical test inputs;
6. measure correctness and cost;
7. change the requirement;
8. generate a new Blueprint;
9. recompose or replace the architecture;
10. verify the new architecture independently.

## Research boundary

The existing technologies establish important individual capabilities. They do not, by themselves, establish the complete WANGA-X loop.

Therefore this repository must distinguish:

- **Existing foundation** — published or implemented technologies;
- **WANGA-X integration hypothesis** — proposed combination;
- **Prototype** — implemented experimental mechanism;
- **Verification** — experimentally demonstrated behavior.

No claim of novelty, priority, or complete implementation is made until the corresponding evidence exists.
