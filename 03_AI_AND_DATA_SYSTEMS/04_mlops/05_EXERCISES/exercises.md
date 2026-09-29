# Praktikum — Level 6: MLOps & Deployment

> **Instruksi**: Ketik ulang setiap kode. Untuk bagian deployment, kamu perlu akses internet dan Docker. Jika belum punya Docker, tetap bisa mengikuti bagian kode dan test API secara local.
> **Waktu**: ~6–8 jam praktikum

---

## Latihan 1: Save & Load Model

**1.1.** Train model Random Forest di dataset Iris.
```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save
joblib.dump(model, 'models/model_rf.joblib')
print(f"Test accuracy: {model.score(X_test, y_test):.4f}")
```

**1.2.** Load model dari file. Prediksi 5 sample acak dari test set.
```python
loaded_model = joblib.load('models/model_rf.joblib')
predictions = loaded_model.predict(X_test[:5])
print(f"Predictions: {predictions}")
print(f"Actual:      {y_test[:5]}")
```

**1.3.** Train 3 model berbeda: LogisticRegression, DecisionTree, RandomForest.
- Save ke folder `models/` dengan nama berbeda.
- Load salah satu, cek akurasinya.

---

## Latihan 2: FastAPI — ML Prediction API

**2.1.** Buat file `main.py` dengan FastAPI:
```python
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(title="Iris Prediction API", version="1.0.0")

# Load model saat start
model = joblib.load('models/model_rf.joblib')

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, lt=10, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, lt=10, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, lt=10, description="Petal length in cm")
    petal_width: float = Field(..., gt=0, lt=10, description="Petal width in cm")

class PredictionResponse(BaseModel):
    prediction: int
    class_name: str
    probabilities: dict

@app.post("/predict", response_model=PredictionResponse)
def predict(data: IrisInput):
    features = np.array([[
        data.sepal_length, data.sepal_width,
        data.petal_length, data.petal_width
    ]])
    pred = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]

    class_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    probabilities = {class_names[i]: float(p) for i, p in enumerate(proba)}

    return PredictionResponse(
        prediction=pred,
        class_name=class_names[pred],
        probabilities=probabilities
    )

@app.get("/health")
def health():
    return {"status": "ok", "model": "RandomForest", "version": "1.0.0"}
```

**2.2.** Jalankan dengan `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

**2.3.** Buka `http://localhost:8000/docs` untuk auto-generated API docs. Test endpoint `/predict`.

**2.4.** Test dengan curl:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

**2.5.** Test dengan Python requests:
```python
import requests

response = requests.post("http://localhost:8000/predict", json={
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
})
print(response.json())
```

---

## Latihan 3: Flask API

**3.1.** Implementasi ulang Latihan 2 dengan Flask:
```python
# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Load model
model = joblib.load('models/model_rf.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    start = time.time()
    data = request.get_json()
    features = np.array([[
        data['sepal_length'], data['sepal_width'],
        data['petal_length'], data['petal_width']
    ]])
    pred = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0].tolist()

    latency = (time.time() - start) * 1000

    # Logging
    logging.info({
        "timestamp": time.time(),
        "input": data,
        "prediction": pred,
        "latency_ms": latency
    })

    return jsonify({
        'prediction': pred,
        'probabilities': proba,
        'latency_ms': round(latency, 2)
    })

@app.route('/model-info', methods=['GET'])
def model_info():
    return jsonify({
        'model': 'RandomForest',
        'n_estimators': 100,
        'n_features': 4,
        'classes': ['setosa', 'versicolor', 'virginica']
    })

@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    data = request.get_json()
    features = np.array(data['samples'])
    predictions = model.predict(features).tolist()
    return jsonify({'predictions': predictions})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**3.2.** Tambahkan logging: catat setiap request (timestamp, input, prediction, latency).

**3.3.** Test batch endpoint: kirim 3 samples sekaligus.

---

## Latihan 4: Docker — Containerize ML API

**4.1.** Buat `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**4.2.** Buat `requirements.txt`:
```
fastapi
uvicorn[standard]
joblib
numpy
scikit-learn
pandas
```

**4.3.** Build image:
```bash
docker build -t ml-api:v1 .
```

**4.4.** Run container:
```bash
docker run -p 8000:8000 --name ml-api-container ml-api:v1
```

**4.5.** Test API yang berjalan di dalam container.

**4.6.** Bonus: buat `docker-compose.yml` untuk API + streamlit UI.

---

## Latihan 5: Model Versioning dengan MLflow

**5.1.** Install MLflow: `pip install mlflow`

**5.2.** Setup MLflow tracking server:
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
# Buka http://localhost:5000
```

**5.3.** Modifikasi training script dengan MLflow tracking:
```python
import mlflow
from sklearn.metrics import accuracy_score, f1_score

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("iris-classifier")

# Log experiment 1: RandomForest
with mlflow.start_run(run_name="RandomForest-baseline"):
    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred, average='macro')

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(model, "random_forest_model")

# Log experiment 2: LogisticRegression
with mlflow.start_run(run_name="LogisticRegression-baseline"):
    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_param("max_iter", 1000)

    from sklearn.linear_model import LogisticRegression
    model2 = LogisticRegression(max_iter=1000, random_state=42)
    model2.fit(X_train, y_train)
    pred2 = model2.predict(X_test)

    mlflow.log_metric("accuracy", accuracy_score(y_test, pred2))
    mlflow.log_metric("f1_score", f1_score(y_test, pred2, average='macro'))
    mlflow.sklearn.log_model(model2, "logistic_regression_model")
