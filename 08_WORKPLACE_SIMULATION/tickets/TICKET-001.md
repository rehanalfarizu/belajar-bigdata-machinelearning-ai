# TICKET-001 — Idempotent Telemetry Ingestion

## Context

Gateway mengirim ulang event ketika acknowledgment terlambat. Dashboard kadang menggandakan energy usage.

## Business requirement

Operator membutuhkan agregasi akurat tanpa kehilangan kemampuan replay.

## Acceptance criteria

- duplicate event tidak mengubah state/agregasi dua kali;
- conflict dengan ID sama tetapi payload berbeda terlihat dan diaudit;
- replay historical event version sama deterministik;
- behavior dan metrics terdokumentasi.

## Constraints

Producer lama tidak dapat diubah selama dua sprint. Throughput p95 saat burst 5.000 events/s. Raw events harus dipertahankan 90 hari.

## Existing system

HTTP gateway → queue → consumer → state store + hourly aggregate. Event memiliki `asset_id`, `timestamp`, dan optional `event_id`.

## Task

Klarifikasi requirement yang hilang, usulkan contract/migration, implement/test minimal safe change, dan tulis rollout/rollback plan. Jangan asumsikan “exactly once” tanpa mendefinisikan boundary.
