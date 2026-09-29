# Lab 10 — Hypothesis Test

## 1. TUJUAN
Menyusun H0, statistic, p-value, keputusan, dan batas kesimpulan.

## 2. PREREQUISITE
Baca lesson 12.

## 3. SETUP
Uji coin: 8 sukses dari 10 terhadap `H0: p=0.5`.

## 4. PREDICTION BEFORE RUN
Secara intuitif nilai seberapa ekstrem 8/10; hitung manual peluang outcome dengan kombinasi binomial.

## 5. LANGKAH PRAKTIKUM
Panggil `coin_two_sided_p_value` dan gambar probabilitas tiap jumlah sukses sebagai bar ASCII.

## 6. OBSERVATION
Catat statistic, p-value, alpha, dan keputusan; bedakan dari effect size.

## 7. WHY
p-value adalah peluang hasil setidaknya se-ekstrem jika H0 benar, bukan peluang H0 benar.

## 8. MODIFICATION
Ubah jumlah trial/sukses dan alpha; prediksi perubahan evidence.

## 9. FAILURE EXPERIMENT
Ulangi banyak test lalu hanya laporkan yang p<0.05.

## 10. DEBUGGING
Hitung jumlah comparison, nyatakan test sebelum data, tampilkan semua hasil, dan hindari klaim kausal tanpa desain.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada A/B test, quality control, model comparison, dan alert validation.

## 12. CHECKPOINT
Rancang test coin baru lengkap dengan intuisi/manual, kode, visual, variasi parameter, keputusan, dan batas klaim.
