# Phase 2 Pedagogical Review

Tanggal review: 29 September 2026.

## Review terhadap learning flow

| Kriteria | Evidence | Hasil |
|---|---|---|
| problem/why sebelum tool | 32 lesson dimulai dari problem, decision, atau failure | PASS |
| beginner language→formal model | grain, quality, association, split, time, neuron dibangun dari contoh kecil | PASS |
| manual→from-scratch→library | rule metrics, regression/distance/metrics, temporal baseline, neuron/gradient | PASS |
| predict→modify→break→debug | 14 lab memiliki kontrak 12 bagian | PASS |
| engineering evidence | CSV, SQL, 5 executable modules, tests, custom Keras loop | PASS |
| alternatives/trade-offs | missing handling, SQL/Pandas, mining methods, algorithms, models, regularization | PASS |
| assumptions/failure/debug | lesson, 47 broken cases, explicit evidence checks | PASS |
| workplace connection | chapter gates/labs/projects mengaitkan analytics, ML review, forecasting, training | PASS |
| reasoning progression | chapter dan global problems Level 1–5 | PASS |
| project growth | Month 2 memakai Month 1 sensor output dan 10 milestone | PASS |

## Pedagogical walkthrough

Learner dapat bergerak dari Phase README ke chapter question, lesson order, lab, problems, broken cases, mini-project, checkpoint, Month 2, lalu gate tanpa mencari path manual. Notebook lama ditempatkan sebagai laboratory/reference; engineering evidence memakai script, SQL, tests, dan project.

## Deliberate boundaries

- Lesson baru ringkas dan berurutan; dokumen lama yang panjang tetap menjadi reference, bukan entrypoint.
- Deep Learning memakai TensorFlow/Keras sebagai primer; PyTorch content lama bukan learning path utama.
- Local synthetic/messy data adalah default agar tidak membutuhkan download.
- Heavy framework execution dipisahkan dari CI ringan agar pull request tidak membutuhkan GPU/download.

## Human-learning limitations

Struktur dan executable evidence tidak membuktikan seorang pemula telah menguasai materi. Checkpoint defense, feedback reviewer, dan penggunaan project nyata tetap diperlukan. EDA visual, sklearn experiments, DuckDB, dan TensorFlow perlu dijalankan learner di environment Phase 2 lengkap.

## Review decision

Pedagogical design: **PASS**. Heavy-runtime verification: **deferred and explicitly bounded**, bukan diklaim telah dieksekusi.
