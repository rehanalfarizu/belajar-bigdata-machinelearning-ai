# Level 07 — Big Data dan Data Engineering

Level ini melengkapi roadmap dengan materi yang belum ada di enam chapter awal. Fokusnya bukan memakai Spark secara membabi buta, tetapi memahami kapan database, Pandas, Polars, atau distributed engine menjadi pilihan yang tepat.

## 1. Model penyimpanan

Data warehouse cocok untuk query analitik terstruktur; data lake menyimpan data mentah dalam object storage; lakehouse menambahkan transaksi, schema, dan governance di atas lake. Format columnar seperti Parquet membaca kolom yang diperlukan dan mendukung compression. Partition berdasarkan kolom yang sering difilter, tetapi hindari terlalu banyak small files.

## 2. Batch pipeline

Pipeline yang baik memiliki ingest, schema validation, cleaning, transform, quality checks, publish, dan observability. Ia idempotent: dijalankan dua kali tidak menggandakan hasil. Gunakan watermark/incremental load untuk menghindari scan seluruh sumber.

## 3. PySpark

Spark DataFrame adalah tabel terdistribusi dengan schema. Transformation bersifat lazy; action menjalankan execution plan. Shuffle pada join/groupBy dapat mahal. Gunakan filter awal, pilih kolom yang perlu, partition yang masuk akal, broadcast join untuk tabel kecil, dan `explain()` untuk melihat plan.

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("sales-etl").getOrCreate()
orders = spark.read.parquet("data/orders")
customers = spark.read.parquet("data/customers")
result = (orders.filter(F.col("amount") > 0)
          .join(F.broadcast(customers.select("customer_id", "segment")), "customer_id")
          .groupBy("segment")
          .agg(F.sum("amount").alias("revenue")))
result.explain()
result.write.mode("overwrite").parquet("artifacts/revenue_by_segment")
```

## 4. SQL dan kualitas data

Kuasai star schema, slowly changing dimension, CTE, window function, query plan, index, constraints, dan data contract. Quality checks minimal: schema, nullability, uniqueness, referential integrity, range, freshness, dan volume anomaly.

## 5. Streaming

Kafka menyimpan event dalam topic yang dibagi menjadi partition. Consumer group membagi beban; offset menentukan posisi baca. Exactly-once sulit dan mahal—pahami at-least-once, idempotent sink, duplicate event, event time, processing time, watermark, dan late data.

## 6. Orchestration dan warehouse

Airflow/Prefect mengatur DAG, dependency, retry, backfill, schedule, dan observability. dbt mengubah data melalui SQL yang teruji. Warehouse memisahkan storage/compute dan membutuhkan biaya-aware query. Jangan mengirim seluruh data ke Python jika filter/aggregate dapat dilakukan engine.

## Proyek akhir

Bangun pipeline CSV → quality checks → Parquet partitioned → Spark aggregate → tabel analitik. Sertakan schema, sample data, test kualitas, job log, retry strategy, dan perbandingan waktu Pandas versus Spark.
