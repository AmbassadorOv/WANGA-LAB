# Government Evidence Chain

## Purpose

This document defines the operational evidence chain for government-facing AI drift reports and related technical publications. It is an implementation profile for traceability and reproducibility, not a legal certification or conformity-assessment scheme.

## Evidence chain

The authoritative chain is:

`Document -> Section -> Claim ID -> Evidence ID -> Observation/Source -> Run ID -> Snapshot ID -> Method Version`

Each released claim must be traceable through this chain far enough to identify what was measured or sourced, under which controlled run and input snapshot, and with which method version.

## Claim controls

1. Every claim receives a stable `CLM-*` identifier.
2. Claims are classified as `OBSERVED`, `SUPPORTED`, `HYPOTHESIS`, or `REFUTED`.
3. `OBSERVED` and `SUPPORTED` claims require at least one `EVD-*` evidence reference.
4. Verification state is recorded separately from claim classification.
5. Jurisdiction and scope are explicit; a finding must not be generalized beyond its documented population, model, time period, or test conditions.
6. Limitations and unresolved items remain attached to the claim or release package rather than being removed during publication editing.

## Evidence controls

Evidence records use the Government Evidence Register schema. Evidence must identify its source, provenance, run/snapshot context, method version, verification status, and limitations where applicable.

Evidence identifiers are stable within an evidence package. Superseded or disputed evidence is retained as historical state rather than silently replaced.

## Release controls

A publication may move to `APPROVED_FOR_RELEASE` or `PUBLISHED` only when its release manifest records a `PASS` quality-gate decision and contains no unresolved release-blocking items.

The publication layer cannot convert an unsupported claim into an observed finding. Editorial changes must preserve claim identifiers and evidence references or create an explicit versioned change record.

## Reproducibility

A release package should preserve, where applicable:

- source repository commit;
- input snapshot identifier;
- method and schema versions;
- execution/run identifiers;
- evidence identifiers;
- content hash of the released artifact;
- reviewer roles and review timestamps;
- known limitations and unresolved questions.

## Government interoperability profile

The evidence chain is designed to support interoperability with established AI governance and risk-management frameworks, including NIST AI RMF, ISO/IEC 42001 concepts, and OECD AI Principles. Alignment language must remain descriptive: this implementation profile does not claim certification, accreditation, legal compliance, or governmental approval.
