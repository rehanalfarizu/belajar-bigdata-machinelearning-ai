# Lesson 10 — Scope

## Problem, context, why

Function mengubah list global secara tak sengaja, atau variable di dalam function tidak tersedia di luar. Scope dan mutability sering tercampur dalam diagnosis.

## Intuisi dan mental model

Setiap function call memiliki meja kerja lokal. Jika name tidak ada, Python mencari ke ruang luar menurut aturan LEGB: Local, Enclosing, Global, Built-ins.

## Definition dan internal mechanism

Scope menentukan tempat name binding dapat ditemukan. Assignment di function biasanya membuat local name. `global`/`nonlocal` mengubah binding target tetapi sebaiknya dipakai terbatas. Object mutable dapat diubah melalui reference tanpa rebinding name, sehingga caller melihat mutation.

## Small manual example

```python
items = ["a"]

def add_item(values):
    values.append("b")
    local_count = len(values)
    return local_count

count = add_item(items)
```

### Predict → run → observe → explain

Prediksi `items`, `count`, dan apakah `local_count` tersedia global. Jelaskan object mutation vs local name.

## Hands-on experiment

Bandingkan `values.append` dengan `values = values + ["b"]`. Inspect `id` sebelum/sesudah. Tentukan contract apakah function mutates input atau returns new.

## Workplace application

Scope membantu mencegah shared mutable state, flaky tests, dan request leakage pada service. Dependency/config sebaiknya eksplisit, bukan diambil diam-diam dari global.

## Common failure dan debugging

`UnboundLocalError` karena assignment membuat name lokal, shadowing built-in, mutation tak terduga, dan notebook global state. Restart kernel dan pass dependency eksplisit untuk menguji.

## Mini exercise dan checkpoint

Refactor function yang memakai global threshold menjadi parameter dengan default tervalidasi. Lulus bila dapat membedakan rebinding name dan mutating object.

## Penutup

**KAMU BARU BELAJAR:** scope mengatur name lookup; mutability mengatur apakah shared object berubah.

**KENAPA INI PENTING:** hidden state membuat code sulit diuji.

**DI DUNIA KERJA DIPAKAI UNTUK:** service isolation, tests, reusable functions, dan configuration.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** ketika contract function gagal, exception menyampaikan failure; Lesson 11 membahasnya.
