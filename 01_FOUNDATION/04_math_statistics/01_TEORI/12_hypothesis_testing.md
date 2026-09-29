# Lesson 12 — Hypothesis Testing

## Problem, context, why

Metric improved 2%. Is that evidence of real difference or plausible sampling noise? A test compares observed statistic with what a null model would often produce.

## Intuisi visual dan mental model

Assume a world where null is true, then ask how extreme our statistic is in that world. A p-value is tail probability under null assumptions—not probability null is true.

## Definition

Specify null/alternative, test statistic, sampling/randomization assumptions, significance plan, and decision context before result. p-value = probability of statistic at least as extreme conditional on null model. Type I/II errors, power, effect size, and confidence interval matter.

## Small manual example

For 10 fair coin tosses, observing 10 heads has two-sided probability based on outcomes at least as extreme. This does not prove coin biased; it quantifies compatibility with fair-coin model.

## Python experiment

Simulate fair coin experiments and count proportion with extreme outcomes. Then change number of tests from 1 to 100 to see false-positive opportunities.

### Predict/run/observe/explain

Predict how multiple uncorrected tests affect chance of at least one small p-value.

## Workplace application

A/B tests, model comparisons, quality changes, and incident metrics. Decisions also need practical effect, cost, safety, and prior evidence.

## Common failure dan debugging

“p<0.05 means hypothesis true”, optional stopping, multiple comparisons, post-hoc primary metric, underpowered negative result, and statistically significant trivial effect. Preserve analysis plan and report all relevant results.

## Mini exercise/checkpoint

Write a test plan for detector delay comparison: unit, split, null, primary metric, effect meaningful, power/uncertainty, and validity threats.

## Penutup

**KAMU BARU BELAJAR:** tests evaluate data compatibility with a null model, not truth probability.

**KENAPA INI PENTING:** random variation can mimic improvement.

**DI DUNIA KERJA DIPAKAI UNTUK:** experiments, quality, model comparison, and research.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** correlation/regression quantify relationships but do not automatically establish causality.
