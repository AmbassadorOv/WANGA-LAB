# Outreach Butterfly Tracker

Adds an outreach-linked observation layer to WANGA-LAB.

## Purpose

For every outbound institutional email, record the send time as **T0** and
observe subsequent documented changes in the recipient and surrounding network.
The engine compares those observations with a declared baseline.

It is an observational research component. A temporal sequence is not treated
as proof of causation.

## Core outputs

- temporal overlap
- action similarity
- counterparty overlap
- asset/domain overlap
- sequence similarity
- baseline deviation
- propagation depth/width
- evidence confidence
- status: NORMAL_OR_UNRELATED, POSSIBLE_PROPAGATION,
  INSUFFICIENT_EVIDENCE, or BUTTERFLY_SIGNAL

## Integration

The tracker is designed to feed the existing Global Drift Network and
International Drift Propagation layers. It does not replace their evidence,
provenance, or verification stages.

Configuration lives in
`ai-drift-forensics/global-drift-network/outreach-butterfly/config.json`.
