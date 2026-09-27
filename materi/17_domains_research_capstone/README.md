# Chapter 17 — Domains, Systems Engineering, Research, dan Expert Capstone

Expert bukan orang yang memakai stack paling banyak. Expert mampu memindahkan abstraction antar-domain, menyatakan assumptions, mengukur uncertainty, menguji failure mode, mempertanggungjawabkan architecture/decision, dan mengetahui kapan twin tidak layak dibuat.

## 1. Common abstraction, domain evidence

Core abstraction:

```text
Asset/Process identity
├── model/schema/version
├── observations + provenance
├── estimated state + uncertainty + effective time
├── relationships/hierarchy
├── behavior models/simulators
├── predictions/anomalies/scenarios
└── recommendations/decisions/audit
```

Abstraction boleh sama, tetapi physics, failure criteria, safety, regulation, timescale, cost, dan evidence berbeda. Model motor tidak menjadi model patient hanya karena field namanya diganti.

## 2. Peta domain

| Domain | State/use case | Model penting | Risiko/constraint khas |
|---|---|---|---|
| Manufacturing | machine/line state, quality, OEE, schedule | discrete-event + equipment physics | worker safety, downtime, legacy OT |
| Energy | generation/load/storage/grid state | power flow, forecast, optimization | stability, regulation, weather |
| Building/HVAC | zone temperature/air quality/occupancy | thermal RC + control | comfort, indoor health, privacy |
| Automotive | vehicle/component health | dynamics, battery, perception | functional safety, latency |
| Transportation | fleet/traffic/network | GIS, routing, agents | public safety, disruption |
| Logistics | inventory/vehicle/order | event simulation + routing | SLA, capacity, uncertain demand |
| Aerospace | structure/propulsion/mission health | high-fidelity + reduced-order | extreme consequence, sparse failure data |
| Infrastructure | bridge/road/water network | structural/hydraulic + GIS | long lifecycle, inspection uncertainty |
| Smart city | system-of-systems | geospatial + federated models | governance, privacy, unequal impact |
| Mining | equipment/haul/terrain/process | fleet, geospatial, process simulation | hazardous OT/environment |
| Agriculture | soil/crop/water/equipment | weather, biological, spatial | uncertainty, connectivity, sustainability |
| Healthcare/device | device/patient-specific conceptual model | physiological/statistical | clinical validation, privacy, regulation; conceptual only here |

Mining adalah satu case study, bukan definisi jalur. Pilih minimal tiga domain dan tulis apa yang reusable versus wajib diganti/divalidasi ulang.

## 3. Systems engineering lifecycle

1. Stakeholder dan decision/use case.
2. System boundary, context, hazards, constraints.
3. Requirements yang measurable: frequency, fidelity, latency, accuracy, availability, safety.
4. Architecture dan interface/data contracts.
5. Model selection, verification, calibration, validation.
6. Integration dalam shadow mode.
7. Operational acceptance, training, runbook, rollback.
8. Monitoring perubahan asset/data/model/schema.
9. Controlled upgrade dan configuration management.
10. Decommissioning, retention, revocation, archival.

Traceability menghubungkan requirement → design → implementation → test → operational evidence. Digital thread membantu lifecycle traceability tetapi tidak identik dengan Digital Twin.

## 4. Research track

### Literature review

Definisikan scope, database/index, query string, time range, inclusion/exclusion, screening, quality assessment, extraction table, dan synthesis. Bedakan standard, peer-reviewed evidence, vendor documentation, benchmark, dan marketing claim. Simpan search date dan DOI/URL.

### Research question dan hypothesis

Pertanyaan harus falsifiable dan membandingkan baseline. Contoh: “Apakah residual hybrid mengurangi median detection delay tanpa menaikkan false alarms per asset-day dibanding EWMA pada tiga operating modes?” Bukan “Apakah AI meningkatkan Digital Twin?”

### Experimental design

- unit of analysis dan independent test assets/time;
- baseline dan oracle/upper bound bila mungkin;
- controlled factors, confounders, seeds;
- train/validation/test chronology;
- sample-size/power atau uncertainty justification;
- ablation dan sensitivity;
- preregistered primary metric bila stakes tinggi;
- reproducible code, config, data version, environment.

### Validity

Bahas internal validity (causal/confounding/leakage), construct validity (metric mewakili tujuan?), external validity (domain/asset/season transfer), dan conclusion validity (uncertainty/multiple comparison). Laporkan negative result dan limitation.

