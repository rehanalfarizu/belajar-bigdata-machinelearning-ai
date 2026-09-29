# Lesson 05 — Temporal Validation dan Model Comparison

Random CV salah bila masa depan memprediksi masa lalu atau observation entity berulang bocor antar-fold. Rolling/expanding window meniru retraining dan deployment horizon.

Model terbaik bukan metric tertinggi saja. Buat decision matrix: baseline improvement, variability, FN/FP cost, calibration, latency, memory, retrain effort, explainability, dan failure mode.

Statistical difference kecil mungkin tidak operationally meaningful. Bandingkan pada fold yang sama, tampilkan distribution, dan jangan melakukan repeated tuning pada test.

Checkpoint: pilih model lebih sederhana bila berada dalam tolerance dan constraints lebih baik; dokumentasikan alasan dan rollback trigger.
