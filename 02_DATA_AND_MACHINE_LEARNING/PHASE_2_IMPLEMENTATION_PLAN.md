# Phase 2 Implementation Plan

## Outcome

Pembelajar bergerak dari raw data yang belum dipercaya menjadi analysis dan model yang dapat direproduksi, diuji, dirusak, di-debug, dievaluasi terhadap baseline, serta dipertanggungjawabkan.

## Urutan implementasi

### Stage 1 — Data trust

- lesson: observation/variable/grain/key/schema/type, missing/duplicate/string/unit/timezone/outlier;
- executable raw→validated→curated pipeline;
- DuckDB SQL untuk join, group, window, CTE, dan reconciliation;
- failure cases untuk dtype, duplicate key, wrong join, timezone, missing, dan unit.

### Stage 2 — Pattern discovery

- KDD dan CRISP-DM;
- association rule manual→simple implementation→library option;
- clustering, outlier, reduction, sequential pattern;
- spurious discovery dan association ≠ causation.

### Stage 3 — Valid ML evidence

- split/baseline/leakage/pipeline;
- algoritma inti problem→math→from-scratch→sklearn;
- regression/classification metrics, CV, bias/variance, error slices.

### Stage 4 — Model decisions

- feature/regularization/ensemble/boosting/search;
- calibration/threshold/imbalance/SMOTE;
- uncertainty, temporal validation, constraints, and comparison.

### Stage 5 — Time-ordered evidence

- timestamp/order/frequency/resampling/lag/rolling;
- trend/seasonality/stationarity/autocorrelation;
- naive/ETS/ARIMA overview, rolling validation, interval, drift;
- mandatory future-leakage experiment.

### Stage 6 — Deep learning bridge

TensorFlow/Keras dipilih sebagai framework primer karena sudah ada di `requirements.txt` dan materi awal paling lengkap menggunakannya. NumPy dipakai sebelum autograd. PyTorch dipertahankan hanya sebagai comparison appendix agar beginner tidak belajar dua framework bersamaan.

## Artifact contract

Setiap chapter memiliki README map, sequential lessons, tutorial/reference, labs dengan 12 bagian, exercises, reasoning problems, broken cases, mini-project, checkpoint, workplace connection, dan navigation.

## Verification

- Markdown links, notebook JSON/static syntax, Python syntax;
- Phase 2 lab contract dan lesson structure;
- lightweight unit tests tanpa download/network/GPU;
- project milestone count dan problem levels;
- repository audit, diff check, empty directory check;
- pedagogical review terhadap why, assumptions, alternatives, failure, debug, evidence, dan workplace.

## Gate

PASS hanya bila keenam chapter runnable pada jalur ringan, tidak memiliki broken link, project mempunyai milestone ladder, Week 5–9 detail, serta learner-facing checkpoints meminta evidence bukan hafalan.
