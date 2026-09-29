# Month 2 — Data & ML System

## Context

Bangun pipeline dari minimal tiga tabel sensor/asset/maintenance menuju quality report, analysis, dan model yang memprediksi outcome terdefinisi.

## Deliverables

- raw/validated/curated layers dan data contract;
- SQL untuk join/aggregation/window serta reconciliation dengan Python;
- EDA dengan minimal lima evidence-backed insights;
- baseline dan model pipeline dengan valid split;
- error slices, calibration/uncertainty bila relevan, model card, dan tests.

## Acceptance criteria

Grain/key eksplisit; join explosion terdeteksi; future/asset leakage dicegah; rerun idempotent; test data tidak dipakai tuning; metric dikaitkan dengan cost; hasil dapat direproduksi dari documented command.

## Evidence

Simpan data dictionary, query, experiment log, comparison table, failure cases, limitations, dan reasoning defense mengapa model terpilih mengalahkan baseline.
