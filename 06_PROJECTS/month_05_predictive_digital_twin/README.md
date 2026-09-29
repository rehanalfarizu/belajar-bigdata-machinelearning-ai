# Month 5 — Predictive / Prescriptive Digital Twin

## Context

Perluas Connected Twin dengan simulator tervalidasi, anomaly/fault analysis, forecast atau RUL, serta what-if/optimization yang menghasilkan recommendation—bukan command.

## Deliverables

- physics/discrete/hybrid model dengan verification, calibration, validation;
- detector/predictor dengan temporal+asset holdout dan uncertainty;
- scenario runner dan constrained optimizer;
- recommendation object berisi assumptions, alternatives, margin, version, expiry;
- architecture/semantic model dan observability.

## Acceptance criteria

Simulation error dilaporkan per regime; anomaly dinilai dengan delay dan false alarm per asset-time; RUL/forecast calibrated bila diklaim probabilistik; optimizer tidak melanggar hard constraints; infeasibility dan model timeout ditangani.

## Evidence

Sertakan baselines/ablations, operating envelope, sensitivity, capacity model, degraded modes, dan decision comparison rule vs optimization.
