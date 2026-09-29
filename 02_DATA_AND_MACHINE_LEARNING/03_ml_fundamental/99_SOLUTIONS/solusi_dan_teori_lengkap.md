# Teori dan Solusi Lengkap — Level 03 Machine Learning

## 1. Formulasi masalah

Sebelum memilih model, tentukan unit prediksi, target, waktu prediksi, fitur yang tersedia pada waktu itu, dan biaya error. Klasifikasi memprediksi kategori; regresi memprediksi angka. Supervised learning memiliki label; clustering tidak. Target yang dibuat setelah kejadian tidak boleh menjadi fitur karena menyebabkan leakage.

## 2. Solusi pipeline klasifikasi yang aman

```python
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

numeric = ["umur", "pendapatan"]
categorical = ["kota", "pekerjaan"]
preprocess = ColumnTransformer([
    ("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
    ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                       ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical),
])
model = Pipeline([("preprocess", preprocess), ("clf", LogisticRegression(max_iter=1000))])
model.fit(X_train, y_train)
```

Semua langkah yang belajar parameter—imputer, scaler, encoder—berada di pipeline. Saat cross-validation, setiap fold memperoleh parameter dari train fold sendiri. Ini adalah perlindungan utama terhadap leakage.

## 3. Evaluasi klasifikasi

Confusion matrix memecah prediksi menjadi TP, TN, FP, FN. Precision menjawab “dari yang diprediksi positif, berapa benar?” Recall menjawab “dari positif sebenarnya, berapa ditemukan?”. F1 menyeimbangkan keduanya. Pilihan metrik mengikuti biaya kesalahan; fraud sering membutuhkan recall tinggi, sedangkan tindakan mahal mungkin membutuhkan precision tinggi.

## 4. Solusi regresi dan residual

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pred = regressor.predict(X_test)
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)
residual = y_test - pred
```

MAE mudah diinterpretasikan dalam unit target; RMSE menghukum error besar lebih kuat; R² membandingkan dengan baseline rata-rata dan dapat negatif di test set. Plot residual terhadap prediksi/waktu untuk melihat pola error yang belum dimodelkan.

## 5. KNN, tree, dan random forest

KNN menggunakan jarak sehingga scaling penting. Decision tree membuat split aturan tetapi mudah overfit; `max_depth`, `min_samples_leaf` mengontrol kompleksitas. Random forest merata-ratakan banyak tree untuk menurunkan variance, tetapi feature importance bukan otomatis hubungan kausal.
