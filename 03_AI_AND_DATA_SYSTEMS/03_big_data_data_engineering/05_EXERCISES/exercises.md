# Praktikum Level 07

## Latihan 1 — SQL

Buat tabel `customers`, `orders`, dan `order_items` di DuckDB. Tulis query untuk revenue harian, top-3 customer per bulan dengan `ROW_NUMBER`, dan customer tanpa order. Verifikasi grain setiap hasil.

## Latihan 2 — Parquet

Baca CSV, bersihkan duplicate ID, cast tanggal, tulis Parquet dengan partition tanggal, lalu bandingkan ukuran file dan waktu query CSV versus Parquet.

## Latihan 3 — Spark DataFrame

Jalankan contoh README. Tambahkan schema eksplisit, quality checks, `explain()`, dan broadcast join. Bandingkan hasil dengan query DuckDB.

## Latihan 4 — Fault tolerance

Simulasikan satu batch gagal setelah staging. Rancang cara retry tanpa menggandakan data. Jelaskan mengapa `mode('append')` polos berbahaya.

## Tantangan data engineering

Bangun ETL harian yang dapat diulang: input bertanggal, validasi, output partitioned, manifest run, dan laporan kualitas. Sertakan satu data rusak dan pastikan pipeline menolaknya dengan pesan yang dapat ditindaklanjuti.