## 5. Metric suite Digital Twin

Jangan berhenti pada accuracy/F1/RMSE:

- synchronization latency dan state age/freshness;
- event loss/duplicate/out-of-order/rejected rates;
- state estimation error dan uncertainty coverage;
- simulation error per regime serta conservation violation;
- forecast/RUL calibration dan sharpness;
- anomaly detection delay, false alarms per asset-time, missed incidents;
- inference/optimization latency dan infeasibility rate;
- availability, recovery time, replay correctness;
- recommendation acceptance/override dan constraint violation;
- decision improvement: downtime, energy, throughput, safety proxy, cost;
- operator workload/trust calibration dan distributional impact.

Satu aggregate score dapat menyembunyikan trade-off; tampilkan dashboard metric dan acceptance thresholds per use case.

## 6. Expert capstone — General-Purpose Intelligent Digital Twin Platform

Platform harus configurable untuk minimal `Tank`, `Motor`, `HVAC`, `Vehicle`, dan `ProductionLine` melalui common interfaces—tanpa `if asset_type == ...` tersebar di seluruh codebase.

Minimal components:

```text
Asset Registry + Model/Schema Registry
→ Telemetry Ingestion + Validation + Raw/DLQ
→ Historical Store + Twin State Store
→ Pluggable State Estimator
→ Pluggable Physics/Simulation Model
→ ML Inference + Anomaly + Forecast/RUL
→ What-if + Optimization
→ Recommendation + Human Approval + Command Guard
→ API/Dashboard + Logging/Metrics/Tracing
```

Required engineering evidence:

- typed/configurable interfaces and lifecycle versions;
- unit, property-based where useful, integration, replay, and failure-injection tests;
- Docker/local compose for broker/store/API/dashboard; secrets tidak di-image;
- API/schema/model compatibility and migration plan;
- observability dashboard dan alert/runbook;
- threat model, safety case boundary, RBAC, audit log;
- benchmark load/freshness/latency dan capacity estimate;
- reproducible experiment report dengan baselines/ablations;
- one-click demo memakai simulated assets, dengan data simulasi berlabel jelas.

Project ladder:

- Beginner: temperature sensor simulator dan tank shadow.
- Intermediate: synchronized tank/HVAC/motor + estimator + anomaly.
- Advanced: multisensor predictive maintenance/RUL/forecast twin.
- Professional: broker, state service, history, model API, observability, Docker.
- Expert: configurable platform, optimization, approval loop, federation/research evidence.

## 7. Acceptance tests capstone

1. Duplicate/reordered/stale telemetry tidak merusak state.
2. Sensor dropout menaikkan uncertainty dan membatasi recommendation.
3. Replay raw log menghasilkan state deterministik untuk version yang sama.
4. Model/schema migration tidak mengubah historical meaning diam-diam.
5. Fault injection terdeteksi dalam delay budget dengan false-alarm budget.
6. What-if tidak menulis physical state.
7. Optimizer tidak dapat melewati hard safety constraint.
8. Operator override dan command outcome tercatat end-to-end.
9. Broker/model/store outage masuk degraded mode yang didefinisikan.
10. Satu asset adapter baru dapat ditambah tanpa mengubah core domain logic.

## Gate Expert/Research

Lulus hanya jika kamu dapat mendemonstrasikan platform, menjelaskan trade-off, mereproduksi experiment, mempertahankan keputusan architecture, menunjukkan failure/rollback, dan menulis batas external validity. Repository ini menyediakan blueprint dan core kecil; membangun capstone penuh tetap proyek multi-iterasi, bukan checklist bacaan.

## Referensi lanjutan

- [ISO/IEC 30173 — concepts and terminology](https://www.iso.org/standard/81442.html)
- [NIST Digital Twins program](https://www.nist.gov/digital-twins)
- [NIST IR 8356 — security and trust](https://csrc.nist.gov/pubs/ir/8356/final)
- [Digital Twin Consortium — Capabilities Periodic Table](https://www.digitaltwinconsortium.org/wp-content/uploads/sites/3/2022/06/Digital-Twin-Capabilities-Periodic-Table.pdf)
- [IDTA Asset Administration Shell specifications](https://industrialdigitaltwin.org/en/content-hub/aasspecifications)

Kembali ke [curriculum utama](../../CURRICULUM_LENGKAP.md) dan catat bukti pada [roadmap tracker](../../ROADMAP_TRACKER.txt).
