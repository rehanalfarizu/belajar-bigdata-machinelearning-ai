# Lab 01 — Split, Baseline, dan Leakage
## 1. TUJUAN
Mendesain evaluation yang meniru data unseen.
## 2. PREREQUISITE
Lesson 01; sklearn.
## 3. SETUP
Buat data asset berulang dengan timestamp dan target.
## 4. PREDICTION BEFORE RUN
Urutkan expected metric random, group, temporal split.
## 5. LANGKAH PRAKTIKUM
Bangun baseline; bandingkan split; fit preprocessing hanya train via Pipeline.
## 6. OBSERVATION
Catat overlap entity/time dan metric gap.
## 7. WHY
Metric sah hanya jika split mewakili deployment.
## 8. MODIFICATION
Ubah target horizon dan redesign split.
## 9. FAILURE EXPERIMENT
Masukkan target-derived feature dan scaler fit seluruh data.
## 10. DEBUGGING
Audit availability time, provenance feature, indices, dan pipeline fit.
## 11. WORKPLACE CONNECTION
Muncul pada model review, experiment approval, dan incident kualitas.
## 12. CHECKPOINT
Tunjukkan baseline, split rationale, deliberate leakage, fix, dan independent evidence.
