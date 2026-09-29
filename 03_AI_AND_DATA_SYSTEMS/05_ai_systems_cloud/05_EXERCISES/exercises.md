# Praktikum Level 09

## Latihan 1 — API contract

Definisikan request/response schema, validasi nilai di luar range, dan tulis test untuk 200, 400, 422, timeout, serta model failure.

## Latihan 2 — Reliability

Tambahkan retry terbatas dengan exponential backoff, idempotency key, dan dead-letter simulation. Jelaskan mengapa retry tanpa batas memperburuk outage.

## Latihan 3 — Monitoring

Catat latency p50/p95, error rate, input null rate, dan prediksi per kelas. Buat alert hanya setelah baseline dan threshold disepakati.

## Tantangan deployment

Containerize API, jalankan CI lokal (`lint`, `compile`, `pytest`, image build), deploy ke environment staging, uji health/readiness, lalu lakukan rollback. Tulis runbook ketika model menghasilkan output tidak valid.
