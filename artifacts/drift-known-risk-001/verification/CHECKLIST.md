# Verification Checklist — drift-known-risk-001

## Required gates

- [ ] Evidence manifest frozen
- [ ] Input artifacts hashed
- [ ] Baseline identified
- [ ] Replay inputs preserved
- [ ] Replay executed
- [ ] Outputs normalized
- [ ] Observed deviation documented
- [ ] Causal/dependency analysis documented
- [ ] Integrity checks passed
- [ ] Replay result independently rechecked
- [ ] External timestamp proof checked, if required
- [ ] External anchor proof checked, if required
- [ ] Final status assigned

## Status rule

A failed or missing verification step blocks VERIFIED status.

VERIFIED means the defined evidence and replay gates passed; it does not mean legal, regulatory, underwriting, or commercial claims have automatically been established.
