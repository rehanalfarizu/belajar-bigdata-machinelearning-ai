# Praktikum — Level 4: Machine Learning Lanjutan

> **Instruksi**: Ketik ulang setiap kode. Pahami bahwa feature engineering sering lebih penting daripada memilih algoritma yang lebih canggih.
> **Waktu**: ~6–8 jam praktikum

---

## Latihan 1: Feature Engineering

**1.1.** Dari data harga rumah:
```python
df = pd.DataFrame({
    'panjang': np.random.randint(50, 200, 100),
    'lebar': np.random.randint(30, 150, 100),
    'harga': np.random.randint(500_000_000, 5_000_000_000, 100)
})
```
Buat fitur baru: luas_total, price_per_sqm, is_expensive, log_price.

**1.2.** Binning: buat kategorik usia dari kolom umur (0-18: anak, 19-35: muda, 36-60: dewasa, 61+: tua).
```python
df['kategori_usia'] = pd.cut(df['umur'], bins=[0, 18, 35, 60, 100],
                               labels=['anak', 'muda', 'dewasa', 'tua'])
```
Visualisasi distribusi.

**1.3.** Date features: buat dataset dengan date range 1 tahun.
Ekstrak: tahun, bulan, hari, hari_dalam_minggu, quarter, is_weekend, is_month_start, is_month_end.

**1.4.** Polynomial features: given 2 fitur. Gunakan PolynomialFeatures(degree=2). Cek shape sebelum dan sesudah.

**1.5.** Korelasi tinggi: buat matriks korelasi, identifikasi pasangan fitur dengan |r| > 0.85, hapus yang redundan.

---

## Latihan 2: Feature Selection

**2.1.** VarianceThreshold: generate 10 fitur (beberapa dengan variance rendah). Seleksi yang variance > 0.5.
```python
from sklearn.feature_selection import VarianceThreshold

X = np.random.randn(100, 10)
X[:, 0] = 1  # variance ~ 0 (konstanta)
X[:, 1] = np.random.randint(0, 2, 100)  # variance rendah

selector = VarianceThreshold(threshold=0.5)
X_selected = selector.fit_transform(X)
print(f"Shape sebelum: {X.shape}, Shape sesudah: {X_selected.shape}")
```

**2.2.** SelectKBest dengan f_classif: pilih 5 fitur terbaik dari dataset iris. Verifikasi dengan compare train accuracy sebelum dan sesudah seleksi.

**2.3.** RFE (Recursive Feature Elimination): gunakan RandomForest sebagai estimator, pilih 5 fitur terbaik.
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10, random_state=42)
rfe = RFE(estimator=rf, n_features_to_select=5)
rfe.fit(X, y)
print(f"Selected: {rfe.support_}")
print(f"Ranking: {rfe.ranking_}")
```

**2.4.** Feature importance dari RandomForest: train RF, plot horizontal bar chart feature importance, interpretasi.

---

## Latihan 3: Hyperparameter Tuning — Grid Search

**3.1.** GridSearchCV untuk RandomForest pada dataset Iris:
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=2
)
grid.fit(X_train, y_train)
print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.4f}")
```

**3.2.** Bandingkan: waktu GridSearchCV vs RandomizedSearchCV (n_iter=20). Apakah hasil mirip?
```python
import time
start = time.time()
# ... GridSearch ...
print(f"GridSearch time: {time.time() - start:.2f}s")
```

---

## Latihan 4: Hyperparameter Tuning — Optuna

**4.1.** Setup Optuna objective function untuk XGBoost. Tune: n_estimators, max_depth, learning_rate, subsample.
```python
import optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)

def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 50, 300)
    max_depth = trial.suggest_int('max_depth', 3, 15)
    learning_rate = trial.suggest_float('learning_rate', 0.01, 0.3, log=True)

    model = xgb.XGBClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate,
        random_state=42,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    return cross_val_score(model, X, y, cv=5, scoring='accuracy').mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50, show_progress_bar=True)
```

**4.2.** Visualisasi: plot `optuna.study.trials_dataframe()` → lihat hubungan hyperparameter vs score.

**4.3.** Interpretasi: fitur apa yang paling penting menurut Optuna?

---

## Latihan 5: Ensemble Methods

**5.1.** Voting Classifier: kombinasikan LogReg, KNN, Decision Tree. Bandingkan dengan masing-masing单独的 dan voting ensemble.
```python
from sklearn.ensemble import VotingClassifier

voting = VotingClassifier(
    estimators=[
        ('logreg', LogisticRegression(max_iter=1000, random_state=42)),
        ('knn', KNeighborsClassifier()),
        ('dt', DecisionTreeClassifier(max_depth=5, random_state=42))
    ],
    voting='hard'
)
voting.fit(X_train, y_train)
print(f"Voting accuracy: {accuracy_score(y_test, voting.predict(X_test)):.4f}")
```

**5.2.** Stacking: RF + KNN + DT sebagai base, LogReg sebagai meta-classifier.
```python
from sklearn.ensemble import StackingClassifier

stacking = StackingClassifier(
    estimators=[
        ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
        ('knn', KNeighborsClassifier()),
        ('dt', DecisionTreeClassifier(random_state=42))
    ],
    final_estimator=LogisticRegression(max_iter=1000),
    cv=5
)
stacking.fit(X_train, y_train)
```

