# Chapter 12 — Time Series dan State Estimation

Sensor memberi **observation**, bukan state sempurna. State estimation menggabungkan model proses, input, observation, serta uncertainty untuk menjawab: “berdasarkan bukti sampai event time ini, kondisi internal terbaik kita apa?”

## 1. Time series sebelum forecasting

Index waktu bukan kolom biasa. Audit:

- timezone dan daylight-saving policy;
- sampling regular/irregular;
- duplicate timestamp dan ordering;
- gaps serta penyebab missing;
- unit/calibration/schema regime;
- operating modes dan maintenance boundaries.

Transformasi penting:

- resampling harus menyatakan aggregation (`mean`, `last`, energy integral, maximum);
- rolling statistic hanya memakai masa lalu pada operational inference;
- lag `x[t-k]` tidak boleh bocor dari masa depan;
- autocorrelation menunjukkan ketergantungan linear pada lag, bukan sebab-akibat;
- trend/seasonality/decomposition membantu membangun baseline;
- stationarity berarti property tertentu stabil terhadap waktu, bukan “data tidak berubah”.

Forecast baseline: naive last value, seasonal naive, moving average, exponential smoothing. ARIMA memberi model linear untuk dependence/differencing; temporal ML memakai lag/calendar/exogenous features; LSTM/Transformer berguna untuk pola tertentu tetapi butuh data/evaluasi lebih besar. Semua harus dikalahkan secara fair oleh baseline.

Validasi gunakan expanding/rolling window. Laporkan horizon-specific error, prediction interval coverage, dan error per operating mode. Concept drift adalah perubahan hubungan input–target; data drift belum tentu menurunkan keputusan.

## 2. State, observation, dan dua model

Model state-space linear:

```text
x_k = F x_(k-1) + B u_k + w_k       process model
z_k = H x_k + v_k                    measurement model
w_k ~ N(0, Q), v_k ~ N(0, R)
```

- `x_k`: state laten;
- `z_k`: measurement;
- `u_k`: input/control yang diketahui;
- `F`: dynamics state;
- `H`: bagaimana state terlihat oleh sensor;
- `Q`: process/model uncertainty;
- `R`: measurement uncertainty.

Noise bukan sekadar gangguan acak yang bisa dihapus. `Q` menyatakan seberapa tidak lengkap model; `R` menyatakan seberapa noisy measurement. Nilainya harus diestimasi/dituning dari data dan divalidasi, bukan dipilih hanya agar plot halus.

## 3. Estimator bertingkat

1. **Last observation**: baseline murah, gagal saat missing/noisy.
2. **Moving/exponential smoother**: mengurangi noise tetapi menambah lag; bukan process model.
3. **Complementary filter**: menggabungkan sensor dengan karakter frequency berbeda.
4. **Fixed-gain observer**: prediction + sebagian innovation; gain tetap.
5. **Kalman Filter (KF)**: gain berasal dari covariance bila linear-Gaussian assumptions cukup.
6. **Extended KF**: linearisasi Jacobian dari nonlinear function; sensitif pada linearization/model.
7. **Unscented KF**: propagasi sigma points; menghindari Jacobian tetapi lebih mahal.
8. **Particle Filter**: distribusi diwakili particles/weights; fleksibel untuk nonlinear/non-Gaussian, rentan degeneracy dan mahal.

“Lebih canggih” bukan otomatis lebih baik. Pilih dari nonlinearity, distribution, dimension, latency, data, dan consequence of error.

## 4. Kalman Filter skalar dari nol

Prediction:

```text
x⁻ = x + u
P⁻ = P + Q
```

Correction:

```text
y = z - x⁻             innovation/residual
S = P⁻ + R             innovation variance
K = P⁻ / S             Kalman gain
x = x⁻ + K y
P = (1 - K) P⁻
```

Jika `R` besar, sensor kurang dipercaya dan `K` kecil. Jika `P⁻` besar, prior tidak pasti dan sensor lebih berpengaruh. Tanpa measurement, lakukan prediction saja sehingga `P` naik oleh `Q`—confidence turun secara eksplisit.

Implementasi: [`estimation.py`](../../01_digital_twin_fundamentals/src/digital_twin_lab/estimation.py). Test membuktikan uncertainty naik saat missing dan turun setelah correction. `fuse_measurements` memasukkan beberapa sensor independen secara sekuensial; sensor ber-variance kecil berpengaruh lebih besar.

Catatan: covariance sensor yang saling berkorelasi tidak boleh diperlakukan independen; informasi yang sama akan dihitung dua kali dan confidence menjadi terlalu tinggi.

## 5. Delay dan out-of-sequence measurement

Jika measurement untuk waktu `k-5` tiba sekarang, update ke state sekarang seolah measurement baru adalah salah. Pilihan:

- buang dari operational estimator tetapi simpan historian;
- buffer sampai lateness bound lalu proses event-time order;
- rewind/replay state dari checkpoint;
- gunakan filter/smoother yang mendukung out-of-sequence measurement.

Smoother memakai observation masa depan untuk memperbaiki state masa lalu; bagus untuk offline analysis, tidak sah sebagai online estimate saat event terjadi. Labeli hasil filtered vs smoothed.

## 6. Uncertainty visualization dan calibration

Plot estimate bersama interval, measurement, ground truth simulator, dan missing periods. Untuk pendekatan Gaussian, `x ± 1.96 sqrt(P)` sering dipakai sebagai interval nominal 95%, tetapi coverage empiris harus diuji; jika assumptions salah, angka 95% dapat tidak calibrated.

Metrik:

- state MAE/RMSE bila ground truth tersedia;
- normalized innovation dan residual whiteness;
- interval coverage dan width;
- uncertainty saat dropout;
- convergence time setelah start/fault;
- latency per update;
- consistency antar operating mode.

## 7. Praktikum

1. Implementasikan fixed-gain observer dan bandingkan gain 0.1/0.5/0.9.
2. Tulis ulang KF skalar tanpa melihat source; jelaskan setiap variance.
3. Simulasikan sensor A (`R=0.01`) dan B (`R=1.0`); uji fusion.
4. Hilangkan sensor 20 langkah; plot `sqrt(P)`.
5. Delay 10% event; bandingkan arrival-order, drop-late, dan replay.
6. Tambah bias sensor; tunjukkan bahwa KF biasa dapat confident tetapi salah. Tambahkan bias sebagai state atau deteksi calibration drift.
7. Forecast 1/5/20 langkah dengan naive dan exponential smoothing; gunakan rolling validation.

## Gate

Lulus bila dapat menurunkan KF skalar, menulis implementation/test, membedakan filter vs smoother, menangani missing/delayed event dengan policy eksplisit, dan memvisualkan uncertainty yang diuji coverage-nya.

## Referensi lanjutan

- Welch & Bishop, *An Introduction to the Kalman Filter*, UNC-Chapel Hill TR 95-041.
- Särkkä & Svensson, *Bayesian Filtering and Smoothing*, Cambridge University Press, 2023.
- [statsmodels Time Series Analysis](https://www.statsmodels.org/stable/tsa.html) untuk implementasi forecasting statistik setelah baseline dari nol dipahami.

Berikutnya: [Simulation, Physics & Hybrid Models](../../04_simulation_physics_hybrid/README.md).
