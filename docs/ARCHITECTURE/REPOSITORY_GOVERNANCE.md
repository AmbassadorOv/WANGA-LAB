# WANGA-LAB Repository Governance

## Architectural intent

GitHub is treated as a research and evidence system, not as a pile of unrelated software projects.

The repository estate is therefore organized by **architectural role** rather than by chronology or programming language.

## Repository arcs

1. **CORE** — authoritative architecture and public identity.
2. **RESEARCH** — scientific hypotheses, formal systems and research artifacts.
3. **AI_INFRA** — execution, orchestration and reusable infrastructure.
4. **SOURCE_UPSTREAM** — external/upstream-derived code. These remain technically useful but are not presented as original research.
5. **GOVERNANCE_AND_INSTITUTIONAL** — governance, institutional and historical architecture.
6. **LEGACY_OR_EXPERIMENTAL** — older, ambiguous or experimental repositories retained for evidence and later reconstruction.

## Operating rule

**Inventory → Classify → Preserve → Connect → Verify → Publish**

No automation is allowed to delete, overwrite, rename, archive or merge a repository merely because its current name looks obsolete.

Historical repositories are evidence. Their architectural role may change after inspection, but their history should remain recoverable.

## Architect / engineering boundary

The architect defines:

- system boundaries
- research domains
- relationships between repositories
- evidence states
- publication surfaces
- verification requirements

Engineering automation handles:

- repeatable inventory
- validation
- consistency checks
- manifests
- reports
- bounded repository changes

The automation must not silently replace architectural decisions with local code-level optimization.

## Required repository metadata

Every managed repository should eventually have:

- clear README
- declared role
- evidence status
- upstream/original status
- relationship to the WANGA architecture
- owner/authority
- publication status
- verification status

## Evidence states

**BUILT · SPECIFIED · PROTOTYPED · TESTED · VERIFIED · PLANNED · HYPOTHETICAL**

These states describe artifacts, not people.

## Safety boundary

This system is intentionally non-destructive. A later migration phase can propose moves, merges, renames or archival actions, but those actions require an explicit architectural decision after repository contents and history have been inspected.
