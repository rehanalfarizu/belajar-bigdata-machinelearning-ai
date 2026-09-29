# Lesson 1 — Program Execution dan Variable

## Problem, context, why

Saat melihat `total = price * quantity`, pemula sering membayangkan variable sebagai kotak tetap. Lalu bingung ketika nama dipasang ulang atau dua nama menunjuk list sama. Kita perlu model eksekusi sebelum menulis banyak syntax.

## Intuisi dan mental model

Variable Python lebih mirip label yang ditempelkan pada object.

```text
source statement → interpreter evaluasi expression → object/value → name binding

price = 10
quantity = 3
total = price * quantity

price ─────→ int(10)
quantity ──→ int(3)
total ─────→ int(30)
```

## Definition dan internal mechanism

Statement melakukan tindakan; expression menghasilkan value. Assignment mengevaluasi sisi kanan terlebih dahulu, lalu mengikat name di kiri ke object. Python mengeksekusi module top-to-bottom, kecuali flow control mengubah urutan. Nama belum ada menghasilkan `NameError`.

## Small manual example

Trace state setelah setiap baris:

```python
x = 2
y = x + 3
x = 10
print(x, y)
```

### Predict → run → observe → explain

Prediksi output sebelum menjalankan. Expected: `10 5`. `y` dihitung saat baris kedua; rebinding `x` tidak menghitung ulang `y`.

## Hands-on experiment

Tambahkan `print(id(x), id(y))`, lalu ubah urutan statement. Buat tabel baris→names→values. Jangan hanya menulis output; jelaskan kapan expression dievaluasi.

## Workplace application

State tracing dipakai saat membaca pipeline transformasi, request handling, model inference, dan debugging variable yang tertimpa.

## Common failure dan debugging

`NameError` berarti name tidak tersedia pada scope/urutan itu. Typo dan urutan eksekusi notebook sering menjadi sebab. Baca traceback, cek baris pertama yang memakai name, lalu trace bindings sebelumnya.

## Mini exercise dan checkpoint

Trace tanpa menjalankan: `a=4; b=a; a=a+1; c=a+b`. Apa `a,b,c`? Setelah menjawab, run dan jelaskan.

Lulus bila dapat membedakan source, statement, expression, object/value, dan name binding.

## Penutup

**KAMU BARU BELAJAR:** interpreter mengevaluasi expression dan mengikat names ke values.

**KENAPA INI PENTING:** semua program adalah perubahan state yang harus dapat ditelusuri.

**DI DUNIA KERJA DIPAKAI UNTUK:** membaca code path dan menemukan state salah.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** value memiliki type dan behavior; Lesson 2 menjelaskan mengapa `"2" + "3"` berbeda dari `2 + 3`.
