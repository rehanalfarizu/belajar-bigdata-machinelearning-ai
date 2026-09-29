# Lesson 6 — Dictionary

## Problem, context, why

List `["motor-1", 82.4, "C"]` tidak menjelaskan arti tiap posisi. Dictionary memberi nama field: `{"sensor_id": "motor-1", "value": 82.4, "unit": "C"}`.

## Intuisi dan mental model

Dictionary seperti lemari berlabel: key memilih slot, value adalah isi. Key unik dan harus hashable.

```text
event
├── "sensor_id" → "motor-1"
├── "value"     → 82.4
└── "unit"      → "C"
```

## Definition dan internal mechanism

`dict` adalah mapping key→value. Lookup rata-rata cepat melalui hash table. Assignment pada key lama mengganti value; key hilang melalui `[]` memunculkan `KeyError`, sementara `get` dapat memberi default. Nested dictionary merepresentasikan struktur, tetapi terlalu dalam membuat validation sulit.

## Small manual example

```python
event = {"sensor_id": "motor-1", "value": 82.4}
unit = event.get("unit", "unknown")
event["unit"] = "C"
```

### Predict → run → observe → explain

Prediksi value `unit` dan state `event` setelah assignment. Default dari `get` tidak otomatis menambahkan key.

## Hands-on experiment

Iterasi `keys`, `values`, dan `items`. Uji duplicate literal key, missing key, serta shallow copy dengan nested value.

## Workplace application

Dictionary umum untuk JSON-like records, configuration, lookup table, aggregation count, dan intermediate data. Production boundary tetap membutuhkan schema/validation; key ada belum menjamin type/unit benar.

## Common failure dan debugging

Key typo, default menyembunyikan data wajib, nested aliasing, dan mencampur records dengan schema berbeda. Print keys dan gunakan explicit validation dekat input.

## Mini exercise dan checkpoint

Buat frequency table quality values tanpa `Counter`. Lulus bila dapat memilih antara `[]`, `get`, dan membership check berdasarkan contract.

## Penutup

**KAMU BARU BELAJAR:** dictionary memetakan key unik ke value dan cocok untuk named fields/lookup.

**KENAPA INI PENTING:** data systems membawa records dengan field bermakna.

**DI DUNIA KERJA DIPAKAI UNTUK:** JSON, config, aggregations, indexes, dan messages.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** setelah state direpresentasikan, program perlu memilih behavior; Lesson 7 membahas condition.
