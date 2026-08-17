# Panduan Kode — Chapter 04: Machine Learning Lanjutan

> File ini adalah **cheat sheet idiom dan anti-pattern** yang akan kamu temui di chapter ini. Bukan duplikat notebook — buka hanya saat kamu butuh mengingat sintaks atau ingin menghindari jebakan umum. Notebook utama `04_ml_advanced.ipynb` adalah sumber pengalaman belajarmu; file ini melengkapi.

---

## 1. Feature Engineering — Membuat Fitur yang Bermakna

### 1.1 Pola: tiga transformasi numerik yang paling sering dipakai

```python
import numpy as np
import pandas as pd

# Log transform — untuk data skewed (harga, pendapatan, view count)
df["log_harga"] = np.log1p(df["harga"])           # log(1+x), aman untuk 0
df["sqrt_jarak"] = np.sqrt(df["jarak"])           # lebih lembut dari log

# Yeo-Johnson power transform — bikin distribusi mendekati normal
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method="yeo-johnson")
X_norm = pt.fit_transform(X)                      # output mean≈0, std≈1

# Binning kontinu → kategorik
df["usia_kat"] = pd.cut(df["usia"],
    bins=[0, 18, 30, 50, 100],
    labels=["remaja", "dewasa_awal", "dewasa", "lansia"])
```

### 1.2 Pola: fitur interaksi dan rasio

Fitur rasio sering lebih informatif dari fitur absolut — karena menormalisasi pengaruh ukuran. Contoh: harga per m², pendapatan per kapita, klik per impresi.

```python
df["harga_per_m2"] = df["harga"] / df["luas"]
df["income_per_member"] = df["household_income"] / df["household_size"]
df["rasio_klik_impresi"] = df["klik"] / (df["impresi"] + 1)   # +1 agar tidak bagi 0
```

### 1.3 Pola: ekstrak komponen datetime

```python
df["tgl"] = pd.to_datetime(df["tanggal"])
df["tahun"] = df["tgl"].dt.year
df["bulan"] = df["tgl"].dt.month
df["hari_dalam_minggu"] = df["tgl"].dt.dayofweek           # 0=Senin, 6=Minggu
df["is_weekend"] = df["tgl"].dt.dayofweek.isin([5, 6]).astype(int)
df["hari_sejak_awal"] = (df["tgl"] - df["tgl"].min()).dt.days
```

### 1.4 Pola: polynomial features menangkap non-linearitas

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_poly = poly.fit_transform(X)       # degree=2 dari 4 fitur → 14 fitur (4 + 4 + 6)
# interaction_only=True → hanya hasil kali (x1*x2), bukan x1², x2²
```

### 1.5 Anti-pattern: fit_transform PowerTransformer di seluruh data

```python
# SALAH — data leakage
pt = PowerTransformer()
X_all = pt.fit_transform(X)              # hitung parameter dari SEMUA data
X_train, X_test, y_train, y_test = train_test_split(X_all, y)

# BENAR — fit hanya di train
pt = PowerTransformer()
X_train = pt.fit_transform(X_train)
X_test = pt.transform(X_test)
```

Aturan yang sama berlaku untuk scaler, encoder, dan transformer apa pun yang belajar dari data.

---

## 2. Feature Selection — Menyaring Fitur yang Benar-Benar Penting

### 2.1 Pola: tiga metode sesuai situasi

| Metode | Cara kerja | Pakai saat |
|---|---|---|
| `VarianceThreshold` | Buang fitur yang variansinya nyaris nol (konstan) | Screening cepat, hapus fitur mati |
| `SelectKBest` | Pilih K fitur dengan skor statistik tertinggi (chi², f_classif) | Cepat, mudah diinterpretasi |
| `RFE` | Eliminasi rekursif: latih model, buang fitur terburuk, ulang | Lebih akurat, tapi lambat |

### 2.2 Pola: VarianceThreshold sebagai filter pertama

```python
from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.01)        # hapus fitur dengan var < 0.01
X_filtered = selector.fit_transform(X)
print(f"Sisa fitur: {X_filtered.shape[1]} dari {X.shape[1]}")
```

### 2.3 Pola: SelectKBest dengan skor F-klasifikasi

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(score_func=f_classif, k=10)
X_new = selector.fit_transform(X_train, y_train)
mask = selector.get_support()                       # boolean array, True = fitur terpilih
selected_features = X.columns[mask]
```

