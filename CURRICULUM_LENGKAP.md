# Kurikulum Lengkap: Data, AI, Big Data, dan Sistem Produksi

Dokumen ini adalah peta utama repository. Setiap tahap memiliki **teori**, **praktik**, **problem solving**, dan **proyek**. Jangan mengukur kemajuan dari banyaknya notebook yang dijalankan; ukur dari kemampuan menjelaskan keputusan dan membangun ulang solusi dari file kosong.

## Kontrak belajar yang konsisten

Untuk setiap topik, gunakan urutan berikut:

1. **Konsep** — definisi, asumsi, intuisi, dan batasan.
2. **Matematika/algoritme** — rumus atau langkah komputasinya.
3. **Implementasi minimal** — tulis versi sederhana tanpa framework.
4. **Implementasi produksi** — gunakan library, validasi input, logging, dan test.
5. **Eksperimen** — ubah satu parameter dan catat sebab-akibat.
6. **Evaluasi** — gunakan metrik yang sesuai dan analisis error.
7. **Proyek** — selesaikan masalah baru dengan dokumentasi.

Template catatan setiap eksperimen:

```text
Pertanyaan: apa yang ingin diketahui?
Hipotesis: perubahan apa yang diperkirakan terjadi dan mengapa?
Perubahan tunggal: parameter/fitur/data yang diubah.
Metrik: definisi, baseline, hasil.
Error case: contoh prediksi yang salah dan penyebabnya.
Keputusan: eksperimen berikutnya.
```

## Jalur inti (wajib)

| Fase | Teori utama | Praktik wajib | Bukti lulus |
|---|---|---|---|
| 0. Komputer & Git | shell, file system, proses, Git, environment | membuat repo, branch, commit, membaca diff | dapat memulihkan perubahan dan menjelaskan error environment |
| 1. Python | tipe, kontrol alur, fungsi, class, exception, modul, testing | 20 latihan typing + program CLI kecil | 80% test lulus tanpa menyalin solusi |
| 2. Matematika & statistik | aljabar linear, kalkulus, probabilitas, inferensi | NumPy dari nol, simulasi distribusi, CI, uji hipotesis | dapat menjelaskan mean, variance, gradient, dan korelasi |
| 3. Data analysis | SQL, NumPy, Pandas, cleaning, EDA, visualisasi | analisis CSV multi-tabel | 5 insight yang didukung grafik dan query |
| 4. ML fundamental | supervised/unsupervised, split, leakage, baseline, metrik | pipeline regresi, klasifikasi, clustering | test set tidak dipakai untuk tuning |
| 5. ML advanced | feature engineering, CV, tuning, ensemble, imbalance, time series | eksperimen terukur dan error analysis | model dibandingkan dengan baseline dan confidence interval |
| 6. Deep learning | tensor, forward/backprop, optimizer, regularisasi, CNN, sequence | MLP, CNN, LSTM, transfer learning | dapat membaca kurva learning dan memperbaiki overfitting |
| 7. Big Data engineering | storage, partition, distributed execution, Spark, streaming | batch ETL PySpark + quality checks | pipeline idempotent dan dapat diulang |
| 8. NLP & generative AI | tokenisasi, embedding, attention, Transformer, RAG | klasifikasi teks + semantic search + RAG kecil | evaluasi retrieval dan jawaban secara terpisah |
| 9. MLOps & cloud | packaging, API, Docker, registry, CI/CD, monitoring, security | deploy pipeline, logging, drift alert | model dapat diulang, dipantau, dan di-rollback |
| 10. Digital twin | IoT, state estimation, simulasi, anomaly, safety | simulasi aset + telemetry + what-if | twin dipisahkan dari plant dan memiliki quality/safety guard |

## Fase 0 — Fondasi komputer dan software engineering

Pahami proses versus thread, path relatif versus absolut, permission, environment variable, HTTP, JSON, dan Git (`status`, `diff`, `log`, `branch`, `merge`). Praktiknya: buat CLI `dataset-info`, tambahkan `argparse`, logging, konfigurasi environment, unit test, dan README cara menjalankan.

