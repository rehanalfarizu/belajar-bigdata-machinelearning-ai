# Lab 11 — Bootstrap

## 1. TUJUAN
Mengestimasi uncertainty dengan resampling dan memahami asumsi representativeness.

## 2. PREREQUISITE
Baca lesson 10–11 dan Lab 09.

## 3. SETUP
Gunakan sample kecil `[2,3,3,5,8]` dan seed tetap.

## 4. PREDICTION BEFORE RUN
Secara intuitif prediksi center bootstrap means; hitung manual dua resample berukuran lima beserta mean.

## 5. LANGKAH PRAKTIKUM
Panggil `bootstrap_mean_interval`, simpan beberapa mean, dan buat histogram ASCII.

## 6. OBSERVATION
Bandingkan mean original, resample manual, distribution, dan percentile interval.

## 7. WHY
Bootstrap memperlakukan empirical sample sebagai proxy population; bias sample tidak diperbaiki oleh pengulangan.

## 8. MODIFICATION
Ubah repeats, confidence, seed, dan tambahkan outlier; prediksi pengaruh.

## 9. FAILURE EXPERIMENT
Gunakan sample tidak representatif atau resample tanpa replacement.

## 10. DEBUGGING
Periksa replacement, ukuran resample, seed, dan kualitas sample awal; nyatakan keterbatasan.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada uncertainty metric, model evaluation, small-sample analysis, dan robust reporting.

## 12. CHECKPOINT
Bootstrap dataset baru: intuisi, dua hitungan manual, kode, histogram, variasi parameter, dan interpretasi.
