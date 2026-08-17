# Panduan Penulisan Kode — Level 6: MLOps & Deployment

> Dibaca bersamaan dengan `06_mlops_deployment.ipynb` — jalankan cell, baca panduan ini, lalu pahami bagaimana model ML sampai ke production.

---

## 1. Apa Itu MLOps? Lifecycle Sebuah Model ML

### 1.1 ML Lifecycle

```
Data Collection → Data Processing → Feature Eng → Model Training
                                                          ↓
                                                         Evaluation
                                                          ↓
Model Packaging → Deployment → Monitoring → Retraining
                                                  ↑_______|
                                               (drift detected)
```

**MLOps = DevOps untuk Machine Learning.**
Bedanya dengan software biasa:
- Code + **Data** → Model (data berubah = model berubah)
- Model bisa degrade → perlu monitoring
- Retraining automation → Continuous Training (CT)

### 1.2 Deployment Pipeline

```
Development (laptop)          Production
────────────────────          ──────────────────
.py / .ipynb       →   trained_model.pkl
                          │
                     FastAPI/Flask
                          │
                     Container (Docker)
                          │
                     Cloud (AWS/GCP/On-prem)
                          │
                     Monitor (accuracy drift)
                          │
                     Trigger retraining (jika perlu)
```

---

## 2. FastAPI — Serve Model sebagai REST API

### 2.1 Dasar FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="ML Prediction API",
    version="1.0.0",
    description="API untuk prediksi model ML"
)

# Load model saat start-up (sekali saja, bukan per request)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Define request body schema
class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    label: str

LABELS = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

