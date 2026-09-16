# WANGA Operating System — Research Computer Architecture

Status: ARCHITECTURAL FOUNDATION
Version: 1.0.0

## Definition

WANGA is defined as an architectural operating system for a research computer whose primary purpose is to measure, organize, test, reproduce, and coordinate knowledge about complex AI systems.

WANGA is not initially defined as a conventional desktop operating system. Its first kernel boundary is the research process itself: measurement → representation → state → transition → behavior → evidence → validated knowledge.

## Core principle

The computer is built around the object of research rather than around a conventional application stack.

The neural-network research core therefore precedes higher-level drift intelligence, global coordination, and user-facing system abstractions.

## Architectural layers

1. RESEARCH KERNEL — experiment identity, method versions, snapshots, provenance, integrity and reproducibility.
2. SENSOR FABRIC — controlled probes that observe model behavior and system conditions.
3. OBSERVATION BUS — immutable measurement records and collection status.
4. REPRESENTATION LAYER — transformations of observations into declared measurable representations.
5. STATE/TRANSITION ENGINE — candidate behavioral states and transitions with uncertainty preserved.
6. EVALUATION ENGINE — comparison against baselines, controls and replication conditions.
7. DRIFT ENGINE — detection and characterization of measurable behavioral change.
8. EARLY-WARNING ENGINE — anomaly, precursor and trigger detection evaluated prospectively.
9. NETWORK/PROPAGATION ENGINE — cross-model, cross-provider, regional, language and temporal relationships.
10. EVIDENCE COMMONS — evidence identifiers, provenance, verification, replication and negative findings.
11. ORCHESTRATION PLANE — agents and workers that execute research tasks without changing scientific rules silently.
12. ARCHITECT INTERFACE — human control, inspection, experiment definition, review and system composition.

## Agent model

Agents are execution components, not authorities. An agent may collect, transform, compare, test or propose an interpretation. Promotion to a validated system fact requires the applicable evidence and verification gates.

Human specialists are introduced where the research graph identifies a domain requiring expertise that is not adequately represented by the existing agent/workflow system.

## Operating rule

`MEASURE → RECORD → REPRESENT → TEST → REPLICATE → VERIFY → PROMOTE`

No stage may be skipped merely because an AI agent produces a plausible result.

## Relationship to Global Drift Network

The existing Global Drift Network becomes a higher-level subsystem consuming validated research-core outputs. It must not redefine the underlying measurement primitives.

## Initial implementation sequence

1. Freeze the architectural vocabulary.
2. Complete probe, observation and run-manifest schemas.
3. Implement a local research harness with deterministic tests.
4. Connect real model interfaces only through explicit adapters and credential isolation.
5. Implement comparator and replication logic.
6. Establish validated state/transition representations.
7. Connect drift detection.
8. Add prospective early-warning evaluation.
9. Add network/propagation analysis.
10. Expose the resulting capabilities through WANGA orchestration.

## Integrity boundaries

- No synthetic observation may be presented as empirical evidence.
- Missing data remain missing.
- API keys and credentials never enter the repository.
- No individual-level surveillance is part of the architecture.
- Temporal succession alone does not establish causality.
- Predictive claims require prospective, out-of-sample evaluation.
- Methods and thresholds are versioned.
- Negative and inconclusive results remain part of the evidence record.

## Current implementation state

The neural-network research core is the first active architectural subsystem. Existing probe definitions and measurement taxonomy form its initial sensor specification. The next executable milestone is the local Probe Runner → Observation Collector → Comparator pipeline.
