# Lesson 9 — Expectation dan Variance

## Problem, context, why

Dua strategies memiliki expected cost sama tetapi risk berbeda. Mean saja tidak menjelaskan spread outcomes.

## Intuisi visual dan mental model

Expectation adalah center of mass distribution; variance adalah average squared distance dari center. Squaring mencegah deviations positif/negatif saling hapus.

## Definition

Discrete expectation `E[X]=ΣxP(X=x)`. Variance `Var(X)=E[(X-μ)²]=E[X²]-μ²`. Standard deviation kembali pada unit X. Expected value bukan outcome yang harus terjadi.

## Small manual calculation

X bernilai 0 dengan probability 0.5 dan 10 dengan 0.5: E[X]=5. Deviations -5,+5; variance=25; std=5. Strategy konstan 5 juga mean 5 tetapi variance 0.

## Python experiment

```python
values = [0, 10]
probabilities = [0.5, 0.5]
mean = sum(x * p for x, p in zip(values, probabilities))
variance = sum((x - mean) ** 2 * p for x, p in zip(values, probabilities))
print(mean, variance)
```

### Predict/run/observe/explain

Bandingkan distributions [0,10] dan [4,6]. Visualisasikan deviations pada number line.

## Workplace application

Expected cost, forecast uncertainty, sensor noise, portfolio/risk, simulation outputs, and service latency. Variance assumes squared-distance is meaningful and is sensitive to extremes.

## Common failure dan debugging

Confusing variance/std units, population vs sample denominator, interpreting mean as typical for skewed data, and ignoring tails. Plot/quantiles accompany summaries.

## Mini exercise/checkpoint

Pilih antara two maintenance policies dengan same mean cost but different variance under risk constraints; explain stakeholder trade-off.

## Penutup

**KAMU BARU BELAJAR:** expectation merangkum center; variance/std merangkum squared spread.

**KENAPA INI PENTING:** keputusan memerlukan outcome dan uncertainty.

**DI DUNIA KERJA DIPAKAI UNTUK:** risk, noise, latency, forecast, simulation.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** statistics memakai sample untuk memperkirakan population mean/variance.
