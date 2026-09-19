# External Architecture Lineage & Integration Registry

Status: SPECIFIED / RESEARCH INTEGRATION
Version: 0.1.0
Scope: PUBLIC RESEARCH
Parent: WANGA Computer Architecture

## Purpose

This registry maps relevant external open-source architecture lineages into the WANGA architecture-family tree.

The objective is not to copy external systems. It is to identify reusable architectural properties, evidence-producing mechanisms, interfaces, and possible descendant architectures.

External projects remain independently owned. Inclusion in this registry does not imply endorsement, partnership, integration, licensing permission, or collaboration.

## Integration rule

For each external lineage:

1. Identify the architectural property.
2. Classify its function.
3. Place the property in the WANGA lineage tree.
4. Identify the compatible WANGA interface.
5. Define a candidate integration or descendant.
6. Preserve attribution and license constraints.
7. Test before treating the property as integrated.
8. Record evidence and verification state.

## Candidate lineages

### 1. VeriGov-AI

Repository: weicaiuw/verigov-ai
URL: https://github.com/weicaiuw/verigov-ai

Observed public architecture:
- ontology-grounded agent capabilities;
- credential registration and verification;
- task-level policy enforcement;
- append-only interaction logging;
- digital-twin participation governance.

WANGA placement:

LINEAGE KNOWLEDGE
  -> GOVERNANCE / AGENT PARTICIPATION LINEAGE
  -> POLITEIA
  -> EVIDENCE / PROVENANCE

Candidate reusable properties:
- capability verification;
- policy-gated participation;
- credential lifecycle;
- append-only interaction records.

Candidate descendant:
VERIFIABLE AGENT GOVERNANCE NODE

Status: OBSERVED / CANDIDATE INTEGRATION
Verification: NOT YET INTEGRATED INTO WANGA

### 2. Governed AI Architecture

Repository: war851/AI-Governance-Architecture
URL: https://github.com/war851/AI-Governance-Architecture

Observed public architecture:
- database-owned process;
- explicit ordered steps;
- runtime skills/configuration;
- constrained LLM calls;
- persistent audit history;
- provider/model agnosticism;
- pre/post orchestration gates.

WANGA placement:

LINEAGE KNOWLEDGE
  -> GOVERNANCE-BY-DESIGN LINEAGE
  -> POLITEIA
  -> VITRUVIUS ORCHESTRATION
  -> EVIDENCE / PROVENANCE

Candidate reusable properties:
- explicit process ownership;
- configuration as governance;
- reconstructable execution history;
- model-provider independence.

Candidate descendant:
CONFIGURATION-GOVERNED TRANSLATION RUNTIME

Status: OBSERVED / CANDIDATE INTEGRATION
Verification: NOT YET INTEGRATED INTO WANGA

License note:
Review the repository's stated licensing terms before any commercial reuse.

### 3. Neuro-Symbolic Runtime Verification

Repository:
atharvay774/Safe-Orbit-AI-Neuro-Symbolic-Runtime-Verification-for-Autonomous-Spacecraft-Navigation
URL: https://github.com/atharvay774/Safe-Orbit-AI-Neuro-Symbolic-Runtime-Verification-for-Autonomous-Spacecraft-Navigation

Observed public architecture:
- neural/RL proposal;
- symbolic runtime verification;
- pre-execution validation;
- verifier-controlled execution boundary.

WANGA placement:

NEURAL LINEAGE
  +
SYMBOLIC VERIFICATION LINEAGE
  -> TRANSLATION ARCHITECTURE
  -> DRIFT / VERIFICATION

Candidate reusable property:
- independent verification gate between proposed computation and execution.

Candidate descendant:
TRANSLATION-TIME VERIFICATION GATE

Status: OBSERVED / CANDIDATE INTEGRATION
Verification: NOT YET INTEGRATED INTO WANGA

### 4. Neuro-Symbolic Transformers / Neural CEGIS

