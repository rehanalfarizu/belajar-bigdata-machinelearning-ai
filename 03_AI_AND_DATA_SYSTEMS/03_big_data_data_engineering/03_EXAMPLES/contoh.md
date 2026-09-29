# Panduan Kode Level 07

## Pandas versus Spark

Gunakan Pandas saat data muat di memori dan eksplorasi interaktif lebih penting. Gunakan Spark ketika data/komputasi melampaui satu mesin atau perlu integrasi cluster. Spark bukan otomatis lebih cepat untuk file kecil karena ada overhead startup.

## Anti-pattern utama

```python
# Buruk: mengambil seluruh tabel ke driver
rows = spark.read.parquet("data/events").collect()

# Lebih baik: filter dan aggregate secara terdistribusi
summary = (spark.read.parquet("data/events")
           .filter("event_date >= '2025-01-01'")
           .groupBy("event_type").count())
```

Jangan memakai `toPandas()` tanpa batas ukuran. Jangan melakukan Python UDF jika fungsi SQL bawaan tersedia karena optimizer tidak dapat mengoptimalkan UDF dengan baik. Validasi schema eksplisit untuk pipeline produksi; `inferSchema` cocok untuk eksperimen.

## Incremental dan idempotency

Gunakan `updated_at` atau offset sebagai watermark. Tulis ke staging, validasi, lalu publish atomik. Jika sink tidak mendukung transaksi, gunakan path versi dan pointer “latest”. Catat run ID, input range, row count, checksum, dan status.

## Observability

Log durasi setiap tahap, input/output rows, null rate, duplicate rate, partition count, dan error. Alert pada perubahan dibanding baseline, bukan hanya ketika job crash.
