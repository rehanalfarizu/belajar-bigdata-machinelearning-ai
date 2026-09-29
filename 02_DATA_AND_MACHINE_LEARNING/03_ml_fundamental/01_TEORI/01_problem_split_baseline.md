# Lesson 01 — Problem, Split, dan Baseline

## Why

ML diperlukan ketika rule manual tidak cukup tetapi historical examples mengandung signal. Sebelum model, definisikan prediction unit, target, decision time, horizon, dan cost kesalahan.

Train adalah latihan; validation memilih pendekatan; test adalah ujian independen. Split harus meniru penggunaan: random untuk IID, temporal untuk masa depan, group untuk entity baru. Preprocessing hanya fit pada train.

Baseline memberi minimum pembanding: mean/median untuk regression, majority/prior/simple rule untuk classification. Tanpa baseline, kompleksitas tidak memiliki justification.

## Failure dan evidence

Target leakage, preprocessing sebelum split, duplicate entity lintas split, dan tuning pada test membuat metric optimistis. Audit feature availability at decision time dan provenance setiap transform.

## Checkpoint

Definisikan unit/target/time/cost, pilih split dengan alasan, buat baseline, dan tulis bukti bahwa test belum memengaruhi keputusan.
