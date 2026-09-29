# Architecture, Semantics, dan Twin Graph

Production twin bukan satu database atau dashboard. Ia adalah sistem dengan boundaries, data contracts, identity, models, state, history, computation, decision, dan governance yang dapat berevolusi tanpa kehilangan makna.

```text
Physical sensor/actuator/asset
  → connectivity + edge validation/buffer
  → broker/stream + raw immutable log/DLQ
  → historian + twin state + registry/semantic graph
  → estimator/simulation/ML/what-if/optimization
  → API/dashboard/alert/recommendation
  → policy/approval → command gateway → physical
```

Control plane mengelola identity, schema/model version, config, access, deployment, audit, retention, backup, dan rollback. Data plane menangani telemetry, state, query, recommendation, dan command flow.

## Storage dan consistency

- Raw log/object store untuk replay, audit, dan backfill.
- Historian/time-series store untuk range query, aggregation, compression, dan retention.
- Twin state store untuk latest effective state, version, freshness, dan uncertainty.
- Semantic/graph store untuk entity relationships dan metadata.
- Model/artifact registry untuk lineage, evaluation, version, dan promotion state.

Gunakan idempotency dan optimistic versioning pada state update. Ordering per asset/partition sering cukup; global transaction lintas semua asset biasanya mahal. Event sourcing memudahkan replay tetapi projection migration dan storage cost harus dirancang.

## Scale, reliability, dan observability

```text
events/second = assets × sensors_per_asset × sample_rate
daily_bytes ≈ events/second × average_event_bytes × 86400
```

Tambahkan burst, replication, indexes, derived data, retention, dan recovery/replay load. Tentukan backpressure/drop policy. SLO bermakna meliputi ingestion availability, event-time lag, state freshness, rejected-event rate, estimator/model latency, recovery time, dan command decision latency. Trace `event_id` serta `state_version` end-to-end.

## Semantics dan graph

Schema menyatakan bentuk; semantic model menyatakan meaning; ontology memformalkan concepts, relationships, dan constraints. Pisahkan type dari instance, hierarchy dari causal/functional relationship, serta current relationship dari historical relationship. Setiap entity memerlukan stable ID, lifecycle, owner, effective time, model version, dan provenance.

Graph memungkinkan contextual query tetapi bukan physics simulator. Semantic consistency tidak membuktikan state accuracy. Rujukan dengan scope berbeda meliputi [ISO/IEC 30173](https://www.iso.org/standard/81442.html), [ISO 23247-1](https://www.iso.org/standard/75066.html), [OPC UA](https://opcfoundation.org/developer-tools/specifications-unified-architecture), dan [Asset Administration Shell](https://industrialdigitaltwin.org/en/content-hub/aasspecifications). Verifikasi version/status resmi sebelum keputusan arsitektur.

Materi spatial/GIS/3D dilanjutkan pada [chapter 07](../../07_spatial_gis_3d/README.md).
