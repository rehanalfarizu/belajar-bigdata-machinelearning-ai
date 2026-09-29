# Phase 3 Implementation Plan

## Outcome

Mengubah model/notebook menjadi data dan AI system yang dapat digunakan, diuji, diobservasi, masuk degraded mode, dan dipulihkan.

## Stage 1 — Computer Vision

Lesson representation→convolution→model tasks→transfer/evaluation→shift/latency/OOD. Visual experiments memakai generated local images. Group-aware video-frame leakage menjadi mandatory failure.

## Stage 2 — NLP & Transformers

Text/token→BoW/TF-IDF→embedding/sequence→manual Q/K/V attention→Transformer/pretrained→retrieval/RAG→LLM application safety. Retrieval dan generation metrics dipisah.

## Stage 3 — Big Data & Data Engineering

Local runnable raw→validation→Parquet→processing→analytics; partition/columnar/shuffle/skew/lazy. Lightweight broker simulator menjadi default streaming path; Kafka lab optional. Event contract, watermark, replay, idempotency, and schema evolution diuji.

## Stage 4 — MLOps

Engineering workspace dengan `src/`, `tests/`, `configs/`, `api/`, `Dockerfile`, `pyproject.toml`, `docs/`. Training/inference/version metadata, FastAPI boundary, Docker/CI, monitoring/drift, shadow/canary/rollback.

## Stage 5 — AI Systems & Cloud

Executable API/service/worker/queue/cache/database-boundary simulator. Failure experiments: dependency down, latency spike, bad config, schema break, model timeout. Setiap incident memakai detect→diagnose→mitigate→recover→prevent.

## Cross-phase artifacts

- sequential chapter maps;
- labs with 12-section contract;
- exercises, Level 1–5 reasoning, broken cases, mini-project, checkpoint;
- Month 3 milestone ladder;
- Week 10–13 daily roadmap;
- expanded audit/CI and Phase 3 test suite.

## Gate

PASS hanya jika local/lightweight system path executable, service/pipeline tests lulus, lab/navigation contract bersih, incident recovery dibuktikan, dan heavy optional paths diberi explicit prerequisites/limitations.
