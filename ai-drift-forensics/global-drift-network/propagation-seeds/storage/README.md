# Propagation Seeds — Cumulative Storage

This directory is the cumulative storage layout for the weekend-to-Monday propagation scan.

## Storage layout

- `incoming/` — raw captured observation batches
- `normalized/` — normalized seed records
- `verified/` — evidence-backed observations that passed validation
- `propagation/` — cross-point propagation events
- `persistence/` — persistence, recovery, return and reversal observations
- `snapshots/` — dated Monday/Tuesday network snapshots
- `reports/` — synthesis and closure reports
- `manifests/` — batch manifests, counts and checksums

## Record rule

Every record retains a stable ID and evidence reference. Deduplication is performed before a record enters `verified/`.

## Scale rule

GitHub is the index and versioned research layer, not the intended long-term warehouse for millions of raw records. GitHub recommends keeping repositories manageable and using object storage for programmatically generated large datasets. citehttps://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits

Large binary artifacts should use Git LFS or external object storage rather than ordinary Git history. citehttps://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