### 2.4 Pola: RFE dengan estimator

```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

rfe = RFE(estimator=RandomForestClassifier(n_estimators=100, random_state=42),
          n_features_to_select=10, step=1)
X_rfe = rfe.fit_transform(X_train, y_train)
print("Ranking tiap fitur:", rfe.ranking_)          # 1 = terpilih, 2+ = urutan eliminasi
```

### 2.5 Anti-pattern: SelectKBest lalu refit scaler di seluruh data

```python
# SALAH — fit scaler di data yang sudah di-select dari semua data
selector = SelectKBest(k=10)
X_sel = selector.fit_transform(X, y)                # lihat SEMUA data
X_train, X_test, y_train, y_test = train_test_split(X_sel, y)

# BENAR — pipeline: scaling + selection di dalam CV
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("select", SelectKBest(k=10)),
    ("model", LogisticRegression())
])
```

---

## 3. Hyperparameter Tuning — Mencari Setting Terbaik

### 3.1 Pola: tiga metode sesuai skala ruang pencarian

| Metode | Cara kerja | Pakai saat |
|---|---|---|
| `GridSearchCV` | Coba SEMUA kombinasi eksplisit | Ruang kecil (<100 kombinasi) |
| `RandomizedSearchCV` | Sampel acak N kombinasi | Ruang besar, waktu terbatas |
| `Optuna` | Bayesian optimization, belajar dari percobaan sebelumnya | Ruang besar, hasil terbaik |

### 3.2 Pola: GridSearchCV dasar

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "C": [0.1, 1, 10],
    "max_depth": [3, 5, 10, None]
}
grid = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1                             # pakai semua core
)
grid.fit(X_train, y_train)
print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)
best_model = grid.best_estimator_
```

### 3.3 Pola: RandomizedSearchCV untuk ruang besar

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_dist = {
    "n_estimators": randint(50, 500),
    "max_depth": randint(3, 20),
    "min_samples_split": randint(2, 20)
}
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=50,                           # coba 50 kombinasi acak
    cv=5,
    scoring="f1",
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train, y_train)
```

### 3.4 Pola: Optuna untuk tuning paling efisien

```python
import optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)   # quiet mode

def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True)
    }
    model = xgb.XGBClassifier(**params, random_state=42)
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
    return scores.mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50, show_progress_bar=False)
print("Best params:", study.best_params)
print("Best CV F1:", study.best_value)
```

### 3.5 Anti-pattern: tuning dengan data test

```python
# SALAH — data test dipakai untuk tuning → akurasi jadi bias
for C in [0.1, 1, 10]:
    model = LogisticRegression(C=C).fit(X_train, y_train)
    acc = model.score(X_test, y_test)              # JANGAN
    if acc > best_acc:
        best_C = C

# BENAR — tuning pakai CV di data train, simpan test untuk evaluasi akhir
grid = GridSearchCV(model, param_grid, cv=5, scoring="f1")
grid.fit(X_train, y_train)
final_acc = grid.score(X_test, y_test)              # sentuh test sekali di akhir
```

### 3.6 Anti-pattern: n_jobs=-1 tanpa cv yang reproducible

```python
# SALAH — hasil beda tiap run
RandomizedSearchCV(..., n_jobs=-1)

# BENAR — set random_state untuk reproduktifitas
RandomizedSearchCV(..., n_jobs=-1, random_state=42)
```

---

## 4. Ensemble Methods — Menggabungkan Banyak Model

### 4.1 Pola: tiga keluarga ensemble

| Keluarga | Cara kerja | Contoh |
|---|---|---|
| Voting | Rata-rata prediksi banyak model berbeda | `VotingClassifier(estimators=[...])` |
| Stacking | Meta-model belajar dari prediksi base models | `StackingClassifier(estimators=[...])` |
| Boosting | Model dilatih berurutan, masing-masing perbaiki kesalahan sebelumnya | `XGBClassifier`, `LGBMClassifier` |

