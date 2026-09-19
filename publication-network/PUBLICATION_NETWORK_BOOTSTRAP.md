# PUBLICATION NETWORK BOOTSTRAP

Status: SPECIFIED / INITIAL IMPLEMENTATION

## Objective

Create a controlled multi-surface publication network from the WANGA-LAB research source of truth.

GitHub remains authoritative for research records, protocols, evidence, provenance, schemas and source revisions. Public publishing surfaces are dissemination layers.

## Initial surfaces

| Surface | Role | Source |
|---|---|---|
| GitHub / WANGA-LAB | technical research + canonical records | authoritative |
| Wix | public research publication | controlled publication target |
| WordPress.com | long-form research journal | downstream |
| Webflow | institutional research portal | downstream |
| Vercel | research applications / interactive publication | downstream |
| Lovable | interactive research experiences | downstream |

## Publication identity

Every article or research release should carry:

- publication_id
- source revision / commit
- evidence status
- content hash
- research domain
- canonical GitHub source
- publication surface
- verification state

## Content rule

The 3,000-article target is a corpus plan, not a claim that 3,000 articles already exist. Articles must be distinct, sourced, versioned and quality-gated. Public surfaces must not be used to manufacture duplicate copies of the same article.

## Status model

BUILT
SPECIFIED
PROTOTYPED
TESTED
VERIFIED
PLANNED
HYPOTHETICAL

No item is reported as live or verified until the relevant deployment/test evidence exists.

## First implementation

1. Keep GitHub as source of truth.
2. Use the existing Wix publication queue and daily digest.
3. Establish a common publication manifest for downstream surfaces.
4. Generate the first article set from existing repository research assets.
5. Publish only after quality review.
6. Add cross-links from every public article to its canonical research record.

## Safety / integrity

No credentials are committed to the repository. No site integration is treated as complete without actual connection/deployment evidence. No scientific claim is upgraded from hypothesis to verified merely by publication.
