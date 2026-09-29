# Lab 01 — Variable dan State Tracing

## 1. TUJUAN
Menelusuri perubahan name, value, dan state program baris demi baris.

## 2. PREREQUISITE
Baca lesson 01; siapkan Python 3 dan kertas tabel trace.

## 3. SETUP
Buat `state_lab.py` berisi assignment `score = 10`, `bonus = score`, perubahan `score += 5`, lalu dua `print`.

## 4. PREDICTION BEFORE RUN
Tulis tabel nilai `score` dan `bonus` setelah setiap baris; jangan menjalankan kode dahulu.

## 5. LANGKAH PRAKTIKUM
Ketik sendiri program, jalankan, dan tambahkan print bernomor setelah setiap transisi state.

## 6. OBSERVATION
Bandingkan trace aktual dengan tabel prediksi dan tandai baris pertama yang berbeda.

## 7. WHY
Assignment mengikat name ke object; re-assignment `score` tidak otomatis mengubah binding `bonus` untuk integer immutable.

## 8. MODIFICATION
Tambahkan `penalty` dan dua update berurutan. Buat prediksi baru sebelum run.

## 9. FAILURE EXPERIMENT
Cetak name sebelum assignment lokalnya atau salah ketik nama variable untuk menghasilkan `NameError`.

## 10. DEBUGGING
Baca baris traceback, inventaris name yang tersedia, perbaiki urutan/ejaan, lalu ulangi trace lengkap.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul saat menelusuri state job ETL, accumulator, request handler, dan preprocessing.

## 12. CHECKPOINT
Dari file kosong, buat program lima transisi state dan tabel prediksi yang seluruhnya cocok dengan output.
