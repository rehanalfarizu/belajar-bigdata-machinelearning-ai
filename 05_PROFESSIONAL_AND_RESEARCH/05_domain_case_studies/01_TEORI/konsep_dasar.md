# Domain Case Studies

Core abstraction dapat dipakai ulang: asset/process identity, versioned schema/model, observations/provenance, estimated state/uncertainty, relationships, simulation, prediction, recommendation, decision, dan audit. Namun validation tidak dapat dipindahkan hanya dengan mengganti nama field.

| Domain | Contoh state/use case | Model | Risiko/constraint khas |
|---|---|---|---|
| Manufacturing | line/equipment health, quality, schedule | discrete-event + equipment physics | worker safety, downtime, legacy OT |
| Energy | load/generation/storage/grid | forecast, power flow, optimization | stability, regulation, weather |
| Building | thermal/air quality/occupancy | RC thermal + control | comfort, health, privacy |
| Transport/logistics | fleet/traffic/inventory/order | GIS, routing, agents | public safety, SLA, disruption |
| Infrastructure | bridge/road/water state | structural/hydraulic + GIS | long lifecycle, inspection uncertainty |
| Mining | equipment/terrain/process | fleet, geospatial, process simulation | hazardous OT, environment |
| Agriculture | soil/crop/water/equipment | biological, weather, spatial | uncertainty, connectivity, sustainability |
| Healthcare/device | device/patient conceptual state | physiological/statistical | clinical validation, privacy, regulation |

Untuk setiap transfer, bandingkan unit, timescale, failure criterion, controllability, uncertainty source, data rights, decision owner, safety consequence, regulation, dan required evidence. Mining adalah satu case, bukan definisi Digital Twin. Healthcare di materi ini bersifat konseptual, bukan clinical guidance.
