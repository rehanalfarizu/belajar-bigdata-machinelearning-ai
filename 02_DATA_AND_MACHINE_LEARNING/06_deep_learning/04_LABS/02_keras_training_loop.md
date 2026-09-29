# Lab 02 — Keras Training Loop dan Overfitting
## 1. TUJUAN
Membangun Dataset→model→training→checkpoint→evaluation yang reproducible.
## 2. PREREQUISITE
Lesson 03–06; TensorFlow dari requirements; CPU cukup; baca `keras_training_loop.py` setelah membuat versimu.
## 3. SETUP
Gunakan synthetic/local tiny dataset tanpa download; set seed/config.
## 4. PREDICTION BEFORE RUN
Prediksi shapes, chance baseline, learning curve small/large model.
## 5. LANGKAH PRAKTIKUM
Ketik dataset, custom GradientTape loop, validation, checkpoint reload, evaluation.
## 6. OBSERVATION
Catat train/validation loss, metric, time, model size.
## 7. WHY
Loop memperlihatkan state yang berubah; checkpoint membuktikan recoverability.
## 8. MODIFICATION
Ubah batch size/dropout/capacity satu per eksperimen.
## 9. FAILURE EXPERIMENT
Shuffle test, evaluate training mode, atau pilih epoch dari test.
## 10. DEBUGGING
Periksa split, shape/dtype, training flag, gradient, seed, checkpoint equivalence.
## 11. WORKPLACE CONNECTION
Muncul pada experiment tracking, training jobs, and model handoff.
## 12. CHECKPOINT
Serahkan loop, curves, overfit experiment, reload test, baseline, limitations.
