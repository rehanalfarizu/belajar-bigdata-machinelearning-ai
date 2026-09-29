# Math & Statistics — Lab Index

Kerjakan 11 panduan pada [chapter map](../README.md) secara berurutan. Semua mengikuti [Standar Praktikum Phase 1](../../PRAKTIKUM_STANDARD.md): intuition → manual calculation → code → visualization → parameter change → interpretation. Script synthesis memakai standard library dan visualisasi ASCII.

## Predict

Sebelum run, prediksi:

- dot product dan norm contoh;
- loss trend learning rates berbeda;
- spread sample means untuk sample size 5 vs 100;
- correlation linear, U-shape, dan outlier.

## Run

```bash
python 01_FOUNDATION/04_math_statistics/04_LABS/foundation_math_lab.py
cd 01_FOUNDATION/04_math_statistics/04_LABS
python -m unittest test_foundation_math_lab.py -v
```

## Observe dan explain

Jangan hanya melihat angka final. Jelaskan representation, unit, assumptions, shape/sample size, source of randomness, dan kondisi saat conclusion gagal.

## Experiment log

Ubah satu variable: learning rate, sample size, seed, outlier magnitude, atau dependence. Catat prediction→result→explanation→next question.
