# Belajar Big Data, Machine Learning, AI, dan Digital Twin

Repository ini adalah kurikulum praktik dari programming/data sampai **general-purpose Intelligent Digital Twin**. Mining tersedia sebagai salah satu domain contoh—bukan tujuan tunggal. Ukuran kemajuan bukan jumlah file yang dibaca, melainkan kemampuan menjelaskan teori, menulis kode, menguji failure mode, mengukur uncertainty, dan mempertanggungjawabkan keputusan.

Mulai dari [tutorial penggunaan](TUTORIAL.md), baca [panduan belajar berbasis gate](STUDY_GUIDE.md), lalu catat bukti di [roadmap tracker](ROADMAP_TRACKER.txt). Hasil audit dan gap yang masih terbuka ada di [GAP_ANALYSIS.md](GAP_ANALYSIS.md).

## Struktur aktual

```text
materi/
├── 00_math_statistics/                    matematika, statistik, eksperimen
├── 01_python_fundamental/                 Python dan problem solving
├── 02_data_analysis/                      NumPy, Pandas, EDA
├── 03_ml_fundamental/                     supervised/unsupervised/evaluasi
├── 04_ml_advanced/                        pipeline, tuning, ensemble, imbalance
├── 05_deep_learning/                      NN, CNN, sequence, transfer learning
├── 06_mlops_deployment/                   API, model lifecycle, Docker, monitoring
├── 07_big_data_data_engineering/          SQL, Spark, streaming, warehouse
├── 08_nlp_transformers/                   NLP, attention, Transformer, RAG
├── 09_ai_systems_cloud/                   reliability, cloud, security, governance
├── 10_digital_twin/                       foundation + tested reference code
├── 11_iot_telemetry_connectivity/         sensor, PLC, MQTT, OPC UA, event semantics
├── 12_time_series_state_estimation/       temporal validation, Kalman, fusion
├── 13_simulation_physics_hybrid/          simulation, calibration, hybrid model
├── 14_anomaly_predictive_maintenance_rul/ anomaly, fault, PdM, RUL
├── 15_architecture_semantics_spatial/      architecture, ontology/graph, GIS/3D
├── 16_optimization_intelligent_twin/       optimization, RL, HITL, safety/security
└── 17_domains_research_capstone/           domains, research, expert platform
```

Folder `00`–`09` adalah fondasi existing yang dipertahankan. Track `10`–`17` mengubah satu chapter Digital Twin yang sebelumnya ringkas menjadi jalur Early→Research. Nomor folder adalah urutan kurikulum, bukan klaim tingkat keahlian.

## Jalur kompetensi dan gate

```text
FOUNDATION → DATA → ML → SYSTEM
→ DIGITAL TWIN FOUNDATION → CONNECTED TWIN
→ PREDICTIVE TWIN → PRESCRIPTIVE TWIN
→ INTELLIGENT/FEDERATED TWIN → EXPERT/RESEARCH
```

Setiap gate membutuhkan lima jenis bukti:

1. teori yang dapat dijelaskan dengan kata sendiri;
2. kode inti yang dapat ditulis ulang;
3. project yang berjalan;
4. debugging/failure injection yang dapat dianalisis;
5. checkpoint dan trade-off yang dapat dipertahankan.

Membaca README atau berhasil menjalankan library belum cukup untuk lulus.

## Apa yang dimaksud Digital Twin di repository ini?

Digital Twin adalah representasi virtual beridentitas dari entity/process dunia nyata, disinkronkan pada frequency dan fidelity yang ditetapkan, memakai model untuk memahami atau memprediksi state, serta menghasilkan output yang dapat divalidasi untuk use case tertentu.

- 3D model tidak otomatis menjadi twin.
- Dashboard atau IoT dashboard tidak otomatis menjadi twin.
- Simulation tanpa koneksi terpelihara ke instance nyata adalah digital model.
- IoT tidak mutlak bila sinkronisasi manual/batch memang sesuai use case.
- Feedback ke actuator tidak selalu wajib; jika ada, safety dan authorization meningkat drastis.

