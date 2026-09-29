# Lab 11 — Integration Test

## 1. TUJUAN
Menguji kerja sama parser, file boundary, config, dan output nyata secara terkendali.

## 2. PREREQUISITE
Selesaikan Lab 09–10.

## 3. SETUP
Buat pipeline kecil file-input → parse → summary-output dan test dengan `tempfile.TemporaryDirectory`.

## 4. PREDICTION BEFORE RUN
Prediksi bug boundary yang tidak akan ditemukan unit test parser saja.

## 5. LANGKAH PRAKTIKUM
Tulis test yang membuat file temporary, menjalankan entry function, lalu membaca output dan exit result.

## 6. OBSERVATION
Catat komponen yang benar-benar terintegrasi dan yang masih diganti/fake.

## 7. WHY
Integration test memberi realism lebih tinggi tetapi setup, diagnosis, dan runtime lebih mahal.

## 8. MODIFICATION
Tambahkan input multi-line dan filename dengan spasi; pertahankan isolation test.

## 9. FAILURE EXPERIMENT
Gunakan path hard-coded atau bergantung pada file hasil test sebelumnya.

## 10. DEBUGGING
Buktikan order dependency, pindahkan state ke temporary directory, cleanup otomatis, lalu jalankan test berulang.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada database adapter, filesystem pipeline, API client, dan release gate.

## 12. CHECKPOINT
Buat satu integration test hermetic dan jelaskan trade-off realism versus kecepatan/stabilitas.
