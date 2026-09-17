# Candidate Standard: Algorithmic Governance & AI Drift Evidence

**Document ID:** AGGI-STD-DRIFT-0.1
**Status:** Candidate Research Specification
**Owner:** Global Algorithmic Governance Institute research program
**Repository:** WANGA-LAB
**Scope:** Technical evidence, interoperability, reproducibility and governance interfaces for AI-system drift observations

> This document is a research specification. It is not an adopted international standard, certification scheme, legal opinion, regulatory rule, or conformity assessment.

## 1. Objective

Define a common technical representation for observing, documenting, reproducing and exchanging evidence of changes in AI-system behavior.

The specification is designed to interoperate with existing AI governance and risk-management frameworks rather than replace them.

## 2. Core principle

A change is not automatically a drift event.

A candidate drift record requires, at minimum:

1. a defined baseline or comparison state;
2. a measurable change;
3. a timestamp or bounded observation interval;
4. provenance for the observation;
5. a reproducible measurement definition;
6. uncertainty information;
7. an explicit treatment of plausible alternative causes.

## 3. Drift evidence object

Each observation should support the following logical fields:

```text
observation_id
case_id
source_id
source_type
observed_at
observation_window
baseline_id
model_or_system_id
model_version
provider
environment
jurisdiction_context
metric
baseline_value
observed_value
delta
delta_t
persistence
signature_id
parent_observation_id
common_source_id
alternative_causes
uncertainty
analyzer_version
evidence_hash
created_at
```

Implementations may serialize these fields as JSON, CSV, database records, or other interoperable representations.

## 4. Propagation model

The default analytical graph is:

```text
SOURCE
  ↓
OUTBOUND WAVE
  ↓
NETWORK OBSERVATIONS
  ↓
RETURN WAVE
  ↓
SOURCE
```

Propagation measurements may include:

- first observed onset;
- propagation delay;
- amplitude change;
- attenuation or amplification;
- persistence;
- coverage;
- signature similarity;
- language/region lag;
- model/provider lag;
- replication status;
- return-wave relationship.

Temporal sequence alone must not be treated as proof of causation.

## 5. Evidence levels

### L0 — Observation

A timestamped, provenance-linked observation exists.

### L1 — Reproducible

The observation can be repeated under defined conditions with materially similar results.

### L2 — Independently verified

A second analysis or independent measurement process confirms the relevant observation under declared conditions.

### L3 — Cross-environment

The pattern has been tested across a defined boundary such as model version, provider, language, geography, infrastructure, or deployment environment.

### L4 — Institutional-ready

The evidence package contains sufficient metadata, lineage, hashes, methodology, uncertainty and alternative-cause records for an external institution to conduct its own assessment.

L4 does not mean certified, legally admissible, regulator-approved, or causally proven.

## 6. Baseline and measurement discipline

The baseline must be frozen or versioned before comparative claims are made.

Changes to the baseline, analyzer, source selection, sampling method or metric definition must produce a new versioned analysis record.

Raw observations should be preserved separately from normalized and derived data.

## 7. Alternative-cause registry

Every material propagation analysis should record known or plausible competing explanations, including:

- model updates;
- provider configuration changes;
- upstream data/feed changes;
- common public-source events;
- policy or regulatory publications;
- infrastructure incidents;
- benchmark or evaluator changes;
- sampling changes;
- analyzer changes.

The absence of an identified alternative cause is not evidence that causality has been established.

## 8. Evidence integrity

Where technically feasible, an evidence package should contain:

```text
raw/
normalized/
derived/
manifest.json
sha256sums.txt
run_metadata.json
methodology.md
```

The manifest should identify source versions, collection timestamps, analyzer version and relevant file hashes.

## 9. Governance interface

The technical record may be consumed by:

- AI developers and deployers;
- independent evaluation laboratories;
- standards organizations;
- insurers and risk-transfer institutions;
- regulators and supervisory bodies;
- academic and civil-society research groups.

Each consumer remains responsible for its own legal, financial, regulatory and institutional conclusions.

## 10. Interoperability target

The Institute should maintain crosswalks to external frameworks, including ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF, OECD AI Principles and the EU AI Act. These references define comparison points; they do not imply endorsement or conformity.

## 11. Change control

Every specification release must contain:

- document ID;
- semantic version;
- publication timestamp;
- change summary;
- previous version reference;
- responsible editor;
- review status;
- unresolved issues.

## 12. Research status

Version 0.1 is intentionally a candidate specification. Before external publication as a formal standard, the program should add test vectors, machine-readable schemas, conformance tests, independent review, security review, and a public change-control process.