@app.get("/")
def read_root():
    return {"message": "ML API is running", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        # Buat array 2D (1 sample, 4 fitur)
        features = np.array([[
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]])

        # Scale
        features_scaled = scaler.transform(features)

        # Predict
        pred = model.predict(features_scaled)[0]
        proba = model.predict_proba(features_scaled)[0]

        return PredictionOutput(
            prediction=int(pred),
            probability=float(proba[pred]),
            label=LABELS[pred]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 2.2 Running & Testing FastAPI

```bash
# Jalankan server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Di terminal lain — test dengan curl:
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'

# Test health endpoint
curl http://localhost:8000/health

# Auto-generated docs: http://localhost:8000/docs (Swagger UI)
# Alternative docs: http://localhost:8000/redoc (ReDoc)
```

### 2.3 Dockerfile — Containerize API

```dockerfile
# Stage 1: Build
FROM python:3.10-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.10-slim

WORKDIR /app

# Copy hanya file yang dibutuhkan (tidak whole project)
COPY --from=builder /root/.local /root/.local
COPY model.pkl .
COPY scaler.pkl .
COPY main.py .

# PATH untuk pip install local
ENV PATH=/root/.local:$PATH

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "from urllib.request import urlopen; urlopen('http://localhost:8000/health')" || exit 1

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

`python:*-slim` tidak menjamin `curl` tersedia. Karena itu health check di atas memakai standard library Python. Alternatifnya adalah memasang `curl` secara eksplisit dengan `apt-get`, tetapi itu membuat image lebih besar.

### 2.4 requirements.txt

```
fastapi==0.109.0
uvicorn[standard]==0.27.0
joblib==1.3.2
scikit-learn==1.4.0
pydantic==2.5.3
python-multipart==0.0.6
```

---

## 3. MLflow — Experiment Tracking

### 3.1 MLflow Tracking Server

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set tracking URI (local file store atau remote server)
mlflow.set_tracking_uri("http://localhost:5000")  # untuk remote server
# mlflow.set_tracking_uri("file:///mlruns")       # untuk local

# Set experiment
mlflow.set_experiment("iris-classification")

# Auto-logging — track parameter, metrics, model secara otomatis
mlflow.sklearn.autolog()

for max_depth in [3, 5, 7, 10]:
    with mlflow.start_run(run_name=f"rf_depth_{max_depth}"):
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=max_depth,
            random_state=42
        )

        model.fit(X_train, y_train)
        train_acc = accuracy_score(y_train, model.predict(X_train))
        test_acc = accuracy_score(y_test, model.predict(X_test))

        # Log custom metrics
        mlflow.log_metric("train_accuracy", train_acc)
        mlflow.log_metric("test_accuracy", test_acc)
        mlflow.log_metric("depth", max_depth)

        print(f"Depth={max_depth}: train={train_acc:.4f}, test={test_acc:.4f}")
```

### 3.2 Manual Logging (lebih kontrol)

```python
from sklearn.metrics import f1_score, precision_score, recall_score

with mlflow.start_run(run_name="manual-logging"):
    # Log parameters
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    # Log model
    mlflow.sklearn.log_model(model, "model", registered_model_name="iris-rf-v1")

    # Log artifacts (file tambahan)
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_artifact("feature_importance.png")

    # Log environment
    mlflow.log_param("python_version", "3.10.0")
    mlflow.log_param("sklearn_version", "1.4.0")

    # Nested runs (sub-experiments)
    with mlflow.start_run(run_name="cross_validation", nested=True):
        # CV fold 1
        pass
```

### 3.3 Load & Use Logged Model

```python
import mlflow.pyfunc

# Load model dari experiment registry
model_uri = "models:/iris-rf-v1/1"  # registered model, version 1
model = mlflow.pyfunc.load_model(model_uri)

# Predict
predictions = model.predict(X_new)

# Atau gunakan sklearn flavor langsung
model = mlflow.sklearn.load_model("runs:/<run_id>/model")
```

### 3.4 MLflow UI

```bash
# Jalankan MLflow tracking server
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

# Atau dengan conda environment
mlflow run .

# Akses UI
# http://localhost:5000 → Experiment dashboard
# Bisa lihat: parameter, metrics, artifacts, compares runs
```

---

## 4. Batch Prediction Pipeline

### 4.1 Offline Prediction — Tidak Real-time

```python
import pandas as pd
import joblib
import numpy as np

def batch_predict(input_csv, output_csv, model_path, scaler_path):
    """
    Pipeline untuk prediksi batch dari CSV.
    Cocok untuk: scheduled job, nightly batch, data pipeline.
    """
    # Load model + scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Load data
    df = pd.read_csv(input_csv)

    # Preprocessing
    feature_cols = ["sepal_length", "sepal_width",
                    "petal_length", "petal_width"]
    X = df[feature_cols].values
    X_scaled = scaler.transform(X)

    # Predict
    predictions = model.predict(X_scaled)
    probabilities = model.predict_proba(X_scaled)

    # Add predictions ke dataframe
    df["prediction"] = predictions
    df["probability"] = np.max(probabilities, axis=1)

    # Save
    df.to_csv(output_csv, index=False)
    print(f"Batch prediction selesai: {len(df)} baris → {output_csv}")

# Usage
batch_predict(
    input_csv="data/unlabeled_data.csv",
    output_csv="data/predictions_2024-01-15.csv",
    model_path="models/rf_model.pkl",
    scaler_path="models/scaler.pkl"
)
```

### 4.2 Cron Job untuk Batch Prediction

```bash
# Di crontab (crontab -e):
# Setiap hari jam 2 pagi
0 2 * * * cd /app && python batch_predict.py >> /var/log/batch.log 2>&1

# Setiap Senin jam 6 pagi
0 6 * * 1 python batch_predict.py
```

---

## 5. Monitoring — Deteksi Model Drift

### 5.1 Concept Drift vs Data Drift

```
Concept Drift:
  P(y|X) berubah → relasi antara fitur dan target bergeser
  Contoh: model prediksi churn, behavior customer berubah setelah pandemi

Data Drift:
  P(X) berubah → distribusi input berubah
  Contoh: karena economic condition berubah, customer profile sekarang berbeda
```

### 5.2 Evidently AI — Monitoring Dashboard

```python
from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab, CatTargetDriftTab

# Compares reference (training data) vs current (new data)
report = Dashboard(tabs=[
    DataDriftTab(),
    CatTargetDriftTab()
])

report.calculate(
    reference_data=df_train,
    current_data=df_new,
    column_mapping=None
)

report.save("monitoring_report.html")
# Buka di browser untuk lihat visual drift report
```

### 5.3 Statistical Monitoring — Custom Implementation

```python
import numpy as np
from scipy import stats

def detect_drift(reference_data, current_data, threshold=0.05):
    """
    Deteksi data drift dengan Kolmogorov-Smirnov test.
    threshold = 0.05 → jika p-value < 0.05, distribusi berbeda signifikan
    """
    results = {}

    for col in reference_data.columns:
        ref = reference_data[col].dropna()
        curr = current_data[col].dropna()

        # KS test — apakah dua distribusi berbeda?
        statistic, p_value = stats.ks_2samp(ref, curr)

        results[col] = {
            "ks_statistic": round(statistic, 4),
            "p_value": round(p_value, 4),
            "drifted": p_value < threshold
        }

        if p_value < threshold:
            print(f"⚠️  Drift detected: {col} (p={p_value:.4f})")

    return results

# Usage: compare training data vs last week's data
drift_results = detect_drift(
    reference_data=X_train_df,
    current_data=X_last_week_df,
    threshold=0.05
)

# Jika banyak fitur drift → trigger retraining
drifted_features = [k for k, v in drift_results.items() if v["drifted"]]
if len(drifted_features) / len(drift_results) > 0.3:
    print("🚨 >30% fitur drift — trigger retraining!")
    # trigger_mlflow_retraining()
```

### 5.4 Model Performance Monitoring

```python
import time
from datetime import datetime

class ModelMonitor:
    def __init__(self, model, scaler, threshold=0.1):
        self.model = model
        self.scaler = scaler
        self.threshold = threshold  # minimum acceptable accuracy
        self.predictions_log = []

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        pred = self.model.predict(X_scaled)
        self.predictions_log.append(pred)
        return pred

    def log_actual(self, y_true, y_pred):
        """Log hasil aktual untuk evaluasi periodik"""
        accuracy = (y_true == y_pred).mean()
        print(f"[{datetime.now()}] Accuracy: {accuracy:.4f}")

        if accuracy < self.threshold:
            print(f"⚠️  Accuracy drops below threshold ({self.threshold})!")
            print(f"🚨 Trigger model retraining!")

    def generate_report(self):
        """Summary report"""
        total = len(self.predictions_log)
        unique, counts = np.unique(self.predictions_log, return_counts=True)
        print(f"\nPrediction Distribution (n={total}):")
        for label, count in zip(unique, counts):
            print(f"  Class {label}: {count} ({count/total*100:.1f}%)")
```

---

## 6. Gradio — Interactive UI untuk Model

### 6.1 Gradio Basics

```python
import gradio as gr
import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
LABELS = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

def predict(sepal_length, sepal_width, petal_length, petal_width):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)[0]
    proba = model.predict_proba(features_scaled)[0]

    return {
        f"{LABELS[i]}: {p:.1%}": p
        for i, p in enumerate(proba)
    }

# Interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Slider(0, 10, value=5.0, step=0.1, label="Sepal Length (cm)"),
        gr.Slider(0, 10, value=3.0, step=0.1, label="Sepal Width (cm)"),
        gr.Slider(0, 10, value=1.5, step=0.1, label="Petal Length (cm)"),
        gr.Slider(0, 10, value=0.5, step=0.1, label="Petal Width (cm)"),
    ],
    outputs=gr.Label(num_top_classes=3),
    title="🌸 Iris Flower Classifier",
    description="Masukkan 4 parameter bunga untuk klasifikasi jenis Iris.",
    examples=[[5.1, 3.5, 1.4, 0.2], [7.0, 3.2, 4.7, 1.4]]
)

demo.launch(server_name="0.0.0.0", server_port=7860)
```

### 6.2 Gradio untuk Image Classification

```python
import gradio as gr
import torch
from torchvision import transforms
from PIL import Image

model = torch.load("cnn_model.pth", map_location="cpu")
model.eval()

labels = ["airplane", "automobile", "bird", "cat", "deer",
          "dog", "frog", "horse", "ship", "truck"]

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

def classify_image(image):
    img = Image.fromarray(image.astype("uint8"), "RGB")
    img_tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        proba = torch.softmax(output, dim=1)[0]

    return {labels[i]: float(proba[i]) for i in range(10)}

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=3),
    title="CIFAR-10 Image Classifier"
)

demo.launch()
```

---

## 7. Docker — Production-Ready Deployment

### 7.1 Docker Commands

```bash
# Build image
docker build -t iris-api:1.0.0 .

# List images
docker images

# Run container
docker run -d --name iris-api -p 8000:8000 iris-api:1.0.0

# Check running container
docker ps

# View logs
docker logs iris-api

# Stop & remove
docker stop iris-api
docker rm iris-api

# Push to registry (Docker Hub, AWS ECR, GCP Container Registry)
docker tag iris-api:1.0.0 myusername/iris-api:1.0.0
docker push myusername/iris-api:1.0.0
```

### 7.2 Docker Compose — Multi-Service Setup

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000
    depends_on:
      - mlflow
    restart: unless-stopped

  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.12.0
    ports:
      - "5000:5000"
    volumes:
      - mlflow_data:/mlruns
    command: mlflow ui --backend-store-uri sqlite:///mlflow.db

volumes:
  mlflow_data:
```

```bash
docker-compose up -d      # start semua service
docker-compose down      # stop
docker-compose logs -f   # view logs
docker-compose ps        # status service
```

### 7.3 Health Check & Graceful Shutdown

```python
from fastapi import FastAPI
import signal
import sys

app = FastAPI()

# Graceful shutdown handler
def shutdown_handler(signum, frame):
    print("Received SIGTERM — shutting down gracefully...")
    # Cleanup: close DB connections, save state, etc.
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    # Readiness check: model loaded, DB connected, etc.
    try:
        model.predict(X_test_sample)  # smoke test
        return {"status": "ready"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
```

---

## 8. Production Checklist

```python
# CHECKLIST sebelum production deployment
checklist = """
  □ Model sudah di-evaluate dengan cross-validation
  □ Hyperparameter sudah di-tune (GridSearchCV / Optuna)
  □ Model sudah disimpan dengan joblib/pickle + versi
  □ API sudah punya health check endpoint
  □ API sudah punya input validation (Pydantic)
  □ API sudah punya error handling (try/except + HTTPException)
  □ Docker image sudah dibuild dan ditest
  □ Dockerfile sudah ada health check
  □ API docs tersedia (/docs atau /redoc)
  □ Monitoring sudah disetup (Evidently / custom)
  □ Logging sudah aktif (request/response + errors)
  □ Environment variables untuk secrets
  □ Concurrency handling (uvicorn workers)
  □ Rate limiting (jika public API)
  □ CI/CD pipeline sudah disetup (GitHub Actions)
  □ Rollback plan sudah ada
"""
print(checklist)
```

---

## Ringkasan Pola Penulisan

| Topik | Pola Kunci |
|---|---|
| FastAPI | `@app.post("/predict")`, `BaseModel`, `HTTPException` |
| FastAPI run | `uvicorn main:app --host 0.0.0.0 --port 8000 --reload` |
| Docker | `docker build -t`, `docker run -d -p`, `docker-compose up -d` |
| MLflow | `mlflow.start_run()`, `mlflow.log_metric()`, `mlflow.sklearn.autolog()` |
| Batch predict | Load model + scaler, predict, save CSV |
| Drift detection | `stats.ks_2samp()` untuk setiap kolom |
| Gradio | `gr.Interface(fn=predict, inputs=..., outputs=...)` |
| Health check | `/health` endpoint, `/ready` endpoint |
| Graceful shutdown | `signal.signal(signal.SIGTERM, handler)` |

---

`★ Insight ─────────────────────────────────────`
**1. FastAPI async**: FastAPI natively supports `async def`. Jika model inference lambat (misal: deep learning), gunakan `run_in_executor` supaya tidak blocking event loop. Untuk model ML sklearn yang cepat, synchronous handler sudah cukup.

**2. MLflow registered model**: `models:/name/version` URI mengijinkan versioning. Production deployment sebaiknya pakai version number, bukan "latest" — supaya perubahan model baru tidak langsung break production tanpa testing.
`─────────────────────────────────────────────────`

---

**Lanjut:** Buka `06_mlops_deployment.ipynb` — train model, serve dengan FastAPI, track dengan MLflow, dan deploy dengan Docker.
