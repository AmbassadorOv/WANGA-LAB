# Forensic Card Schema

## Purpose

A forensic card is a bounded evidence object representing one aspect of an AI system, event, observation, intervention, or verification result.

Cards are designed to make forensic records composable without pretending that every field is always available.

## Common Envelope

Every card should contain, where available:

```yaml
case_id: "CASE-YYYY-NNN"
card_id: "CARD-YYYY-NNN-NNN"
card_type: "SYSTEM|MODEL|ENVIRONMENT|DATA|CONFIGURATION|EVENT|TIMELINE|EVIDENCE|ATTRIBUTION|INTERVENTION|VERIFICATION"
status: "DRAFT|OBSERVED|PRESERVED|VERIFIED|DISPUTED|SUPERSEDED"
created_at: "ISO-8601"
observed_at: "ISO-8601 or interval"
source: "human|system|log|measurement|provider|third-party"
provenance_ref: "identifier"
content_hash: "hash if available"
operator: "identifier or role"
notes: "free text"
```

## Card Types

### SYSTEM

Defines the system boundary and the object under examination.

Required conceptual fields:
- system identity;
- owner/operator role, if known;
- operational purpose;
- scope boundary;
- observation window.

### MODEL

Records model identity and deployment context.

Fields may include:
- provider;
- model family;
- version or deployment identifier;
- model configuration;
- release/deployment timestamp;
- model artifact reference, where legitimately available.

### ENVIRONMENT

Records the execution environment relevant to reproducibility.

Fields may include:
- runtime;
- infrastructure;
- region;
- software dependencies;
- external services;
- hardware or accelerator context;
- environment snapshot reference.

### DATA

Records data provenance and measurable distribution observations.

Fields may include:
- dataset or stream identifier;
- collection window;
- provenance;
- schema version;
- distribution metrics;
- sampling conditions;
- known limitations.

### CONFIGURATION

Records mutable control-plane state.

Examples:
- prompts;
- policies;
- thresholds;
- routing;
- tools;
- feature flags;
- system instructions;
- deployment parameters.

Sensitive values should be represented by controlled references or redacted derivatives rather than unnecessarily copied into public records.

### EVENT

Records an observed, reported, or deliberately controlled event.

Fields:
- event type;
- start/end time;
- trigger;
- observed effect;
- affected component;
- evidence references;
- confidence/status.

### TIMELINE

Represents ordered events and state transitions.

A timeline should distinguish:
- directly observed timestamps;
- inferred timestamps;
- reported timestamps;
- synchronization uncertainty.

### EVIDENCE

Represents a preserved artifact or measurement.

Fields may include:
- artifact identifier;
- artifact type;
- acquisition timestamp;
- acquisition method;
- content hash;
- storage reference;
- chain-of-custody events;
- transformation history.

### ATTRIBUTION

Maps candidate contributors without collapsing uncertainty prematurely.

A useful structure is:

```text
OBSERVED EFFECT
    |
    +-- candidate component A
    +-- candidate dependency B
    +-- candidate configuration C
    +-- environmental factor D
    +-- unresolved / alternative explanation
```

Each edge should carry evidence references and an attribution status such as `SUPPORTED`, `CONSISTENT`, `UNRESOLVED`, or `REFUTED`.

### INTERVENTION

Records a corrective or preventive action.

Fields may include:
- intervention objective;
- pre-intervention state reference;
- action;
- operator/authority;
- start/end time;
- expected effect;
- evidence captured during action;
- rollback state, if applicable.

### VERIFICATION

Records whether the intervention changed the measured condition.

Verification should specify:
- baseline used;
- test procedure;
- observed result;
- reproducibility status;
- residual drift;
- independent reviewer, if any;
- unresolved limitations.

## Evidence-State Model

```text
DECLARED
   ↓
OBSERVED
   ↓
CAPTURED
   ↓
PRESERVED
   ↓
REPRODUCED
   ↓
INDEPENDENTLY VERIFIED
```

These states are not interchangeable. A provider statement, a log record, a captured artifact, a reproduced behavior, and an independent verification result have different evidentiary meanings.

## Public/Private Boundary

Public documentation should expose methodology, non-sensitive evidence references, status, limitations, and reproducibility claims that can be supported.

Private case material may contain sensitive technical details. Public records must not disclose credentials, secrets, personal data, proprietary material, or security-sensitive implementation details unless authorized and appropriate.
