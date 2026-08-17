# Teori dan Solusi Lengkap — Level 09 AI Systems, Cloud, dan Governance

## 1. Dari model ke sistem

Sistem AI mencakup client, API gateway, authentication, validation, model service, storage, queue, monitoring, dan manusia yang mengambil keputusan. Model dengan accuracy tinggi bisa gagal sebagai produk bila latency tinggi, input schema berubah, biaya tidak terkendali, atau output tidak aman.

## 2. Solusi desain endpoint produksi

Tentukan request contract, response contract, ukuran payload, timeout, rate limit, error code, model version, dan data retention. Gunakan validasi di boundary supaya model menerima input yang telah bersih.

```python
from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    age: int = Field(ge=0, le=120)
    income: float = Field(ge=0, le=10_000_000_000)

class PredictionResponse(BaseModel):
    prediction: int
    model_version: str
    request_id: str
```

`422` cocok untuk input tidak valid, `429` untuk rate-limited, `503` bila dependency tidak siap. Jangan mengembalikan traceback/secret ke client.

## 3. Reliability pattern

Timeout mencegah request menunggu tanpa batas. Retry hanya untuk error sementara dan harus memiliki batas, exponential backoff, serta jitter. Operasi tulis memerlukan idempotency key agar retry tidak menggandakan transaksi. Circuit breaker menghentikan request ke dependency yang sedang gagal. Queue dan dead-letter queue memisahkan kerja lambat/rusak dari jalur utama.

## 4. Cloud dan security

Gunakan IAM least privilege, secret manager, encryption saat transit/diam, network segmentation, audit log, dan dependency/image scanning. Pisahkan dev/staging/production. Infrastructure as code membuat perubahan dapat direview dan diulang. Cost guardrail meliputi quota, budget alert, autoscaling limit, dan observasi egress/GPU.

## 5. Governance dan incident response

Model card menjelaskan tujuan, data provenance, metrik, subgroup limitation, misuse, serta owner. Ketika insiden terjadi: stabilkan dampak (rollback/disable), simpan bukti, cari perubahan terakhir, komunikasikan status, lalu buat postmortem tanpa menyalahkan individu. Retraining otomatis bukan respons universal; bisa memperbesar insiden bila data upstream rusak.
