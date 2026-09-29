# Teori dan Solusi Lengkap — Level 07 Big Data dan Data Engineering

## 1. Kapan data disebut “besar”?

Data besar bukan angka baris tertentu. Ia menjadi masalah ketika data tidak muat di memori, query terlambat, update terus masuk, atau reliability satu mesin tidak cukup. Solusinya bukan selalu Spark: database/warehouse bisa lebih efektif untuk query SQL, Polars/Pandas untuk data satu mesin, dan Spark untuk kerja terdistribusi yang benar-benar memerlukannya.

## 2. Solusi SQL revenue harian

Tentukan grain: satu baris output per hari. Filter data invalid sebelum agregasi, gunakan `COUNT(DISTINCT order_id)` jika satu order dapat memiliki beberapa item.

```sql
WITH valid_orders AS (
    SELECT order_id, CAST(order_date AS DATE) AS order_date, amount
    FROM orders
    WHERE amount >= 0 AND order_date IS NOT NULL
)
SELECT order_date,
       COUNT(DISTINCT order_id) AS total_orders,
       SUM(amount) AS revenue,
       AVG(amount) AS avg_order_value
FROM valid_orders
GROUP BY order_date
ORDER BY order_date;
```

Setelah join, cek count sebelum dan sesudah. Bila revenue tiba-tiba berlipat, mungkin join many-to-many menggandakan order.

## 3. Solusi batch PySpark yang dapat diulang

```python
from pyspark.sql import SparkSession, functions as F, types as T

schema = T.StructType([
    T.StructField("order_id", T.StringType(), False),
    T.StructField("order_date", T.DateType(), False),
    T.StructField("amount", T.DoubleType(), False),
])
spark = SparkSession.builder.appName("daily-sales").getOrCreate()
raw = spark.read.schema(schema).option("header", True).csv("data/orders.csv")
clean = raw.dropDuplicates(["order_id"]).filter(F.col("amount") >= 0)
daily = clean.groupBy("order_date").agg(F.sum("amount").alias("revenue"))
daily.write.mode("overwrite").partitionBy("order_date").parquet("artifacts/daily_sales")
```

`mode("overwrite")` di path output yang spesifik membuat rerun input yang sama tidak menduplikasi output. Untuk production, gunakan staging/versioned path dan publish atomik agar pembaca tidak melihat hasil setengah jadi.

## 4. Partition, shuffle, dan skew

Partition memungkinkan worker memproses subset data. `groupBy`, join, distinct, dan order dapat menyebabkan shuffle: data dipindahkan antar worker. Filter/pilih kolom sebelum shuffle, broadcast tabel kecil, dan cek key sangat dominan (skew). `cache()` hanya berguna jika dataset yang sama dipakai berulang kali dan memori cukup.

## 5. Streaming dan kualitas

Event bisa duplicate, terlambat, atau out-of-order. Simpan event ID, event time, ingest time, offset, dan reason bila ditolak. Data contract minimal memeriksa schema, null, unique key, range, freshness, dan volume. Pipeline tanpa quality check hanya memindahkan kesalahan lebih cepat.
