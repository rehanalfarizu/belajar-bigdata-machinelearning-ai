# Teori dan Solusi Lengkap — Level 04 ML Advanced

## 1. Feature engineering dan selection

Feature yang baik merepresentasikan informasi tersedia saat prediksi dibuat. Contoh: `harga_per_unit = total / jumlah`, log transform untuk distribusi sangat skewed, lag untuk time series. Jangan membuat feature menggunakan target atau data masa depan. Feature selection harus berada di pipeline/CV; melakukan `SelectKBest.fit_transform(X, y)` sebelum split membocorkan label test.

## 2. Solusi tuning yang benar

```python
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
search = RandomizedSearchCV(
    pipeline,
    param_distributions={"clf__n_estimators": [100, 300, 500], "clf__max_depth": [3, 5, 10, None]},
    n_iter=8, scoring="f1_macro", cv=cv, random_state=42, n_jobs=-1,
)
search.fit(X_train, y_train)
final_model = search.best_estimator_
```

Test set tidak masuk `search.fit`. Gunakan test hanya sesudah parameter dan threshold final dipilih. Untuk estimasi performa yang lebih jujur pada data kecil, gunakan nested CV.

## 3. Imbalanced classification

Accuracy 95% dapat diperoleh dengan selalu menebak kelas mayoritas jika prevalensinya 95%. Gunakan PR curve, F1, recall/precision kelas minoritas, dan threshold bisnis. SMOTE membangun contoh sintetis di train fold, bukan di test atau seluruh data.

## 4. Time series

Urutkan berdasarkan waktu. Buat lag dan rolling feature hanya dari nilai sebelum target. Gunakan walk-forward/`TimeSeriesSplit`, bandingkan dengan baseline naïf, dan evaluasi periode terbaru. Random split mencampur masa depan ke masa lalu dan membuat skor terlalu optimistis.

## 5. Model persistence

Simpan pipeline utuh dan metadata: schema input, versi dependency, git commit, seed, training window, metric, threshold. Saat load, uji satu sample known-good. Model `.pkl` atau `.joblib` tidak portabel bebas antar versi library dan tidak aman dari sumber tak tepercaya.
