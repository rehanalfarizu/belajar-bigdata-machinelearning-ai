# Level 6 — MLOps & Deployment

> **Tujuan**: Deploy model ML dari laptop ke production. Sekarang kamu bukan cuma bisa bikin model yang bagus — tapi bisa serve model itu ke dunia nyata, monitor performanya, dan automate pipeline-nya.
> **Asumsi**: Kamu sudah punya model trained dari Level 3–5.

---

## 1. Model Persistence — Save dan Load

### 1.1 joblib vs pickle

```python
import joblib
import pickle

# joblib — recommended untuk sklearn models (handle numpy arrays lebih baik)
joblib.dump(model, 'model.joblib')
model = joblib.load('model.joblib')

# pickle — built-in Python serialization
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
```

### 1.2 Save Pipeline Utuh

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)

# Save entire pipeline
joblib.dump(pipeline, 'pipeline.joblib')

# Load — langsung predict tanpa preprocessing manual
loaded_pipeline = joblib.load('pipeline.joblib')
predictions = loaded_pipeline.predict(X_new)
```

---

## 2. FastAPI — REST API untuk ML Model

### 2.1 Kenapa FastAPI?

```
Flask:          lebih kontrol, lebih banyak boilerplate, async limited
FastAPI:        otomatis OpenAPI docs, async native, Pydantic validation,
                auto-generated docs (Swagger UI)
Django:         overkill untuk API sederhana, full-stack framework
```

FastAPI adalah standar de facto untuk ML API di tahun 2024 karena: fast, automatic docs, type safety, async.

### 2.2 Aplikasi Lengkap

```python
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import joblib
import numpy as np

app = FastAPI(title="ML Prediction API", version="1.0.0")

# Load model saat startup
try:
    model = joblib.load('models/model_rf.joblib')
    print("Model loaded successfully")
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None


class PredictionInput(BaseModel):
    features: List[float] = Field(..., min_length=4, max_length=4,
                                  description="4 fitur: sepal_l, sepal_w, petal_l, petal_w")


class PredictionOutput(BaseModel):
    prediction: int
    class_name: str
    probabilities: dict


@app.get("/")
def root():
    return {"message": "ML Prediction API", "version": "1.0.0", "status": "ok"}


@app.get("/health")
def health():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy", "model": "RandomForest"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    features = np.array(data.features).reshape(1, -1)
    pred = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]

    class_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    probabilities = {class_names[i]: float(round(p, 4)) for i, p in enumerate(proba)}

    return PredictionOutput(
        prediction=pred,
        class_name=class_names[pred],
        probabilities=probabilities
    )


@app.post("/batch-predict")
def batch_predict(data: List[PredictionInput]):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    features = np.array([d.features for d in data])
    predictions = model.predict(features).tolist()

    return {"predictions": predictions, "count": len(predictions)}


# Run: uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2.3 Test API

```bash
# dengan curl
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# atau pakai httpie (lebih readable)
http POST http://localhost:8000/predict features:='[5.1, 3.5, 1.4, 0.2]'
```

### 2.4 Dockerize API

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Create models directory
RUN mkdir -p models

# Copy model
COPY models/model_rf.joblib models/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build image
docker build -t ml-api:v1 .

# Run container
docker run -p 8000:8000 --name ml-api-container ml-api:v1

# Test
curl http://localhost:8000/health
```

---

## 3. MLflow — Experiment Tracking

MLflow adalah tools open-source untuk mengelola lifecycle ML: experiment tracking, model registry, serving.

### 3.1 MLflow Tracking Server

```bash
# Jalankan MLflow UI
mlflow ui --backend-store-uri sqlite:///mlflow.db
# Buka http://localhost:5000
```

### 3.2 Log Experiments

```python
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("iris-classifier")

def train_and_log(model_name, model, X_train, X_test, y_train, y_test):
    with mlflow.start_run(run_name=model_name):
        # Log hyperparameters
        mlflow.log_param("model_type", model_name)
        if hasattr(model, 'n_estimators'):
            mlflow.log_param("n_estimators", model.n_estimators)
        if hasattr(model, 'max_depth'):
            mlflow.log_param("max_depth", model.max_depth)

        # Train
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Log metrics
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision_macro": precision_score(y_test, y_pred, average='macro'),
            "recall_macro": recall_score(y_test, y_pred, average='macro'),
            "f1_macro": f1_score(y_test, y_pred, average='macro')
        }
        mlflow.log_metrics(metrics)

        # Log model
        mlflow.sklearn.log_model(model, model_name)

        return metrics

# Train multiple models
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

results = {}
results['LogReg'] = train_and_log("LogisticRegression",
    LogisticRegression(max_iter=1000, random_state=42),
    X_train, X_test, y_train, y_test)

results['RandomForest'] = train_and_log("RandomForest",
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_train, X_test, y_train, y_test)

results['XGBoost'] = train_and_log("XGBoost",
    GradientBoostingClassifier(n_estimators=100, random_state=42),
    X_train, X_test, y_train, y_test)
