# Lab 04 — Generator Streaming

## 1. TUJUAN
Mengamati lazy evaluation, single-use iterator, dan memory-friendly processing.

## 2. PREREQUISITE
Baca lesson 05.

## 3. SETUP
Gunakan ide `valid_numbers` dari `patterns_lab.py`, tetapi ketik generator baru yang mencatat tiap line yang dibaca.

## 4. PREDICTION BEFORE RUN
Prediksi output saat generator dibuat, saat satu `next`, saat dihabiskan, dan saat diiterasi ulang.

## 5. LANGKAH PRAKTIKUM
Jalankan empat tahap; bandingkan generator expression dengan list comprehension pada range besar memakai `tracemalloc`.

## 6. OBSERVATION
Catat waktu produksi output, state konsumsi, serta peak memory relatif.

## 7. WHY
Generator menyimpan state iterasi dan menghasilkan item on demand, bukan menyimpan seluruh hasil.

## 8. MODIFICATION
Tambahkan filter dan batching; prediksi kapan upstream benar-benar dibaca.

## 9. FAILURE EXPERIMENT
Konsumsi generator untuk logging, lalu coba memprosesnya lagi.

## 10. DEBUGGING
Buktikan iterator sudah exhausted, tentukan apakah perlu materialisasi atau generator factory, lalu uji dua consumer.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada file besar, database cursor, stream event, dan ETL.

## 12. CHECKPOINT
Proses 100.000 item secara lazy, tunjukkan konsumsi bertahap, dan jelaskan trade-off memory versus reusability.
