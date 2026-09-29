# Lesson 5 — Gradient dan Chain Rule

## Problem, context, why

Loss bergantung pada banyak parameters dan nested computations. Kita perlu direction perubahan terbesar dan cara mengalirkan sensitivity melalui composition.

## Intuisi visual dan mental model

Gradient adalah kompas pada permukaan: menunjuk uphill tercepat; negative gradient downhill lokal. Chain rule mengalikan sensitivities sepanjang jalur computation.

```text
x → z = 2x → y = z²
dy/dx = (dy/dz) × (dz/dx)
```

## Definition

Untuk scalar function banyak variables, gradient `∇f=[∂f/∂x₁,...]`. Chain rule untuk composition `f(g(x))`: derivative outer pada inner output dikali derivative inner. Shape derivative/Jacobian harus konsisten pada systems besar.

## Small manual calculation

`y=(2x)²`. Pada x=3: z=6, dy/dz=12, dz/dx=2, sehingga dy/dx=24. Direct derivative `4x²→8x=24`.

## Python experiment

Hitung finite differences partial untuk `f(x,y)=x²+3y²` pada (2,1), bandingkan gradient analytic [4,6]. Ubah satu coordinate per experiment.

### Predict/run/observe/explain

Prediksi arah yang menaikkan f paling cepat. Coba langkah kecil searah dan berlawanan gradient.

## Workplace application

Backpropagation, calibration, sensitivity, uncertainty propagation lokal, dan optimization.

## Common failure dan debugging

Sign salah, derivative outer dievaluasi di titik salah, shape mismatch, gradient exploding/vanishing, dan nondifferentiable point. Trace computation graph values dan local derivatives.

## Mini exercise/checkpoint

Turunkan `loss=(wx-y)²` terhadap w secara manual dan verifikasi finite difference.

## Penutup

**KAMU BARU BELAJAR:** gradient mengumpulkan partial derivatives; chain rule mengalirkan sensitivity.

**KENAPA INI PENTING:** model terdiri dari composition banyak operations.

**DI DUNIA KERJA DIPAKAI UNTUK:** backprop, calibration, optimization, sensitivity.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** gradient memberi direction; gradient descent memilih step untuk menurunkan objective.
