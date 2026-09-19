# WANGA-LAB — Independent AI Evidence, Drift Forensics & Verification

WANGA-LAB is the systems architecture and evidence-integrity layer for **AI drift forensics, provenance preservation, reconstruction, and independent verification**.

**Architecture navigation:** [WANGA Global Computational Architecture](docs/WANGA_GLOBAL_COMPUTATIONAL_ARCHITECTURE.md) · [Protected Core → Independent Evidence Infrastructure](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/research/PROTECTED_CORE_AND_EVIDENCE_INFRASTRUCTURE.md) · [Rational Logic — Protected IP Boundary](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/research/RATIONAL_LOGIC_IP_BOUNDARY.md) · [Repository Ecosystem](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/REPOSITORY_ECOSYSTEM.md)


## Vitruvian Atomic Architecture — the computer we are building

The current WANGA concept is larger than GitHub. GitHub is one **evidence-bearing implementation surface**, not the final home of the architecture.

The central idea is a **Vitruvian Atomic Architecture**: Vitruvius continuously decomposes the system from architecture → family → subfamily → child → family atom → subatom, then discovers relationships between atoms even when the same atom belongs to multiple families. Each atom carries lineage, governance, evidence state and a deterministic neural endpoint, and the resulting relationships fold into a global computational network.

The intended computer is therefore not organized as a flat repository tree. It is organized as a **recursive, multi-family architecture graph** in which computation, evidence, governance, research and publication can intersect at atomic level.

GitHub currently provides the source-control and evidence surface for this work. A future platform layer may provide the larger persistent graph and orchestration substrate. Current candidates include graph-computing infrastructure such as Apache TinkerPop, property-graph/knowledge-graph platforms such as Neo4j, and standards-based RDF/SHACL representations. TinkerPop explicitly supports graph databases and graph analytics; Neo4j provides node/relationship traversal and knowledge-graph capabilities; W3C RDF/SHACL provides a standards-based representation and constraint-validation layer. These are **candidate building blocks, not a final platform selection**. citeturn0search1turn0search8turn0search5

The architectural requirement is platform-independent: the substrate must preserve recursive hierarchy, multi-family membership, cross-family atom bridges, provenance, governance constraints, verification state, and machine-traversable relationships. W3C's Web of Things work is another useful interoperability reference because its Thing Description model is designed to describe entities and their interfaces in a machine-readable form and to support integration across heterogeneous systems. citeturn0search0turn0search4

**Conceptual target:** GitHub and other external systems become connected surfaces feeding the Vitruvian graph; they are not the graph itself.

```
                         WANGA COMPUTATIONAL ARCHITECTURE
                                      │
                              VITRUVIUS ENGINE
                                      │
                 ┌────────────────────┼────────────────────┐
                 ▼                    ▼                    ▼
          FAMILY ATOMS          CROSS-FAMILY          GOVERNANCE
                 │               RELATIONSHIPS             │
                 └────────────────────┼────────────────────┘
                                      ▼
                           GLOBAL COMPUTATIONAL GRAPH
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
                 GitHub          Research/Data       Future Platforms
                    │                 │                 │
                    └─────────────────┴─────────────────┘
                                      │
                                      ▼
                              WANGA COMPUTING SYSTEM
```

## WANGA and Rational Logic

WANGA is treated in this research as a distinct computing architecture, not simply as a wrapper around a language model.

Within WANGA:

**Rational Logic = the canonical logic and reasoning layer**

This is a statement about system architecture. It does not claim separate physical hardware. The public repository documents the relationship between the system and its logic layer; deeper formal details and proprietary implementation remain outside the public disclosure boundary.

## Core distinction

WANGA-LAB is not primarily an AI engine.

Its public role is to provide an **independent evidence layer around AI systems**:

**Evidence Protocol → Drift Artifact → Verification Chain → Governance Interface**

The system under examination may be internal, external, proprietary, open-source, or supplied by another organization.

The purpose is to establish what happened, preserve relevant evidence, reconstruct the event, and verify the resulting finding without treating the evaluated model as the sole authority on its own correction or validity.

## Service scope

WANGA-LAB / Drift Forensics is intended to provide independent technical evidence, AI-drift analysis, model-behavior analysis, provenance reconstruction, and systemic-exposure assessment to insurance companies and institutional risk holders with material exposure to banks and other critical financial infrastructure.

The service is an evidence and forensic-analysis layer. It does not itself provide insurance coverage, underwriting, a financial guarantee, solvency assurance, or a regulated insurance product. Commercial and regulatory classification must be reviewed for the applicable jurisdiction before customer use.

## Architectural chain

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers / Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

The expanded system architecture is documented in **[WANGA Global Computational Architecture](docs/WANGA_GLOBAL_COMPUTATIONAL_ARCHITECTURE.md)**.

Rational Logic is a protected reasoning component in this architecture. Its implementation is intentionally outside the public research corpus.

## Evidence and verification

A representative verification chain is:

**Canonical Representation → SHA-256 Integrity → Timestamp Evidence → Deterministic Replay → Comparison → Verification Result**

The exact mechanism set depends on the case. Hashes, timestamps, anchors, signatures, replay and verification answer different evidentiary questions and must not be treated as interchangeable.

External timestamping or anchoring is not treated as complete until actual proof is received and checked.

## Current empirical fixture

**CASE_REF_2026_DRIFT_KNOWN_RISK_001**

Current evidence status: **VERIFIED**

[Open the verified synthetic case package](artifacts/drift-known-risk-001/README.md)

The canonical case package demonstrates a repository-level, deterministic criterion-drift finding and provides the structure for:

- case metadata and scope;
- evidence inventory and hashes;
- replay inputs and instructions;
- normalized outputs;
- verification and integrity checks.

A planned fixture is not represented as a completed client investigation, legal finding, regulatory certification, underwriting decision, or commercial performance result.

## Drift forensics

The central research sequence is:

**Baseline → Observation → Drift Detection → Evidence Preservation → Reconstruction → Causal / Dependency Analysis → Attribution → Risk Quantification → Intervention → Verification**

The evaluation chain is:

**Model → Answer → Evaluation → Correction → Criterion Change → Re-evaluation**

Research distinguishes point error from changes in definition, premise, inference, criteria, question fidelity, evidence/source fidelity, terminology, and response trajectory.

## Implemented evidence infrastructure

The repository contains implemented evidence-integrity and workflow components, including:

- canonical representations;
- SHA-256 integrity chains;
- contract/hash binding;
- timestamp adapters;
- verification tests;
- deterministic replay fixtures;
- CI-based verification workflows;
- insurer-intake triage and controlled case-queue mechanisms.

Implementation existence does not by itself establish external verification.

## Operating discipline

The preferred engineering sequence is:

**READ → CLAIM → IMPLEMENT → TEST → VERIFY → COMMIT → PR → REVIEW**

No component is treated as complete merely because code exists.

Evidence states remain explicit:

**BUILT · SPECIFIED · PROTOTYPED · TESTED · VERIFIED · PLANNED · HYPOTHETICAL**

## Legal and governance boundary

Software and cryptographic evidence mechanisms do not automatically establish legal admissibility, regulatory status, underwriting authority, or contractual enforceability.

WANGA-LAB therefore keeps technical evidence, governance research, legal review, institutional authority, and protected intellectual property as distinct layers.

## Public / protected model

The public research layer documents:

**methodology · architecture · provenance · drift analysis · verification interfaces · reproducible evidence artifacts**

The protected layer may retain:

**implementation details · algorithms · mechanisms · proprietary technical material**

This separation is intentional. The public system documents the evidence capability without publishing the protected reasoning implementation.
