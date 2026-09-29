# Lab 02 — Clean, Validate, dan Curate
## 1. TUJUAN
Menghasilkan curated rows dan rejected rows yang dapat direconcile.
## 2. PREREQUISITE
Lab 01 dan `quality_pipeline.py`.
## 3. SETUP
Buat output sementara; pertahankan raw immutable.
## 4. PREDICTION BEFORE RUN
Prediksi accepted/rejected count serta hasil Fahrenheit→Celsius/UTC.
## 5. LANGKAH PRAKTIKUM
Ketik rule satu per satu, jalankan pipeline, lalu unit test conversion, timezone, key, dan accounting.
## 6. OBSERVATION
Catat input=accepted+rejected dan reason per rejected row.
## 7. WHY
Quarantine menjaga evidence; silent drop membuat quality tidak dapat diaudit.
## 8. MODIFICATION
Ubah operating range atau alias category dan nilai dampak.
## 9. FAILURE EXPERIMENT
Terima timestamp naive atau konversi unit dua kali.
## 10. DEBUGGING
Telusuri raw→normalized→validated, perbaiki rule, jalankan regression test.
## 11. WORKPLACE CONNECTION
Muncul pada bronze/silver pipeline, ingestion, dan feature preparation.
## 12. CHECKPOINT
Buat satu rule baru lengkap dengan test sukses, failure, reason, dan reconciliation.
