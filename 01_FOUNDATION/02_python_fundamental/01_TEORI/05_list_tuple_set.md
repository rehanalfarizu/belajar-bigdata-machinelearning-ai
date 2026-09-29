# Lesson 5 — List, Tuple, dan Set

## Problem, context, why

Kamu perlu menyimpan banyak reading. Apakah urutan penting? Apakah isi boleh berubah? Apakah duplicate harus dipertahankan? Jawaban ini menentukan collection yang tepat.

## Intuisi dan mental model

- list: daftar berurutan yang dapat berubah;
- tuple: record/sequence berurutan yang tidak dapat diubah in-place;
- set: kumpulan unique items untuk membership/operasi himpunan.

## Definition dan internal mechanism

List dan tuple adalah sequences dengan index mulai 0 dan slicing. List mutable: append/update mengubah object. Tuple immutable: elemennya tidak dapat diganti, meskipun object mutable di dalamnya masih dapat berubah. Set tidak menjanjikan urutan semantic dan memerlukan elements hashable.

## Small manual example

```python
readings = [20.1, 20.4]
alias = readings
alias.append(20.8)
print(readings)
```

### Predict → run → observe → explain

Expected: list asli juga terlihat berubah karena `alias` dan `readings` menunjuk object sama. Bandingkan dengan `copy = readings.copy()`.

## Hands-on experiment

Trace append, slice copy, membership, dedup dengan set, dan urutan hasil. Jangan memakai set bila duplicate/order memiliki makna, misalnya event stream.

## Workplace application

List untuk batch ordered, tuple untuk coordinate/return record sederhana, set untuk IDs seen/permissions/tags. Pemilihan collection menyatakan invariant.

## Common failure dan debugging

Aliasing mutable, index error, mengubah list saat iterasi, mengira set sorted, dan kehilangan duplicate saat dedup. Inspect `id`, length, sample, dan invariants sebelum/after.

## Mini exercise dan checkpoint

Diberi readings dengan duplicates dan timestamp order, tentukan collection untuk raw events, unique sensor IDs, dan coordinate. Jelaskan trade-off.

## Penutup

**KAMU BARU BELAJAR:** collection dipilih dari order, mutability, duplicate, dan lookup behavior.

**KENAPA INI PENTING:** representation yang salah menghapus informasi.

**DI DUNIA KERJA DIPAKAI UNTUK:** batches, records, dedup keys, permissions, dan features.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** saat item perlu diakses berdasarkan nama/key, dictionary memberi mapping.
