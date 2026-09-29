# Tutorial Penyelesaian — Level 09 AI Systems, Cloud, dan Governance

## Rancang sebelum deploy

Tulis kontrak sistem: siapa pengguna, input/output, latency target, availability, data sensitif, failure mode, biaya, dan siapa yang dapat melakukan rollback. Arsitektur adalah jawaban terhadap kebutuhan ini, bukan kumpulan layanan cloud.

## Checklist endpoint produksi

1. Authentication dan authorization least privilege.
2. Schema/range/size validation pada request.
3. Timeout, rate limit, retry terbatas, dan idempotency untuk operasi tulis.
4. `/health` untuk proses dan `/ready` untuk dependency penting.
5. Structured logging tanpa secret/PII.
6. Metric latency p50/p95, error rate, traffic, serta versi model.
7. Alert yang memiliki runbook dan pemilik.

## Deployment aman

Build image deterministik, scan dependency, gunakan tag immutable, deploy ke staging, jalankan smoke test, lalu promote bertahap. Simpan konfigurasi/secrets di secret manager atau environment yang aman; jangan di Git.

## Incident response

Saat error meningkat, hentikan dampak dulu: rollback/circuit-break, catat request ID dan versi model, lalu periksa perubahan terakhir. Jangan retrain model sebagai reaksi otomatis. Setelah pulih, tulis postmortem: dampak, timeline, akar penyebab, tindakan pencegahan, dan owner.

## Governance AI

Buat model card: tujuan, data provenance, metrik per kelompok relevan, batasan, misuse yang diperkirakan, privasi, serta proses eskalasi. Sistem yang akurat namun membocorkan data tetap gagal.
