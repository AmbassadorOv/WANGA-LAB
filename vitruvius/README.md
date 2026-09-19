# Vitruvius Index / Orchestrator

Status: ARCHITECTURE SPECIFICATION
Version: 0.1.0

## Purpose

Vitruvius is the index and orchestration layer that connects WANGA-LAB architectures without collapsing them into one undifferentiated subsystem.

## Role

Vitruvius maps:

```text
ARCHITECTURE
    <-> COMPONENT
    <-> INTERFACE
    <-> DEPENDENCY
    <-> LINEAGE
    <-> CAPABILITY
    <-> STATE
    <-> EVIDENCE
```

## Position

```text
                 VITRUVIUS
                     |
      +--------------+--------------+
      |              |              |
      v              v              v
   POLITEIA      TRANSLATION      COMPUTE
      |              |              |
      +--------------+--------------+
                     |
                     v
                  LOGIC
                     |
                     v
                DERIVATION
                     |
                     v
                 FORENSICS
                     |
                     v
                  EVIDENCE
```

## Responsibilities

1. Maintain the canonical architecture index.
2. Resolve architecture and component dependencies.
3. Map lineage knowledge to candidate computational structures.
4. Route work to the correct architecture.
5. Preserve explicit interfaces between specialized subsystems.
6. Track configuration and state references.
7. Expose verification and evidence dependencies.
8. Support future dynamic architecture materialization from a Blueprint.

## Non-responsibilities

Vitruvius does not:

- define Rational Logic;
- replace Politeia;
- become the model;
- become the evidence itself;
- convert predictions into verified facts.

## Core flow

```text
REQUEST
  |
  v
VITRUVIUS INDEX
  |
  +--> identify architectures
  +--> resolve dependencies
  +--> consult lineage knowledge
  +--> invoke Politeia
  +--> route translation
  +--> collect derivation
  +--> invoke verification
  +--> bind evidence
  |
  v
TRACEABLE RESULT
```

The implementation of orchestration is intentionally separate from the protected Rational Logic implementation.
