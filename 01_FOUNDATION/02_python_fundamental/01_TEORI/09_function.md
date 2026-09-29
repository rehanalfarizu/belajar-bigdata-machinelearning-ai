# Lesson 9 — Function

## Problem, context, why

Calculation yang sama tersebar di lima tempat. Ketika rule berubah, satu copy terlupa. Function memberi nama pada behavior dan membuat contract input→output.

## Intuisi dan mental model

Function seperti mesin kecil: parameter adalah input ports, body adalah mechanism, return adalah output. `print` bukan return; output layar berbeda dari value untuk caller.

## Definition dan internal mechanism

`def` membuat function object dan mengikat name. Call mengevaluasi arguments, membuat local frame, bind parameters, menjalankan body, lalu mengembalikan value. Tanpa `return` eksplisit, hasilnya `None`. Default argument dievaluasi saat function didefinisikan—hindari default mutable.

## Small manual example

```python
def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("below absolute zero")
    return celsius + 273.15
```

### Predict → run → observe → explain

Prediksi hasil 0, -273.15, dan -300. Bedakan validation error dari result. Trace parameter/local state.

## Hands-on experiment

Buat versi yang `print` hasil tetapi tidak return; coba pakai hasilnya dalam calculation. Observe `NoneType` failure dan jelaskan contract.

## Workplace application

Function memisahkan parsing, validation, domain calculation, dan formatting agar dapat diuji. Function kecil bukan tujuan sendiri; boundary dan naming harus mengikuti responsibility.

## Common failure dan debugging

Lupa return, mutable default, terlalu banyak responsibilities, positional arguments tertukar, dan side effect tersembunyi. Inspect signature, inputs, return, exception, dan state eksternal yang berubah.

## Mini exercise dan checkpoint

Tulis function summary readings yang menerima list dan mengembalikan dictionary count/min/max/mean atau failure terdefinisi untuk no valid data.

## Penutup

**KAMU BARU BELAJAR:** function memiliki parameters, local frame, return, dan failure contract.

**KENAPA INI PENTING:** behavior reusable/testable membutuhkan boundary jelas.

**DI DUNIA KERJA DIPAKAI UNTUK:** domain logic, validation, transformations, dan service handlers.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** local frame memperkenalkan scope; Lesson 10 menjelaskan bagaimana names dicari.
