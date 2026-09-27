# Panduan Belajar Berbasis Gate

Urutan belajar ditentukan oleh bukti kompetensi, bukan target bulan. Kamu boleh bergerak lebih cepat pada topik yang sudah dikuasai, tetapi jangan melewati gate hanya karena notebook berhasil dijalankan.

## Cara memakai satu chapter

1. Baca konteks, problem, mental model, assumptions, dan failure modes.
2. Ketik ulang implementasi minimal; jangan mulai dari solution.
3. Jalankan test/baseline dan simpan hasil awal.
4. Ubah satu variable per experiment dan catat hypothesis→result→decision.
5. Kerjakan praktikum serta challenge tanpa melihat solusi.
6. Buat mini project dari file kosong pada hari berbeda.
7. Jawab checkpoint dengan kata sendiri dan tunjukkan evidence.

Saat error, baca traceback dari baris terakhir, kecilkan menjadi minimal failing example, lalu periksa type, shape, unit, time order, missing value, state version, dan assumptions. Ubah satu hypothesis setiap percobaan.

## Gate 1 — Foundation

Materi: `00_math_statistics`, `01_python_fundamental`, dan fondasi komputer/software engineering pada curriculum.

- **Teori**: process/thread, memory/file/network/HTTP/serialization/API; function/class, typing, exception, iterator/generator, context manager, decorator, async; vector/matrix, derivative, probability, uncertainty.
- **Kode**: CLI modular dengan config/logging, parser JSON/CSV, dataclass, tests, package kecil.
- **Project**: sensor simulator CLI dengan timestamp UTC dan test.
- **Debugging**: traceback, environment/import/path, race/timeouts dasar, numerical instability dasar.
- **Checkpoint**: mengapa async tidak sama dengan parallel? Mengapa floating-point bukan real number exact?

Jangan lanjut bila kamu belum dapat memisahkan I/O, domain logic, dan state dalam kode.

## Gate 2 — Data

Materi: `02_data_analysis`, SQL/data-quality portion `07`, serta data mining di curriculum.

- **Teori**: grain/key/join, NumPy/Pandas, EDA/cleaning, data quality/provenance, time series, KDD/CRISP-DM, pattern/anomaly/clustering.
- **Kode**: load→validate→clean→join→aggregate→visualize; SQL CTE/window; data contract.
- **Project**: multi-table analysis dengan raw/curated separation dan reproducible report.
- **Debugging**: join explosion, duplicate key, unit mismatch, time zone, leakage dari future.
- **Checkpoint**: kapan missing bukan nol? Mengapa correlation/pattern bukan causal knowledge?

## Gate 3 — ML

Materi: `03_ml_fundamental`, `04_ml_advanced`, `05_deep_learning`, dan bila perlu `08_nlp_transformers`.

- **Teori**: supervised/unsupervised, regression/classification/clustering, trees/ensemble/SVM/probabilistic models, calibration, uncertainty, explainability, bias/variance, temporal validation; NN/backprop/CNN/RNN/LSTM/Transformer/autoencoder.
- **Kode**: baseline→pipeline→CV→evaluation→error analysis; implementasi algorithm kecil dari nol.
- **Project**: model temporal atau predictive-maintenance precursor dengan asset/time holdout.
- **Debugging**: leakage, imbalance, bad threshold, miscalibration, distribution shift, unstable training.
- **Checkpoint**: kapan model lebih kompleks gagal memberi nilai? Apa beda probability score dan calibrated probability?

## Gate 4 — System

Materi: `06_mlops_deployment`, `07_big_data_data_engineering`, `09_ai_systems_cloud`.

- **Teori**: API, packaging, testing, config/secrets, Docker, distributed systems, event streaming, storage, reliability, observability, security/governance.
- **Kode**: typed API, idempotent ingestion, unit+integration test, structured logs, health/readiness.
- **Project**: deploy lokal end-to-end dengan replay/rollback/runbook.
- **Debugging**: duplicate message, partial failure, retry storm, schema incompatibility, backpressure, model timeout.
- **Checkpoint**: apa arti exactly-once pada boundary berbeda? Apa degraded mode saat dependency down?

## Gate 5 — Digital Twin Foundation

Materi: [`10_digital_twin`](materi/10_digital_twin/README.md).

