# Python Professional — Lab Index

Kerjakan 13 panduan pada [chapter map](../README.md) secara berurutan. Semua mengikuti [Standar Praktikum Phase 1](../../PRAKTIKUM_STANDARD.md). `patterns_lab.py` adalah executable synthesis untuk dataclass, generator, context manager, dan async; ia bukan pengganti lab per topik.

## Predict

Sebelum run, baca `patterns_lab.py` dan prediksi:

1. kapan generator mulai mem-parsing;
2. apakah context manager mencatat cleanup saat failure;
3. urutan dan total waktu dua async jobs;
4. exception untuk Reading invalid.

## Run

```bash
python 01_FOUNDATION/03_python_professional/04_LABS/patterns_lab.py
python -m unittest 01_FOUNDATION/03_python_professional/04_LABS/test_patterns_lab.py -v
```

## Observe dan explain

Hubungkan setiap output dengan dataclass invariant, lazy generator, context manager lifecycle, serta async scheduling. Ubah satu variable per experiment.

## Challenge synthesis

Tambahkan config dataclass dan logger pada entrypoint. Tambah satu test sebelum implementation. Jangan menambahkan dependency baru.
