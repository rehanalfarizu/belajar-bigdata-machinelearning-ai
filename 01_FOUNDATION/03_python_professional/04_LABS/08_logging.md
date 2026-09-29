# Lab 08 — Logging

## 1. TUJUAN
Menghasilkan event log berlevel dan berkonteks tanpa membocorkan secret.

## 2. PREREQUISITE
Baca lesson 09.

## 3. SETUP
Buat logger module, konfigurasi format timestamp/level/message hanya di entry point.

## 4. PREDICTION BEFORE RUN
Prediksi event yang terlihat pada level INFO dan DEBUG.

## 5. LANGKAH PRAKTIKUM
Log start, record count, invalid record, dan completion; ubah level dan bandingkan.

## 6. OBSERVATION
Catat filter level, destination, urutan, dan context yang membantu diagnosis.

## 7. WHY
Logging merekam event operasional; level adalah kebijakan visibility, bukan pengganti penanganan error.

## 8. MODIFICATION
Tambahkan correlation ID dengan `LoggerAdapter`; jangan log token atau seluruh payload.

## 9. FAILURE EXPERIMENT
Konfigurasi handler dua kali sehingga log duplikat dan sengaja hampir mencetak secret dummy.

## 10. DEBUGGING
Inspeksi handler/propagation, pastikan config hanya di boundary, redact field, lalu verifikasi satu event satu baris.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada production incident, audit trail, pipeline observability, dan SRE.

## 12. CHECKPOINT
Buat log tiga level dengan context aman dan jelaskan trade-off detail diagnosis versus noise/privacy.