### 4.2 Pola: VotingClassifier soft (pakai probabilitas)

```python
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000, random_state=42)),
        ("rf", RandomForestClassifier(n_estimators=100, random_state=42))
    ],
    voting="soft"                            # "hard" = majority vote, "soft" = rata-rata probabilitas
)
voting.fit(X_train, y_train)
```

### 4.3 Pola: StackingClassifier

```python
from sklearn.ensemble import StackingClassifier
from sklearn.neighbors import KNeighborsClassifier

stacking = StackingClassifier(
    estimators=[
        ("rf", RandomForestClassifier(n_estimators=100, random_state=42)),
        ("xgb", xgb.XGBClassifier(n_estimators=100, random_state=42))
    ],
    final_estimator=LogisticRegression(max_iter=1000, random_state=42),
    cv=5                                      # base models di-CV untuk dapat prediksi OOF
)
stacking.fit(X_train, y_train)
```

### 4.4 Pola: XGBoost untuk klasifikasi

```python
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    use_label_encoder=False,
    eval_metric="logloss"                     # diamkan warning
)
model.fit(X_train, y_train)
y_proba = model.predict_proba(X_test)[:, 1]   # probabilitas kelas positif
```

### 4.5 Pola: LightGBM (lebih cepat dari XGBoost untuk data besar)

```python
import lightgbm as lgb

model = lgb.LGBMClassifier(
    n_estimators=200,
    max_depth=-1,                             # -1 = no limit
    learning_rate=0.1,
    num_leaves=31,
    random_state=42,
    verbose=-1
)
model.fit(X_train, y_train)
```

### 4.6 Anti-pattern: gabungkan model yang SAMA variasinya

```python
# SALAH — ensemble 5 Random Forest dengan hyperparam beda = sia-sia, mereka berkorelasi tinggi
VotingClassifier(estimators=[
    ("rf1", RandomForestClassifier(n_estimators=100)),
    ("rf2", RandomForestClassifier(n_estimators=200)),
    ...
])

# BENAR — ensemble model yang BERBEDA keluarga untuk diversitas
VotingClassifier(estimators=[
    ("lr", LogisticRegression()),
    ("rf", RandomForestClassifier()),
    ("xgb", xgb.XGBClassifier())
])
```

---

## 5. Time Series — Urutan Waktu Penting

### 5.1 Pola: resample untuk ubah frekuensi waktu

```python
df["tgl"] = pd.to_datetime(df["tanggal"])
df = df.set_index("tgl")

# Harian → bulanan (jumlah per bulan)
monthly = df.resample("M").sum()

# Harian → mingguan (rata-rata)
weekly = df.resample("W").mean()

# 3 hari sekali
tri_daily = df.resample("3D").mean()
```

### 5.2 Pola: rolling window untuk menghaluskan noise

```python
# 7-hari moving average
df["sales_ma7"] = df["sales"].rolling(window=7).mean()
df["sales_ma30"] = df["sales"].rolling(window=30).mean()

# Exponential weighted (beri bobot lebih besar ke data terbaru)
df["sales_ewm"] = df["sales"].ewm(span=7).mean()
```

### 5.3 Pola: lag features untuk prediksi

```python
# Prediksi sales hari ini berdasarkan sales 1, 7, 30 hari lalu
df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)
df["lag_30"] = df["sales"].shift(30)
df = df.dropna()                                # drop baris dengan NaN dari shift
```

### 5.4 Pola: TimeSeriesSplit untuk validasi time-aware

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
# Fold 1: train [0:100], test [100:120]
# Fold 2: train [0:120], test [120:140]
# dst — data test SELALU setelah data train (tidak boleh acak!)

