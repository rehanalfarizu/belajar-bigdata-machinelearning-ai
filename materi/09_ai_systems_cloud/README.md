# Level 09 — AI Systems, Cloud, dan Governance

Level ini menghubungkan model dengan sistem nyata. Materinya bersifat vendor-neutral; setelah paham konsep, pilih AWS, Azure, atau GCP.

## Arsitektur sistem

Bedakan offline training, batch inference, online inference, feature store, vector store, API gateway, queue, cache, observability, dan human-in-the-loop. Pilih synchronous versus asynchronous berdasarkan latency dan reliability.

## Reliability

Gunakan timeout, retry dengan backoff dan jitter, circuit breaker, idempotency key, dead-letter queue, health/readiness probe, graceful degradation, dan rollback. Ukur SLI/SLO: latency, availability, error rate, freshness, dan kualitas model.

## Security

Terapkan least privilege IAM, secret manager, encryption in transit/at rest, network isolation, dependency scanning, signed artifact, input validation, redaction PII, audit trail, dan threat modeling. Jangan memasukkan secret ke notebook atau image.

## Cloud dan biaya

Pahami object storage, managed SQL, container service, Kubernetes, autoscaling, quota, region, egress, GPU utilization, dan FinOps. Pisahkan dev/staging/prod dan gunakan infrastructure as code agar perubahan dapat direview.

## Governance AI

Dokumentasikan intended use, out-of-scope use, data provenance, known limitations, fairness slices, privacy impact, model card, approval, dan incident response. Sistem yang akurat tetapi tidak aman bukan sistem produksi yang baik.

## Proyek akhir

Deploy API model dengan Docker, CI lint/test/build, registry, secret injection, health check, structured logging, dashboard latency, model version endpoint, dan rollback ke versi sebelumnya. Tambahkan threat model satu halaman.
