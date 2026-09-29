# Lab 09 — Confidence Interval

## 1. TUJUAN
Menghitung interval estimasi mean dan menginterpretasikan uncertainty tanpa klaim berlebihan.

## 2. PREREQUISITE
Baca lesson 11 dan selesaikan Lab 08.

## 3. SETUP
Gunakan data `[9,11,10,12,8,10,9,11]` dan z 1.96 sebagai pendekatan lab.

## 4. PREDICTION BEFORE RUN
Hitung manual mean, sample stdev, SE, margin, dan interval.

## 5. LANGKAH PRAKTIKUM
Panggil `confidence_interval_mean` dan gambar garis ASCII lower—mean—upper.

## 6. OBSERVATION
Bandingkan semua komponen manual dengan kode dan lebar visual.

## 7. WHY
Interval merefleksikan prosedur sampling dan assumptions; bukan peluang 95% parameter tetap berada di interval setelah data diamati.

## 8. MODIFICATION
Duplikasi ukuran sample dengan data baru dan ubah confidence; prediksi lebar.

## 9. FAILURE EXPERIMENT
Gunakan satu observasi atau data sangat skewed lalu tetap membuat klaim normal tanpa catatan.

## 10. DEBUGGING
Periksa n, independence, shape, dan approximation; pilih bootstrap bila assumption lemah.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada KPI, experiment lift, sensor calibration, dan reporting uncertainty.

## 12. CHECKPOINT
Hitung interval dataset baru: intuisi, manual, kode, visual, perubahan n/confidence, dan interpretasi benar.
