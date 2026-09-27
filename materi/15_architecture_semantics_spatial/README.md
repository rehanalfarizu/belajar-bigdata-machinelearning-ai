# Chapter 15 — Architecture, Semantics, Twin Graph, 3D, dan GIS

Production twin bukan satu database atau dashboard. Ia adalah sistem dengan boundaries, data contracts, identity, models, state, history, computation, decision, dan governance yang dapat berevolusi tanpa kehilangan makna.

## 1. Reference architecture

```text
Physical: sensor / actuator / PLC / asset
    ↓
Connectivity: fieldbus / OPC UA / MQTT / network security
    ↓
Edge: buffer / normalize / local rule / safe degraded mode
    ↓
Ingestion: broker / stream / schema validation / DLQ
    ├── raw immutable log / object storage
    ├── historian / time-series database
    └── curated event stream
              ↓
Twin state service ↔ asset registry / semantic graph
    ├── state estimator
    ├── model & simulation service
    ├── ML inference / anomaly / forecast / RUL
    └── what-if / optimization
              ↓
API / dashboard / spatial view / alerts
              ↓
recommendation → policy/approval → command gateway → physical
```

Control plane mengelola identity, model/schema versions, config, access, deployments, audit, observability, retention, backup, and rollback. Data plane menangani telemetry/state/query/command flow.

## 2. Storage dan consistency

- **Raw object/log storage**: replay, audit, backfill; append-oriented.
- **Historian/time-series store**: range query, aggregation, compression, retention.
- **Twin state store**: latest effective state, version, freshness, uncertainty; low-latency lookup.
- **Semantic/graph store**: entity relationships dan metadata.
- **Model registry/artifact store**: model binary, parameters, data lineage, evaluation.
- **Cache**: mempercepat read tetapi memunculkan invalidation/staleness.

State update perlu optimistic version/idempotency. Jangan mengejar satu global transaction lintas ribuan asset tanpa kebutuhan; ordering per asset/partition sering cukup. Event sourcing memudahkan replay, tetapi projection/version migration dan storage cost harus dirancang.

## 3. Scale, latency, reliability, observability

Capacity model minimal:

```text
events/second = asset_count × sensors_per_asset × sample_rate
daily_bytes ≈ events/second × average_event_bytes × 86400
```

Masukkan burst, replication, indexes, derived data, retention, dan replay load. Partition berdasarkan access/order pattern, bukan kebiasaan. Backpressure lebih aman daripada memory tumbuh tak terbatas; edge buffer harus punya capacity/drop policy.

SLO yang bermakna: ingestion availability, event-time lag p95/p99, state freshness, estimator/model latency, rejected-event rate, replay recovery time, command decision latency, and system availability. Trace satu `event_id` dan `state_version` end-to-end.

Failure mode: broker unavailable, device offline, duplicated replay, clock drift, schema incompatible, model timeout, database lag, graph unavailable, partial region failure. Tentukan degraded mode dan recovery semantics.

## 4. Asset model, semantics, ontology, graph

Schema mengatakan bentuk data; semantic model mengatakan meaning; ontology memformalkan concepts/relationships/constraints untuk interoperability/reasoning.

```text
Factory ─contains→ Line ─contains→ Machine
Machine ─has_component→ Motor
Sensor ─observes→ BearingTemperature
Motor ─component_of→ Machine
Truck ─located_on→ RoadSegment
```

Setiap entity butuh stable ID, type/model version, lifecycle status, owner, properties, relationships, valid/effective time, dan provenance. Bedakan:

- type/model `Motor` dari instance `motor-17`;
- component embedded dari entity yang punya identity/lifecycle sendiri;
- hierarchy (`contains`) dari causal/functional relationship (`feeds`, `cools`, `observes`);
- current relationship dari historical relationship.

Twin graph membuat context query mungkin—misalnya semua sensor yang mengobservasi motor pada line tertentu—tetapi graph bukan physics simulator. Semantic consistency tidak menjamin state accuracy.

Standard/reference yang relevan berbeda scope:

- ISO/IEC 30173: concepts/terminology general-purpose;
- ISO 23247: framework manufacturing;
- OPC UA: communication + information modeling industrial;
- Asset Administration Shell: standardized industrial digital representation/metamodel/API;
- DTDL/Azure Digital Twins dan AWS IoT TwinMaker: platform-specific modeling/graph capabilities;
- OGC SensorThings: Web API/data model untuk sensing/tasking geospatial.

Verifikasi version/status pada sumber resmi sebelum membuat keputusan procurement/architecture.

## 5. Spatial, GIS, BIM, CAD, dan 3D

Spatial twin memerlukan lebih dari menempel icon di peta:

- coordinate reference system (CRS), datum, axis order, units;
- vector vs raster; DEM/terrain;
- GPS uncertainty dan map matching;
- geofencing dengan boundary/temporal semantics;
- spatial index dan topology;
- BIM/CAD identity mapping ke operational asset ID;
- 3D scene/mesh/point cloud level of detail dan update policy.

Contoh:

- building twin: BIM space/component + HVAC state + occupancy;
- city/infrastructure: GIS network + traffic/weather/work order;
- transport/fleet: trajectory + road graph + vehicle state;
- mining: terrain/orebody/haul road + equipment state;
- energy: grid topology + asset/geographic risk.

3D adalah projection/view. Source of truth untuk command/state tetap service dengan version, access control, dan audit. Coordinate transformation yang salah dapat menghasilkan keputusan fisik berbahaya walau visual terlihat meyakinkan.

## 6. Security boundaries

Pisahkan IT dan OT zones, inventory data flow, authenticate device/workload/operator, authorize per resource/action, encrypt in transit/at rest sesuai threat model, rotate credentials, validate firmware/schema/command, dan audit perubahan. Cloud-to-OT command harus melewati command gateway dan local safety control; cloud outage tidak boleh menghapus protection function.

## 7. Praktikum arsitektur

1. Buat asset registry untuk Factory–Line–Machine–Sensor dengan IDs dan versions.
2. Rancang query “sensor temperature stale pada line-2” tanpa scan semua event.
3. Hitung throughput/storage untuk 10.000 asset × 20 sensor × 1 Hz.
4. Tentukan partition key, retention, replay, and disaster-recovery assumptions.
5. Buat sequence diagram telemetry valid, duplicate, late, dan poison message.
6. Pilih CRS untuk route fleet dan tunjukkan konsekuensi salah axis/unit.
7. Threat-model spoofed sensor, replayed command, stolen gateway credential, dan poisoned model.

## Gate

Lulus bila dapat merancang architecture dengan state/history/graph terpisah, menghitung capacity, menyatakan consistency/failure semantics, memodelkan hierarchy/relationships versioned, dan menjelaskan kapan spatial/3D dibutuhkan.

## Referensi lanjutan

- [ISO/IEC 30173](https://www.iso.org/standard/81442.html)
- [ISO 23247-1](https://www.iso.org/standard/75066.html)
- [OPC UA online reference](https://reference.opcfoundation.org/)
- [IDTA Asset Administration Shell specifications](https://industrialdigitaltwin.org/en/content-hub/aasspecifications)
- [Azure Digital Twins model concepts](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models)
- [AWS IoT TwinMaker knowledge graph](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-graph.html)
- [OGC SensorThings API](https://www.ogc.org/standards/sensorthings/)

Berikutnya: [`16_optimization_intelligent_twin`](../16_optimization_intelligent_twin/README.md).
