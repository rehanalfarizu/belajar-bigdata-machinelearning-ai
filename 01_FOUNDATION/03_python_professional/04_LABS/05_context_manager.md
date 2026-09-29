# Lab 05 — Context Manager

## 1. TUJUAN
Menjamin acquire/use/release pada jalur sukses dan gagal.

## 2. PREREQUISITE
Baca lesson 07.

## 3. SETUP
Ketik context manager `measured` dengan `contextlib.contextmanager` dan log start/finish.

## 4. PREDICTION BEFORE RUN
Prediksi urutan output normal dan ketika body mengangkat exception.

## 5. LANGKAH PRAKTIKUM
Jalankan dua jalur, letakkan cleanup dalam `finally`, lalu buat class context manager ekuivalen.

## 6. OBSERVATION
Catat urutan `__enter__`, body, `__exit__`, dan propagasi exception.

## 7. WHY
Context manager mengikat lifecycle resource ke block sehingga cleanup deterministik.

## 8. MODIFICATION
Tambahkan pilihan menelan hanya exception custom; jelaskan konsekuensinya.

## 9. FAILURE EXPERIMENT
Pindahkan cleanup setelah `yield` tanpa `finally` dan buat body gagal.

## 10. DEBUGGING
Buktikan cleanup hilang, kembalikan `try/finally`, dan assertion bahwa resource selalu released.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada file, transaction, lock, tracing span, dan koneksi.

## 12. CHECKPOINT
Buat context manager resource palsu yang bersih di dua jalur dan jelaskan trade-off suppressing exception.