```

### 3.3 Model Registry — Versioning Model

```python
# Register best model
best_model = RandomForestClassifier(n_estimators=200, random_state=42)
best_model.fit(X_train, y_train)

mlflow.sklearn.log_model(
    sk_model=best_model,
    artifact_path="random_forest_model",
    registered_model_name="IrisClassifier"
)

# Atau dari existing run:
model_uri = "runs:/<run_id>/random_forest_model"
mlflow.register_model(model_uri, "IrisClassifier")

# Load registered model
from mlflow.tracking import MlflowClient

client = MlflowClient()
latest_version = client.get_latest_version("IrisClassifier")
model = mlflow.sklearn.load_model(f"models:/IrisClassifier/{latest_version.version}")
```

---

## 4. Data Drift Detection — Monitor Production Model

### 4.1 Kenapa Perlu Deteksi Drift?

Model ML diasumsikan data di production punya distribusi sama dengan training data. Reality check:
- Customer behavior berubah seiring waktu
- Ekonomi berubah
- Seasonality effects

Jika distribusi berubah → model performance degrade → business impact

### 4.2 Kolmogorov-Smirnov Test

```python
import numpy as np
from scipy.stats import ks_2samp

def detect_drift(reference_data, current_data, threshold=0.1):
    """
    Deteksi data drift menggunakan Kolmogorov-Smirnov test.
    Kembali ke H0: distribusi sama → tidak ada drift.
    Jika p-value < 0.05 atau KS statistic > threshold → drift detected.
    """
    results = {}
    for i in range(reference_data.shape[1]):
        statistic, p_value = ks_2samp(reference_data[:, i], current_data[:, i])
        results[f"feature_{i}"] = {
            "ks_statistic": round(statistic, 4),
            "p_value": round(p_value, 4),
            "drifted": p_value < 0.05 or statistic > threshold,
            "direction": "increase" if np.mean(current_data[:, i]) > np.mean(reference_data[:, i]) else "decrease"
        }
    return results

# Usage
reference = np.random.randn(1000, 5)  # dari batch pertama
current = np.random.randn(1000, 5) + np.array([0.5, 0, 0.2, -0.3, 0])  # drift di beberapa fitur

drift_report = detect_drift(reference, current, threshold=0.1)

# Ringkasan
drifted_features = [k for k, v in drift_report.items() if v['drifted']]
print(f"Drifted features: {len(drifted_features)}/{len(drift_report)}")
print(f"Details: {drift_report}")
```

### 4.3 Alerting Setup

```python
def check_drift_and_alert(reference_path, current_path, threshold_pct=0.5):
    """
    Check drift dan trigger alert jika terlalu banyak fitur yang drifting.
    """
    reference = np.load(reference_path)
    current = np.load(current_path)

    drift_results = detect_drift(reference, current, threshold=0.1)
    drifted_count = sum(1 for r in drift_results.values() if r['drifted'])
    drifted_pct = drifted_count / len(drift_results)

    alert = {
        "alert": drifted_pct >= threshold_pct,
        "drifted_features": drifted_count,
        "total_features": len(drift_results),
        "drift_percentage": round(drifted_pct * 100, 1),
        "details": drift_results
    }

    if alert["alert"]:
        print(f"⚠️ DRIFT ALERT: {drifted_count}/{len(drift_results)} fitur drifting ({drifted_pct*100:.1f}%)")
        # Kirim notifikasi (email, Slack, dll)
        send_alert_notification(alert)

    return alert
```

---

## 5. Batch Prediction Pipeline

### 5.1 Production Batch Prediction Script

```python
# predict_batch.py
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_artifacts():
    """Load model dan preprocessor."""
    model = joblib.load('models/model_rf.joblib')
    scaler = joblib.load('models/scaler.joblib')
    return model, scaler


