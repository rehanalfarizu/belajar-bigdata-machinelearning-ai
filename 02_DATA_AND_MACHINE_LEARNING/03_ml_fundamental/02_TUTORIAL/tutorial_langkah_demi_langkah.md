# Tutorial Penyelesaian — Level 03 Machine Learning Fundamental

## Resep pipeline klasifikasi

Gunakan resep ini untuk hampir semua soal klasifikasi tabular. Jangan mengubah test set selama proses memilih model.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
pipe = Pipeline([("scaler", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
```

Urutan ini penting: split dulu, `fit` hanya pada train, lalu `predict` test. Pipeline memastikan scaler tidak melihat test data.

## Menyelesaikan soal evaluasi

Untuk klasifikasi, mulai dengan confusion matrix. Dari sana jawab: kelas mana paling sering tertukar, apakah false positive atau false negative lebih mahal, dan apakah accuracy cukup. Untuk regresi, tampilkan MAE, RMSE, R² serta residual plot.

## Model comparison

Bandingkan model dengan cross-validation di train set. Pilih kandidat berdasarkan mean dan variasi skor, latih ulang pada seluruh train, lalu pakai test satu kali.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="accuracy")
print(scores.mean(), scores.std())
```

Jika hasil sangat tinggi, cek duplicate, leakage target, feature dari masa depan, dan split yang tidak sesuai. Skor tinggi bukan bukti model benar.

## Debugging shape dan preprocessing

Scikit-learn meminta `X` 2D dan `y` 1D. Satu sampel harus `model.predict([[...]])`, bukan `model.predict([...])`. Categorical feature perlu `ColumnTransformer` dan `OneHotEncoder(handle_unknown="ignore")`.
