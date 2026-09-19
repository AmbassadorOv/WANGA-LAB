# WANGA-LAB — Independent AI Evidence, Drift Forensics & Verification

WANGA-LAB is the systems architecture and evidence-integrity layer for **AI drift forensics, provenance preservation, reconstruction, and independent verification**.

**Architecture navigation:** [Protected Core → Independent Evidence Infrastructure](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/research/PROTECTED_CORE_AND_EVIDENCE_INFRASTRUCTURE.md) · [Rational Logic — Protected IP Boundary](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/research/RATIONAL_LOGIC_IP_BOUNDARY.md) · [Repository Ecosystem](https://github.com/AmbassadorOv/AmbassadorOv/blob/main/REPOSITORY_ECOSYSTEM.md)

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

## WANGA Computer Architecture

The current architecture baseline composes the existing WANGA structures into a unified computational architecture:

**Lineage Knowledge → WANGA Politeia → Translation Architecture → Rational Logic → Derivation → Drift / Error Verification → Evidence / Provenance**

`Vitruvius Index / Orchestrator` provides the architecture-index and coordination layer across these subsystems.

The central design rule is:

> Logic is the reference point. Models and model compositions are selected according to their demonstrated ability to translate that logic into derivations under defined constraints.

See:
- [WANGA Computer Architecture](docs/ARCHITECTURE/WANGA_COMPUTER_ARCHITECTURE.md)
- [Logic-to-Derivation Translation Architecture](docs/ARCHITECTURE/LOGIC_TRANSLATION_ARCHITECTURE.md)
- [Vitruvius Index / Orchestrator](vitruvius/README.md)
- [WANGA Politeia](docs/ARCHITECTURE/WANGA_POLITEIA.md)

The architecture also distinguishes materially constrained computation from higher-level digital orchestration. This is a systems model for future research, not a claim that a steam-engine-like physical computer has already been implemented.

## Service scope

WANGA-LAB / Drift Forensics is intended to provide independent technical evidence, AI-drift analysis, model-behavior analysis, provenance reconstruction, and systemic-exposure assessment to insurance companies and institutional risk holders with material exposure to banks and other critical financial infrastructure.

The service is an evidence and forensic-analysis layer. It does not itself provide insurance coverage, underwriting, a financial guarantee, solvency assurance, or a regulated insurance product. Commercial and regulatory classification must be reviewed for the applicable jurisdiction before customer use.

## Architectural chain

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers / Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

Rational Logic is a protected reasoning component in this architecture. Its implementation is intentionally outside the public research corpus. See the protected-IP boundary documentation above.

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
## Vitruvius Global Architecture Processor

The repository now contains the first executable layer of the Vitruvius architecture processor: a family taxonomy, an architecture-book data store, a GitHub repository scanner, and a scheduled GitHub Actions workflow for refreshing observed architecture records.

```text
GITHUB -> DISCOVER -> CLASSIFY -> LINEAGE -> VITRUVIUS
       -> POLITEIA -> TRANSLATION -> RATIONAL LOGIC
       -> DERIVATION -> VERIFICATION -> LINEAGE UPDATE
```

The current implementation is an observational indexer, not an automatic code-merger. External repositories remain independent source lineages; the processor records repository identity, default branch, family, WANGA target, evidence state and licensing-review state. Model-assisted GPT/LLM/neural extraction can be attached through the normalized Vitruvius Model Bridge without granting model output verification authority.

Primary implementation files:
- vitruvius/architecture_indexer.py
- vitruvius/data/family_roots.json
- vitruvius/data/architecture_book.json
- .github/workflows/vitruvius-global-index.yml
- vitruvius/MODEL_BRIDGE.md

Architecture status: ACTIVE DEVELOPMENT / OBSERVATIONAL INDEX IMPLEMENTED. A global GitHub scan remains an expanding process rather than a claim of exhaustive coverage.