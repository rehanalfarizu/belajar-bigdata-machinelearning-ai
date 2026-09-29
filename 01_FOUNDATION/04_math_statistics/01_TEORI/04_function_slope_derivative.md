# Lesson 4 — Function, Slope, dan Derivative

## Problem, context, why

Biaya berubah saat parameter model berubah. Kita ingin tahu arah dan kecepatan perubahan lokal: jika parameter dinaikkan sedikit, apakah loss naik atau turun?

## Intuisi visual dan mental model

Function adalah mesin input→output. Slope secant memakai dua titik; derivative adalah batas slope ketika jarak titik mengecil.

```text
y
|       curve
|    • / tangent slope at x
|  •--  secant between two points
+------------ x
```

## Definition

Function `f(x)` memetakan input ke output. Average rate `[f(x+h)-f(x)]/h`. Derivative `f'(x)` adalah limit saat `h→0` bila ada. Derivative lokal bukan perubahan global dan bisa tidak ada di kink/discontinuity.

## Small manual calculation

Untuk `f(x)=x²` pada x=3: dengan h=1 slope=7; h=0.1 slope=6.1; h=0.01 slope=6.01, mendekati derivative `2x=6`.

## Python experiment

```python
def f(x):
    return x * x

for h in [1, 0.1, 0.01, 0.001]:
    slope = (f(3 + h) - f(3)) / h
    print(h, slope)
```

### Predict/run/observe/explain

Prediksi trend dan coba h sangat kecil. Jelaskan approximation error vs floating-point cancellation.

## Workplace application

Sensitivity, optimization, rate of change, numerical simulation, dan model training.

## Common failure dan debugging

Derivative dianggap finite difference exact, h terlalu besar/kecil, units derivative tidak dijelaskan, dan local slope diekstrapolasi jauh. Bandingkan analytic/numeric dan variasikan h.

## Mini exercise/checkpoint

Hitung derivative manual `f(x)=3x+2` dan finite difference; jelaskan unit output per unit input.

## Penutup

**KAMU BARU BELAJAR:** derivative mengukur perubahan lokal sebagai limit slope.

**KENAPA INI PENTING:** optimization dan dynamics membutuhkan sensitivity.

**DI DUNIA KERJA DIPAKAI UNTUK:** training, calibration, simulation, dan sensitivity analysis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** banyak parameters membutuhkan vector derivatives—gradient dan chain rule.
