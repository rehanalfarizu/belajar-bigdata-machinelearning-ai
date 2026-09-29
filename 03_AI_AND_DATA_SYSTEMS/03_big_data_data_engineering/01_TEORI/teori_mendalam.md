# Teori Mendalam — Level 07: Big Data dan Data Engineering

## 1. Scale, reliability, dan layout data

Data engineering mengubah event/data sumber menjadi dataset yang reliable untuk analitik dan produk. Volume, velocity, variety, veracity, dan cost adalah aspek scale. File besar tidak otomatis memerlukan cluster; distributed system menambah network, serialization, scheduling, failure, dan operasi. Gunakan engine paling sederhana yang memenuhi kebutuhan.

Row format cocok untuk transaksi point lookup; columnar format seperti Parquet cocok untuk scan analitik karena hanya kolom perlu yang dibaca dan compression efektif. Partition membantu pruning, tetapi cardinality tinggi membuat banyak file/partition kecil. Schema evolution perlu aturan kompatibilitas; schema-on-read fleksibel tetapi dapat memindahkan error ke waktu query, schema-on-write memberi kontrol lebih awal.

## 2. Distributed processing dan Spark

Spark membagi data menjadi partition dan menjalankan task dekat data bila mungkin. Transformation bersifat lazy sehingga optimizer dapat menyusun plan; action memicu eksekusi. Narrow transformation tidak membutuhkan perpindahan data besar, sedangkan wide transformation/shuffle seperti groupBy/join/distinct memindahkan data antar executor dan sering menjadi bottleneck. `explain()` membantu melihat plan, tetapi harus dibaca bersama volume/skew actual.

Broadcast join mengirim tabel kecil ke worker untuk menghindari shuffle tabel besar. Data skew terjadi ketika satu key memiliki jauh lebih banyak data sehingga satu task menjadi lambat. Repartition menambah/mengatur partition dengan shuffle, coalesce mengurangi partition lebih ringan. Cache hanya berguna bila dataset dipakai ulang dan tidak menekan memory executor.

## 3. Data correctness

Pipeline benar bukan hanya “job sukses”. Definisikan contract: schema, unique key, referential integrity, null/range, freshness, volume, dan semantic rule. Idempotent berarti rerun input sama menghasilkan state akhir sama. Incremental load membutuhkan watermark/offset, deduplication key, late data policy, dan backfill strategy. Raw immutable layer memudahkan audit/reprocess; curated layer menyediakan data siap pakai.

## 4. Streaming dan warehouse

Event stream memiliki event time dan processing/ingest time. Event dapat duplicate, terlambat, out-of-order, atau hilang. Consumer offset, idempotent sink, watermark, window, dan dead-letter queue adalah bagian desain correctness. Exactly-once adalah properti end-to-end yang mahal, bukan checkbox broker.

Warehouse mengoptimalkan query analitik. Star schema memisahkan fact (event terukur) dan dimension (konteks), sehingga grain fact harus jelas. dbt/SQL transformation, orchestration, lineage, test, dan documentation membuat transformasi dapat dipercaya. Cost governance penting: scan data, concurrency, storage tier, dan egress dapat lebih mahal daripada compute model.