Kriteria: kamu dapat membaca `ModuleNotFoundError`, `PermissionError`, dan `FileNotFoundError`, lalu memperbaiki akar masalahnya tanpa mengganti kode secara acak.

## Fase 1 — Python dan quality

Pelajari object model, mutability, iterables, generator, context manager, decorator, type hints, dataclass, exception design, packaging, dan testing. Gunakan `ruff`, `pytest`, dan `mypy` sebagai kebiasaan engineering, bukan hanya setelah kode selesai.

Praktik bertahap: kalkulator CLI → parser CSV → cache decorator → pipeline fungsi → package kecil dengan test unit dan test integrasi.

## Fase 2 — Matematika, statistik, dan eksperimen

### Aljabar linear

Vektor adalah titik/fitur, matriks adalah transformasi atau kumpulan observasi, dan tensor adalah generalisasi multi-dimensi. Kuasai dot product, norma, proyeksi, rank, eigenvector, SVD, dan kondisi numerik. Dalam ML, `X @ w` adalah kombinasi linear; PCA memakai arah variance terbesar dari dekomposisi matriks.

### Kalkulus dan optimisasi

Turunan mengukur perubahan lokal. Gradient adalah kumpulan turunan terhadap parameter. Gradient descent memperbarui `theta <- theta - learning_rate * gradient`; learning rate terlalu besar membuat divergen, terlalu kecil membuat lambat. Pelajari convex versus non-convex, momentum, Adam, dan regularisasi.

### Probabilitas dan statistik

Pahami random variable, expectation, variance, conditional probability, Bayes, sampling, confidence interval, hypothesis test, p-value, effect size, power, bootstrap, dan multiple testing. Bedakan korelasi dari sebab-akibat.

Praktik: implementasikan mean/variance/linear regression dengan NumPy, simulasi Central Limit Theorem, bootstrap confidence interval, A/B test sederhana, dan laporan asumsi. Jangan menulis “p-value kecil berarti hipotesis benar”.

## Fase 3 — Data analysis dan SQL

Pelajari grain tabel, primary/foreign key, normalisasi, `JOIN`, `GROUP BY`, `HAVING`, CTE, window function, query plan, dan indeks. Setelah itu gunakan Pandas hanya untuk eksplorasi/transformasi yang sesuai skala; data besar perlu SQL engine atau Spark.

Praktik: buat database DuckDB/SQLite dari tiga CSV, validasi jumlah baris setelah join, hitung cohort/retention dengan window function, lalu cocokkan hasil SQL dengan Pandas.

## Fase 4–5 — Machine learning

Selalu mulai dari baseline sederhana. Pisahkan train/validation/test; semua transformer yang belajar dari data harus `fit` hanya pada train dan berada di dalam `Pipeline`. Pilih metrik dari biaya kesalahan bisnis. Untuk kelas timpang, accuracy dapat menipu; gunakan precision-recall, calibration, dan threshold tuning.

Topik teori: bias-variance, regularisasi L1/L2, probabilistic classification, tree impurity, bagging, boosting, calibration, interpretability, missingness mechanism, causal leakage, cross-validation untuk time series, dan uncertainty.

Proyek: churn, fraud, demand forecasting, atau ranking. Laporan wajib memuat baseline, split, feature provenance, eksperimen, error slices, dan batasan.

## Fase 6 — Deep learning

Pelajari tensor shapes, initialization, activation, loss, backpropagation, SGD/Adam, batch normalization, dropout, augmentation, transfer learning, dan mixed precision. CNN cocok untuk struktur spasial; RNN/Transformer untuk urutan. Jangan menambah layer sebelum memahami apakah masalahnya underfitting, overfitting, data, atau label.

Gunakan notebook Level 5 yang sudah diperbaiki, lalu praktikkan satu eksperimen perubahan per run. Simpan seed, dataset split, konfigurasi, dan history training.

## Fase 7 — Big Data dan data engineering

### Konsep inti