for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    # model.fit(...) dan evaluasi
```

### 5.5 Anti-pattern: train/test split acak untuk time series

```python
# SALAH — masa depan bocor ke masa lalu
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# BENAR — split kronologis: train = lama, test = baru
split_idx = int(len(X) * 0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]
```

### 5.6 Anti-pattern: fit StandardScaler di seluruh deret waktu

```python
# SALAH — mean dan std dihitung dari data test juga
scaler = StandardScaler()
X_all = scaler.fit_transform(X)

# BENAR — fit hanya di train
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

## 6. Imbalanced Dataset — Ketika Satu Kelas Jarang

### 6.1 Pola: tiga strategi umum

| Strategi | Cara kerja | Trade-off |
|---|---|---|
| `class_weight="balanced"` | Loss function beri bobot proporsional kebalikan frekuensi | Tidak tambah data, ubah bobot training |
| Oversampling (misal `RandomOverSampler`) | Gandakan sampel kelas minoritas | Risiko overfit pada duplikat |
| SMOTE | Buat sampel sintetis kelas minoritas dengan interpolasi | Lebih beragam dari random, tapi sintetis |

### 6.2 Pola: class_weight balanced

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",                 # atau dict manual: {0:1, 1:99}
    random_state=42
)
model.fit(X_train, y_train)
```

Untuk `LogisticRegression`: `LogisticRegression(class_weight="balanced")`.

### 6.3 Pola: SMOTE via imbalanced-learn

```python
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline        # PENTING: pakai pipeline imblearn, bukan sklearn

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)
print(f"Sebelum: {dict(pd.Series(y_train).value_counts())}")
print(f"Sesudah: {dict(pd.Series(y_res).value_counts())}")
```

### 6.4 Pola: SMOTE di dalam pipeline + CV

```python
from imblearn.pipeline import Pipeline as ImbPipeline

pipe = ImbPipeline([
    ("scaler", StandardScaler()),
    ("smote", SMOTE(random_state=42)),
    ("model", LogisticRegression(max_iter=1000, random_state=42))
])
scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="f1")
```

### 6.5 Anti-pattern: SMOTE di data test

```python
# SALAH — sintetis di data test = evaluasi bias
smote = SMOTE()
X_all, y_all = smote.fit_resample(X, y)        # test ikut disintesis
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all)

# BENAR — SMOTE hanya di train
smote = SMOTE()
X_train, y_train = smote.fit_resample(X_train, y_train)
X_test, y_test = X_test, y_test                 # test apa adanya
```

### 6.6 Anti-pattern: pakai akurasi untuk data imbalanced

```python
# SALAH — 99% akurasi untuk data 99:1 = model bodoh yang selalu tebak kelas mayoritas
model.fit(X_train, y_train)
print(model.score(X_test, y_test))             # 0.99 — menyesatkan!

# BENAR — pakai F1, ROC-AUC, atau PR-AUC untuk data imbalanced
from sklearn.metrics import f1_score, roc_auc_score
print("F1:", f1_score(y_test, model.predict(X_test)))
print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))
```

---

## 7. ROC-AUC, Precision-Recall, dan Threshold Tuning

### 7.1 Pola: kapan pakai ROC-AUC vs PR-AUC

| Kurva | Sumbu X | Sumbu Y | Pakai saat |
|---|---|---|---|
| ROC | FPR | TPR (recall) | Kelas seimbang, ingin lihat trade-off global |
| PR | Recall | Precision | **Imbalanced**, kelas positif lebih penting |

### 7.2 Pola: hitung ROC-AUC

```python
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

y_proba = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_proba)           # 0.5 = random, 1.0 = sempurna

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label=f"ROC (AUC={auc:.3f})")
plt.plot([0,1], [0,1], "k--")
plt.xlabel("FPR"); plt.ylabel("TPR"); plt.legend()
```

### 7.3 Pola: pilih threshold optimal dari kurva PR

```python
from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
# F1 = 2 * (P * R) / (P + R)
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
best_idx = f1_scores.argmax()
best_threshold = thresholds[best_idx]
print(f"Threshold terbaik: {best_threshold:.3f}, F1: {f1_scores[best_idx]:.3f}")
```

### 7.4 Pola: pakai threshold sendiri saat prediksi

```python
custom_threshold = 0.3                          # lebih rendah dari default 0.5
y_proba = model.predict_proba(X_test)[:, 1]
y_pred_custom = (y_proba >= custom_threshold).astype(int)
```

### 7.5 Anti-pattern: pakai predict() langsung untuk data imbalanced

```python
# SALAH — threshold default 0.5 sering salah untuk data imbalanced
y_pred = model.predict(X_test)

