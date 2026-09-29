# Exercises — Python Fundamental

Gunakan pola prediksi→run→observe→explain. Jangan buka `99_SOLUTIONS` sebelum mencoba minimal 20–30 menit.

## Level 1 — Trace dan recall

1. Trace names/values pada lima assignments dan satu rebinding.
2. Prediksi type/result delapan expressions, termasuk conversion gagal.
3. Tentukan output slicing string/list dan boundaries.
4. Trace condition dan loop state per iteration.

## Level 2 — Apply

1. Parse satu line `sensor_id,value,unit` menjadi dictionary tervalidasi.
2. Hitung count/min/max/mean readings valid dan abaikan missing berdasarkan rule eksplisit.
3. Buat function conversion Celsius↔Kelvin dengan range validation.
4. Baca file JSON kecil dan keluarkan summary.

## Level 3 — Analyze

1. Jelaskan aliasing pada dua names yang menunjuk list sama.
2. Temukan boundary errors pada classification rule.
3. Bandingkan function yang print dengan function yang return.
4. Bedakan missing file, invalid JSON, dan valid JSON dengan schema salah.

## Level 4 — Design

1. Rancang module `sensor.py` dengan parse, validate, summarize tanpa I/O terminal.
2. Rancang CLI contract: arguments, input, output, stderr, exit codes, dan invalid cases.
3. Tentukan collections yang menjaga raw order, unique IDs, dan per-sensor aggregation.

## Level 5 — Debug / Workplace

Kerjakan minimal empat [broken cases](../07_DEBUGGING/broken_cases.md), termasuk import, empty list, invalid JSON, dan wrong type. Tulis prevention berupa test atau validation.
