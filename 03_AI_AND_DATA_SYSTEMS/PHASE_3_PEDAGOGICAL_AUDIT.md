# Phase 3 Pedagogical Audit

Tanggal audit: 29 September 2026. Phase 2 gate telah PASS sebelum audit ini dimulai.

## Kondisi awal

Phase 3 memiliki 37 file pada lima chapter. Computer Vision hanya empat file dan teori sembilan baris; NLP, Big Data, dan AI Systems memiliki ringkasan/reference tetapi tanpa lab; MLOps memiliki satu notebook dan teori 598 baris. Month 3 hanya satu halaman deliverable tanpa milestone.

## Gap lintas chapter

| Area | Evidence | Risiko | Keputusan |
|---|---|---|---|
| Teori | summary 9–45 baris atau monolit 598 baris | lompat konsep atau cognitive overload | sequential lessons problem→mechanism→failure |
| Lab | hanya MLOps memiliki notebook | tidak ada executable system evidence | add visual/script/SQL/service/tests |
| CV split | disebut, tidak diuji | adjacent video-frame leakage | mandatory group/time leakage lab |
| NLP | Transformer/RAG terlalu dekat entrypoint | foundation/retrieval mechanism lemah | text→BoW→TF-IDF→embedding→sequence→attention→RAG |
| Big Data | konsep tanpa runnable raw→Parquet path | notebook mindset | local DuckDB/Parquet default, optional Spark/Kafka |
| MLOps | monolit+notebook | notebook menjadi source of truth | `src/tests/configs/api/Dockerfile/pyproject/docs` lab |
| AI systems | mostly design text | failure handling tidak dialami | executable dependency/timeout/retry/idempotency/incident |
| Assessment | CV saja checkpoint; no broken/project ladders | gate tidak terbukti | all chapters full practice path |
| Project/roadmap | Month 3 no milestones; Week 10–13 one row | integration unclear | 8+ milestones and daily roadmap |

## Chapter findings

- **Computer Vision:** perlu pixel/RGB/normalization/convolution manual, augmentation assumptions, classification→detection→segmentation→tracking overview, metrics/shift/OOD/abstention/latency.
- **NLP:** perlu manual attention, separate retrieval/generation evaluation, chunking/privacy/prompt injection/structured output/cost/latency/guardrails.
- **Big Data:** perlu partition/columnar/small files/shuffle/skew/lazy plus event time/watermark/backpressure/idempotency/replay/schema evolution.
- **MLOps:** perlu runnable package/service/container boundaries, tracking/versioning, monitoring/drift, shadow/canary/rollback.
- **AI Systems:** perlu API/worker/queue/cache/database boundary dan incident loop detect→diagnose→mitigate→recover→prevent.

## Constraints

Default labs harus lokal dan ringan. Kafka/Spark/MLflow/Docker execution dapat menjadi optional environment; core semantics tetap dibuktikan oleh simulator standard-library. Heavy infrastructure tidak dijalankan di CI default.

## Audit decision

**NOT READY** sebelum implementation. Tidak ada blocker struktur; lanjut ke plan.
