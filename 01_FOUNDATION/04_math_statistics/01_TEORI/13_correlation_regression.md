# Lesson 13 — Correlation dan Regression Interpretation

## Problem, context, why

Temperature and failure correlate. Can we say temperature causes failure? Not without ruling out operating load, age, selection, and time trends.

## Intuisi visual dan mental model

Correlation describes co-movement; regression fits conditional relationship under model assumptions. A third variable can move both.

```text
load ──→ temperature
  └────→ failure

temperature ↔ failure correlation
does not alone identify causal arrow
```

## Definition

Pearson correlation standardizes covariance and captures linear association, ranges -1..1. Linear regression models expected response `E[Y|X]=β₀+β₁X` under assumptions for estimation/inference. Slope units are Y per X; intercept may be meaningless outside observed range.

## Small manual calculation

For points (1,2),(2,4),(3,6), line y=2x fits perfectly. Add one outlier (10,-10): correlation/slope change strongly, showing sensitivity.

## Python experiment

Use lab to compute mean/covariance/correlation manually for small points, then inspect ASCII scatter pairs. Compare linear relation, nonlinear U-shape, and one outlier.

### Predict/run/observe/explain

Predict correlation for U-shape centered at zero. Low linear correlation does not mean no relationship.

## Workplace application

EDA, calibration, trend analysis, feature/model interpretation, and experiments. Prediction relation may be useful without causal claim, but intervention decisions need stronger design.

## Common failure dan debugging

Correlation→causation, extrapolation, omitted variables, time trend spurious correlation, repeated units treated independent, and regression coefficient interpreted outside model. Plot data/residuals and state population/assumptions.

## Mini exercise/checkpoint

Create two causal diagrams that can yield same observed correlation and propose data/experiment that distinguishes them.

## Penutup

**KAMU BARU BELAJAR:** correlation measures association; regression estimates conditional relation under assumptions.

**KENAPA INI PENTING:** relationship summaries can mislead operational decisions.

**DI DUNIA KERJA DIPAKAI UNTUK:** EDA, calibration, forecasting baselines, and experiment analysis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Phase 2 applies these foundations to SQL/data quality, data mining, and ML evaluation.
