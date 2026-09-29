# Lab 01 — Future Leakage Experiment
## 1. TUJUAN
Membuktikan random split/centered rolling memberi metric palsu.
## 2. PREREQUISITE
Lesson 01–02 dan `temporal_lab.py`.
## 3. SETUP
Buat series bertimestamp dengan trend dan regime change.
## 4. PREDICTION BEFORE RUN
Prediksi random vs temporal metric dan feature time lineage.
## 5. LANGKAH PRAKTIKUM
Buat lag valid; bandingkan random/temporal; sengaja buat centered/future feature.
## 6. OBSERVATION
Catat metric gap dan latest source timestamp.
## 7. WHY
Future information tidak tersedia ketika forecast dibuat.
## 8. MODIFICATION
Ubah horizon dan regime-change point.
## 9. FAILURE EXPERIMENT
Scale seluruh series dan random shuffle.
## 10. DEBUGGING
Assert feature_time ≤ decision_time, refit transform per window, retest.
## 11. WORKPLACE CONNECTION
Muncul pada demand, sensor, finance, dan predictive maintenance.
## 12. CHECKPOINT
Tunjukkan leakage metric, diagnosis lineage, perbaikan, dan honest result.
