# Month 2 — Data & ML System

Project melanjutkan Sensor Simulator Month 1: event sensor menjadi dataset yang dipercaya, dianalisis, dan dipakai untuk model dengan evaluation jujur. Tidak ada full solution.

## M1 — Inspect raw data

Definisikan question dan inventory source. **DoD:** raw immutable, profile awal, issue log, dan sample lineage.

## M2 — Define grain, schema, dan keys

Tulis data dictionary dan relationship. **DoD:** uniqueness/referential tests gagal pada deliberate bad row.

## M3 — Clean dan validate

Normalisasi string/unit/time, quarantine invalid, curate. **DoD:** input=accepted+rejected dan rerun idempotent.

## M4 — SQL analysis

DuckDB join/group/window/CTE. **DoD:** join cardinality diuji, totals direconcile, tiga question terjawab.

## M5 — EDA dan baseline

Report distribution/time/groups serta simple baseline. **DoD:** minimal lima insights dengan evidence, denominator, limitation.

## M6 — Feature pipeline

Split sebelum fitting transform; feature availability audit. **DoD:** no target/future leakage dan pipeline repeatable.

## M7 — Candidate models

Manual tiny algorithm lalu library candidates. **DoD:** experiment log, valid CV, parameter/config/seed tercatat.

## M8 — Evaluation dan threshold

Metric dari cost, calibration bila relevan, locked test. **DoD:** baseline comparison, variability, confusion/errors.

## M9 — Error analysis dan constraints

Slice site/time/range, latency/memory/maintainability. **DoD:** decision table serta corrective action.

## M10 — Reproducibility dan report

Documented commands, tests, model/data card, limitations; optional local API. **DoD:** clean rerun menghasilkan artifacts dan reviewer dapat mengubah satu requirement.

## Final evidence

Raw/validated/curated layers, contract, SQL, EDA, baseline, model pipeline, test output, error slices, comparison table, failure experiments, limitations, dan reasoning defense.

## Acceptance gate

Grain/key eksplisit; join explosion terdeteksi; future/entity leakage dicegah; test tidak dipakai tuning; metric terkait cost; hasil reproducible; model complexity mengalahkan baseline secara bermakna.