- **Teori**: history, physical/virtual entity, observation/state/model/synchronization/lifecycle, model–shadow–twin, frequency/fidelity, maturity.
- **Kode**: jalankan dan tulis ulang core tank separation.
- **Project**: tank shadow dengan noisy/missing sensor.
- **Debugging**: ground-truth leakage, timestamp/unit mismatch, residual salah dihitung.
- **Checkpoint**: mengapa 3D/dashboard/simulation saja bukan twin? Apakah IoT/actuation selalu wajib?

## Gate 6 — Connected Twin

Materi: chapter [`11`](materi/11_iot_telemetry_connectivity/README.md) dan [`12`](materi/12_time_series_state_estimation/README.md).

- **Teori**: MQTT/OPC UA/streaming scope, event/processing time, late/out-of-order/duplicate, estimator/noise/uncertainty/Kalman/fusion.
- **Kode**: contract validator + ledger + Kalman dari nol + missing/multi-sensor test.
- **Project**: synchronized tank/HVAC/motor dari simulator melalui event boundary ke state.
- **Debugging**: replay, sequence gap/reboot, sensor bias, delayed observation, overconfident covariance.
- **Checkpoint**: apa beda last reading dan estimated state? Mengapa QoS bukan correctness end-to-end?

## Gate 7 — Predictive Twin

Materi: chapter [`13`](materi/13_simulation_physics_hybrid/README.md) dan [`14`](materi/14_anomaly_predictive_maintenance_rul/README.md).

- **Teori**: simulation paradigms, verification/calibration/validation, hybrid/residual model, anomaly–fault–diagnosis–failure, PdM/RUL, uncertainty.
- **Kode**: simulator tervalidasi, detector streaming, temporal forecasting/RUL baseline.
- **Project**: multi-sensor predictive-maintenance twin dengan detection delay dan calibrated RUL.
- **Debugging**: timestep instability, parameter non-identifiability, contaminated baseline, window leakage, concept drift.
- **Checkpoint**: kapan residual besar berarti model salah, bukan asset fault? Apa failure criterion RUL?

## Gate 8 — Prescriptive Twin

Materi: chapter [`15`](materi/15_architecture_semantics_spatial/README.md) dan [`16`](materi/16_optimization_intelligent_twin/README.md).

- **Teori**: layered architecture, state/history/graph, semantics/ontology/spatial, objective/constraints, optimization, RL limits, HITL, safety/security.
- **Kode**: what-if + optimizer baseline + recommendation + command guard/audit.
- **Project**: architecture lokal dengan state service, history, model API, dashboard, observability, Docker.
- **Debugging**: stale cache/state, graph/schema migration, infeasible solver, unsafe recommendation, spoof/replay.
- **Checkpoint**: mengapa recommendation bukan command? Apa yang tetap aman ketika cloud/model gagal?

## Gate 9 — Intelligent/Federated Twin

- **Teori**: adaptive model lifecycle, fleet/system/system-of-systems/federation, identity/semantic/access contracts, change governance.
- **Kode**: versioned model/schema, shadow/canary update, rollback, cross-twin query/event contract.
- **Project**: configurable multi-asset platform sesuai [chapter 17](materi/17_domains_research_capstone/README.md).
- **Debugging**: semantic drift, cross-owner authorization, partial federation, model update regression.
- **Checkpoint**: apa evidence adaptasi memberi manfaat dan dapat dibatalkan?

## Gate 10 — Expert/Research

- **Teori**: systematic review, research gap/question/hypothesis, experiment design, baseline, ablation, reproducibility, statistical validation, threats to validity.
- **Kode/project**: capstone platform + reproducible research artifact.
- **Debugging**: challenge assumptions, reproduce from clean environment, failure injection, independent holdout, negative result analysis.
- **Checkpoint**: klaim apa yang didukung data, pada population/operating envelope mana, dan apa yang belum dapat disimpulkan?

## Aturan portofolio

Setiap project menyertakan problem/use case, stakeholder/decision, data provenance, assumptions, baseline, experiment log, metrics, uncertainty, failure cases, security/safety boundary, run command, tests, dan limitations. Screenshot dashboard tanpa kode/evidence bukan portofolio sistem.
