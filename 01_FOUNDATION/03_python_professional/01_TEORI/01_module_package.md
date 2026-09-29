# Lesson 1 — Module dan Package

## Problem, context, why

Project mempunyai `app.py`, `utils.py`, dan copy-paste functions. Nama `utils` tidak menjelaskan ownership; imports mulai circular. Kita perlu boundary berdasarkan capability/domain.

## Intuisi dan mental model

Module adalah satu ruang bernama; package adalah kumpulan ruang yang menawarkan pintu publik.

```text
sensor_tool/
├── __init__.py      public surface
├── domain.py        invariant/logic
├── io.py            file boundary
└── cli.py           user boundary
```

## Definition dan internal mechanism

Module adalah object hasil eksekusi file Python. Package mengelompokkan modules dalam namespace. Import resolution memakai interpreter environment dan search path; relative import hanya bermakna dalam package. `__init__.py` dapat menandai package dan mengekspor public names, tetapi jangan memberi side effects berat.

## Small example

Buat package minimal dan import `sensor_tool.domain`. Prediksi kapan top-level print muncul, inspect `module.__file__`, lalu import lagi. Observe cache `sys.modules`.

### Predict → run → observe → explain

Tulis dulu urutan output import pertama dan kedua. Jalankan dari project root, amati module path/cache, lalu jelaskan mengapa top-level code tidak dieksekusi ulang pada import biasa dalam process yang sama.

## Workplace application

Boundaries membantu code ownership, testing, API stability, dan dependency direction. Domain sebaiknya tidak bergantung pada CLI/framework.

## Common failure dan debugging

Circular import, module menutupi stdlib, running file internal sebagai script, missing package root, dan public API bocor. Inspect dependency graph, executable, cwd, `sys.path`, dan `__file__`.

## Mini exercise/checkpoint

Pecah Sensor Log CLI menjadi `domain`, `io`, dan `cli`; gambar arah dependency. Lulus bila import domain tidak menjalankan I/O.

## Penutup

**KAMU BARU BELAJAR:** package adalah namespace dan boundary, bukan sekadar folder.

**KENAPA INI PENTING:** dependency yang jelas mengurangi circularity dan memudahkan test.

**DI DUNIA KERJA DIPAKAI UNTUK:** shared library, services, CLI, dan deployment artifact.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** di dalam domain package, object dan composition membantu menempatkan state/behavior.
