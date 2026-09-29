# Governed Intelligent Digital Twin

Intelligent twin menutup loop observation→state→analysis→decision→outcome, tetapi “intelligent” bukan izin untuk autonomous actuation.

```text
Physical → Telemetry → Quality → State + Uncertainty
→ Diagnosis/Prediction → What-if/Optimization → Recommendation
→ Policy + Human Decision → Validated Command → Physical
→ Independent Observation → Outcome Evaluation → controlled learning
```

Pisahkan monitoring, recommendation, decision, command, dan actuation. Recommendation menyertakan assumptions, alternatives, expected range, model/state version, freshness, uncertainty, expiry, dan rationale. Command memerlukan authenticated actor, authorization, idempotency key, bounds, rate limits, state precondition, expiry, dan audit. Actuation outcome dikonfirmasi melalui observation bila stakes menuntut.

Adaptasi model harus melewati offline evaluation, shadow, canary, approval, monitoring, dan rollback. Online exploration tidak dilakukan pada hazardous asset. RL hanya relevan bila sequential decision/delayed outcome penting dan baseline rule/control/optimization tidak cukup; sim-to-real gap, reward hacking, unsafe exploration, dan distribution shift harus diuji.

Fleet/federated twin memerlukan identity, semantic, access, trust, and change contracts lintas owner. Availability satu cloud service tidak boleh menghapus local safety function. Security, model accuracy, dan safety adalah evidence berbeda.

Rujukan risiko: [NIST IR 8356](https://csrc.nist.gov/pubs/ir/8356/final), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), dan [ISO/IEC 42001](https://www.iso.org/standard/81230.html). Verifikasi revisi terbaru sebelum adopsi formal.
