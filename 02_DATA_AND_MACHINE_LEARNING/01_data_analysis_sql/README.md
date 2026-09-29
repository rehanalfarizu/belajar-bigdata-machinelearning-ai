# Mulai dari sini — Data Analysis & SQL

## Pertanyaan utama

Apa sebenarnya bentuk data ini dan apakah data ini dapat dipercaya? Chapter membangun jalur raw→inspect→profile→clean→validate→curated→SQL→analysis→report.

## Prerequisite dan effort

Lulus Phase 1. Estimasi 16–22 jam. Gunakan Pandas/NumPy untuk table work, DuckDB untuk analytical SQL, dan script/test untuk pipeline reusable.

## Lesson map

1. [Shape, grain, schema, key](01_TEORI/01_data_shape_grain_keys.md)
2. [Data-quality contract](01_TEORI/02_data_quality_contract.md)
3. [String, unit, timestamp, timezone](01_TEORI/03_time_units_categories.md)
4. [NumPy/Pandas execution](01_TEORI/04_numpy_pandas_execution.md)
5. [SQL JOIN/aggregation/window](01_TEORI/05_sql_joins_aggregation.md)
6. [EDA/visualization/validation](01_TEORI/06_eda_visualization_validation.md)

Materi lama [teori mendalam](01_TEORI/teori_mendalam.md) dan [contoh](03_EXAMPLES/contoh.md) menjadi reference setelah lesson.

## Practice path

[Profile messy data](04_LABS/01_profile_messy_data.md) → [clean/validate/curate](04_LABS/02_clean_validate_curate.md) → [DuckDB join/window](04_LABS/03_duckdb_join_window.md) → [exercises](05_EXERCISES/exercises.md) → [problems](06_PROBLEM_SOLVING/problems.md) → [broken cases](07_DEBUGGING/broken_cases.md) → [project](08_PROJECT/README.md) → [checkpoint](09_CHECKPOINT/CHECKPOINT.md).

## Workplace dan gate

Dipakai pada analytics, data engineering, data quality, dan feature pipelines. Lulus bila dapat mendefinisikan grain/key/schema, menjaga raw, reconcile cleaning/join, menulis SQL, dan membatasi insight dengan evidence.

## Navigasi

- Previous: [04 Math & Statistics](../../01_FOUNDATION/04_math_statistics/README.md)
- Next: [02 Data Mining](../02_data_mining/README.md)
