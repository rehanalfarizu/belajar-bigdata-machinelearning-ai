# Mini-Project — Sensor Log CLI

## Problem

Sebuah file JSON Lines berisi readings sensor. Buat CLI yang memvalidasi setiap line, menghitung summary, dan melaporkan invalid input tanpa berhenti pada error pertama.

## Input contract

Setiap valid event memiliki `sensor_id` string nonempty, `value` angka finite, `unit` yang didukung, dan timestamp text. Pada chapter ini timestamp cukup dipertahankan sebagai text; parsing waktu profesional dibahas kemudian.

## Milestones

1. Parse satu JSON line menjadi dictionary.
2. Validasi required keys, type, dan range.
3. Ubah parsing/validation menjadi functions.
4. Proses banyak lines secara incremental.
5. Hitung accepted/rejected dan per-sensor summary.
6. Pisahkan module domain dari CLI.
7. Tambah arguments input/output dan `--help`.
8. Gunakan stderr/exit code untuk failure file-level.
9. Tambah tests manual atau automated untuk empty, malformed, wrong type, dan no-valid-data.
10. Dokumentasikan run command, sample, assumptions, dan limitations.

## Constraints

Gunakan standard library. Jangan menyimpan semua lines bila tidak perlu. Jangan mengubah raw input. Jangan memberi full solution dari awal; setiap milestone harus runnable sebelum lanjut.

## Acceptance criteria

Valid dan invalid events dapat dibedakan; satu bad line tidak menghapus good lines; no-data memiliki behavior eksplisit; module dapat diimport tanpa menjalankan CLI; hasil dapat diulang dari README.
