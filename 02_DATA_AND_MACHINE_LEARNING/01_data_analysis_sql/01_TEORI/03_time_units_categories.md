# Lesson 03 — Dirty String, Unit, Timestamp, dan Timezone

## Problem

`"OK"`, `" ok "`, dan `"Okay"` dapat berarti sama; 75°C dan 75°F tidak sama; `08:00` tanpa timezone tidak menunjuk instant global yang pasti.

## Why dan how

Normalisasi string menghapus variasi representasi, bukan variasi makna. Unit conversion memerlukan source unit yang eksplisit. Timestamp perlu parsing, timezone localization bila asalnya naive, lalu conversion ke standard seperti UTC.

Urutan aman: preserve raw → trim/case map dengan dictionary → parse value → convert unit → parse/localize time → validate range/category.

## Manual example

75°F menjadi `(75-32)×5/9 = 23.89°C`. `2026-01-01 08:00 Asia/Jakarta` adalah `01:00 UTC`. Jangan menempel `+00:00` tanpa conversion karena itu mengubah arti instant.

## Assumptions dan alternatives

Mapping category mengasumsikan synonym diketahui. Unit dapat dinormalisasi saat ingestion atau query; ingestion memberi consistency, query menjaga raw flexibility. Simpan keduanya bila lineage penting.

## Failure/debugging/evidence

Bandingkan distribution sebelum/sesudah, unknown categories, source-unit count, parse failure, dan min/max UTC. Uji daylight-saving untuk zona relevan.

## Workplace dan checkpoint

Dipakai pada IoT, finance cutoff, log correlation, dan multi-site analytics. Konversi tiga record manual, buat satu timezone failure, lalu jelaskan perbaikannya.
