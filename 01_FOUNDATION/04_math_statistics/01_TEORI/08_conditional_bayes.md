# Lesson 8 — Conditional Probability dan Bayes

## Problem, context, why

Alarm test 95% sensitif terdengar sangat meyakinkan. Tetapi jika failure sangat langka, banyak alarm positif tetap false. Base rate matters.

## Intuisi visual dan mental model

Conditional probability mempersempit dunia ke condition tertentu. Bayes membalik arah pertanyaan dari “alarm jika failure?” menjadi “failure jika alarm?”.

## Definition

`P(A|B)=P(A∩B)/P(B)`. Bayes: `P(A|B)=P(B|A)P(A)/P(B)`. Prior adalah belief/base rate sebelum evidence; likelihood adalah probability evidence di bawah hypothesis; posterior setelah update.

## Small manual calculation

Dalam 1.000 assets: 10 failure. Test menangkap 9 (90% sensitivity) dan false-positive 5% dari 990 ≈ 50. Dari ~59 positives, hanya 9 failure: precision sekitar 15%, bukan 90%.

## Python experiment

```python
failures = 10
healthy = 990
true_positive = 9
false_positive = round(0.05 * healthy)
precision = true_positive / (true_positive + false_positive)
print(precision)
```

### Predict/run/observe/explain

Ubah prevalence 1%, 10%, 50%. Visualisasikan counts table, bukan hanya formula. Jelaskan perubahan posterior.

## Workplace application

Diagnostics, alert triage, fraud, quality control, and model thresholding. Costs dan action juga penting; posterior bukan keputusan otomatis.

## Common failure dan debugging

Confusing P(test|failure) with P(failure|test), mengabaikan base rate, double-counting dependent evidence, dan prior arbitrary tanpa sensitivity. Gunakan contingency table.

## Mini exercise/checkpoint

Hitung posterior untuk test negatif dan jelaskan false reassurance risk. Lulus bila dapat membalik conditional dengan Bayes.

## Penutup

**KAMU BARU BELAJAR:** conditional probability bergantung pada condition; Bayes menggabungkan base rate dan evidence.

**KENAPA INI PENTING:** metric test/model tanpa prevalence menyesatkan.

**DI DUNIA KERJA DIPAKAI UNTUK:** alarms, diagnosis, risk, fraud, dan inspection.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** expectation dan variance merangkum center/spread distribution untuk keputusan.
