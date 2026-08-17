# Belajar Big Data, Machine Learning & AI

Repository ini adalah kurikulum praktik untuk Python, analisis data, machine learning, deep learning, dan MLOps. Mulai dari [TUTORIAL.md](TUTORIAL.md), lalu ikuti [panduan belajar](STUDY_GUIDE.md) dan checklist di `ROADMAP_TRACKER.txt`.

---

## Struktur

```
belajar-bigdata-machinelearning-ai/
├── materi/
│   ├── 00_math_statistics/       # Matematika, statistik, eksperimen
│   ├── 01_python_fundamental/   # Python dasar (variabel, loop, fungsi, ekosistem)
│   ├── 02_data_analysis/        # NumPy, Pandas, Matplotlib, Seaborn, EDA
│   ├── 03_ml_fundamental/       # ML supervised, unsupervised, evaluasi
│   ├── 04_ml_advanced/           # Tuning, pipeline, ensemble, imbalanced data
│   ├── 05_deep_learning/        # Neural network, CNN, RNN/LSTM, transfer learning
│   ├── 06_mlops_deployment/     # MLflow, Flask/FastAPI, Docker, monitoring
│   ├── 07_big_data_data_engineering/ # SQL, Spark, streaming, warehouse
│   ├── 08_nlp_transformers/     # NLP, embedding, Transformer, RAG
│   ├── 09_ai_systems_cloud/     # reliability, cloud, security, governance
│   └── 10_digital_twin/         # IoT, simulasi, telemetry, twin, safety
│
├── ROADMAP_TRACKER.txt          # Progress tracker sampai jalur Big Data/AI lanjut
├── STUDY_GUIDE.md               # Urutan belajar, proyek, dan cara problem solving
└── requirements.txt             # Environment Python yang dapat diulang
```

Setiap folder level berisi:
- `README.md`   — Materi teori sangat detail (bukan hanya inti, tapi penjelasan kenapa)
- `praktikum.md` — Soal latihan per topik
- `TEORI_MENDALAM.md` — Teori luas: konsep, asumsi, rumus/arsitektur, batasan, dan hubungan ke praktik
- `TUTORIAL_PENYELESAIAN.md` — Cara berpikir, langkah pengerjaan, verifikasi, dan debugging
- `SOLUSI_DAN_TEORI_LENGKAP.md` — Teori rinci serta solusi kode untuk konsep dan latihan utama
- `*.ipynb`     — Notebook Jupyter untuk dikerjakan langsung (tersedia di Level 01–06)

Mulai setiap latihan dari [CARA_MENGERJAKAN_LATIHAN.md](CARA_MENGERJAKAN_LATIHAN.md), lalu buka tutorial penyelesaian di folder level yang sedang dipelajari hanya setelah mencoba sendiri.

---

## Roadmap Belajar

```
Level 0 ─ Matematika, Statistik & Eksperimen
  │
Level 1 ─ Python Fundamental
  │
Level 2 ─ Data Analysis & SQL
  │
Level 3 ─ ML Fundamental
  │
Level 4 ─ ML Lanjutan
  │
Level 5 ─ Deep Learning
   │
Level 6 ─ MLOps & Deployment
   │
Level 7 ─ Big Data & Data Engineering
   │
Level 8 ─ NLP, Transformer & Generative AI
   │
Level 9 ─ AI Systems, Cloud & Governance
   │
Level 10 ─ Digital Twin & Industrial AI
```

Level 00–09 sekarang memiliki teori dan praktik Markdown. Level 01–06 juga memiliki notebook interaktif. Notebook untuk Level 07–09 dapat ditambahkan setelah dependency opsional dipasang; contoh kode dan latihan sudah disediakan agar pembelajaran tetap dapat dimulai tanpa cluster/cloud.

---

## Cara Belajar

### Per Level:

1. **Baca `materi/XX_nama/README.md`** — Pahami teori dan konsep (baca pelan-pelan)
2. **Buka `materi/XX_nama/XX_nama.ipynb`** — Notebook untuk dikerjakan langsung
3. **Kerjakan `materi/XX_nama/praktikum.md`** — Soal latihan tambahan
4. **Review** — Pahami setiap baris kode, tidak hanya jalankan

### Prinsip:

- **Ketik ulang** semua kode. Jangan copy-paste.
- Baca error message sebelum bertanya.
- Jika tidak paham satu baris: pecah jadi bagian kecil, test satu per satu.
- Setelah bisa menjalankan, coba modifikasi: "Apa yang terjadi jika...".

---

## Persiapan Environment

```bash
# Buat virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows

# Install dependency yang dipakai materi
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Dependency lanjutan dipasang sesuai jalur, tidak harus semuanya
python -m pip install -r requirements-bigdata.txt
python -m pip install -r requirements-nlp.txt
python -m pip install -r requirements-digital-twin.txt

# Daftarkan environment ini sebagai kernel notebook (jalankan sekali)
python -m ipykernel install --user --name belajar-ai --display-name "Python (belajar-ai)"

# Jalankan notebook
jupyter lab
```

Docker bukan package Python. Untuk latihan container di Level 6, instal Docker Desktop secara terpisah dan pastikan `docker --version` berhasil di terminal.

Di JupyterLab, pilih kernel **Python (belajar-ai)** untuk setiap notebook. Jika `import numpy` gagal padahal sudah instal dependency, hampir pasti notebook sedang memakai kernel Python lain.

---

## Library per Level

| Level | Library | Tujuan |
|---|---|---|
| 0 | NumPy, SciPy | Matematika dan statistik |
| 1 | Python stdlib | Fondasi |
| 2 | numpy, pandas, matplotlib, seaborn | Data manipulation & visualisasi |
| 3 | scikit-learn | ML models & evaluasi |
| 4 | scikit-learn, imbalanced-learn | Advanced ML |
| 5 | tensorflow, pillow | Deep learning |
| 6 | mlflow, FastAPI, Flask, joblib | MLOps |
| 7 | DuckDB, PySpark, Polars | Big Data & data engineering |
| 8 | PyTorch, Transformers, sentence-transformers | NLP & generative AI |
| 9 | Docker, cloud SDK, pytest | Sistem produksi & governance |
| 10 | NumPy, Pandas, SimPy, MQTT | Digital twin & industrial AI |

---

## Dataset yang Digunakan

- **Level 2+**: Iris dataset (`sklearn.datasets.load_iris()` atau `sns.load_dataset('iris')`)
- **Level 3+**: Breast Cancer, Diabetes (`sklearn.datasets`)
- **Level 4+**: Titanic dari Kaggle atau data sintetis
- **Level 5+**: MNIST (`tensorflow.keras.datasets.mnist`)

---

## Progress Tracker

Gunakan `ROADMAP_TRACKER.txt` untuk mencatat progress belajar.

| Level | Status | Tanggal Selesai |
|---|---|---|
| 01 — Python Fundamental | [ ] | |
| 02 — Data Analysis | [ ] | |
| 03 — ML Fundamental | [ ] | |
| 04 — ML Lanjutan | [ ] | |
| 05 — Deep Learning | [ ] | |
| 06 — MLOps & Deployment | [ ] | |

---

## Tips

- **1–2 jam/hari** lebih baik daripada belajar maraton hanya di akhir pekan.
- Tulis notes tangan untuk konsep yang sulit.
- Ajarkan ke orang lain (fake teaching) — ini cara terbaik untuk verifikasi pemahaman.
- Jika stuck > 15 menit di satu error: istirahat, kembali dengan fresh mind.
