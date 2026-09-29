# Lab 04 — Loop Tracing

## 1. TUJUAN
Menelusuri iterator, accumulator, condition, dan termination.

## 2. PREREQUISITE
Baca lesson 07–08.

## 3. SETUP
Buat data `[3, -1, 4, 0, 2]` dan tabel kolom index, value, condition, total.

## 4. PREDICTION BEFORE RUN
Isi seluruh tabel untuk loop yang menjumlah hanya angka positif dan berhenti saat nol.

## 5. LANGKAH PRAKTIKUM
Ketik loop dengan print trace per iterasi; jalankan dan cocokkan dengan tabel.

## 6. OBSERVATION
Catat iterasi yang dilewati, update total, dan posisi `break`.

## 7. WHY
Loop adalah transisi state berulang; urutan condition, update, `continue`, dan `break` menentukan hasil.

## 8. MODIFICATION
Pindahkan nol ke awal/akhir dan ubah `break` menjadi `continue`. Prediksi setiap hasil.

## 9. FAILURE EXPERIMENT
Buat `while` yang lupa memperbarui counter; hentikan manual setelah membuktikan pola berulang.

## 10. DEBUGGING
Tambahkan invariant dan guard maksimum iterasi, temukan state yang tidak berubah, perbaiki, lalu verifikasi termination.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada pembacaan stream, retry, pagination API, batch processing, dan training epoch.

## 12. CHECKPOINT
Tulis loop dari kosong, berikan trace tiga iterasi, dan buktikan kapan serta mengapa loop berhenti.
