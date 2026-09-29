# Lesson 7 — Random Variable dan Probability

## Problem, context, why

Sensor membaca nilai berbeda meski keadaan hampir sama. Kita tidak dapat menjamin satu outcome; kita perlu model kemungkinan outcomes.

## Intuisi visual dan mental model

Experiment menghasilkan outcome; random variable memetakan outcome ke angka; probability distribution memberi bobot kemungkinan.

```text
physical/random experiment → outcome → X(outcome) → distribution
coin toss               → H/T    → X=1/0
```

## Definition

Sample space berisi outcomes. Event adalah subset. Probability memenuhi 0–1 dan total sample space 1. Random variable adalah function outcome→number; discrete memiliki probability mass, continuous memakai density dan probability pada interval.

## Small manual calculation

Dua toss fair: outcomes HH, HT, TH, TT masing-masing 1/4. X=jumlah heads memiliki P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4.

## Python experiment

```python
import random

rng = random.Random(42)
heads = 0
for _ in range(1_000):
    heads += rng.choice([0, 1])
print(heads / 1_000)
```

### Predict/run/observe/explain

Prediksi apakah hasil tepat 0.5. Ubah sample size dan seed; bedakan probability model dari observed frequency.

## Workplace application

Noise models, reliability, forecasts, A/B experiments, anomaly thresholds, dan uncertainty. Probability adalah model conditional pada assumptions, bukan kepastian.

## Common failure dan debugging

Menyamakan probability dengan frequency kecil-sample, density dengan probability, independence tanpa evidence, dan seed sebagai bukti generality. Tulis sample space dan assumptions.

## Mini exercise/checkpoint

Bangun distribution jumlah alarm dari dua independent binary sensors; lalu jelaskan apa yang rusak jika sensors correlated.

## Penutup

**KAMU BARU BELAJAR:** random variable memetakan outcomes; distribution menyatakan probability.

**KENAPA INI PENTING:** uncertainty tidak boleh disembunyikan oleh satu angka.

**DI DUNIA KERJA DIPAKAI UNTUK:** noise, risk, forecasts, experiments, reliability.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** informasi baru mengubah probability; conditional probability dan Bayes menjelaskannya.
