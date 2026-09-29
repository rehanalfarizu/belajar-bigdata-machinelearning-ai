# Lab 02 — Matrix Transformation

## 1. TUJUAN
Melihat matrix sebagai transformasi vector, bukan sekadar tabel angka.

## 2. PREREQUISITE
Baca lesson 02 dan selesaikan Lab 01.

## 3. SETUP
Gunakan vector `[2, 1]` dan matrix skala `[[2, 0], [0, 3]]`.

## 4. PREDICTION BEFORE RUN
Gambar intuisi transformasi; hitung manual dua row-dot-vector.

## 5. LANGKAH PRAKTIKUM
Panggil `matrix_vector` dan tampilkan vector sebelum/sesudah pada ASCII grid.

## 6. OBSERVATION
Bandingkan endpoint manual, kode, dan visualisasi.

## 7. WHY
Setiap row menghasilkan satu komponen output; kolom menunjukkan efek basis input.

## 8. MODIFICATION
Ganti matrix dengan rotasi 90° `[[0,-1],[1,0]]` dan shear; prediksi dahulu.

## 9. FAILURE EXPERIMENT
Berikan matrix ragged atau dimensi vector tidak cocok.

## 10. DEBUGGING
Tulis shape input/output, cek panjang setiap row, perbaiki, lalu verifikasi dengan basis `[1,0]` dan `[0,1]`.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada transformasi koordinat, layer linear neural network, PCA, dan graphics.

## 12. CHECKPOINT
Rancang satu transformasi 2D, hitung manual, jalankan kode, visualisasikan, ubah parameter, dan interpretasikan.
