# Lesson 12 — File I/O

## Problem, context, why

Program perlu membaca sensor log dan menyimpan summary. File dapat hilang, encoding salah, JSON invalid, disk penuh, atau write terputus. I/O bukan sekadar `open`.

## Intuisi dan mental model

File adalah resource eksternal. Process meminta handle, melakukan read/write, lalu wajib melepaskannya. Context manager seperti petugas yang memastikan pintu ditutup walau terjadi error.

## Definition dan internal mechanism

`open` mengembalikan file object. Mode `r/w/a` menentukan behavior; `w` dapat menimpa file. Text mode melakukan encoding/decoding; binary mode memberi bytes. `with` memanggil enter/exit sehingga close terjadi saat block selesai atau exception.

## Small manual example

```python
from pathlib import Path
import json

path = Path("event.json")
with path.open(encoding="utf-8") as handle:
    event = json.load(handle)
```

### Predict → run → observe → explain

Prediksi failure untuk missing file, invalid JSON, dan wrong encoding. Bedakan filesystem error dari parse/schema error.

## Hands-on experiment

Buat temporary JSON valid, JSON syntax invalid, dan JSON valid tetapi field `value` bertipe string. Catat lapisan mana yang mendeteksi tiap failure.

## Workplace application

Dipakai untuk config, dataset, model metadata, logs, dan export. Raw input sebaiknya tidak ditimpa; output critical dapat ditulis temporary lalu diganti atomically bila requirement mendukung.

## Common failure dan debugging

Wrong cwd, destructive `w`, handle tidak ditutup, membaca file besar sekaligus, encoding mismatch, dan menganggap valid JSON sama dengan valid schema. Inspect path/size/encoding/sample aman sebelum transform.

## Mini exercise dan checkpoint

Baca JSON Lines satu baris demi satu, hitung valid/invalid, dan simpan invalid line number tanpa menghentikan seluruh file. Jangan beri full solution; rancang contract dulu.

## Penutup

**KAMU BARU BELAJAR:** I/O memiliki acquisition, operation, validation, cleanup, dan failure layers.

**KENAPA INI PENTING:** data/config/model masuk melalui boundary eksternal.

**DI DUNIA KERJA DIPAKAI UNTUK:** ingestion, config, artifacts, logs, dan reports.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** saat code membesar, behavior file/parser dipisah ke module; Lesson 13 membahas import.
