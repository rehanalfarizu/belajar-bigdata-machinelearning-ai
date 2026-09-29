# Month 6 — Final Capstone: General-Purpose Intelligent Digital Twin

## Context

Bangun platform configurable untuk minimal tiga asset types dari `Tank`, `Motor`, `HVAC`, `Vehicle`, dan `ProductionLine` melalui common interfaces—tanpa conditional asset type tersebar di core logic.

```text
Registry + versioned contracts
→ ingestion/validation/raw/DLQ
→ history + state + uncertainty
→ pluggable estimator/simulator/ML
→ what-if/optimization/recommendation
→ policy + human approval + command guard
→ audit + outcome feedback + controlled model lifecycle
```

## Deliverables

- typed/configurable adapters dan lifecycle versions;
- unit, integration, replay, compatibility, dan failure-injection tests;
- local reproducible deployment; secrets tidak berada di image/source;
- API/schema/model migration plan, metrics/traces/alerts/runbook;
- threat model, safety boundary, RBAC, audit, backup/rollback;
- reproducible experiment report dengan baseline/ablation;
- simulated one-command demo berlabel jelas.

## Acceptance criteria

1. Duplicate/reordered/stale events tidak merusak state.
2. Dropout/contradiction menaikkan uncertainty dan membatasi authority.
3. Replay state deterministik untuk version sama.
4. Schema/model migration menjaga historical meaning.
5. What-if tidak menulis physical state.
6. Optimizer/model tidak melewati hard safety constraint.
7. Approval, command, actuation outcome, dan override dapat diaudit.
8. Broker/model/store outage mempunyai tested degraded mode.
9. Model update melewati shadow/canary dan dapat di-rollback.
10. Asset adapter baru tidak mengubah core domain logic.

## Evidence dan defense

Serahkan source, tests, configs, architecture decision records, benchmark, experiment report, threat/safety boundaries, runbook, demo, limitations, dan journal. Defense harus menjelaskan trade-off, negative results, external validity, serta kapan platform tidak layak dipakai. Demo sendiri tidak cukup.
