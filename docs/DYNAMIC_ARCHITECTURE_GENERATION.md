# WANGA-LAB — Dynamic Architecture Generation

WANGA-LAB treats computational architecture as a dynamically materializable object rather than assuming that one fixed architecture must remain in place for the lifetime of a workload.

## Core architectural principle

A computation request may determine the architecture required to execute that computation.

A human discovery may also reveal that the current requirement or architecture assumption is incomplete. That discovery becomes a research trigger, not evidence.

The central architecture representation is a **Blueprint**. The Blueprint is not merely documentation: it is intended to be the representation from which an executable architecture can be materialized.

```
HUMAN / SYSTEM DISCOVERY
      ↓
REQUIREMENT
      ↓
ARCHITECTURE BLUEPRINT
      ↓
ARCHITECTURE MATERIALIZATION
      ↓
EXECUTION
      ↓
NEW COMPUTE REQUIREMENT
      ↓
NEW BLUEPRINT / NEW ARCHITECTURE
```

When a suitable architecture already exists, the system may materialize that architecture. When no suitable architecture exists, the target architecture may be constructed from compatible architectural parts and then materialized for execution.

## Discovery-to-architecture transition

The system must distinguish five states:

1. **Discovery** — a researcher identifies a possible missing mechanism or requirement.
2. **Hypothesis** — the discovery is translated into a falsifiable technical proposition.
3. **Requirement** — the proposition is expressed as computational constraints or objectives.
4. **Blueprint** — an executable architecture candidate is specified.
5. **Evidence** — experimental execution produces observations that can be independently checked.

This prevents the origin of an idea from being confused with validation of the idea.

## Three functions in one architectural representation

The model intentionally keeps these functions conceptually unified:

1. **Blueprint** — what architecture is required.
2. **Build/materialization** — how that architecture becomes executable.
3. **Change/replacement** — how a new computational requirement results in a new architecture.

The architecture may therefore be replaced rather than merely modified in place.

## Existing technology vs. WANGA-LAB research direction

Related technologies already exist in areas such as hardware description, high-level synthesis, runtime reconfiguration, virtual processors, programmable accelerators, and dynamic execution systems.

WANGA-LAB does **not** claim that these underlying technologies were invented here.

The research direction documented here is the proposed unification of:

**human/system discovery → requirement formalization → compute-demand-driven Blueprint generation → architecture materialization → architecture replacement**, including the possibility of assembling a new architecture from reusable parts of existing architectures.

This is recorded as a research hypothesis/design direction until implemented and experimentally verified.



## Research foundations

The initial implementation path will build on established research rather than recreate every mechanism from zero. WANGA-X will use four foundation families: High-Level Synthesis (HLS), Software-Defined Accelerators (SODA), requirement-to-architecture synthesis, and runtime/adaptive architecture.

### HLS / XLS

High-Level Synthesis provides the starting mechanism for translating high-level computation into generated hardware. Google XLS is a useful reference because it provides a central IR, multiple execution/simulation paths, and generation of synthesizable Verilog/SystemVerilog.

WANGA-X extraction: **computation → intermediate representation → generated architecture → execution/verification**.

### SODA

SODA provides automated generation of specialized accelerators from high-level programming frameworks and design-space exploration. It is useful as a foundation for reusable components, specialization, synthesis, and optimization loops.

WANGA-X extraction: **high-level computation → specialized architecture → design-space exploration → generated implementation**.

### Requirement-to-Architecture research

Recent LLM-based architecture research demonstrates mapping requirements to architectural decisions and candidate architectures. WANGA-X will use this as the starting point for requirement formalization and architectural candidate generation.

WANGA-X extraction: **requirement → architectural constraints/choices → architecture candidate**.

### Runtime adaptation

Runtime/adaptive architecture research provides mechanisms for changing system structure when conditions change. WANGA-X extends the research question from runtime reconfiguration toward requirement-driven generation of a new computational Blueprint and architecture.

WANGA-X extraction: **changed requirement → new computational specification → new Blueprint → new architecture**.

### Unified dynamic layer

These foundations are not treated as separate experiments. WANGA-X will investigate a common dynamic layer:

```
RATIONAL LOGIC
      ↓
COMPUTATIONAL REQUIREMENT
      ↓
ARCHITECTURE REASONING
      ↓
BLUEPRINT / IR
      ↓
MATERIALIZATION
      ↓
EXECUTION
      ↓
EVIDENCE / VERIFICATION
      ↓
CHANGED REQUIREMENT
      ↓
NEW BLUEPRINT
      ↓
RECOMPOSE / REBUILD / REPLACE
```

The first prototype remains virtual/software-defined. The goal is to demonstrate that the same computational requirement interface can produce different executable architectures and that a changed requirement can produce a new architecture while preserving explicit state, evidence, and verification boundaries.

See `docs/WANGA_X_RESEARCH_FOUNDATIONS.md` for the source-family map and prototype plan.

## Performance principle

A pre-materialized architecture may be available for rapid activation. If the required architecture is not already available, additional preparation/materialization latency is expected.

No fixed latency claim is made at this stage. Performance targets are experimental until measured.

## Status

- **Discovery input:** supported as a research trigger.
- **Concept:** defined.
- **Prior-art relationship:** related technologies identified; exact system-level novelty requires dedicated research.
- **Implementation:** not yet claimed as complete.
- **Verification:** not yet established.
- **Research priority:** architecture generation, dynamic materialization, and reversible change.