**5.3.** Gradient Boosting: train XGBoost dan LightGBM. Bandingkan accuracy dan training time.

---

## Latihan 6: Time Series — Resampling & Rolling

**6.1.** Buat dataset time series: tanggal 1 tahun daily, nilai random.
```python
df = pd.DataFrame({
    'tanggal': pd.date_range('2024-01-01', periods=365),
    'harga': np.random.randn(365).cumsum() + 1000
})
df.set_index('tanggal', inplace=True)
```
Resample:
- Weekly mean: `df['harga'].resample('W').mean()`
- Monthly sum: `df['harga'].resample('M').sum()`
- Quarterly average: `df['harga'].resample('Q').mean()`
- Yearly total: `df['harga'].resample('Y').sum()`

**6.2.** Rolling stats: hitung 7-day MA, 30-day MA, 7-day std, 30-day std. Plot original + MA di satu chart.

**6.3.** Lag features: buat lag 1, 7, 30. Hitung korelasi antara fitur dan lag-nya.

---

## Latihan 7: Time Series — Train/Test Split & Evaluation

**7.1.** Split time series data tanpa shuffle (preserve temporal order). Gunakan TimeSeriesSplit(5).
```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in tscv.split(X):
    print(f"Train: {len(train_idx)}, Test: {len(test_idx)}")
```

**7.2.** Train model pada setiap fold. Plot train/test accuracy per fold. Apakah ada pattern overfitting?

**7.3.** Forecast: bagi data 80% train, 20% test. Prediksi 20% terakhir. Hitung RMSE.

---

## Latihan 8: Imbalanced Dataset

**8.1.** Buat dataset imbalanced: 95% kelas 0, 5% kelas 1.
```python
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, weights=[0.95, 0.05], random_state=42)
```

**8.2.** Train LogReg TANPA handling imbalanced. Evaluate — accuracy akan tinggi tapi semua prediksi kelas 0. Cek classification_report.

**8.3.** Handle dengan SMOTE. Retrain. Compare: accuracy, precision, recall, F1 sebelum dan sesudah SMOTE.
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
print(f"Sebelum SMOTE: {pd.Series(y_train).value_counts().to_dict()}")
print(f"Setelah SMOTE: {pd.Series(y_resampled).value_counts().to_dict()}")
```

**8.4.** Bandingkan juga dengan class_weight='balanced' di LogReg (tanpa SMOTE).

---

## Latihan 9: ROC-AUC & Precision-Recall Curve

**9.1.** Train RandomForest pada dataset binary classification. Hitung probability prediksi.
```python
y_proba = model.predict_proba(X_test)[:, 1]
```

**9.2.** Plot ROC Curve. Hitung AUC.
```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC (AUC={roc_auc:.4f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.title('ROC Curve')
plt.show()
```

**9.3.** Plot Precision-Recall Curve. Bandingkan dengan ROC. Kapan PR lebih relevan dari ROC?
Hint: PR lebih relevan untuk dataset imbalanced.

**9.4.** Threshold tuning: plot precision, recall, f1 vs threshold. Cari threshold optimal untuk F1 maximum.

---

## Latihan 10: Model Persistence & Deployment

**10.1.** Train model, save dengan pickle dan joblib. Load kembali, verify accuracy sama.
```python
import joblib

joblib.dump(model, 'model_rf.joblib')
loaded = joblib.load('model_rf.joblib')
print(f"Original accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")
print(f"Loaded accuracy:   {accuracy_score(y_test, loaded.predict(X_test)):.4f}")
```

**10.2.** Build pipeline lengkap: preprocess (StandardScaler) + model (RandomForest). Save entire pipeline.
```python
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, 'pipeline.joblib')
```

**10.3.** Challenge: buat fungsi `predict_single(pipeline, feature_dict)` yang menerima dictionary fitur dan mengembalikan prediksi label.

---

## Tantangan: End-to-End Advanced ML Pipeline

Bangun pipeline ML advanced tanpa copy-paste:

1. Load dataset (pakai make_classification dengan 500 sampel, 15 fitur, 10% noise, imbalance ratio 0.9)
2. EDA: cek distribusi kelas, korelasi, missing
3. Feature engineering: polynomial degree=2, seleksi 10 fitur terbaik
4. Split: stratified 80/20
5. Handling imbalanced: coba SMOTE vs class_weight
6. Model comparison: LogReg, KNN, DT, RF, XGBoost, LightGBM
7. Hyperparameter tuning: Optuna untuk 2 model terbaik
8. Stacking ensemble dari top-3 model
9. Evaluasi: accuracy, precision, recall, F1, ROC-AUC, PR curve
10. Save best model + inference function
11. Buat deployment script: load model → predict → return JSON

---

## Tantangan: Feature Engineering Competition

Dari dataset salary (generate synthetic):
- 20 fitur: sebagian redundan, sebagian noise, beberapa missing
- Target: salary (regression)

Tantangan:
1. Identifikasi dan hapus fitur redundan (korelasi > 0.8)
2. Hapus fitur noise (variance rendah)
3. Seleksi 5 fitur terbaik (RF importance + RFE)
4. Bandingkan R² dengan: semua fitur, fitur hasil seleksi, hanya polynomial interaction
5. Tune hyperparameters pada feature set terbaik
6. Ringkas: fitur apa yang paling penting dan kenapa
