# Global Algorithmic Governance Institute — Standards Registry V0.1

Status: RESEARCH / REFERENCE MAPPING ONLY
Version: 0.1.0

## Purpose

This registry maps the Institute's proposed technical work to existing public AI governance, risk-management, and standards frameworks. It does **not** claim adoption, certification, legal equivalence, regulatory approval, or conformity with any external standard.

The Institute's candidate standard should be developed as an interoperable research layer that can be compared against established frameworks.

## Primary reference set

| Reference | Role in the mapping | Institute interface |
|---|---|---|
| ISO/IEC 42001:2023 | AI management-system requirements | Governance, lifecycle controls, continual improvement |
| ISO/IEC 23894:2023 | AI risk-management guidance | Risk taxonomy, risk records, treatment and monitoring |
| NIST AI RMF 1.0 | Voluntary AI risk-management framework | Govern / Map / Measure / Manage; TEVV alignment |
| OECD AI Principles (2024 update) | Intergovernmental principles | International interoperability and policy vocabulary |
| EU AI Act (Regulation (EU) 2024/1689) | Binding EU legal framework | Traceability, logging, monitoring, conformity-assessment interface |
| EU AI Act standardisation programme | Technical standardisation interface | Mapping candidate requirements to future harmonised standards |

## Candidate Institute layers

### AGGI-01 — Evidence Identity

Every observation receives a stable identifier, source reference, timestamp, collection method, analyzer version, and evidence hash where technically applicable.

### AGGI-02 — Baseline

A drift claim requires a defined baseline or reference state. Baseline selection must be explicit and reproducible.

### AGGI-03 — Drift Observation

Record what changed, the magnitude of change, onset time, persistence, and measurement uncertainty.

### AGGI-04 — Propagation

Represent observations across models, providers, regions, languages, infrastructure, or public information surfaces without assuming causality from temporal sequence alone.

### AGGI-05 — Attribution

Separate observed sequence from causal attribution. Record common-source explanations, external events, model changes, and other alternative causes.

### AGGI-06 — Reproducibility

A result should include enough technical metadata for an independent party to attempt reproduction.

### AGGI-07 — Conformance

Candidate conformance levels:

- L0 — OBSERVATION
- L1 — REPRODUCIBLE
- L2 — VERIFIED
- L3 — CROSS-ENVIRONMENT
- L4 — INSTITUTIONAL-READY

These levels describe the evidence package, not legal status or regulatory approval.

## Evidence chain

```text
SOURCE
  ↓
BASELINE
  ↓
OBSERVATION
  ↓
SIGNATURE
  ↓
PROPAGATION
  ↓
ALTERNATIVE-CAUSE ANALYSIS
  ↓
INDEPENDENT VERIFICATION
  ↓
CONFORMANCE RECORD
```

## Separation rule

Scientific evidence, legal conclusions, economic allocation, insurance decisions, and institutional decisions are separate domains. A technical observation must not be converted automatically into a legal, financial, or regulatory conclusion.

## External reference URLs

- ISO/IEC 42001: https://www.iso.org/standard/42001
- ISO/IEC 23894: https://www.iso.org/standard/77304.html
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Playbook: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
- OECD AI Principles: https://www.oecd.org/en/topics/ai-principles.html
- EU AI Act: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU AI Act standardisation: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation

## Next work

1. Build a requirement-to-evidence crosswalk.
2. Define the machine-readable observation schema.
3. Define the forensic evidence package and manifest.
4. Define conformance tests.
5. Add versioning and change-control rules.
6. Add an external-review process.
7. Publish the candidate standard as a research specification before any claim of adoption or certification.
