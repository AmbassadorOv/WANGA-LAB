# Wix ↔ GitHub Publication Registry

## Technical source of truth
GitHub: https://github.com/AmbassadorOv/WANGA-LAB

## Public publication layer
Wix: https://beywolf5.wixsite.com/global-algorithmic-2

## Current state
- GitHub corpus: CREATED on branch agent/wanga-copernicus/system-100-articles
- Wix site: EXISTING / PUBLIC
- Direct automated GitHub→Wix synchronization: NOT YET CONFIGURED
- Article-by-article publication: NEXT IMPLEMENTATION STEP
- Approved Wix content must preserve the GitHub source text rather than being silently regenerated.

## Synchronization contract
Article ID → title → slug → GitHub path → status → Wix path → publication status → verification timestamp