# BENAR — pakai predict_proba lalu threshold eksplisit
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= 0.3).astype(int)           # 0.3 = chosen threshold
```

---

## 8. Model Persistence — Simpan dan Muat Model

### 8.1 Pola: joblib untuk model scikit-learn (lebih cepat dari pickle)

```python
import joblib

# Simpan
joblib.dump(model, "model_v1.pkl")

# Muat
loaded_model = joblib.load("model_v1.pkl")
y_pred = loaded_model.predict(X_new)
```

### 8.2 Pola: simpan pipeline (scaler + model jadi satu file)

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
pipe.fit(X_train, y_train)
joblib.dump(pipe, "pipeline_v1.pkl")            # scaler + model jadi satu
```

### 8.3 Pola: pickle sebagai fallback

```python
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)
```

### 8.4 Anti-pattern: simpan model dan scaler terpisah tanpa versioning

```python
# SALAH — kalau scaler atau model diupdate, sinkronisasi hilang
joblib.dump(scaler, "scaler.pkl")
joblib.dump(model, "model.pkl")                 # versi mana? parameter apa?

# BENAR — satu file pipeline + timestamp/nama versi
joblib.dump(pipe, f"pipeline_{timestamp}_v1.pkl")
```

### 8.5 Anti-pattern: pickle model dari environment yang berbeda

```python
# SALAH — pickle hanya aman untuk Python + library versi yang sama
# Model di-train dengan scikit-learn 1.3 di Python 3.10
# Di-load di scikit-learn 1.0 Python 3.8 → bisa crash

# Untuk kompatibilitas luas: ONNX, skops, atau simpan hyperparameters + retrain
```

---

## 9. Pola End-to-End Pipeline

### 9.1 Pola: pipeline lengkap untuk tabular supervised

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

# 1. Pisahkan fitur numerik & kategorik
num_cols = ["age", "income", "tenure"]
cat_cols = ["plan_type", "region"]

# 2. Preprocessor per jenis kolom
num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipe, num_cols),
    ("cat", cat_pipe, cat_cols)
])

# 3. Pipeline final
pipe = Pipeline([
    ("preprocess", preprocessor),
    ("model", RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced"))
])

# 4. Train + evaluasi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y, random_state=42)
pipe.fit(X_train, y_train)
scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="f1")
print(f"CV F1: {scores.mean():.3f} ± {scores.std():.3f}")

# 5. Evaluasi akhir di test
from sklearn.metrics import classification_report
print(classification_report(y_test, pipe.predict(X_test)))
```

### 9.2 Pola: tuning hyperparameter dalam pipeline

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "model__n_estimators": [100, 200, 500],
    "model__max_depth": [5, 10, None]
}
grid = GridSearchCV(pipe, param_grid, cv=5, scoring="f1", n_jobs=-1)
grid.fit(X_train, y_train)
print("Best:", grid.best_params_, "CV F1:", grid.best_score_)
```

### 9.3 Anti-pattern: preprocessing di luar pipeline

```python
# SALAH — preprocessing manual, lalu fit model → data leakage saat CV
X_scaled = scaler.fit_transform(X)             # lihat seluruh data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
model.fit(X_train, y_train)                    # CV di sini tetap pakai X_scaled yang bocor

# BENAR — semua preprocessing + model dalam pipeline, CV yang fit_transform-ulang tiap fold
```

---

## 10. One-Liner Patterns

Kumpulan snippet pendek yang sering dipakai ulang:

