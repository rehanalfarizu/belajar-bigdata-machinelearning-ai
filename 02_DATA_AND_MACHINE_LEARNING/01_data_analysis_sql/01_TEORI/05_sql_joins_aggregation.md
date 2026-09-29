# Lesson 05 — SQL, JOIN, dan Aggregation

## Problem dan why

Entity dipisah untuk mengurangi duplication dan menjaga update consistency. SQL JOIN menyatukan hubungan ketika menjawab pertanyaan, tetapi cardinality yang salah menggandakan row dan aggregate.

## Mental model

`INNER JOIN` menyimpan match; `LEFT JOIN` mempertahankan semua left row. `GROUP BY` mengubah grain. CTE memberi nama tahap reasoning, bukan otomatis mempercepat query. Window function menghitung konteks kelompok tanpa meruntuhkan grain row.

## Manual example

Dua readings untuk asset A dijoin ke dua maintenance events A menghasilkan empat row. Menjumlah value setelah join berarti double counting. Agregasikan maintenance ke grain asset dahulu atau pisahkan metric.

## Why DuckDB?

DuckDB menjalankan analytical SQL lokal langsung pada CSV/Parquet dan cocok untuk lab. Pandas lebih fleksibel untuk transformasi Python; database server lebih cocok untuk concurrency/serving. DuckDB bukan kebutuhan universal.

## Failure/debugging/evidence

Sebelum JOIN: catat row count, grain, key uniqueness. Sesudah JOIN: cek row multiplier, unmatched keys, distinct business key, dan reconcile total terhadap source.

## Workplace dan checkpoint

Dipakai pada BI, warehouse, feature table, dan data quality. Hitung join kecil manual, tulis query, sengaja buat many-to-many, lalu buktikan perbaikannya.
