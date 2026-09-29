# REVIEW-001 — Review Command Endpoint

Review konsep endpoint berikut tanpa menulis solusi penuh:

```python
def set_pump_speed(asset_id, speed, model_score):
    if model_score > 0.8:
        device.send({"asset": asset_id, "speed": speed})
    return {"ok": True}
```

## Task

Tulis komentar review terurut berdasarkan severity. Periksa contract/type/range, authz, current state/freshness/uncertainty, safety envelope, idempotency/expiry, concurrency/precondition, human policy, device acknowledgment, audit, timeout/error, observability, tests, serta pemisahan recommendation dari command. Nyatakan pertanyaan blocker dan perubahan minimal sebelum merge.
