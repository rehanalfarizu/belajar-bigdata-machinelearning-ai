# Tutorial Penyelesaian — Level 07 Big Data dan Data Engineering

## Mulai dari SQL, bukan cluster

Untuk setiap pertanyaan bisnis, tulis grain hasil: “satu baris per apa?” Baru pilih tabel, join key, filter, dan agregasi. Setelah join, cek row count agar many-to-many join tidak menggandakan revenue.

```sql
WITH daily AS (
  SELECT order_date, COUNT(DISTINCT order_id) AS orders, SUM(amount) AS revenue
  FROM orders
  WHERE amount >= 0
  GROUP BY order_date
)
SELECT * FROM daily ORDER BY order_date;
```

## Langkah ETL PySpark

1. Baca schema eksplisit dan tampilkan sample.
2. Validasi required column, tipe, null, duplicate, serta range.
3. Bersihkan dengan aturan yang dapat dijelaskan.
4. Aggregate dan cek `explain()`.
5. Tulis output partitioned serta manifest run.
6. Jalankan ulang input yang sama untuk membuktikan idempotency.

Hindari `collect()` dan `toPandas()` pada data besar. Jika job lambat, cari shuffle, skew key, file kecil, atau join besar sebelum menambah worker.

## Streaming

Definisikan event key, event time, ordering expectation, deduplication key, offset, dan sink idempotent. Gunakan dead-letter path untuk event rusak. “Exactly once” harus dibuktikan pada seluruh pipeline, bukan hanya consumer Kafka.

## Deliverable proyek

Sertakan data contract, diagram aliran, log row count, test kualitas, strategi backfill/retry, dan biaya/latency perkiraan.
