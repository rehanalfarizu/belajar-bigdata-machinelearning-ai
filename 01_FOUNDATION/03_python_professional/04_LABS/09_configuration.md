# Lab 09 — Configuration

## 1. TUJUAN
Menggabungkan default, file, environment, dan CLI dengan precedence serta validasi eksplisit.

## 2. PREREQUISITE
Baca lesson 10.

## 3. SETUP
Buat dataclass `Config` berisi host, port, dan debug; gunakan JSON serta environment dummy.

## 4. PREDICTION BEFORE RUN
Tulis tabel nilai akhir untuk konflik default < file < environment < CLI.

## 5. LANGKAH PRAKTIKUM
Implementasikan load, merge, conversion, validation, dan safe summary tanpa secret.

## 6. OBSERVATION
Catat nilai dan sumber pemenang setiap field.

## 7. WHY
Precedence deterministik membuat runtime behavior dapat dijelaskan dan diuji.

## 8. MODIFICATION
Ubah urutan precedence dengan sengaja, prediksi dampak, lalu putuskan kebijakan yang masuk akal.

## 9. FAILURE EXPERIMENT
Berikan port `"abc"`, port di luar rentang, dan key salah eja.

## 10. DEBUGGING
Pisahkan missing, conversion, dan validation; fail fast dengan sumber field, lalu tambah test matriks.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada deployment dev/staging/prod, container, feature flag, dan service config.

## 12. CHECKPOINT
Buat loader dua sumber dengan precedence dan validasi; jelaskan trade-off fleksibilitas versus kompleksitas.
