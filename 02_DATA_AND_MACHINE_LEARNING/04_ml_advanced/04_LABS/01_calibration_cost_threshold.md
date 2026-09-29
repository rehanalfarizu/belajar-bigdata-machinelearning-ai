# Lab 01 — Calibration dan Cost Threshold
## 1. TUJUAN
Memisahkan ranking, probability quality, dan decision policy.
## 2. PREREQUISITE
Lesson 03–04 dan `decision_lab.py`.
## 3. SETUP
Gunakan fixed labels/probabilities dan FN/FP cost.
## 4. PREDICTION BEFORE RUN
Prediksi threshold saat FN sepuluh kali lebih mahal.
## 5. LANGKAH PRAKTIKUM
Hitung Brier, cost per threshold, reliability bins, dan pilih pada validation.
## 6. OBSERVATION
Catat threshold, confusion, cost, dan calibration gap.
## 7. WHY
Threshold 0.5 bukan hukum; probability harus sesuai frekuensi bila dipakai sebagai risiko.
## 8. MODIFICATION
Ubah prevalence/capacity/cost.
## 9. FAILURE EXPERIMENT
Pilih threshold pada test atau calibrate pada data training sama.
## 10. DEBUGGING
Pisahkan fit/calibration/selection/test dan ulangi evidence.
## 11. WORKPLACE CONNECTION
Muncul pada fraud, maintenance alarm, dan human review queue.
## 12. CHECKPOINT
Pilih policy dengan cost table, calibration evidence, dan rollback condition.
