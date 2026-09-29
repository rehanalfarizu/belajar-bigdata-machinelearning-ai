# Lab 07 — Exception Handling

## 1. TUJUAN
Menentukan boundary penanganan exception tanpa menyembunyikan bug.

## 2. PREREQUISITE
Baca lesson 11.

## 3. SETUP
Buat fungsi `parse_temperature(text)` dan tiga input: valid, teks, dan di luar rentang.

## 4. PREDICTION BEFORE RUN
Prediksi exception type, baris asal, serta input mana yang seharusnya ditangani caller.

## 5. LANGKAH PRAKTIKUM
Ketik parser yang mengangkat `ValueError` bermakna; caller menangkap hanya `ValueError` dan melanjutkan record berikutnya.

## 6. OBSERVATION
Catat traceback sebelum handler, pesan setelah handler, dan record yang berhasil diproses.

## 7. WHY
Exception memindahkan control ke handler yang cocok; catch terlalu luas menghapus bukti bug tak terduga.

## 8. MODIFICATION
Tambahkan exception custom untuk range invalid dan bedakan pesannya dari format invalid.

## 9. FAILURE EXPERIMENT
Ganti handler menjadi `except Exception: pass` lalu masukkan typo internal.

## 10. DEBUGGING
Buktikan bug tertelan, sempitkan handler, gunakan chaining `raise ... from error`, dan verifikasi traceback menjaga cause.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada validasi input, ingestion data, retry network, API errors, dan job recovery.

## 12. CHECKPOINT
Buat parser dua failure mode, tangani di boundary yang tepat, dan tunjukkan bug programmer tetap terlihat.
