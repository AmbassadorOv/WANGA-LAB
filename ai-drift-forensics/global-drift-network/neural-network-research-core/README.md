# Neural Network Research Core

Status: FOUNDATIONAL RESEARCH MODULE  
Version: 0.1.0

## Purpose

The Neural Network Research Core is the first research layer for WANGA's future architectural computer. Its purpose is to build an empirical, reproducible model of neural-network behavior before higher-level drift, early-warning, propagation, or operating-system layers are treated as established architecture.

The core does not assume that a neural network has been understood merely because its outputs can be observed. It separates observable measurements from inferred structure and requires reproducible evidence before promoting an inference into a system primitive.

## Research chain

`INPUT → PROCESSING OBSERVATIONS → REPRESENTATIONS → STATE → TRANSITION → OUTPUT → BEHAVIOR`

Each stage is recorded independently where measurement access exists.

## Initial research questions

1. What can be measured reliably from a neural network or model interface?
2. Which measurements are stable under repeated controlled probes?
3. Which internal or external representations correlate with observable behavior?
4. Can behavioral states and transitions be defined reproducibly?
5. Which changes are ordinary variance, which are anomalies, and which constitute measurable drift?
6. Which apparent structures survive replication across prompts, runs, models, providers, languages, and time?

## Design principles

- Observation precedes interpretation.
- Measurement and inference are separate record types.
- No claim of full interpretability is made from partial observability.
- No causal claim follows from temporal order alone.
- Methods, probe definitions, baselines, thresholds, and versions are immutable within an experiment.
- Missing measurements remain missing; they are never replaced with synthetic observations.
- Negative and inconclusive findings are retained.
- Public or explicitly authorized data only.
- Reproducibility is a first-class requirement.

## Module boundary

This module is upstream of:

- international drift detection
- precursor and early-warning detection
- propagation and network analysis
- WANGA orchestration and operating-system abstractions

Those systems may consume validated outputs from this core, but must not silently redefine its measurements.

## Planned components

- `RESEARCH_PROTOCOL_V1.md` — foundational research protocol
- `OBSERVATION.schema.json` — raw measurement record
- `REPRESENTATION.schema.json` — representation-level record
- `STATE_TRANSITION.schema.json` — candidate state/transition record
- `PROBE_REGISTRY.json` — controlled probe definitions
- `MEASUREMENT_TAXONOMY.md` — measurement vocabulary and units
- `REPLICATION_PROTOCOL_V1.md` — repeatability and cross-condition tests
- `INTERPRETABILITY_BOUNDARIES.md` — what the system can and cannot claim

## Current maturity

This is a research foundation, not a production interpretability system. The next stage is to define the schemas and controlled probe protocol before implementing automation.