Mulai dari [Digital Twin Fundamental](materi/10_digital_twin/README.md).

## Reference implementation yang dapat diuji

Chapter 10 memiliki package kecil tanpa dependency eksternal untuk mengajarkan boundary inti:

```text
TelemetryEvent → validation/dedup/order → estimated state + uncertainty
→ residual anomaly → recommendation → safety guard + human approval
```

Jalankan:

```bash
cd materi/10_digital_twin
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m digital_twin_lab.demo --steps 500 --fault-step 300
```

Audit link lokal, JSON/sintaks notebook, sintaks Python, dan generated artifact dari root repository:

```bash
python scripts/audit_repository.py
```

Kode memisahkan plant ground truth, noisy/missing sensor, estimator, detector, dan command boundary agar leakage terlihat. Ini reference implementation pedagogis, bukan safety controller produksi.

## Persiapan environment

Python 3.11 direkomendasikan.

```bash
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate           # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Dependency opsional dipasang hanya saat mengambil track-nya:

```bash
python -m pip install -r requirements-bigdata.txt
python -m pip install -r requirements-nlp.txt
python -m pip install -r requirements-digital-twin.txt
```

Docker, broker MQTT/Kafka, OPC UA server, dan cloud service bukan package Python; siapkan terpisah saat chapter terkait memerlukannya. Jangan memasukkan credentials ke notebook atau Git.

## Cara belajar setiap topik

Gunakan pola berikut meskipun satu chapter belum menyediakan semua dalam file terpisah:

1. sejarah/konteks dan masalah;
2. alasan konsep muncul dan mental model;
3. teori, matematika, assumptions;
4. cara kerja internal;
5. implementasi minimal dari nol;
6. implementasi library/framework;
7. example dan controlled experiment;
8. common mistakes, anti-pattern, debugging;
9. latihan, challenge, mini project;
10. checkpoint dan hubungan ke Digital Twin.

Notebook existing ada pada chapter tertentu, bukan semua folder. Jangan menganggap absennya notebook berarti kode konseptual production-ready; status material dijelaskan di [gap analysis](GAP_ANALYSIS.md).

## Project ladder

| Tahap | Project | Bukti utama |
|---|---|---|
| Beginner | simulated temperature sensor, tank shadow | timestamp/unit/quality benar; plant ≠ sensor |
| Intermediate | synchronized tank/HVAC/motor | estimator, uncertainty, anomaly, delayed/missing data |
| Advanced | predictive maintenance/RUL/forecast | temporal+asset holdout, calibration, detection delay |
| Professional | broker + state/history/model API + dashboard | replay, observability, Docker, failure recovery |
| Expert | configurable Intelligent Digital Twin Platform | multi-asset abstraction, what-if, optimization, approval, safety/security, research evidence |

Spesifikasi capstone berada di [chapter 17](materi/17_domains_research_capstone/README.md).

## Batas repository saat ini

Track Digital Twin kini memiliki coverage teori luas dan tested core. Namun repository belum menyediakan broker/cloud deployment end-to-end, database persistence, GIS/3D executable project, full predictive-maintenance notebook, CI, atau capstone platform lengkap. Itu adalah workstream lanjutan yang sengaja dinyatakan terbuka; “expert” hanya diberikan setelah deliverable dan evidence benar-benar dibuat.

## Referensi authoritative awal

- [ISO/IEC 30173 — Digital twin concepts and terminology](https://www.iso.org/standard/81442.html)
- [ISO 23247-1 — framework for manufacturing](https://www.iso.org/standard/75066.html)
- [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
- [OPC Foundation — OPC UA specifications](https://opcfoundation.org/developer-tools/specifications-unified-architecture)
- [NIST IR 8356 — Digital Twin security and trust](https://csrc.nist.gov/pubs/ir/8356/final)

Gunakan relative links untuk navigasi repository dan sumber resmi untuk klaim standard/protocol yang dapat berubah.
