# Lab 06 — Decorator

## 1. TUJUAN
Membungkus behavior fungsi sambil mempertahankan contract dan metadata.

## 2. PREREQUISITE
Baca lesson 06.

## 3. SETUP
Buat decorator `trace_calls` yang mencetak nama fungsi dan durasi.

## 4. PREDICTION BEFORE RUN
Prediksi urutan decoration time dan call time serta nilai `function.__name__`.

## 5. LANGKAH PRAKTIKUM
Ketik closure wrapper, aplikasikan ke dua fungsi, lalu tambahkan `functools.wraps`.

## 6. OBSERVATION
Catat metadata dan return value sebelum/sesudah `wraps`.

## 7. WHY
Decorator mengganti reference fungsi dengan wrapper; `wraps` menyalin metadata penting.

## 8. MODIFICATION
Buat decorator factory dengan label; tumpuk dua decorator dan prediksi urutannya.

## 9. FAILURE EXPERIMENT
Lupa mengembalikan hasil fungsi asli atau wrapper hanya menerima nol argument.

## 10. DEBUGGING
Bandingkan signature/return, gunakan `*args, **kwargs` dengan bijak, tambah test behavior dan metadata.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada auth, retry, metrics, caching, route registration, dan tracing.

## 12. CHECKPOINT
Buat decorator parameterized yang transparan terhadap hasil fungsi dan jelaskan trade-off magic versus reuse.