Big Data bukan sekadar file besar. Masalah utamanya adalah volume, velocity, variety, biaya pemindahan data, reliability, dan koordinasi worker. Pahami object storage, data lake, warehouse, lakehouse, schema-on-read/write, partitioning, columnar format (Parquet), compression, small-files problem, dan data quality.

### Spark

Spark memecah pekerjaan menjadi transformations (lazy) dan actions. DataFrame memiliki schema; Catalyst optimizer menyusun execution plan; shuffle adalah operasi mahal saat data berpindah antar-partition. Pelajari `select`, `filter`, `join`, `groupBy`, window, `repartition`, `cache`, broadcast join, checkpoint, dan Structured Streaming.

Praktik minimal:

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("sales-etl").getOrCreate()
sales = spark.read.option("header", True).option("inferSchema", True).csv("data/sales.csv")
clean = (sales.dropDuplicates(["order_id"])
               .filter(F.col("amount") >= 0)
               .withColumn("order_date", F.to_date("order_date")))
daily = (clean.groupBy("order_date")
               .agg(F.sum("amount").alias("revenue"), F.countDistinct("order_id").alias("orders")))
daily.write.mode("overwrite").partitionBy("order_date").parquet("artifacts/daily_sales")
```

Uji: hitung row count sebelum/sesudah deduplication, cek null dan schema, bandingkan satu sampel dengan Pandas, lalu jalankan ulang dan pastikan hasil sama (idempotent).

### Streaming, orchestration, warehouse

Pelajari Kafka topic/partition/offset/consumer group, at-least-once versus exactly-once, watermark dan late events. Pelajari Airflow/Prefect DAG, retry, backfill, observability, serta warehouse star schema dan dbt. Data contract harus memeriksa schema, freshness, uniqueness, dan range sebelum model memakai data.

## Fase 8 — NLP, Transformer, dan generative AI

Tokenisasi mengubah teks menjadi token; embedding memetakan token menjadi vektor; self-attention menghitung hubungan query-key-value; Transformer memakai positional information dan residual connection. Bedakan pretraining, fine-tuning, instruction tuning, dan retrieval augmented generation.

Praktik berurutan:

1. TF-IDF + Logistic Regression untuk sentiment baseline.
2. Embedding dan cosine similarity untuk semantic search.
3. Fine-tuning classifier kecil dengan split berbasis dokumen (hindari duplikasi antar split).
4. RAG: chunk → embed → retrieve → rerank → prompt → citation. Evaluasi retrieval recall dan kualitas jawaban secara terpisah.

Risiko wajib: prompt injection, data leakage, PII, hallucination, copyright, biaya token, dan evaluasi yang tidak representatif.

## Fase 9 — MLOps, cloud, dan keamanan

Model adalah artefak yang bergantung pada kode, data, dependency, konfigurasi, dan hardware. Simpan pipeline utuh, metadata, hash dataset, metric, dan schema input. API harus memvalidasi tipe/range, memiliki `/health`, timeout, logging tanpa PII, dan versioning.

Pelajari Docker image layers, registry, CI (lint/test/build), CD (deploy/rollback), secrets manager, least privilege, model monitoring, data/concept drift, alert fatigue, dan retraining approval. Di cloud, pahami object storage, managed database, container service/Kubernetes, IAM, network boundary, cost/quotas, dan disaster recovery.

## Portofolio akhir

Bangun satu sistem end-to-end: ingest data → quality checks → feature pipeline → baseline/model → evaluation → registry → API/batch inference → dashboard metrics → drift alert → rollback. Sertakan diagram arsitektur, threat model, biaya perkiraan, runbook insiden, dan keputusan trade-off.

Untuk jalur industrial/IoT, lanjutkan dengan Digital Twin: model satu aset, schema telemetry, state estimator, residual anomaly, skenario what-if, dan human-approved control. Materi tersedia di `materi/10_digital_twin`.

## Definisi “expert”

Expert bukan hafal semua library. Expert mampu memilih abstraksi yang tepat, mengukur ketidakpastian, menemukan leakage, menjelaskan trade-off latency/accuracy/cost, menguji sistem, dan menolak solusi yang tidak aman atau tidak dapat dipelihara.
