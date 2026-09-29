# Lesson 13 — Module dan Import

## Problem, context, why

Satu file berisi CLI, parsing, calculation, dan formatting menjadi sulit diuji. Copy-paste function ke file lain menimbulkan versi berbeda. Module memungkinkan reuse melalui namespace.

## Intuisi dan mental model

File Python adalah module. Import seperti membuka toolbox bernama, bukan menempelkan semua alat tanpa identitas.

```text
project/
├── app.py          imports sensor.py
└── sensor.py       defines parse_event(), summarize()

import sensor
sensor.summarize(...)
```

## Definition dan internal mechanism

Saat import pertama, Python mencari module pada import path, membuat module object, mengeksekusi top-level code, lalu cache di `sys.modules`. Karena top-level dieksekusi, side effect import harus diminimalkan. Guard `if __name__ == "__main__"` memisahkan execution entrypoint dari importable definitions.

## Small manual example

```python
# sensor.py
def normalize(value):
    return float(value)

# app.py
import sensor
print(sensor.normalize("27.5"))
```

### Predict → run → observe → explain

Tambahkan print top-level pada `sensor.py`. Prediksi kapan ia muncul. Jelaskan mengapa import bukan sekadar text include.

## Hands-on experiment

Jalankan `app.py` dari dua cwd dan inspect `sys.path`. Jangan memperbaiki import dengan random path mutation; pahami project root dan entrypoint.

## Workplace application

Modules memisahkan domain logic, adapters, CLI, dan tests. Public names/namespaces membuat ownership dan reuse lebih jelas.

## Common failure dan debugging

`ModuleNotFoundError` karena interpreter/cwd/package path, circular imports karena responsibilities saling bergantung, module name menutupi stdlib, dan side effects saat import. Inspect executable, cwd, `sys.path`, dan module `__file__`.

## Mini exercise dan checkpoint

Pecah script parser menjadi `parser.py` dan `app.py`; buktikan parser dapat diimport tanpa menjalankan CLI.

## Penutup

**KAMU BARU BELAJAR:** module adalah namespace executable yang dicari melalui import system dan di-cache.

**KENAPA INI PENTING:** reuse dan testability memerlukan boundaries.

**DI DUNIA KERJA DIPAKAI UNTUK:** project structure, shared utilities, domain modules, dan test imports.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Lesson 14 menyatukan input, domain functions, output, dan exit code menjadi CLI.
