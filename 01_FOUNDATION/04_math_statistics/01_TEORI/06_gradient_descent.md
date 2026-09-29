# Lesson 6 — Gradient Descent

## Problem, context, why

Kita tahu slope loss, tetapi bagaimana memilih parameter yang menurunkannya secara iteratif?

## Intuisi visual dan mental model

Seperti turun bukit berkabut: lihat kemiringan lokal, ambil langkah berlawanan gradient, ukur lagi. Langkah terlalu besar melewati lembah; terlalu kecil lambat.

```text
θₜ₊₁ = θₜ - learning_rate × gradient(θₜ)
```

## Definition

Gradient descent adalah iterative first-order optimization. Convergence bergantung objective, initialization, learning rate, scaling, noise, dan stopping rule. Pada nonconvex objective, hasil dapat local/saddle dan tidak menjamin global optimum.

## Small manual calculation

Minimalkan `f(w)=(w-3)²` dari w=0, learning rate 0.25. Gradient `2(w-3)`:

- step 0: gradient -6, w=1.5;
- step 1: gradient -3, w=2.25;
- bergerak mendekati 3.

## Python experiment

```python
w = 0.0
rate = 0.25
for step in range(6):
    gradient = 2 * (w - 3)
    loss = (w - 3) ** 2
    print(step, w, loss, gradient)
    w -= rate * gradient
```

### Predict/run/observe/explain

Uji rate 0.01, 0.25, 1.0, dan 1.1. Visualisasikan table/ASCII loss trend dan jelaskan convergence/oscillation/divergence.

## Workplace application

Training models, parameter fitting, calibration, dan control optimization. Baseline/solver lain mungkin lebih tepat; jangan memakai gradient descent karena populer saja.

## Common failure dan debugging

Wrong sign, gradient tidak direset, scaling buruk, rate terlalu besar/kecil, leakage objective, dan stopping hanya fixed iterations. Log loss/gradient norm/parameters dan compare analytic vs numeric gradient.

## Mini exercise/checkpoint

Tambahkan early stopping berdasarkan perubahan loss; jelaskan tolerance dan risiko berhenti pada plateau.

## Penutup

**KAMU BARU BELAJAR:** gradient descent memperbarui parameter berlawanan gradient dengan step size.

**KENAPA INI PENTING:** optimization menghubungkan model dan data.

**DI DUNIA KERJA DIPAKAI UNTUK:** training, fitting, calibration, dan decision optimization.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** data/noise membuat outcome tidak pasti; probability memberi bahasa uncertainty.
