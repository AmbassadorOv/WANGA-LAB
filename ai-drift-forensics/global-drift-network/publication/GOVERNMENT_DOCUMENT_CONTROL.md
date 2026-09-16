# Government Document Control Standard

## Purpose

This standard defines the document-control layer for Global Drift Network government-facing white papers, technical reports, evidence packages, and policy briefs.

It is designed for interoperability with established public-sector AI risk-management practices. It is an implementation profile, not a claim of certification or legal compliance.

## 1. Document identity

Every controlled publication MUST have:

- `document_id`
- `title`
- `document_type`
- `version`
- `status`
- `classification`
- `owner`
- `authoring_unit`
- `issue_date`
- `review_date`
- `supersedes`
- `language`
- `jurisdiction`
- `evidence_package_id`

## 2. Controlled status

Allowed statuses:

- `DRAFT`
- `INTERNAL_REVIEW`
- `TECHNICAL_REVIEW`
- `EVIDENCE_REVIEW`
- `POLICY_REVIEW`
- `APPROVED_FOR_RELEASE`
- `PUBLISHED`
- `SUPERSEDED`
- `WITHDRAWN`

A document MUST NOT be labelled `PUBLISHED` without passing the evidence and quality gates.

## 3. Versioning

Use semantic document versions: `MAJOR.MINOR.PATCH`.

- MAJOR: substantive change to findings, scope, methodology, or conclusions.
- MINOR: new evidence, analysis, section, or material clarification without changing the document's core identity.
- PATCH: editorial, formatting, typographical, or metadata correction.

Every released version MUST retain a change log.

## 4. Review independence

Technical review, evidence review, and policy review SHOULD be separately identifiable even when performed by the same organization.

The evidence register MUST distinguish collection from interpretation.

## 5. Traceability

Each material claim SHOULD resolve through:

`Document → Section → Claim ID → Evidence ID → Observation/Source → Run ID → Snapshot ID → Method Version`

Broken traceability is a review finding and may block release.

## 6. Classification

The publication layer MUST support a jurisdiction-specific classification field without assuming a particular national security classification scheme.

Default values:

- `PUBLIC`
- `OFFICIAL`
- `RESTRICTED`
- `CONFIDENTIAL`
- `NATIONAL_SECURITY_CLASSIFIED`

Use of these labels does not itself establish a legal classification authority.

## 7. Records integrity

Released artifacts SHOULD include:

- content hash
- generation timestamp
- source repository commit
- evidence package identifier
- schema version
- author/reviewer roles
- machine-readable manifest

## 8. International alignment

The profile is designed to map operationally to:

- NIST AI RMF: GOVERN, MAP, MEASURE, MANAGE.
- ISO/IEC 42001: AI management-system concepts, documented processes, continual improvement, and accountability.
- OECD AI Principles: transparency, robustness/security/safety, accountability, and lifecycle traceability.

This mapping is an interoperability profile and MUST NOT be represented as certification, accreditation, or formal conformity assessment.
