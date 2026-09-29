# Lab 03 — DuckDB JOIN, CTE, dan Window
## 1. TUJUAN
Menjawab pertanyaan lintas tabel tanpa join explosion.
## 2. PREREQUISITE
Lesson 05; DuckDB tersedia; `analysis.sql` dan raw CSV.
## 3. SETUP
Jalankan DuckDB dari folder lab dan buat view CSV.
## 4. PREDICTION BEFORE RUN
Hitung manual row count join readings×maintenance untuk A-1.
## 5. LANGKAH PRAKTIKUM
Ketik key checks, LEFT JOIN unmatched, wrong direct join, aggregate-before-join CTE, dan window ordering.
## 6. OBSERVATION
Catat multiplier, unmatched keys, total cost, grain setiap result.
## 7. WHY
JOIN menggabungkan setiap match; GROUP BY mengubah grain; window mempertahankannya.
## 8. MODIFICATION
Tambahkan maintenance event dan prediksi query yang berubah.
## 9. FAILURE EXPERIMENT
Jumlahkan reading setelah many-to-many direct join.
## 10. DEBUGGING
Reconcile distinct keys/count/totals sebelum-sesudah dan perbaiki grain.
## 11. WORKPLACE CONNECTION
Muncul pada BI, warehouse, feature tables, dan finance reconciliation.
## 12. CHECKPOINT
Tulis query CTE+window baru, buktikan cardinality aman, dan jelaskan why setiap tahap.
