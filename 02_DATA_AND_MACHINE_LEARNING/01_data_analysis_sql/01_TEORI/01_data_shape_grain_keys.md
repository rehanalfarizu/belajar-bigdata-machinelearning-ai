# Lesson 01 — Data Shape, Grain, Schema, dan Key

## Problem dan context

Satu baris bertuliskan `asset-7, 75, 08:00` belum bermakna sebelum kita tahu apakah baris mewakili sensor reading, ringkasan harian, atau maintenance event. Pertanyaan pertama bukan “chart apa?”, melainkan “satu baris mewakili apa?”

## Why dan mental model

**Grain** adalah arti satu row. Variable adalah sifat yang diukur; observation adalah kejadian/entity pada grain tersebut. Schema menyatakan nama, type, nullable, unit, dan constraint. Primary key mengidentifikasi row secara unik; foreign key menghubungkan entity.

Tanpa grain/key, duplicate tidak dapat didefinisikan dan join dapat menggandakan nilai. Sebelum database relasional, data sering disimpan sebagai file besar berulang; normalisasi mengurangi duplication dan update inconsistency, tetapi membuat JOIN diperlukan.

## Manual example

`readings(event_id, asset_id, time, value)` memiliki grain “satu sensor event”. `assets(asset_id, site)` memiliki grain “satu asset”. Jika `assets` berisi dua row untuk satu `asset_id`, join bukan lagi many-to-one.

Precondition: business question dan entity dipahami. Action: nyatakan grain/key/schema. Postcondition: uniqueness dan relationship dapat diuji.

## Alternatives dan trade-off

Wide table mudah dibaca tetapi berulang; normalized tables konsisten tetapi memerlukan join. Natural key mudah dipahami tetapi dapat berubah; surrogate key stabil tetapi perlu constraint business key.

## Failure, debugging, evidence

Gejala: total naik setelah join. Periksa row count, uniqueness setiap key, unmatched keys, dan cardinality sebelum/after. Evidence benar: assertion key unik dan reconciliation total.

## Workplace dan checkpoint

Ini muncul pada analytics contract, warehouse modelling, API event, dan feature table. Dari tiga tabel kecil, tulis grain, candidate key, relationship, dan satu assertion sebelum membaca lesson berikutnya.