def predict_batch(input_csv, output_csv, model, scaler):
    """Batch prediction untuk seluruh CSV."""
    logger.info(f"Loading data from {input_csv}")
    df = pd.read_csv(input_csv)

    logger.info(f"Preprocessing {len(df)} records")
    X = df.values
    X_scaled = scaler.transform(X)

    logger.info("Running inference")
    predictions = model.predict(X_scaled)
    probas = model.predict_proba(X_scaled)

    # Tambah hasil ke dataframe
    df['prediction'] = predictions
    df['prob_class_0'] = probas[:, 0]
    df['prob_class_1'] = probas[:, 1]
    df['prob_class_2'] = probas[:, 2]
    df['prediction_time'] = datetime.now().isoformat()

    logger.info(f"Saving results to {output_csv}")
    df.to_csv(output_csv, index=False)

    # Summary
    logger.info(f"Done: {len(df)} predictions")
    logger.info(f"Class distribution: {pd.Series(predictions).value_counts().to_dict()}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python predict_batch.py <input.csv> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    model, scaler = load_artifacts()
    predict_batch(input_file, output_file, model, scaler)
```

### 5.2 Automation dengan Cron / Prefect

```bash
# Cron job — jalan setiap jam
0 * * * * cd /app && python predict_batch.py data/hourly_batch.csv data/outputs/hourly_$(date +\%Y\%m\%d_\%H).csv >> logs/batch.log 2>&1
```

```python
# Prefect pipeline
from prefect import flow, task

@task
def load_data():
    return pd.read_csv('data/batch.csv')

@task
def preprocess(data):
    scaler = joblib.load('models/scaler.joblib')
    return scaler.transform(data.values)

@task
def predict(X):
    model = joblib.load('models/model_rf.joblib')
    return model.predict(X)

@task
def save_results(predictions):
    df = pd.DataFrame({'prediction': predictions})
    df.to_csv('data/results.csv', index=False)

@flow
def batch_pipeline():
    data = load_data()
    X = preprocess(data)
    predictions = predict(X)
    save_results(predictions)
```

---

## 6. Gradio — User Interface untuk ML Model

Gradio = cara fastest untuk membuat interactive UI untuk ML model:

```python
import gradio as gr
import joblib
import numpy as np

model = joblib.load('models/model_rf.joblib')
iris_classes = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}


def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    return {
        "Prediksi": iris_classes[pred],
        "Setosa": f"{proba[0]*100:.1f}%",
        "Versicolor": f"{proba[1]*100:.1f}%",
        "Virginica": f"{proba[2]*100:.1f}%"
    }


demo = gr.Interface(
    fn=predict_flower,
    title="🌸 Iris Flower Classifier",
    description="Klasifikasi spesies bunga Iris berdasarkan ukuran petal dan sepal",
    inputs=[
        gr.Slider(0, 10, value=5.1, step=0.1, label="Sepal Length (cm)"),
        gr.Slider(0, 10, value=3.5, step=0.1, label="Sepal Width (cm)"),
        gr.Slider(0, 10, value=1.4, step=0.1, label="Petal Length (cm)"),
        gr.Slider(0, 10, value=0.2, step=0.1, label="Petal Width (cm)"),
    ],
    outputs=gr.Label(num_top_classes=3),
    examples=[
        [5.1, 3.5, 1.4, 0.2],
        [7.0, 3.2, 4.7, 1.4],
        [6.3, 3.3, 6.0, 2.5]
    ]
)

demo.launch(server_name="0.0.0.0", server_port=7860)
# Buka http://localhost:7860
```

---

## 7. Deployment Options — Gratis

### 7.1 Render.com (Recommended untuk Pemula)

1. Buat `render.yaml`:
```yaml
services:
  - type: web
    name: ml-api
    env: docker
    dockerfilePath: ./Dockerfile
    plan: free
    region: singapore
```

2. Connect GitHub repo di render.com → auto deploy dari Dockerfile

### 7.2 Railway.app

```bash
railway login
railway init
railway up
```

### 7.3 Hugging Face Spaces — untuk Gradio/Streamlit

```bash
# Buat HF Space
# Upload files: app.py + requirements.txt + models/
# Pilih "Gradio" atau "Streamlit" sebagai SDK
# HF auto-build dan host

# requirements.txt
gradio
joblib
numpy
scikit-learn
```

---

## Ringkasan — Level 6

`★ Insight ─────────────────────────────────────`
**1. Model tanpa deployment = model yang tidak berguna**: Kamu bisa bangun model terbaik di dunia, tapi jika tidak bisa diakses oleh user/sistem, nilai bisnisnya nol. Di industri, deployment infrastructure sering memakan waktu lebih banyak daripada building model-nya sendiri.

**2. Monitoring production model sama pentingnya dengan building-nya**: Model bisa degrade karena data drift, concept drift, atau upstream data pipeline changes. Siapkan monitoring dari awal, bukan afterthought.

**3. Experiment tracking bukan luxury**: Tanpa MLflow atau tool serupa, kamu tidak bisa reproducibly membandingkan model. Dalam tim, ini adalah prerequisite untuk collaboration yang efektif.
`─────────────────────────────────────────────────`

---

## Checklist Deployment Checklist

```
□ Model di-save dengan joblib/pickle
□ API di-test dengan curl/Postman
□ Dockerfile dibuild dan run berhasil
□ Health check endpoint berfungsi
□ Input validation (Pydantic/serializer)
□ Error handling (try/except, return appropriate HTTP codes)
□ Logging (setiap request logged dengan timestamp)
□ Container image size kecil (use python:3.10-slim, bukan python:3.10)
□ Environment variables untuk secrets (DB password, API keys)
□ Graceful shutdown handling
□ Rate limiting (opsional, untuk production)
□ Load testing (berapa request per detik bisa handle?)
□ Monitoring (log, metrics, alerting)
```

---

**Selamat!** Kamu sudah menyelesaikan seluruh roadmap. Dari Python dasar sampai deployment production ML pipeline.

Untuk next steps, cek `ROADMAP_TRACKER.txt` untuk milestone checklist dan next learning goals.