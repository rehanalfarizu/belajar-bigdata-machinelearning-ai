# Lesson 14 — Concurrency Mental Model

## Problem, context, why

Dua workers memperbarui counter dan hasil akhir lebih kecil dari jumlah events. Masing-masing code terlihat benar, tetapi operasi read→modify→write saling menyela.

## Intuisi dan mental model

Concurrency seperti dua orang mengedit papan tulis bersama. Walau masing-masing mengikuti langkah benar, urutan interleaving dapat menghilangkan update.

```text
counter = 0
Task A read 0
Task B read 0
Task A write 1
Task B write 1    expected 2, actual 1
```

## Definition dan internal mechanism

Concurrency adalah multiple tasks in progress; parallelism adalah simultaneous execution. Thread berbagi process memory; process umumnya memory terpisah dan berkomunikasi eksplisit; async tasks berbagi thread/event loop secara cooperative. Race condition membuat outcome bergantung timing. Lock, queue, immutability, partition ownership, dan idempotency adalah coordination options.

GIL pada CPython tidak membuat compound domain operations atomic dan tidak menghilangkan race. CPU-bound parallelism sering memakai processes/native code; pilih berdasarkan workload dan measurement.

## Small experiment

Gunakan [micro-lab](../04_LABS/README.md) untuk membandingkan sequential async waits dan shared-counter reasoning. Prediksi interleavings sebelum run.

### Predict → run → observe → explain

Tulis sedikitnya dua interleavings counter sebelum menjalankan eksperimen. Setelah run, bedakan outcome yang diamati dari seluruh outcome yang mungkin dan jelaskan invariant yang harus dijaga.

## Workplace application

Workers, web requests, schedulers, telemetry consumers, dan training pipelines semuanya menghadapi shared state, ordering, duplicate, cancellation, serta shutdown.

## Common failure dan debugging

Flaky timing, deadlock, unbounded queue, lost update, duplicate effects, cancellation leak, dan assuming exactly-once. Tambah task/event IDs, deterministic tests bila mungkin, dan invariant/reconciliation.

## Mini exercise/checkpoint

Pilih design untuk 1.000 files CPU-light I/O-heavy dan 8 CPU-heavy simulations. Jelaskan thread/process/async/queue trade-off; jangan jawab “async selalu cepat”.

## Penutup

**KAMU BARU BELAJAR:** concurrency membutuhkan ownership, coordination, cancellation, dan failure semantics.

**KENAPA INI PENTING:** timing membuat code benar secara lokal gagal secara sistem.

**DI DUNIA KERJA DIPAKAI UNTUK:** servers, consumers, workers, pipelines, dan simulations.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Math & Statistics memberi bahasa untuk data, perubahan, uncertainty, dan evidence yang diproses software ini.
