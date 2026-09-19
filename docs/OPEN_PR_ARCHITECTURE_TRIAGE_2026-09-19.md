# Open PR Architecture Triage — 2026-09-19

This record classifies the repository's PR history by architectural responsibility and records the disposition of the open work reviewed during the 2026-09-19 integration pass.

## Integrated groups

| Group | Responsibility | Source PR | Result |
|---|---|---:|---|
| Repository Governance | operating contract, evidence discipline, hygiene | #13, #12 | MERGED |
| Governance Engine | continuity, governance object, audit kernel | #26 → #37 | CLEAN INTEGRATION MERGED |
| Runtime / NTM | executable runtime and verification | #28 | MERGED |
| Epistemic Reasoning | explicit-state reasoning frontier | #7 | MERGED |
| Governance Standards | candidate drift/governance standard | #11 | MERGED / RESEARCH SPECIFICATION |
| Publication Network | GitHub/Wix/WordPress/publication contracts | #31 | MERGED |
| Research Composition | 172-hour composition map and candidate-discovery topology | #32 | MERGED / RESEARCH STATUS |
| Copernicus Corpus | 100 research drafts | #29 | MERGED / RESEARCH DRAFT |
| Copernicus Publication Layer | source-controlled static publication stack | #30 | MERGED |
| Global Drift Network | observation, events, evidence, queue, regional collection | #9 + #14 → #38 | SECURE CLEAN INTEGRATION MERGED |
| WANGA-X | reversible/dynamic architecture research | #27 → #39 | CLEAN RESEARCH INTEGRATION MERGED |
| Vitruvius | research-driven indexing and work composition | #18 → #40 | CLEAN NON-MUTATING INTEGRATION MERGED |
| Global Work Manager / Model Fabric | work manager, model agents, discovery, work memory, bridge contracts | #15 → #41 | CLEAN CONTRACT INTEGRATION MERGED |
| Insurer Intake | intake, bounded queue, replay, oversight | #36 | MERGED |

## Superseded source PRs

The following PRs remain in GitHub history as source artifacts but are no longer active integration targets:

- #33 — superseded by the separate AmbassadorOv/AmbassadorOv professional profile integration.
- #26 — superseded by clean governance integration #37.
- #19 — superseded by bounded executable runtime #28 and later queue/pipeline work.
- #9 — superseded by secure clean Global Drift Network integration #38.
- #14 — its security fix was incorporated into #38.
- #27 — superseded by clean WANGA-X research integration #39.
- #18 — superseded by non-mutating Vitruvius integration #40.
- #15 — superseded/decomposed into the smaller verified integration #41 plus subsequent controlled automation.
- #3, #5, #6 — retained as historical ARK / experimental source material; not core WANGA-LAB integration targets.

## Evidence rule

Merge state is not evidence of scientific validity.

A merged specification remains a specification until implementation and verification establish otherwise. Synthetic replay verifies pipeline mechanics only; it does not establish a real client incident.

## Current main architecture

WANGA OS → Global Work Manager → Model Fabric / Digital Model Agents → Runtime → Evidence & Provenance → Drift Forensics → Verification → Research / Publication

Specialized children connect through explicit interfaces:

- Global Drift Network
- WANGA-X / Copernicus research
- Vitruvius research indexing
- Insurer Intake / Forensic Case Pipeline
- Governance and candidate standards
- Publication network

## Operational objective

The repository should converge on fewer, clearer integration surfaces:

**one responsibility → one canonical owner → explicit interface → evidence status → verification gate**

Old branches remain preserved unless separately audited for archival deletion.