Repository: poolanithinreddy/Neurosymbolic-Transformers
URL: https://github.com/poolanithinreddy/Neurosymbolic-Transformers

Observed public architecture:
- neural learner;
- symbolic constraint verifier;
- counterexample-guided training;
- adaptive constraint weighting;
- evidence-conditioned constraint gating;
- reusable verification API.

WANGA placement:

NEURAL LINEAGE
  +
FORMAL LOGIC LINEAGE
  +
COUNTEREXAMPLE / VERIFICATION LINEAGE
  -> RATIONAL LOGIC INTERFACE
  -> TRANSLATION
  -> VERIFICATION

Candidate reusable properties:
- verifier-generated counterexamples;
- verification-feedback loop;
- constraint diagnostics;
- explicit separation between learned computation and symbolic checking.

Candidate descendant:
COUNTEREXAMPLE-GUIDED TRANSLATION VERIFIER

Status: OBSERVED / CANDIDATE INTEGRATION
Verification: NOT YET INTEGRATED INTO WANGA

### 5. AI Governance Digital Twin

Repository: luccamasini-AI/ai-governance-digital-twin
URL: https://github.com/luccamasini-AI/ai-governance-digital-twin

Observed public architecture:
- digital-twin representation;
- data lineage / traceability;
- explainability-oriented state presentation;
- dynamic baselines;
- governance-oriented monitoring.

WANGA placement:

DIGITAL-TWIN LINEAGE
  -> VITRUVIUS
  -> STATE REPRESENTATION
  -> EVIDENCE / PROVENANCE
  -> DRIFT FORENSICS

Candidate reusable properties:
- state representation;
- lineage visibility;
- baseline comparison;
- governance-oriented observability.

Candidate descendant:
ARCHITECTURAL STATE TWIN

Status: OBSERVED / CANDIDATE INTEGRATION
Verification: NOT YET INTEGRATED INTO WANGA

## Family-tree synthesis

The candidate combinations are represented as architectural marriages rather than repository mergers:

NEURAL
  + SYMBOLIC VERIFICATION
  -> NEURO-SYMBOLIC VERIFICATION

NEURO-SYMBOLIC VERIFICATION
  + GOVERNANCE
  -> GOVERNED NEURO-SYMBOLIC SYSTEM

GOVERNED NEURO-SYMBOLIC SYSTEM
  + PROVENANCE
  -> AUDITABLE NEURO-GOVERNANCE

AUDITABLE NEURO-GOVERNANCE
  + VITRUVIUS
  -> ARCHITECTURALLY MEASURABLE NEURO-GOVERNANCE

ARCHITECTURALLY MEASURABLE NEURO-GOVERNANCE
  + POLITEIA
  -> GOVERNED COMPOSABLE ARCHITECTURE

GOVERNED COMPOSABLE ARCHITECTURE
  + DEPTH TRANSLATION
  -> COMMON DEPTH ARCHITECTURAL NETWORK

## Boundary conditions

This registry does not claim that any external project has adopted WANGA concepts.

It does not claim that WANGA has integrated external code.

It does not grant commercial, patent, copyright, or license rights.

It is a research map for identifying architectural compatibility and future collaboration opportunities.

## Next research actions

1. Fetch and classify each project's architecture documentation.
2. Extract interfaces rather than implementation details.
3. Record licenses and reuse constraints.
4. Build adapter specifications in WANGA.
5. Create isolated proof-of-concept integrations.
6. Run tests and verification.
7. Record measured results in the lineage tree.
8. Only then promote a candidate property from OBSERVED to INTEGRATED.

## Relationship to protected IP

Rational Logic remains a protected architectural component.

External research may inform interfaces, verification mechanisms, governance patterns, or adapter designs, but does not disclose or reproduce the protected Rational Logic implementation.

## Current evidence state

All entries in this document are:
- OBSERVED from public repository material;
- CANDIDATE INTEGRATION;
- NOT YET INTEGRATED;
- NOT YET VERIFIED as WANGA components.

This distinction is mandatory.