```

**5.4.** Buka MLflow UI → bandingkan performa kedua model. Model mana yang lebih baik?

---

## Latihan 6: Data Drift Detection

**6.1.** Generate reference data dan current data (dengan drift):
```python
import numpy as np
from scipy.stats import ks_2samp

np.random.seed(42)
reference_data = np.random.randn(1000, 5)  # mean=0, std=1
np.random.seed(99)
current_data = np.random.randn(1000, 5) + np.array([2, 0.5, 1, 0, 0.5])  # mean bergeser!
```

**6.2.** Implementasi Kolmogorov-Smirnov test untuk deteksi drift per fitur:
```python
def detect_drift(reference, current, threshold=0.1):
    results = {}
    for i in range(reference.shape[1]):
        stat, p_value = ks_2samp(reference[:, i], current[:, i])
        results[f"feature_{i}"] = {
            "ks_statistic": round(stat, 4),
            "p_value": round(p_value, 4),
            "drifted": stat > threshold
        }
    return results

drift_results = detect_drift(reference_data, current_data, threshold=0.1)
for feat, result in drift_results.items():
    status = "DRIFTED" if result['drifted'] else "OK"
    print(f"{feat}: {status} (KS={result['ks_statistic']}, p={result['p_value']})")
```

**6.3.** Visualisasi distribusi reference vs current dengan overlay histogram.

**6.4.** Challenge: buat alert jika lebih dari 50% fitur drifting.

---

## Latihan 7: Batch Prediction Pipeline

**7.1.** Buat script `predict_batch.py`:
```python
import joblib
import pandas as pd
import numpy as np

def batch_predict(input_csv, output_csv, model_path, scaler_path):
    # Load model dan scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Baca CSV
    df = pd.read_csv(input_csv)

    # Preprocess
    X = df.values
    X_scaled = scaler.transform(X)

    # Predict
    predictions = model.predict(X_scaled)
    probabilities = model.predict_proba(X_scaled)

    # Simpan hasil
    df['prediction'] = predictions
    df['prob_class_0'] = probabilities[:, 0]
    df['prob_class_1'] = probabilities[:, 1]
    df['prob_class_2'] = probabilities[:, 2]

    df.to_csv(output_csv, index=False)
    print(f"Hasil disimpan ke {output_csv}")

# Usage
batch_predict('data/test_data.csv', 'data/predictions.csv',
              'models/model_rf.joblib', 'models/scaler.joblib')
```

**7.2.** Buat script `train_pipeline.py`:
1. Download/generate data
2. Preprocess (split, scale)
3. Train model
4. Evaluate
5. Save model + scaler
6. Log metrics ke file

---

## Latihan 8: Gradio Interface

**8.1.** Buat Gradio app untuk model classification:
```python
# app.py
import gradio as gr
import joblib
import numpy as np

model = joblib.load('models/model_rf.joblib')
iris_feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_classes = ['setosa', 'versicolor', 'virginica']

def predict(*features):
    features = np.array(features).reshape(1, -1)
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    return dict(zip(iris_classes, proba.tolist()))

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label='Sepal Length (cm)', value=5.1),
        gr.Number(label='Sepal Width (cm)', value=3.5),
        gr.Number(label='Petal Length (cm)', value=1.4),
        gr.Number(label='Petal Width (cm)', value=0.2),
    ],
    outputs=gr.Label(num_top_classes=3),
    title="🌸 Iris Flower Classifier",
    description="Klasifikasi bunga Iris ke 3 spesies menggunakan Random Forest"
)

demo.launch(server_name="0.0.0.0", server_port=7860)
```

**8.2.** Launch di local, coba interaksi dengan berbagai nilai.

**8.3.** Tambahkan visualisasi: bar chart probabilitas menggunakan matplotlib + gr.Plot()

---

## Tantangan: End-to-End Deployment Pipeline

**Deploy model ke cloud (gratis)**

### Langkah:

1. **Pilih dataset**: sklearn datasets (Iris, Wine, Breast Cancer)
2. **Train model** Random Forest
3. **Save model + scaler** ke file
4. **Buat FastAPI app** dengan 3 endpoints:
   - `POST /predict` — single prediction
   - `GET /model-info` — metadata model
   - `GET /health` — health check
5. **Buat Dockerfile**
6. **Deploy ke Railway / Render / Fly.io**
   - Railway: Connect GitHub repo → auto deploy dari Dockerfile
   - Render: Buat `render.yaml`
   - Fly.io: `fly launch`, `fly deploy`
7. **Test API** yang sudah di-deploy (bisa diakses dari internet!)
8. **Gradio UI**: deploy streamlit atau gradio app ke huggingface spaces

### Gratis deployment options:

| Platform | Kelebihan | Cara |
|---|---|---|
| **Render.com** | Easiest, auto-deploy dari GitHub | Connect repo → Dockerfile detected |
| **Railway.app** | $5 credit/month, cepat | `railway login`, `railway up` |
| **Fly.io** | 3 shared CPU gratis, persistent | `fly launch`, `fly deploy` |
| **Hugging Face Spaces** | Gratis untuk Gradio/Streamlit | Push to HF, create Space |

---

## Bonus: Streamlit Dashboard

```python
# dashboard.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

st.set_page_config(page_title="ML Model Dashboard", page_icon="📊")

model = joblib.load('models/model_rf.joblib')

st.title("📊 ML Model Monitoring Dashboard")

# Upload data
uploaded_file = st.file_uploader("Upload CSV data", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Prediksi
    if st.button("Prediksi"):
        predictions = model.predict(df.values)
        st.write(f"Total predictions: {len(predictions)}")
        st.bar_chart(pd.Series(predictions).value_counts())
```
