# Phase 2 Pedagogical Audit

Tanggal audit: 29 September 2026. Phase 1 dipakai sebagai baseline dan tidak direstrukturisasi.

## Kondisi awal

Phase 2 memiliki enam chapter dan 49 file. Data Analysis, ML Fundamental, ML Advanced, dan Deep Learning mempunyai materi lama serta notebook; Data Mining dan Time Series masing-masing hanya memiliki README, satu ringkasan teori, exercise, dan checkpoint.

## Temuan lintas chapter

| Area | Evidence awal | Risiko belajar | Keputusan |
|---|---|---|---|
| Entry point | README chapter hanya 15–17 baris | urutan lesson/lab tidak terlihat | buat chapter map, prerequisite, effort, gate |
| Teori | beberapa teori 9–37 baris; DL 526 baris | summary terlalu tipis atau dokumen terlalu padat | pecah menjadi lesson kecil berbasis problem dan why |
| Praktikum | Data Mining/Time Series tanpa `04_LABS` | konsep tidak menghasilkan evidence | tambah lab berkontrak 12 bagian |
| Engineering | lab didominasi notebook | pipeline reusable/testable tidak terlatih | tambah `.py`, SQL, data, dan tests |
| Data realism | belum ada raw→validated→curated yang eksplisit | cleaning terasa kosmetik | tambah messy dataset dan quality contract |
| SQL | tidak ada executable DuckDB path | join/window/CTE tidak tervalidasi | gunakan DuckDB sebagai lab SQL; SQLite/stdlib tetap untuk test ringan |
| ML reasoning | materi library lebih kuat daripada from-scratch | learner menghafal API | manual/from-scratch sebelum sklearn |
| Leakage | tersebar sebagai anti-pattern | risiko tidak diuji langsung | tambah deliberate leakage labs |
| Deep learning | materi lama mencampur TensorFlow dan PyTorch | cognitive load dan dependency ganda | TensorFlow/Keras menjadi primer; PyTorch hanya comparison appendix |
| Assessment | hanya 2/6 checkpoint | kelulusan chapter tidak dapat dibuktikan | checkpoint, debugging, problems, project milestone |
| Roadmap | Week 5–9 masih chapter map | ritme harian/evidence tidak jelas | detailkan per hari setelah implementasi |

## Gap per chapter

### Data Analysis & SQL

Kekuatan awal: Pandas/NumPy, EDA, contoh cleaning. Gap: grain/key/schema belum menjadi gerbang; SQL dan DuckDB belum nyata; timezone, unit mismatch, join explosion, dan reconciliation belum menjadi eksperimen.

### Data Mining

Kekuatan awal: daftar scope sudah benar. Gap: KDD/CRISP-DM, Apriori manual, clustering/outlier/sequential pattern, multiple testing, lab, project, dan debugging belum diimplementasikan.

### ML Fundamental

Kekuatan awal: contoh sklearn dan anti-leakage cukup luas. Gap: alur problem→math→from-scratch→library belum konsisten; baseline, split reasoning, group/temporal caveat, PR metric, dan error analysis perlu menjadi lesson/lab eksplisit.

### ML Advanced

Kekuatan awal: pipeline, tuning, imbalance, model persistence. Gap: calibration, cost threshold, constraints, uncertainty, temporal validation, dan model comparison perlu dipisah dari “akurasi terbesar”.

### Time Series

Scope disebut tetapi hampir seluruhnya ringkasan. Tidak ada executable future-leakage experiment, rolling validation, naive baseline, forecast interval, atau drift lab.

### Deep Learning

Konten banyak tetapi padat, framework bercampur, dan dimulai terlalu cepat dari API. Belum ada jalur konsisten neuron→NumPy network→autograd→training loop→checkpoint→learning curve.

## Risiko implementasi

- Dataset/download eksternal membuat lab rapuh; gunakan data kecil lokal sebagai default.
- DuckDB, sklearn, dan TensorFlow tidak cocok untuk audit standard-library; pisahkan static/lightweight CI dari optional dependency execution.
- Banyak file tidak membuktikan pemahaman; gate harus meminta evidence, explanation, failure, dan defense.
- Notebook lama tetap dipertahankan sebagai laboratory/reference, bukan source of truth.

## Rekomendasi prioritas

1. Bangun chapter maps dan lesson path.
2. Buat messy local dataset, executable validation, SQL, serta tests.
3. Buat lab nyata untuk mining, ML evaluation/leakage, time series, dan DL loop.
4. Lengkapi debugging, checkpoints, problem ladders, dan Month 2 milestones.
5. Perluas audit otomatis dan CI ringan.
6. Detailkan Week 5–9, lalu jalankan Phase 2 gate.
