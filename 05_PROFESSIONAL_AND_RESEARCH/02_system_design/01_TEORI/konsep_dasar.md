# System Design dari Requirement ke Evidence

Mulai dengan actor/use case, scale, latency, availability, durability, consistency, privacy/safety, cost, dan growth. Bedakan hard requirement dari preference. Buat capacity estimate: requests/events per second, payload, storage/retention, read/write ratio, burst, dan recovery load.

API contract mencakup identity, schema, validation, versioning, pagination, idempotency, errors, auth, dan rate limit. Data model mengikuti access pattern dan invariants. Partitioning memberi scale tetapi menciptakan hot key/cross-partition cost. Cache mengurangi latency tetapi menambah staleness/invalidation. Queue memisahkan producer/consumer tetapi menambah duplicate/order/backlog semantics.

Distributed transaction sering diganti workflow dengan idempotency, outbox, saga/compensation, atau reconciliation. Tentukan source of truth dan acceptable consistency per operation. Availability memerlukan timeout, bounded retry, circuit breaking, backpressure, load shedding, redundancy, backup/restore, dan tested failover.

Observability berasal dari user journey dan SLO: metric, structured log, trace, audit, alert, dashboard, runbook. Design harus menyertakan security boundaries, capacity/cost, deployment/migration, compatibility, and rollback. Diagram tanpa trade-off dan failure behavior belum menjadi design.
