# Lab 02 — Cluster, Sequence, dan Spurious Pattern
## 1. TUJUAN
Menguji stability pattern terhadap scale, order, seed, dan holdout.
## 2. PREREQUISITE
Lesson 03–04; sklearn optional untuk clustering.
## 3. SETUP
Buat data dua feature berbeda scale dan sequence alarm per asset.
## 4. PREDICTION BEFORE RUN
Prediksi cluster raw/scaled dan transition counts setelah sorting.
## 5. LANGKAH PRAKTIKUM
Bandingkan K-Means raw/scaled; hitung transition; split discovery/confirmation.
## 6. OBSERVATION
Catat membership/stability/support pada holdout.
## 7. WHY
Distance dan order merupakan assumptions, bukan detail preprocessing.
## 8. MODIFICATION
Tambahkan outlier, ubah seed/window, dan interpretasikan sensitivity.
## 9. FAILURE EXPERIMENT
Acak timestamp atau pilih hanya pattern paling bagus dari banyak candidate.
## 10. DEBUGGING
Audit ordering, duplicate, scale, comparisons, dan repeatability.
## 11. WORKPLACE CONNECTION
Muncul pada segmentasi asset dan alarm cascade investigation.
## 12. CHECKPOINT
Pertahankan satu pattern dengan stability evidence dan satu limitation.
