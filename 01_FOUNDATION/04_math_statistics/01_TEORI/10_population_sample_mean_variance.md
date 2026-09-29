# Lesson 10 — Population, Sample, Mean, dan Variance

## Problem, context, why

Kita ingin mengetahui rata-rata lifetime seluruh pumps tetapi hanya mengamati sebagian. Sample summary dapat berbeda dari population truth karena sampling variability dan bias.

## Intuisi visual dan mental model

Population adalah target universe; sample adalah jendela yang dipilih. Jendela besar tetapi miring tetap memberi gambaran bias.

```text
target population ── sampling mechanism ──→ observed sample
parameter (unknown)                       statistic (computed)
```

## Definition

Population parameter seperti μ/σ² adalah property target. Sample statistic seperti x̄/s² dihitung dari data. Sample mean `x̄=Σxᵢ/n`. Unbiased sample variance umum memakai denominator n-1 karena mean diestimasi dari sample.

## Small manual calculation

Sample [2,4,6]: mean 4; squared deviations 4,0,4. Population-style variance 8/3; sample variance 8/2=4. Denominator bergantung estimand, bukan pilihan kosmetik.

## Python experiment

```python
import statistics

sample = [2, 4, 6]
print(statistics.mean(sample))
print(statistics.pvariance(sample))
print(statistics.variance(sample))
```

### Predict/run/observe/explain

Prediksi outputs dan behavior sample size 1. Jelaskan parameter vs statistic.

## Workplace application

Quality samples, telemetry subsets, benchmark assets, and user cohorts. Sampling mechanism determines external validity.

## Common failure dan debugging

Convenience sample treated representative, survivor bias, duplicated units, wrong grain, and denominator confusion. Define target population, unit, frame, inclusion, missingness.

## Mini exercise/checkpoint

Audit a sample of inspected machines when only suspicious machines are inspected. What can and cannot be estimated?

## Penutup

**KAMU BARU BELAJAR:** sample statistics estimate population parameters through a sampling mechanism.

**KENAPA INI PENTING:** more rows do not fix biased selection.

**DI DUNIA KERJA DIPAKAI UNTUK:** quality, surveys, experiments, fleet analysis, benchmarks.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** repeated samples create sampling distributions, leading to CLT and confidence intervals.
