# Lab 07 — Exception Design

## 1. TUJUAN
Mendesain taxonomy exception dan menerjemahkan error antar-layer dengan cause.

## 2. PREREQUISITE
Baca lesson 08.

## 3. SETUP
Buat `ReadingError`, `ReadingFormatError`, dan `ReadingRangeError` serta parser kecil.

## 4. PREDICTION BEFORE RUN
Petakan tiga input gagal ke exception dan layer yang bertanggung jawab menanganinya.

## 5. LANGKAH PRAKTIKUM
Ketik parser, terjemahkan `ValueError` memakai `raise ... from error`, dan tangani base domain exception di CLI boundary.

## 6. OBSERVATION
Catat type, message, `__cause__`, dan exit behavior.

## 7. WHY
Taxonomy memberi caller pilihan handling stabil tanpa bergantung pada detail implementasi.

## 8. MODIFICATION
Tambahkan field line number dan bad value; nilai informasi versus risiko membocorkan data.

## 9. FAILURE EXPERIMENT
Tangkap semua exception di layer terdalam dan ganti dengan pesan generik tanpa cause.

## 10. DEBUGGING
Buktikan hilangnya konteks, sempitkan catch, pertahankan cause, lalu test taxonomy.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada API error mapping, SDK, ingestion, database adapter, dan job orchestration.

## 12. CHECKPOINT
Desain tiga exception terkait, tunjukkan translation dan chaining, lalu jelaskan trade-off detail versus abstraction.
