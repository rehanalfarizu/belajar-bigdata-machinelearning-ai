# Lesson 4 — String

## Problem, context, why

Data nama, path, log, CSV, URL, dan JSON tiba sebagai text. Jika string diperlakukan seperti “sekadar huruf”, whitespace, encoding, case, dan format dapat merusak comparison atau parsing.

## Intuisi dan mental model

String adalah sequence karakter Unicode yang immutable. Operasi “mengubah” string membuat string baru.

```text
" sensor-01 "
 indices: 0 ... 10
strip() → "sensor-01" (object baru)
split("-") → ["sensor", "01"]
```

## Definition dan internal mechanism

`str` menyimpan text Unicode. Index/slice memilih bagian; batas `stop` tidak termasuk. Method seperti `strip`, `lower`, `replace`, dan `split` mengembalikan value baru. Encoding mengubah text menjadi bytes; decoding sebaliknya.

## Small manual example

```python
raw = "  Sensor-01,27.5 C  "
clean = raw.strip()
sensor, reading = clean.split(",", maxsplit=1)
print(sensor.lower(), reading)
```

### Predict → run → observe → explain

Prediksi apakah `raw` berubah. Expected: tidak; `clean` menunjuk string baru. Trace value setelah setiap transformasi.

## Hands-on experiment

Uji input dengan spaces, comma tambahan, karakter Indonesia, dan string kosong. Bedakan formatting untuk manusia dari representation machine-readable.

## Workplace application

Dipakai untuk cleaning identifiers, parsing logs/config, membangun messages, dan validation API. Jangan membangun SQL/shell command dari concatenation input tidak tepercaya.

## Common failure dan debugging

Index out of range, split menghasilkan jumlah bagian tak terduga, case/whitespace mismatch, serta bytes/string confusion. Gunakan `repr(value)` untuk melihat whitespace tersembunyi dan inspect encoding boundary.

## Mini exercise dan checkpoint

Parse `"motor-07 | 82.4 | C"` menjadi tiga field tervalidasi tanpa menghilangkan makna unit. Lulus bila dapat menjelaskan immutability dan slice stop.

## Penutup

**KAMU BARU BELAJAR:** string adalah sequence Unicode immutable dan parsing membutuhkan contract.

**KENAPA INI PENTING:** banyak boundary sistem adalah text.

**DI DUNIA KERJA DIPAKAI UNTUK:** log, path, config, HTTP, CSV, dan identifiers.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** satu string tidak cukup untuk banyak item; Lesson 5 membandingkan list, tuple, dan set.
