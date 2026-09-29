# Mini-Project — Sensor Uncertainty Report

## Problem

Dua sensors mengukur quantity sama tetapi memiliki noise, missing readings, dan kemungkinan bias berbeda. Buat report yang membandingkan data dan menyatakan apa yang dapat/tidak dapat disimpulkan.

## Milestones

1. Definisikan quantity, unit, event order, dan target population/time window.
2. Visualisasikan raw values dan missingness secara sederhana.
3. Hitung per-sensor mean, variance/std, median, dan count.
4. Hitung differences/pairs hanya saat timestamps sesuai.
5. Estimasikan bias/noise assumptions dan weighted combination sederhana.
6. Gunakan sampling simulation/bootstrap atau justified interval.
7. Uji one hypothesis yang ditetapkan sebelum melihat semua results.
8. Analisis correlation tanpa causal overclaim.
9. Lakukan sensitivity terhadap outlier/missing/dependence.
10. Tulis findings, uncertainty, assumptions, limitations, dan next evidence.

## Acceptance criteria

Manual calculation kecil cocok dengan Python; units/shapes jelas; no future leakage; effective independent unit dijelaskan; point estimate disertai uncertainty; correlation tidak disebut causation; report reproducible.
