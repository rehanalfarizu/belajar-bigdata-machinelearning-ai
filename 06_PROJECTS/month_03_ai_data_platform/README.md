# Month 3 — AI Data Platform

## Context

Jadikan satu model vision/NLP sebagai layanan yang menerima data tervalidasi dari pipeline dan dapat dioperasikan saat dependency sebagian gagal.

## Deliverables

- versioned API/schema, inference service, batch/stream input boundary;
- container/config/secrets separation;
- unit dan integration tests;
- metrics/logs/traces, dashboard/alerts, health/readiness;
- deployment, canary/rollback, data/model monitoring, dan runbook.

## Acceptance criteria

Duplicate/retry tidak menggandakan effect; incompatible schema ditolak; timeout/backpressure bounded; model/data version terlacak; alert actionable; service masuk degraded mode yang didefinisikan; rollback diuji.

## Evidence

Sertakan architecture diagram, capacity estimate, load/failure-test results, security boundary, cost assumptions, operational demo, dan postmortem dari satu injected incident.
