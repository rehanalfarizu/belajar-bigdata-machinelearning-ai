# Teori Mendalam — Level 10: Digital Twin

## 1. Twin sebagai estimasi state

Digital twin menyatukan identitas aset, model, telemetry, state, dan keputusan. State adalah kondisi internal yang relevan namun tidak selalu dapat diukur langsung: level, temperatur inti, degradasi, mode operasi, atau remaining useful life. Sensor memberi observation parsial dengan noise, delay, dropout, bias, calibration drift, dan unit yang mungkin salah. Karena itu twin tidak boleh menyamakan satu reading sensor dengan kebenaran aset; ia membuat estimasi berdasarkan model dan observasi berkualitas.

Digital model tidak tersinkron, digital shadow menerima aliran fisik-ke-digital, sedangkan digital twin memiliki feedback digital-ke-fisik yang dikendalikan. Perbedaan ini penting untuk safety: semakin dekat twin pada kontrol fisik, semakin besar tuntutan validasi, authorization, fail-safe, dan human oversight.

## 2. Model fisik, data-driven, dan hybrid

Physics-based model menyatakan conservation law, kinematics, heat transfer, electrical relationship, atau domain equation. Ia dapat diekstrapolasi lebih masuk akal saat data sedikit tetapi membutuhkan parameter/calibration dan mungkin terlalu sederhana. Data-driven model mempelajari pola dari histori; ia fleksibel namun rentan distribution shift dan sulit menjelaskan outside-data behavior. Hybrid model memakai fisika sebagai backbone lalu ML untuk residual/parameter estimation. Pilih model dari keputusan yang dibantu, data, latency, explainability, dan consequence of error.

## 3. State estimation dan uncertainty

Prediction menggunakan state sebelumnya serta input/control. Correction menggabungkan prediction dengan observation. Observer sederhana memakai gain tetap; Kalman filter memodelkan covariance proses/sensor dan memberi gain adaptif bila asumsi linear-Gaussian cukup; particle filter menangani nonlinearity/distribution lain dengan biaya lebih tinggi. Estimator tanpa uncertainty dapat memberi kepastian palsu. Saat sensor stale/dropout, uncertainty harus naik dan action mungkin dibatasi.

## 4. Telemetry dan time

Event telemetry memerlukan asset ID, metric, value, unit, event time, ingest time, sequence/quality, schema version, dan provenance. Event time menyatakan kapan fenomena terjadi; processing time kapan sistem memprosesnya. Delay/out-of-order event membuat rolling feature, alarm, dan simulator salah bila tidak ditangani. Raw event immutable mendukung audit/replay; curated event memenuhi contract; twin state store memberi snapshot cepat.

## 5. Diagnosis, simulation, dan control

Residual antara observation dan model prediction menunjukkan mismatch, bukan akar penyebab tunggal. Fault isolation perlu sensor lain, mode operasi, maintenance log, dan hypothesis test. What-if menjalankan skenario pada twin untuk menilai trade-off tanpa menyentuh aset. Control loop tertutup membutuhkan safety envelope, hard constraint, command allowlist, rate limit, manual override, emergency stop, authentication, audit, dan proses engineering domain. Model ML tidak boleh langsung menjadi actuator tanpa guardrail.

## 6. Fleet, lifecycle, dan governance

Fleet twin membandingkan banyak aset untuk benchmark, predictive maintenance, dan parameter transfer, tetapi aset dapat berbeda umur/konfigurasi/lingkungan. Model/twin lifecycle mencakup commissioning, calibration, validation, monitoring, change management, decommissioning, dan data retention. OT security memerlukan network segmentation, asset identity, patch/change procedure, dan incident coordination; availability/safety bisa lebih penting daripada feature baru. Nilai twin diukur dari keputusan lebih baik, downtime/risk turun, dan auditability—bukan semata detail visualisasi.
