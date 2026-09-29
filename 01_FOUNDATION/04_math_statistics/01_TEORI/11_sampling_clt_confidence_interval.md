# Lesson 11 — Sampling, CLT, dan Confidence Interval

## Problem, context, why

Sample mean 27.4°C bukan population mean exact. Kita need interval/procedure that quantifies sampling uncertainty under assumptions.

## Intuisi visual dan mental model

Take many hypothetical samples: each gives a different mean. Distribution of those means narrows as independent effective sample size grows.

## Definition

Sampling distribution is distribution of a statistic across repeated samples. Under conditions, CLT says standardized sample mean approaches normal as n grows. Standard error of mean approximately `s/√n` for independent observations. A frequentist 95% confidence procedure covers true parameter in 95% repeated studies under assumptions—not 95% probability for a fixed parameter after interval is observed.

## Small manual calculation

If sample mean 100, sample std 20, n=100, SE=2. Approximate 95% interval: 100 ± 1.96×2 = [96.08,103.92]. This ignores finite population/dependence and uses large-sample approximation.

## Python experiment

Simulate repeated samples with a fixed RNG seed, collect means, and draw an ASCII histogram using the lab. Compare n=5 and n=100.

### Predict/run/observe/explain

Predict center and spread. Introduce correlated repeated readings per asset; explain why row count overstates independent information.

## Workplace application

Experiment estimates, service latency means, quality measurements, and model metric uncertainty. Cluster/bootstrap/time dependence may need different methods.

## Common failure dan debugging

CI interpreted as range of individual observations, p-hacking interval after many metrics, independence ignored, and normal approximation in tiny/skewed samples. Inspect unit of analysis and sampling design.

## Mini exercise/checkpoint

Explain why 10,000 readings from one sensor may provide less generalization evidence than 100 readings from 100 independent sensors.

## Penutup

**KAMU BARU BELAJAR:** statistics vary across samples; CLT/SE support interval procedures under assumptions.

**KENAPA INI PENTING:** point estimates hide sampling uncertainty.

**DI DUNIA KERJA DIPAKAI UNTUK:** experiments, quality, benchmarks, and metric reporting.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** hypothesis tests formalize compatibility of data with a null model, but require careful interpretation.
