# Teori dan Solusi Lengkap — Level 06 MLOps dan Deployment

## 1. Apa yang harus direproduksi?

Model tidak cukup disimpan sebagai bobot/classifier. Hasil training bergantung pada data versi tertentu, split, preprocessing, seed, hyperparameter, kode, library, dan hardware. MLOps mengelola dependency ini agar eksperimen dapat dibandingkan dan model dapat diaudit/diulang.

## 2. Solusi persistence: simpan pipeline utuh

```python
from pathlib import Path
import joblib

artifact_path = Path("artifacts/models/churn_pipeline.joblib")
artifact_path.parent.mkdir(parents=True, exist_ok=True)
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, artifact_path)

loaded_pipeline = joblib.load(artifact_path)
assert (pipeline.predict(X_test) == loaded_pipeline.predict(X_test)).all()
```

Pipeline mencegah API lupa memakai scaler/encoder yang sama. Jangan load `joblib`/`pickle` dari internet atau pengguna tidak tepercaya; format ini dapat menjalankan kode pada saat deserialisasi.

## 3. Solusi API FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np

app = FastAPI(title="Iris API", version="1.0.0")

class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0, le=20)
    sepal_width: float = Field(gt=0, le=20)
    petal_length: float = Field(gt=0, le=20)
    petal_width: float = Field(gt=0, le=20)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: IrisInput) -> dict[str, float | int]:
    features = np.array([[payload.sepal_length, payload.sepal_width,
                          payload.petal_length, payload.petal_width]])
    prediction = int(pipeline.predict(features)[0])
    probability = float(pipeline.predict_proba(features)[0].max())
    return {"prediction": prediction, "confidence": probability}
```

Dalam aplikasi nyata, `pipeline` dimuat sekali pada startup dan kegagalan load harus membuat readiness gagal. Tambahkan request ID, structured log, timeout, serta test endpoint.

## 4. Docker dan CI

Image menyatukan Python, dependency, kode, dan model. Build harus deterministic: pin dependency, gunakan `.dockerignore`, jangan masukkan secret, dan jalankan sebagai user non-root bila memungkinkan. CI minimal menjalankan formatter/linter, syntax/test, build image, serta scan dependency. CD harus memiliki staging dan rollback, bukan langsung mengganti production.

## 5. Monitoring dan drift

Data drift adalah perubahan distribusi input; concept drift adalah hubungan input-target berubah. Keduanya tidak identik dengan model failure. Monitor schema, missing rate, range, PSI/KS, latency, error rate, traffic, prediction distribution, dan ground-truth metric bila label balik tersedia. Buat alert dengan owner dan runbook agar alarm dapat ditindaklanjuti.
