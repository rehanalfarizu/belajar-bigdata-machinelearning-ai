# Lab 02 — Type dan Conversion

## 1. TUJUAN
Membedakan value, type, representasi teks, dan konversi valid.

## 2. PREREQUISITE
Baca lesson 02; Python 3 tersedia.

## 3. SETUP
Buat `conversion_lab.py` dengan input teks `"42"`, `"3.5"`, `""`, dan `"empat"`.

## 4. PREDICTION BEFORE RUN
Prediksi hasil `int`, `float`, `bool`, dan `str` untuk setiap input, termasuk exception.

## 5. LANGKAH PRAKTIKUM
Ketik loop yang mencetak `repr(value)`, `type(value).__name__`, dan hasil setiap konversi dalam blok `try` kecil.

## 6. OBSERVATION
Catat pasangan input-konversi yang berhasil dan gagal; perhatikan khusus `bool("False")`.

## 7. WHY
Konversi mengikuti aturan type, bukan makna bahasa sehari-hari; string nonkosong selalu truthy.

## 8. MODIFICATION
Buat fungsi `parse_bool` yang hanya menerima variasi eksplisit `true/false/1/0`.

## 9. FAILURE EXPERIMENT
Masukkan `"12kg"` ke `int` dan biarkan `ValueError` terlihat.

## 10. DEBUGGING
Pisahkan validasi dari konversi, tampilkan input bermasalah dengan `repr`, perbaiki parser, lalu uji batas.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada CSV, environment variable, form, CLI, dan payload API yang awalnya berupa teks.

## 12. CHECKPOINT
Buat parser integer positif yang menolak kosong, desimal, teks, nol, dan negatif dengan pesan berbeda.
