# Lesson 4 — Type Hints

## Problem, context, why

Function menerima “readings”, tetapi reviewer tidak tahu element type, no-data behavior, atau return shape. Bug baru ditemukan saat runtime jauh dari sumber mismatch.

## Intuisi dan mental model

Type hint adalah peta kontrak untuk manusia dan static tooling. Peta tidak membangun pagar runtime.

## Definition dan internal mechanism

Annotations disimpan sebagai metadata dan umumnya tidak memvalidasi runtime. Gunakan concrete types, `Sequence`/`Iterable` sesuai kebutuhan, `Optional`/`| None` hanya bila absence sah, dan protocol/interface untuk behavior. Return type memaksa keputusan error/no-data terlihat.

## Small example

```python
from collections.abc import Iterable

def mean(values: Iterable[float]) -> float:
    collected = list(values)
    if not collected:
        raise ValueError("no values")
    return sum(collected) / len(collected)
```

### Predict/run/observe/explain

Panggil dengan list angka dan list string. Observe bahwa Python runtime tetap mencoba. Jelaskan perbedaan static feedback, runtime validation, dan tests.

## Workplace application

Hints membantu IDE, review, refactor, library API, dan CI type checker bila dipasang. Boundary eksternal tetap harus divalidasi.

## Common failure dan debugging

`Any` menyebar, optional tanpa handling, hint terlalu spesifik, serta menganggap annotation sebagai security/data validation. Periksa contract dari caller dan actual runtime sample.

## Mini exercise/checkpoint

Tambahkan hints ke parser event, termasuk failure contract. Jelaskan mengapa `dict` saja kurang informatif.

## Penutup

**KAMU BARU BELAJAR:** type hints menyatakan intent statis; runtime tetap membutuhkan validation.

**KENAPA INI PENTING:** contract eksplisit mempercepat review dan refactor.

**DI DUNIA KERJA DIPAKAI UNTUK:** package APIs, IDE, CI checks, dan collaboration.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Iterable pada hint memiliki protocol runtime; Lesson 5 membedakan iterable, iterator, dan generator.
