# Interaction Drift Metrics

The institute uses separate metrics for detection, persistence, and correction. No single score is treated as a universal Drift score.

## Core measures

- `D_m`: measured behavioral/representational displacement from a declared baseline.
- `F_a`: frame-adoption rate across controlled probes.
- `P_s`: persistence after the triggering interaction is removed.
- `R_r`: residual signal after Human-Trait Peeling.
- `T_o`: time/turn index at first detectable deviation.
- `T_r`: recovery time after correction or neutralization.
- `C_x`: cross-run replication consistency.
- `U_c`: uncertainty/confidence attached to the measurement.

## Interaction-specific decomposition

`D_total = D_context + D_role + D_persona + D_memory + D_style + D_epistemic`

The terms are measured independently where possible. They must not be summed unless their scales have been normalized and the aggregation rule has been pre-registered.

## Detection rule

A candidate drift event requires a declared baseline and a measurable change. A single surprising answer is insufficient to establish persistent drift.

## Correction rule

A correction is successful only if the target signal decreases while unrelated capability and task performance remain within the predefined tolerance band.
