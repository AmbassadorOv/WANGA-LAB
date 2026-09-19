# WordPress Research Fleet Architecture

Status: SPECIFIED
Date: 2026-09-19

## Purpose

Define a scalable WordPress publication fleet for research agents, scientists, journals, methodology, evidence, datasets, and technical publications.

## Source of Truth

GitHub/WANGA-LAB remains the canonical research and provenance layer. WordPress is a publication and collaboration surface.

## Fleet Model

The target is a scalable fleet, potentially up to 2,000 sites, but sites are created only when a defined research role, ownership boundary, content scope, and publication pipeline exist.

Initial architecture families:

1. Research Domain Hubs
2. Research Group Journals
3. Agent Publication Hubs
4. Scientist / Lab Portals
5. Methodology Journals
6. Technical Notes
7. Evidence and Dataset Portals
8. Case Study Archives
9. Research Release Sites
10. Experimental / Interactive Research Sites

## Site Identity

Every site MUST have:

- site_id
- research_domain
- research_group
- canonical_github_repository
- canonical_path or record IDs
- publication policy
- responsible agent/group
- verification policy
- status

## Publication State

DRAFT -> QUALITY_REVIEW -> APPROVED -> PUBLISHED

Rejected material remains traceable and is not silently deleted from the research record.

## Content Provenance

Each substantive publication should retain:

- publication_id
- source_commit
- generated_at
- evidence_status
- content_hash
- canonical_source
- publication_surface
- verification_state

## Temporary Domain Strategy

GitHub Pages may serve as a temporary public research surface when enabled for a repository. A project-page URL can follow the GitHub Pages convention:

https://<github-account>.github.io/<repository>/

This is NOT a WordPress site and must not be represented as one. It can function as a temporary canonical/public landing surface while an actual WordPress site is connected.

## WordPress Connection Boundary

The WordPress connector currently has no connected site. An actual WordPress site URL is required before WP Agent/WPWriter can connect and modify it.

No password should be requested or stored in chat.

## Scaling Rule

Do not create empty or duplicate sites merely to reach a numeric target. Scale the fleet when research domains, agents, scientists, publication volume, or institutional boundaries justify another site.

## First Build

Once the first WordPress URL is connected, use it as the Master Research Site and implement the common information architecture before expanding the fleet.
