# Lesson 3 — Operator dan Expression

## Problem, context, why

`2 + 3 * 4` menghasilkan 14, bukan 20. `and` dan `or` bahkan dapat berhenti sebelum mengevaluasi operand berikutnya. Tanpa model expression, condition menjadi sulit dipercaya.

## Intuisi dan mental model

Expression adalah pohon operasi. Precedence menentukan cabang mana dievaluasi dulu; parentheses membuat intent eksplisit.

```text
2 + 3 * 4
    └─ 3*4 = 12
└───── 2+12 = 14
```

## Definition dan internal mechanism

Operator arithmetic (`+ - * / // % **`), comparison (`== != < <= > >=`), dan boolean (`and or not`) menghasilkan value sesuai operand. Comparison dapat dirantai. `and/or` memakai short-circuit: operand berikutnya hanya dievaluasi bila diperlukan.

`==` membandingkan equality; `is` membandingkan identity dan umumnya dipakai untuk `None`. Assignment `=` bukan comparison.

## Small manual example

```python
x = 0
safe = x != 0 and 10 / x > 2
```

### Predict → run → observe → explain

Prediksi apakah division dijalankan. Expected: tidak; kondisi pertama False membuat hasil `and` sudah diketahui.

## Hands-on experiment

Buat tabel untuk `a,b` pada `and`, `or`, `not`. Uji `7 // 3`, `7 % 3`, `-7 // 3`, dan `-7 % 3`. Jelaskan identity `dividend == divisor*(//) + (%)`.

## Workplace application

Operator membentuk validation, threshold, feature calculation, retry rule, dan access policy. Parentheses serta names sementara sering lebih aman daripada expression satu baris yang rumit.

## Common failure dan debugging

Salah precedence, pembagian nol, memakai `is` untuk number/string equality, atau short-circuit order yang salah. Pecah expression menjadi langkah bernama dan print/test intermediate values.

## Mini exercise dan checkpoint

Tulis rule: suhu valid hanya jika value ada, berupa angka, dan berada -50..150. Jelaskan evaluation order. Lulus bila dapat menggambar expression tree sederhana.

## Penutup

**KAMU BARU BELAJAR:** expression dievaluasi menurut precedence dan short-circuit.

**KENAPA INI PENTING:** decisions dan calculations bergantung pada urutan evaluasi benar.

**DI DUNIA KERJA DIPAKAI UNTUK:** validation, threshold, filtering, dan policy.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** text juga mendukung operasi khusus; Lesson 4 membahas string dan representation.
