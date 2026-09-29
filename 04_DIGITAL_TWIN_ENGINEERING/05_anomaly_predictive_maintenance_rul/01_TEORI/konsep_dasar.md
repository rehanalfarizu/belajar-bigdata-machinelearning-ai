# Chapter 14 — Anomaly, Fault, Predictive Maintenance, dan RUL

Tujuan chapter ini adalah mengubah deviation menjadi keputusan maintenance yang terukur—tanpa menyebut setiap outlier sebagai kerusakan.

## 1. Pisahkan istilah dan label

```text
anomaly → evidence bahwa pola menyimpang
fault   → kondisi internal/komponen tidak memenuhi fungsi tertentu
diagnosis → inferensi jenis/lokasi/penyebab fault
failure → sistem tidak dapat memenuhi fungsi yang disyaratkan
```

Sebuah anomaly bisa berasal dari sensor bias, unit salah, maintenance terjadwal, mode operasi baru, cyberattack, atau fault aset. Fault dapat ada sebelum detector melihat anomaly. Failure bisa mendadak tanpa pola awal yang cukup. Karena itu alarm harus membawa score, threshold/version, context, uncertainty, dan hypotheses—bukan diagnosis palsu.

## 2. Detector dari baseline ke model

- **Rule/range/rate-of-change**: mudah diaudit; kuat bila batas fisik diketahui.
- **Z-score/IQR**: baseline univariat; rentan nonstationarity dan multimodal operation.
- **EWMA/CUSUM/change point**: mendeteksi shift kecil/temporal; perlu trade-off sensitivity-delay.
- **Isolation Forest/LOF/One-Class SVM**: nonlinear multivariate; scaling, contamination, dan operating modes penting.
- **Autoencoder**: reconstruction error; dapat merekonstruksi fault bila training terkontaminasi atau capacity terlalu besar.
- **Forecast/model residual**: membandingkan observation dengan expected behavior; mismatch juga bisa berasal dari model.

Bedakan point anomaly, contextual anomaly, collective/temporal anomaly, dan multivariate relationship anomaly. Temperature 80°C mungkin normal saat high load tetapi aneh saat idle.

[`RunningZScoreDetector`](../../01_digital_twin_fundamentals/src/digital_twin_lab/anomaly.py) memakai Welford online sehingga tidak melihat masa depan. Residual alarm tidak dimasukkan ke baseline untuk mengurangi fault contamination; drift sehat memerlukan recalibration policy terpisah.

## 3. Evaluasi anomaly yang operasional

Accuracy hampir tidak berguna saat anomaly jarang. Ukur:

- event-level precision/recall dan PR curve;
- false alarms per asset-day/operator-shift;
- detection delay dari fault onset;
- missed event dan time-under-undetected-fault;
- alarm duration/chattering dan deduplication;
- performa per mode/asset/site;
- cost/downtime avoided serta investigation burden.

Threshold ditentukan dari biaya false alarm vs missed/delayed detection, bukan angka tiga sigma secara otomatis. Hindari point-level metric yang memberi reward berlebihan pada ratusan alarm dalam satu incident.

## 4. Predictive maintenance pipeline

```text
telemetry + work order + operating context
→ quality/alignment
→ features or learned representation
→ health indicator
→ degradation/fault probability
→ RUL distribution
→ maintenance options + constraints
→ recommendation
→ planner/operator approval
→ outcome feedback
```

Maintenance label sering noisy: tanggal work order bukan selalu onset fault; replaced part belum tentu penyebab; asset sehat belum tentu negative lengkap. Cegah leakage dari fields yang hanya dibuat setelah failure/maintenance.

Split berdasarkan waktu dan asset. Jika window dari asset yang sama masuk train dan test, model dapat menghafal identity/trajectory.

## 5. Remaining Useful Life

RUL pada waktu `t` adalah waktu/cycle tersisa sampai failure criterion tertentu. Tanpa criterion dan future operating profile, RUL ambigu.

Pendekatan:

- **Degradation model**: fit trajectory health indicator menuju threshold; interpretable tetapi threshold/dynamics harus valid.
- **Survival analysis**: model time-to-event dan censoring; memberi survival/hazard, cocok ketika banyak asset belum gagal.
- **Regression RUL**: prediksi scalar dari window feature; perlu asymmetric cost dan temporal/asset split.
- **Sequence model**: RNN/LSTM/Transformer membaca urutan; data-hungry dan tidak otomatis calibrated.
- **Physics/hybrid**: estimasi parameter degradasi lalu propagasi scenario operasi.

Laporkan distribution/interval atau quantile, bukan hanya point estimate. Evaluasi MAE/RMSE bersama calibration/coverage, early-vs-late penalty, performa sepanjang lifecycle, dan stability antar update. RUL yang meloncat dari 50 ke 500 jam tanpa explanation merusak kepercayaan operator.

## 6. Mini project wajib — Predictive Maintenance Twin

Pilih motor/pump/battery. Deliverable:

1. asset/telemetry schema dan simulated/real data provenance;
2. normal operation modes dan fault definition;
3. raw/curated split dengan quality report;
4. physics/rule baseline;
5. health indicator dari vibration/temperature/current atau domain setara;
6. anomaly detector dan event-level evaluation;
7. degradation/RUL baseline dengan temporal+asset holdout;
8. uncertainty dan calibration plot;
9. maintenance recommendation dengan parts/crew/downtime constraints;
10. failure cases, safety limits, dan human approval.

Eksperimen ablation: tanpa operating context, tanpa state estimator, tanpa physics residual, tanpa sensor tertentu. Ablation menjawab komponen mana benar-benar memberi nilai.

## 7. Debugging dan anti-pattern

- Threshold dihitung memakai periode fault/test.
- Window saling overlap di train dan test.
- `NaN` diisi nol lalu dianggap vibration nol.
- Maintenance event mengubah sensor distribution tetapi dianggap fault.
- Model belajar asset age/ID dan gagal pada asset baru.
- RUL di-clip sehingga metric terlihat bagus tanpa melaporkan clipping.
- Alarm threshold dipilih dari test set.
- Recommendation mengganti komponen tanpa inventory/cost/safety constraint.

## Gate

Lulus bila dapat membedakan anomaly–fault–diagnosis–failure, membangun baseline streaming tanpa future leakage, menghitung detection delay/false alarms, membuat RUL dengan censoring/uncertainty awareness, dan menghasilkan rekomendasi yang tetap memerlukan decision workflow.

## Referensi lanjutan

- [NIST — Digital Twin-Based Cyber-Attack Detection Framework](https://www.nist.gov/publications/digital-twin-based-cyber-attack-detection-framework-cyber-physical-manufacturing)
- scikit-learn documentation untuk [novelty and outlier detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- NASA C-MAPSS dapat dipakai sebagai dataset pembelajaran RUL; dokumentasikan bahwa itu benchmark simulasi turbofan, bukan bukti siap pakai lintas domain.

Berikutnya: [Architecture, Semantics & Graph](../../06_architecture_semantics_graph/README.md).
