# Lesson 7 — Context Manager

## Problem, context, why

File/lock/connection harus dilepas walau operation di tengah gagal. Menaruh `close` hanya di akhir happy path menyebabkan leak.

## Intuisi dan mental model

Context manager seperti meminjam kunci: acquire sebelum masuk, selalu kembalikan saat keluar—normal atau exception.

```text
__enter__ / acquire
        ↓
with block/use
        ↓ normal atau exception
__exit__ / release
```

## Definition dan internal mechanism

Protocol `__enter__`/`__exit__` atau `contextlib.contextmanager` mengelola setup/cleanup. `__exit__` menerima exception info dan dapat menekan exception bila mengembalikan truthy—gunakan sangat hati-hati.

## Small example

```python
from contextlib import contextmanager

@contextmanager
def announced(name):
    print("open", name)
    try:
        yield name
    finally:
        print("close", name)
```

### Predict/run/observe/explain

Raise error di dalam `with`. Prediksi output dan apakah exception hilang. Expected: cleanup jalan, exception tetap propagate.

## Workplace application

File, database transaction, lock, temporary directory, tracing span, dan test fixtures memakai lifecycle pattern.

## Common failure dan debugging

Acquire partial lalu cleanup tidak aman, menekan exception tanpa alasan, resource dipakai setelah exit, atau context terlalu panjang. Test success dan failure path.

## Mini exercise/checkpoint

Buat context manager timer yang mencatat duration walau body gagal, tanpa menelan exception.

## Penutup

**KAMU BARU BELAJAR:** context manager menjamin acquire/use/release boundary.

**KENAPA INI PENTING:** cleanup harus bekerja pada failure path.

**DI DUNIA KERJA DIPAKAI UNTUK:** files, locks, transactions, temporary resources, dan observability.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** exception yang melewati context perlu taxonomy dan translation yang baik.
