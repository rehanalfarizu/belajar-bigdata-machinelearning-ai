# Lab 10 — Unit Test

## 1. TUJUAN
Menguji behavior kecil secara terisolasi dengan kasus normal, batas, dan gagal.

## 2. PREREQUISITE
Baca lesson 11; pahami `unittest`.

## 3. SETUP
Pilih `Reading` atau `valid_numbers` dari `patterns_lab.py` dan baca test yang sudah ada.

## 4. PREDICTION BEFORE RUN
Prediksi test yang tetap lulus bila implementasi internal direfactor tanpa behavior berubah.

## 5. LANGKAH PRAKTIKUM
Tambahkan tiga test bernama behavior: happy path, boundary, expected exception. Jalankan `python -m unittest -v`.

## 6. OBSERVATION
Catat test discovery, failure diff, dan waktu eksekusi.

## 7. WHY
Unit test melindungi contract kecil; test implementation detail membuat refactor mahal.

## 8. MODIFICATION
Refactor implementation tanpa mengubah test, lalu tambahkan parameter cases via `subTest`.

## 9. FAILURE EXPERIMENT
Sengaja masukkan bug off-by-one dan buat satu test terlalu longgar.

## 10. DEBUGGING
Pastikan test gagal karena bug, perketat assertion, perbaiki production code, dan jalankan seluruh suite.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada CI, regression prevention, code review, dan safe refactor.

## 12. CHECKPOINT
Tulis minimal empat test yang gagal saat behavior rusak dan jelaskan trade-off isolation versus realism.