```python
# Pipeline scaling + model
pipe = make_pipeline(StandardScaler(), LogisticRegression())

# Train/test split stratified + reproducible
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                     stratify=y, random_state=42)

# Cross-validation stratified
scores = cross_val_score(model, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=42),
                          scoring="f1")

# Confusion matrix + classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Probabilitas kelas positif
y_proba = model.predict_proba(X_test)[:, 1]

# ROC AUC
print(roc_auc_score(y_test, y_proba))

# Simpan & muat model
joblib.dump(pipe, "model.pkl")
pipe = joblib.load("model.pkl")

# Hitung feature importance dari tree model
importances = pd.Series(model.feature_importances_, index=feature_names).sort_values(ascending=False)

# Bikin data sintetis untuk eksperimen
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10,
                           weights=[0.95, 0.05], random_state=42)   # 5% minoritas
```

---

## 11. Anti-Pattern Ringkasan

Daftar pendek anti-pattern yang paling sering bikin model "tidak berguna":

| Anti-pattern | Gejala | Solusi |
|---|---|---|
| Fit scaler/encoder di seluruh data | Akurasi CV terlalu optimis | Pakai `Pipeline` |
| Tuning dengan data test | Laporan akurasi bias | Tuning di CV, test disentuh sekali |
| Train/test split acak untuk time series | Masa depan bocor ke masa lalu | Pakai `TimeSeriesSplit` atau split kronologis |
| SMOTE di data test | Evaluasi bias | SMOTE hanya di train, lebih baik dalam pipeline |
| Pakai akurasi untuk data imbalanced | 99% tapi model bodoh | Pakai F1, ROC-AUC, atau PR-AUC |
| Threshold default 0.5 untuk data imbalanced | False negative/positive tinggi | Threshold tuning dari PR curve |
| Ensemble model yang mirip | Tidak ada diversitas, ensemble sia-sia | Pakai model dari keluarga berbeda |
| Simpan scaler dan model terpisah tanpa versioning | Sinkronisasi hilang saat deploy | Simpan satu file pipeline + versi |
| Polynomial degree tinggi tanpa CV | Overfit parah | `GridSearchCV` untuk pilih degree |
| Lupa `random_state` | Hasil tidak bisa direproduksi | Set `random_state=42` di semua estimator |

---

## 12. Cheat Sheet Algoritma

| Algoritma | Keluarga | Pakai saat | Hyperparameter kunci |
|---|---|---|---|
| `LogisticRegression` | Linear | Data linearly separable, butuh probabilitas | `C`, `penalty`, `class_weight` |
| `RandomForestClassifier` | Tree ensemble | Baseline kuat, fitur campuran | `n_estimators`, `max_depth`, `max_features` |
| `XGBClassifier` | Gradient boosting | Kompetisi, data tabular | `n_estimators`, `max_depth`, `learning_rate` |
| `LGBMClassifier` | Gradient boosting | Dataset besar (jauh lebih cepat dari XGB) | `n_estimators`, `num_leaves`, `learning_rate` |
| `VotingClassifier` | Ensemble | Gabungkan model berbeda keluarga | `voting` (hard/soft), `estimators` |
| `StackingClassifier` | Ensemble | Meta-model belajar bobot optimal | `estimators`, `final_estimator` |

**Default pertama yang harus dicoba untuk data tabular:** `LGBMClassifier` atau `XGBClassifier` — keduanya hampir selalu mengalahkan Logistic Regression / Random Forest di data nyata.

---

## Catatan Penutup

Bab 04 menutupi teknik lanjutan yang membedakan praktisi ML biasa dari yang expert. Tiga hal yang paling sering bikin model "naik kelas":

1. **Feature engineering yang cermat** — fitur rasio, transformasi log untuk data skewed, ekstrak komponen datetime, lag untuk time series.
2. **Hyperparameter tuning yang benar** — Grid/Randomized/Optuna dalam pipeline, simpan test set untuk evaluasi akhir saja.
3. **Menangani kasus khusus** — imbalanced dataset dengan SMOTE/class_weight + threshold tuning, time series dengan TimeSeriesSplit, ensemble model dari keluarga berbeda.

Setelah chapter 04, kamu masuk ke chapter 05: Deep Learning — neural network, CNN, RNN/LSTM, transfer learning.
