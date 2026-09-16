# DAILY SCIENCE PUBLICATION PIPELINE

## Purpose

Create a controlled publication bridge from the GitHub research record to the public Wix research site.

The public layer is a dissemination surface, not the authoritative research record. GitHub remains the source repository for protocols, observations, schemas, raw records, derived analysis, and provenance.

## Daily flow

```text
GITHUB CHANGES
    ↓
CHANGE DETECTION
    ↓
EVIDENCE / FINDING SELECTION
    ↓
SCIENTIFIC DIGEST
    ↓
QUALITY GATES
    ↓
WIX DRAFT
    ↓
PUBLISH
    ↓
PUBLIC DAILY RESEARCH UPDATE
```

## What gets published

Each daily update should contain only material supported by the repository at publication time:

- new observations or validated derived measurements;
- meaningful changes to drift timelines or interaction matrices;
- successful or failed reproductions;
- newly resolved or newly unresolved research questions;
- protocol or schema changes that materially affect interpretation;
- links/references to the underlying GitHub records.

Routine commits, formatting changes, dependency noise, and internal implementation details should not automatically become scientific findings.

## Scientific safeguards

1. Never invent a finding because a commit exists.
2. Never convert temporal association into causal attribution.
3. Keep observed, derived, interpreted, and hypothesized statements separate.
4. Preserve negative/null results where scientifically relevant.
5. Mark synthetic data as synthetic.
6. Include the observation/reporting date and the repository revision used.
7. Every published claim should point back to an identifiable repository record.
8. If the daily evidence is insufficient for a substantive finding, publish a short "No material finding" update rather than fabricate significance.

## Publication modes

### Mode A — Daily digest

One scientist-facing post per day summarizing material changes since the previous publication checkpoint.

### Mode B — Event window

During the 72-hour high-resolution window, publication frequency may increase if the evidence pipeline produces material, reproducible observations. Frequency must not override evidence quality.

### Mode C — Research release

A larger publication when a complete analysis, dataset, protocol revision, or verification package reaches a defined release state.

## Wix integration boundary

The intended integration uses the Wix Blog API to create a draft and publish it. The exact Wix credentials, site context, and author/member identity must be supplied through secure secrets/configuration; they must never be committed to GitHub.

The repository automation should therefore treat Wix as a publication target and keep the research data authoritative in GitHub.

## Audit record

For every publication, retain:

- publication ID;
- UTC publication timestamp;
- Git commit/revision used;
- included file paths or record IDs;
- generated digest hash;
- Wix post/draft ID when available;
- publication status;
- any rejected claims or unresolved publication errors.

A content hash supports integrity checking; it does not by itself prove that the underlying source data is immutable.
