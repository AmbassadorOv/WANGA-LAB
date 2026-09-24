# מילות ההגיון — Orchestrator

## Purpose
This directory is the persistent retrieval layer for the 175-term index of Maimonides' *Milaot HaHigayon*.

## Structure
- 175 numbered term records: `terms/001.md` … `terms/175.md`
- This orchestrator is the routing/index layer.
- The supplied Hebrew list is the current input specification, not an independently verified critical edition.

## Verification rule
The term, gate, and location below are indexed from the supplied document. A quotation must not be marked VERIFIED until checked against the actual source edition (R. Moses ibn Tibbon translation) and its exact textual location.

## Retrieval protocol
1. Identify the requested term.
2. Route to its numbered record.
3. Read its gate/location metadata.
4. If exact wording is required, require source-text verification before asserting it as exact.
5. Preserve relations between terms; do not flatten the index into an undifferentiated glossary.

## Status vocabulary
- INDEXED: term and supplied location registered.
- SOURCE-CHECKED: exact source wording checked.
- RELATION-CHECKED: relations to adjacent terms checked.
- VERIFIED: evidence supports the stated source record.

## Count
175 term records are expected.