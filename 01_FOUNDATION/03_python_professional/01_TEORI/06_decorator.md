# Lesson 6 — Decorator

## Problem, context, why

Beberapa functions perlu timing atau authorization check. Copy-paste wrapper logic menghasilkan inkonsistensi, tetapi decorator yang berlebihan menyembunyikan control flow.

## Intuisi dan mental model

Function adalah object. Decorator menerima function dan mengembalikan function lain yang membungkus behavior.

```text
original function
    ↓ passed to decorator at definition/import time
wrapper function
    ↓ called later
before → original(*args, **kwargs) → after
```

## Definition dan internal mechanism

Syntax `@decorator` setara dengan `func = decorator(func)`. Closure menyimpan reference ke original. `functools.wraps` mempertahankan name/doc/metadata penting untuk debug/tooling.

## Small example

```python
from functools import wraps

def traced(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("start", function.__name__)
        return function(*args, **kwargs)
    return wrapper
```

### Predict/run/observe/explain

Prediksi kapan decorator dieksekusi vs wrapper dipanggil. Inspect `__name__` dengan/tanpa `wraps`.

## Workplace application

Decorator dapat menangani tracing, metrics, retry policy terbatas, atau authorization pada framework. Business decision utama sebaiknya tetap terlihat.

## Common failure dan debugging

Metadata hilang, exception tertelan, retry non-idempotent, wrapper signature terlalu generik, dan urutan decorator membingungkan. Unwrap dan test original/wrapper behavior terpisah.

## Mini exercise/checkpoint

Buat decorator penghitung call tanpa mengubah return/exception. Jelaskan thread-safety limitation state counter.

## Penutup

**KAMU BARU BELAJAR:** decorator melakukan higher-order wrapping pada definition time.

**KENAPA INI PENTING:** cross-cutting behavior dapat direuse tetapi control flow harus tetap observable.

**DI DUNIA KERJA DIPAKAI UNTUK:** metrics, tracing, framework routes, dan policies.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** resource lifecycle lebih tepat memakai context manager daripada decorator umum.
