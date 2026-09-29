# Month 4 — Connected Digital Twin

## Context

Bangun twin untuk Tank, HVAC, atau Motor simulasi. Jangan menghubungkan ke actuator nyata. Plant truth, sensor observation, dan estimated twin state harus terpisah.

## Deliverables

- asset registry dan versioned telemetry contract;
- validator/unit conversion/dedup/order/quarantine/replay;
- historical events dan current state dengan freshness/uncertainty;
- state estimator serta dashboard/API read-only;
- tests untuk duplicate, late, missing, invalid unit, reboot, dan replay.

## Acceptance criteria

Tidak ada ground-truth leakage; duplicate/reordered event tidak merusak state; dropout menaikkan uncertainty; replay version sama menghasilkan state deterministik; stale state terlihat dan tidak diperlakukan current.

## Evidence

Sertakan sequence diagram, data-quality metrics, estimator experiment, failure-injection results, trace satu event end-to-end, dan limitations.
