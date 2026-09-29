# Lab 03 — Metrics dan Error Analysis
## 1. TUJUAN
Memilih metric dari cost dan menemukan failure slice.
## 2. PREREQUISITE
Lesson 05–06.
## 3. SETUP
Siapkan actual, score, site, dan threshold candidates.
## 4. PREDICTION BEFORE RUN
Hitung confusion/precision/recall/F1 manual untuk satu threshold.
## 5. LANGKAH PRAKTIKUM
Verifikasi code, sweep threshold, lalu metric per site/time/range.
## 6. OBSERVATION
Catat trade-off FN/FP dan slice terburuk.
## 7. WHY
Aggregate metric menyembunyikan siapa yang gagal.
## 8. MODIFICATION
Ubah prevalence/cost dan pilih threshold baru.
## 9. FAILURE EXPERIMENT
Laporkan accuracy pada 95:5 dan abaikan baseline.
## 10. DEBUGGING
Periksa denominator, label positive, imbalance, dan slice size.
## 11. WORKPLACE CONNECTION
Muncul pada alarm policy, model card, dan launch decision.
## 12. CHECKPOINT
Serahkan manual metric, threshold-cost rationale, error slice, action, limitation.
