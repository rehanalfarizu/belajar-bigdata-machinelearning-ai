# Lab 12 — Async I/O

## 1. TUJUAN
Mengamati cooperative scheduling, concurrency I/O, ordering, dan exception propagation.

## 2. PREREQUISITE
Baca lesson 13–14; gunakan `asyncio` standard library.

## 3. SETUP
Gunakan `delayed_name` pada `patterns_lab.py` sebagai referensi dan ketik eksperimen baru tiga task.

## 4. PREDICTION BEFORE RUN
Prediksi durasi sequential versus `gather` serta urutan hasil untuk delay berbeda.

## 5. LANGKAH PRAKTIKUM
Ukur kedua versi dengan `perf_counter`; log start/finish task dan bandingkan completion order dengan result order.

## 6. OBSERVATION
Catat durasi, interleaving, urutan selesai, dan urutan list hasil.

## 7. WHY
`await` memberi kesempatan task lain berjalan; concurrency I/O tidak otomatis mempercepat CPU-bound work.

## 8. MODIFICATION
Tambahkan timeout dan semaphore batas dua task; prediksi perubahan durasi.

## 9. FAILURE EXPERIMENT
Lupa `await` coroutine atau buat satu task mengangkat exception.

## 10. DEBUGGING
Identifikasi warning coroutine, inspeksi task/exception, tambah cleanup/cancellation, lalu verifikasi tidak ada task tertinggal.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada banyak request API, database async, crawler, dan service fan-out.

## 12. CHECKPOINT
Buktikan tiga operasi I/O concurrent, tangani satu failure, dan jelaskan trade-off throughput versus kompleksitas.
