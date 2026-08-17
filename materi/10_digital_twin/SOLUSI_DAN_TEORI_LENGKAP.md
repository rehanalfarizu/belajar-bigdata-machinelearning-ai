# Teori dan Solusi Lengkap — Level 10 Digital Twin

## 1. Definisi operasional

Digital twin bukan satu produk dan bukan sekadar visualisasi 3D. Definisi operasional yang berguna adalah: model digital beridentitas jelas yang menyimpan state aset, menerima observasi bertimestamp, memprediksi atau mensimulasikan perilaku, dan menghasilkan insight yang dapat diuji terhadap aset. Kualitas twin diukur dari kesesuaian keputusan yang dibantu, bukan realisme gambar.

## 2. Solusi model tangki

Neraca massa mengubah selisih inflow dan outflow menjadi perubahan volume. Jika luas penampang konstan, perubahan tinggi setara perubahan volume dibagi area. Outflow akar tinggi adalah pendekatan sederhana berdasarkan tekanan hidrostatik; pada aset nyata coefficient perlu dikalibrasi.

```python
import numpy as np

def step_plant(level, inflow, coefficient, area, dt):
    outflow = coefficient * np.sqrt(max(level, 0.0))
    next_state = level + dt / area * (inflow - outflow)
    return max(0.0, next_state), outflow

def observe(level, rng, noise_std=0.05, dropout_probability=0.05):
    if rng.random() < dropout_probability:
        return np.nan
    return level + rng.normal(0, noise_std)
```

Plant dan sensor dipisahkan agar bias/noise dapat diuji. Dalam produksi, ground truth sering tidak tersedia; karena itu kalibrasi memakai inspeksi, sensor redundant, atau periode operasi yang diketahui sehat.

## 3. Solusi state estimator

Twin lebih dulu melakukan prediction dari model fisika, lalu melakukan correction bila observasi berkualitas baik. Ini bentuk sederhana observer; Kalman filter memperluas ide tersebut dengan uncertainty covariance dan model noise.

```python
def step_twin(previous_estimate, inflow, coefficient, area, dt, measurement, gain=0.35):
    predicted, _ = step_plant(previous_estimate, inflow, coefficient, area, dt)
    if np.isnan(measurement):
        return predicted, predicted
    estimate = predicted + gain * (measurement - predicted)
    return estimate, predicted
```

Nilai pertama adalah state setelah correction, nilai kedua adalah prediction sebelum melihat sensor. Residual anomaly harus memakai prediction sebelum correction; memakai estimate setelah correction mengecilkan residual dan menyembunyikan fault.

## 4. Solusi simulasi, evaluasi, dan alarm

```python
import pandas as pd

rng = np.random.default_rng(42)
rows, true_level, twin_level = [], 2.0, 2.0
for t in range(500):
    inflow = 1.2 + 0.3 * np.sin(t / 30)
    coefficient = 0.55 if t < 300 else 0.40  # clog sesudah t=300
    true_level, outflow = step_plant(true_level, inflow, coefficient, area=10, dt=1)
    measured = observe(true_level, rng)
    twin_level, predicted = step_twin(twin_level, inflow, 0.55, area=10, dt=1,
                                      measurement=measured, gain=0.35)
    rows.append({"t": t, "true": true_level, "measured": measured,
                 "predicted": predicted, "estimate": twin_level,
                 "residual": measured - predicted})

result = pd.DataFrame(rows)
normal_residual = result.loc[result["t"] < 250, "residual"].dropna()
residual_center = normal_residual.mean()
threshold = 3 * normal_residual.std(ddof=1)
result["alarm"] = (result["residual"] - residual_center).abs() > threshold
mae = (result["estimate"] - result["true"]).abs().mean()
print(f"Twin MAE: {mae:.3f} m")
```

Threshold dua sisi memakai `abs(residual - mean) > 3 * std`, sehingga fault bias positif maupun negatif dapat dideteksi. Tetap uji keduanya; satu threshold yang baik pada simulator belum tentu baik pada sensor nyata.

## 5. Dari simulator ke aset nyata

Ganti `observe()` secara bertahap dengan adapter telemetry yang divalidasi. Simpan raw event, quality result, state version, parameter model, serta rekomendasi. Sebelum autonomous action, lakukan shadow mode: twin memberi rekomendasi tetapi operator yang memutuskan; bandingkan rekomendasi dengan outcome. Tambahkan limit fisik, emergency stop, manual override, access control, dan audit sebelum control loop tertutup.
