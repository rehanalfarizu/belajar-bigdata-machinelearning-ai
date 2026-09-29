# Lab 08 — Sampling Distribution

## 1. TUJUAN
Membedakan distribusi data dari distribusi estimator dan memahami standard error.

## 2. PREREQUISITE
Baca lesson 09–11.

## 3. SETUP
Populasi simulasi memiliki mean 10 dan standard deviation 2.

## 4. PREDICTION BEFORE RUN
Prediksi center mean sample dan perubahan spread saat n dari 5 menjadi 100; hitung manual SE `2/sqrt(n)`.

## 5. LANGKAH PRAKTIKUM
Jalankan `repeated_sample_means`, hitung stdev means, dan buat histogram ASCII per bin.

## 6. OBSERVATION
Bandingkan mean/SE teoritis dengan simulasi dan bentuk visual.

## 7. WHY
Setiap sample memberi estimator berbeda; sample lebih besar mengurangi variasi mean.

## 8. MODIFICATION
Ubah n, repeats, dan seed; prediksi stabilitas sebelum run.

## 9. FAILURE EXPERIMENT
Anggap 500 repeated means sebagai 500 observasi independen dari satu eksperimen nyata.

## 10. DEBUGGING
Identifikasi unit analisis dan proses sampling; pisahkan data mentah dari estimator.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada metric dashboard, batch quality, experiment estimate, dan polling.

## 12. CHECKPOINT
Tunjukkan intuisi/manual SE, kode, histogram, perubahan n, dan interpretasi distribution estimator.
