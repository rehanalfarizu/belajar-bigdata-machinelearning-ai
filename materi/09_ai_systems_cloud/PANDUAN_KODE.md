# Panduan Kode Level 09

## Konfigurasi aman

```python
import os

MODEL_PATH = os.environ.get("MODEL_PATH", "models/pipeline.joblib")
ENVIRONMENT = os.environ.get("APP_ENV", "development")
if ENVIRONMENT == "production" and "MODEL_PATH" not in os.environ:
    raise RuntimeError("MODEL_PATH wajib diisi di production")
```

Jangan membaca secret dari source code. Validasi environment saat startup dan log hanya nama versi, bukan token.

## Request boundary

API memvalidasi schema, range, ukuran payload, timeout, dan error response. Pisahkan input parsing, business logic, model call, dan response serialization agar dapat dites sendiri-sendiri.

## Observability

Gunakan structured JSON log dengan request ID, model version, latency, status, dan error class. Jangan mencatat teks pengguna atau fitur sensitif secara mentah. Tambahkan metric p50/p95 dan counter error.
