# Lesson 13 — Async / Await

## Problem, context, why

Program menunggu banyak network responses satu per satu. CPU menganggur selama I/O, tetapi membuat thread/process untuk setiap request juga memiliki overhead.

## Intuisi dan mental model

Satu koki dapat menaruh beberapa panci saat menunggu air mendidih, selama tiap pekerjaan rela menyerahkan kontrol. Async adalah cooperative scheduling, bukan parallel CPU magic.

```text
event loop
├── run task A sampai await
├── run task B sampai await
├── I/O A ready → resume A
└── cancellation/timeout juga bagian contract
```

## Definition dan internal mechanism

`async def` menghasilkan coroutine saat dipanggil. Event loop menjalankan tasks; `await` memberi kesempatan task lain saat menunggu awaitable. Blocking call di event loop memblokir semua tasks. Async cocok untuk high-concurrency I/O, bukan otomatis mempercepat CPU-bound work.

## Small example

```python
import asyncio

async def job(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    results = await asyncio.gather(job("a", 0.1), job("b", 0.1))
    print(results)

asyncio.run(main())
```

### Predict/run/observe/explain

Prediksi total waktu sequential vs gather. Observe order result dan completion. Ganti `asyncio.sleep` dengan blocking sleep dan jelaskan perubahan.

## Workplace application

Async digunakan server I/O, network clients, dan concurrent polling. Timeout, cancellation, bounded concurrency, cleanup, dan backpressure wajib didesain.

## Common failure dan debugging

Coroutine tidak di-await, blocking call di loop, task exception tidak diobservasi, unlimited gather, cancellation tertelan, dan shared state race. Aktifkan debug/log task identity dan kecilkan concurrency.

## Mini exercise/checkpoint

Rancang async fetch simulator dengan semaphore limit, timeout, dan per-item result/error tanpa internet.

## Penutup

**KAMU BARU BELAJAR:** async menginterleave cooperative I/O tasks pada event loop.

**KENAPA INI PENTING:** waiting dapat dimanfaatkan tanpa thread per task.

**DI DUNIA KERJA DIPAKAI UNTUK:** APIs, clients, polling, dan I/O services.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** async adalah satu bentuk concurrency; Lesson 14 membandingkan task, thread, process, race, dan coordination.
