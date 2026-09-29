# Lesson 2 — Type dan Value

## Problem, context, why

Input terminal `"21"` terlihat seperti angka, tetapi `"21" + 1` gagal. Python tidak menilai dari penampilan; setiap object memiliki type yang menentukan operation valid.

## Intuisi dan mental model

Value adalah isi bermakna; type adalah aturan penggunaan. Label botol saja tidak mengubah air menjadi minyak.

```text
object
├── identity
├── type → operasi/behavior yang tersedia
└── value
```

## Definition dan internal mechanism

Type umum: `int`, `float`, `str`, `bool`, dan `NoneType`. Python dynamic typing berarti name dapat menunjuk object type berbeda; bukan berarti type tidak ada. Conversion seperti `int("21")` membuat value baru atau gagal bila representation invalid.

`bool` memiliki `True/False`. `None` berarti tidak ada value yang bermakna pada contract tertentu; bukan nol atau string kosong. Float merepresentasikan bilangan secara terbatas sehingga beberapa decimal tidak exact.

## Small manual example

```python
age_text = "21"
age = int(age_text)
next_age = age + 1
```

### Predict → run → observe → explain

Prediksi `type(age_text)`, `type(age)`, dan hasil `0.1 + 0.2 == 0.3`. Jalankan. Jelaskan conversion dan keterbatasan float, bukan menyebut Python “salah hitung”.

## Hands-on experiment

Coba conversion untuk `"21"`, `"21.5"`, `"abc"`, `""`, dan `None`. Catat success/exception, lalu tulis validation policy input umur.

## Workplace application

API/data parser harus memvalidasi type, missingness, range, unit, dan semantic meaning. Casting buta dapat mengubah data rusak menjadi hasil menyesatkan.

## Common failure dan debugging

- `TypeError`: operation tidak mendukung kombinasi type.
- `ValueError`: conversion memahami target type tetapi representation invalid.
- `None` mengalir terlalu jauh: validasi dekat boundary.
- compare float exact: gunakan tolerance bila sesuai.

## Mini exercise dan checkpoint

Buat table input→desired type→valid range→error message untuk umur, suhu, dan sensor ID. Lulus bila dapat menjelaskan dynamic typing tanpa mengatakan “variable tidak punya type sama sekali”.

## Penutup

**KAMU BARU BELAJAR:** object memiliki type dan value; conversion adalah operation yang dapat gagal.

**KENAPA INI PENTING:** correctness dimulai dari representation dan validation.

**DI DUNIA KERJA DIPAKAI UNTUK:** parsing form/API/CSV/config dan menjaga data contract.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** operator menggabungkan values sesuai aturan type; itu fokus Lesson 3.
