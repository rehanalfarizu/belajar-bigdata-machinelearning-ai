# Panduan Kode — Chapter 03: Machine Learning Fundamental

> File ini adalah **cheat sheet idiom dan anti-pattern** yang akan kamu temui di chapter ini. Bukan duplikat notebook — buka hanya saat kamu butuh mengingat sintaks atau ingin menghindari jebakan umum. Notebook utama `03_ml_fundamental.ipynb` adalah sumber pengalaman belajarmu; file ini melengkapi.

---

## 1. API Scikit-learn yang Konsisten

### 1.1 Pola fit → predict untuk SEMUA estimator

Apapun algoritmanya (Logistic Regression, KNN, Decision Tree, Random Forest, dll), alur pakainya selalu sama:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000, random_state=42)   # 1. instantiate
model.fit(X_train, y_train)                                  # 2. latih
y_pred  = model.predict(X_test)                              # 3. prediksi label
y_proba = model.predict_proba(X_test)                        # 4. prediksi probabilitas (kalau ada)
```

Konsistensi ini disengaja — kamu bisa tukar estimator dengan mengubah satu baris import. Itulah kekuatan scikit-learn.

### 1.2 Beda fit, transform, fit_transform, predict

| Method | Dipakai di | Tujuan |
|---|---|---|
| `fit(X)` | Scaler, encoder, model | Hitung parameter dari data (mean, std, dst) |
| `transform(X)` | Scaler, encoder | Terapkan transformasi pakai parameter yang sudah di-fit |
| `fit_transform(X)` | Scaler, encoder (di data train) | Gabungan: hitung + terapkan, hanya untuk data train |
| `predict(X)` | Model | Prediksi label (klasifikasi) atau nilai (regresi) |
| `predict_proba(X)` | Model klasifikasi (yang support) | Prediksi probabilitas per kelas |
| `score(X, y)` | Model | Akurasi (klasifikasi) atau R² (regresi) |

**Aturan emas:** `fit_transform` hanya di data training. Untuk data test, pakai `transform` saja (pakai parameter dari train). Lebih lengkap di bagian Preprocessing.

### 1.3 Bentuk X dan y

```python
# X: 2D — shape (n_samples, n_features)
# y: 1D — shape (n_samples,)
print(X.shape)   # (150, 4) untuk Iris
print(y.shape)   # (150,)

# Kalau target kamu DataFrame atau kolom dari DataFrame:
y = df['target'].values   # selalu konversi ke numpy array 1D
```

---

## 2. Train/Test Split

### 2.1 Pakai stratified + random_state untuk reproduktifitas

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y           # jaga proporsi kelas di train & test
)
```

Tiga parameter ini hampir selalu kamu isi: `test_size` (proporsi test), `random_state` (seed agar hasilnya bisa diulang), `stratify=y` (klasifikasi, agar proporsi kelas seimbang di kedua subset). Untuk regresi, `stratify` tidak relevan.

### 2.2 Test set "sentuh sekali"

Sebelum melatih model, tetapkan: data test hanya dipakai di akhir, untuk evaluasi final. Kalau kamu pakai test set untuk tuning hyperparameter, laporan akurasimu akan bias (terlalu optimis). Untuk tuning, pakai cross-validation. Lebih lengkap di section 8.

### 2.3 KFold dan StratifiedKFold

```python
from sklearn.model_selection import KFold, StratifiedKFold

# Regresi atau klasifikasi tanpa peduli proporsi kelas
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Klasifikasi dengan proporsi kelas terjaga per fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

Gunakan `StratifiedKFold` untuk klasifikasi, terutama kalau kelasnya tidak seimbang. `KFold` untuk regresi atau saat proporsi kelas tidak penting.

---

## 3. Preprocessing

### 3.1 Tiga scaler dan kapan pakainya

| Scaler | Rumus | Pakai saat |
|---|---|---|
| `StandardScaler` | (x - mean) / std | Data berdistribusi normal, mayoritas algoritma |
| `MinMaxScaler` | (x - min) / (max - min) | Data bounded (misal 0-1, 0-255 untuk gambar) |
| `RobustScaler` | (x - median) / IQR | Data punya outlier banyak |

Untuk algoritma berbasis jarak (KNN, SVM, LogReg dengan regularisasi) **wajib** scaling. Untuk tree-based (Decision Tree, Random Forest) tidak wajib.

### 3.2 Anti-pattern: fit scaler di seluruh data

```python
# JANGAN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)              # fit di seluruh data!
X_train, X_test = train_test_split(X_scaled, ...)  # leakage

# YANG BENAR
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit hanya di train
X_test_scaled  = scaler.transform(X_test)         # transform saja, pakai parameter train
```

`fit` scaler di seluruh data = test set "bocor" ke training. Model terlihat bagus di test, tapi gagal di data baru. Ini kesalahan paling fatal dan paling sering di ML.

### 3.3 LabelEncoder vs OneHotEncoder

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# LabelEncoder → 1D output, untuk y (target) atau fitur ordinal
le = LabelEncoder()
y_encoded = le.fit_transform(y)   # ['cat', 'dog', 'bird'] → [0, 1, 2]

# OneHotEncoder → 2D output, untuk fitur nominal (tanpa urutan)
ohe = OneHotEncoder(sparse_output=False)
X_onehot = ohe.fit_transform(X_cat)   # [[0, 1, 0], [1, 0, 0], ...]
```

**Aturan praktis:** gunakan `LabelEncoder` terutama untuk target `y` (atau fitur yang memang ordinal). Untuk fitur nominal, termasuk fitur biner, `OneHotEncoder` paling aman dan konsisten dalam `ColumnTransformer`. Mengubah kategori nominal menjadi angka 0/1/2 dapat membuat model linear atau berbasis jarak membaca urutan palsu.

### 3.4 Pipeline dan ColumnTransformer

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Pipeline untuk satu jenis preprocessing
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])
pipe.fit(X_train, y_train)       # scaling & fit di internal
pipe.predict(X_test)             # scaling pakai parameter train, lalu prediksi

# ColumnTransformer untuk data campuran numerik + kategorik
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'income']),
    ('cat', OneHotEncoder(), ['city', 'job'])
])
full_pipe = Pipeline([
    ('prep', preprocessor),
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])
full_pipe.fit(X_train, y_train)
```

`Pipeline` memastikan scaler di-fit di training dan dipakai di test secara konsisten. Tanpa Pipeline, kamu harus ingat manual setiap kali — dan itu resep bencana.

---

## 4. Klasifikasi

### 4.1 Empat algoritma dan kapan pakai

| Algoritma | Ide singkat | Kelebihan | Kekurangan |
|---|---|---|---|
| Logistic Regression | Garis batas linear + sigmoid | Cepat, interpretable, koefisien jelas | Hanya batas linear |
| KNN | Tetangga terdekat | Sederhana, tanpa training | Lambat di prediksi, perlu scaling |
| Decision Tree | Bentuk kotak-kotak dari fitur | Mudah dijelaskan, tidak perlu scaling | Mudah overfit |
| Random Forest | Ratusan Decision Tree dijumlahkan | Stabil, akurasi tinggi | Lambat, kurang interpretable |

Untuk dataset tabular standar, mulai dari Logistic Regression (baseline), lalu coba Random Forest (sering juara). KNN jarang jadi pilihan produksi tapi bagus untuk belajar.

### 4.2 predict vs predict_proba

```python
y_pred  = model.predict(X_test)       # label kelas (integer)
y_proba = model.predict_proba(X_test) # shape (n_samples, n_classes), tiap baris jumlah = 1

# Contoh probabilitas untuk klasifikasi biner
# y_proba[i] = [P(kelas_0), P(kelas_1)]
# Kelas yang dipilih = argmax dari y_proba[i]
```

`predict_proba` hanya tersedia untuk model yang menghitung probabilitas (LogReg, RF, dll). SVM dengan `probability=False` (default) tidak punya `predict_proba`. KNN punya, tapi nilai probabilitasnya diskrit (0, 0.33, 0.5, 0.67, 1.0) karena berbasis voting.

### 4.3 feature_importances_ pada tree-based

```python
import pandas as pd

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

imp = pd.DataFrame({
    'fitur'     : feature_names,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(imp)
```

`feature_importances_` mengembalikan skor 0-1 per fitur; totalnya = 1. Skor dihitung dari berapa kali fitur itu dipakai untuk split dan seberapa besar penurunannya. Fitur dengan importance 0 praktis tidak berkontribusi. Hanya tersedia untuk tree-based model. Logistic Regression pakai `coef_` (koefisien) untuk interpretasi serupa.

---

## 5. Regresi

### 5.1 Tiga metrik utama

| Metrik | Rumus sederhana | Satuan | Interpretasi |
|---|---|---|---|
| MAE | mean(\|y_true - y_pred\|) | Sama dengan y | Rata-rata selisih absolut |
| RMSE | sqrt(mean((y_true - y_pred)²)) | Sama dengan y | Seperti MAE tapi penalti lebih besar untuk error besar |
| R² | 1 - (SSE/SST) | Tanpa satuan (0-1) | Proporsi variasi yang dijelaskan model |

`R²` bisa negatif kalau model lebih buruk dari prediksi rata-rata. `RMSE` dan `MAE` selalu non-negatif. Untuk bisnis, `MAE` lebih mudah dijelaskan ("rata-rata prediksi meleset 5.000 rupiah"); untuk tuning, `RMSE` lebih sensitif terhadap outlier.

### 5.2 Linear vs Ridge vs Lasso

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Linear — OLS biasa, tidak ada regularisasi
lin = LinearRegression()

# Ridge (L2) — koefisien diperkecil tapi tidak pernah 0
ridge = Ridge(alpha=1.0)

# Lasso (L1) — koefisien bisa jadi 0, otomatis feature selection
lasso = Lasso(alpha=0.1)
print(f"Fitur non-zero: {(lasso.coef_ != 0).sum()}")
```

`alpha` adalah kekuatan regularisasi: kecil = regularisasi lemah (mendekati Linear), besar = regularisasi kuat (koefisien menyusut ke 0). Tuning `alpha` adalah pekerjaan utama regresi regularisasi. Pakai Ridge kalau kamu mau semua fitur tetap; pakai Lasso kalau kamu curiga banyak fitur tidak relevan.

### 5.3 R² pada test set vs train set

```python
print(f"Train R²: {model.score(X_train, y_train):.3f}")   # selalu lebih tinggi
print(f"Test  R²: {model.score(X_test, y_test):.3f}")      # jujur
```

Selisih besar antara train dan test = tanda overfitting. Untuk regresi, R² = 0.7-0.9 di test = bagus; R² > 0.95 = curiga data leakage atau fitur bocor.

---

## 6. Cross-Validation

### 6.1 cross_val_score

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Scores: {scores.round(3)}")
print(f"Mean:   {scores.mean():.3f} ± {scores.std():.3f}")
```

`cross_val_score` melatih `cv` model berbeda (tiap fold satu model) dan mengembalikan skor per fold. Mean mengukur performa umum; std mengukur stabilitas. Std besar = model sensitif terhadap split data.

### 6.2 Scoring metrics yang sering dipakai

| Task | Scoring string |
|---|---|
| Klasifikasi akurasi | `'accuracy'` |
| Klasifikasi F1 | `'f1'` (biner), `'f1_macro'` (multi-kelas) |
| Klasifikasi ROC-AUC | `'roc_auc'` (biner), `'roc_auc_ovr'` (multi-kelas) |
| Regresi MSE | `'neg_mean_squared_error'` |
| Regresi R² | `'r2'` |
| Regresi MAE | `'neg_mean_absolute_error'` |

`'neg_*'` artinya skor dinegasikan karena sklearn惯例: lebih besar = lebih baik. Untuk dapat MSE/MAE positif, cukup negasikan.

### 6.3 stratified split wajib untuk klasifikasi

```python
# BENAR untuk klasifikasi
cross_val_score(model, X, y, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42))

# TIDAK IDEAL untuk klasifikasi
cross_val_score(model, X, y, cv=5)   # default KFold, bisa kehilangan kelas minoritas
```

Untuk klasifikasi multi-kelas dengan kelas langka, `StratifiedKFold` memastikan tiap fold punya wakil semua kelas.

---

## 7. Evaluasi Klasifikasi

### 7.1 Confusion matrix dan cara baca

```
              Predicted
              Negatif  Positif
Actual Negatif   TN       FP
       Positif   FN       TP
```

Diagonal (TN, TP) = prediksi benar. Off-diagonal (FP, FN) = prediksi salah. Baris = kelas aktual, kolom = kelas prediksi. Untuk klasifikasi multi-kelas, matrix jadi n×n dan diagonal = prediksi benar per kelas.

### 7.2 Precision, Recall, F1

```python
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['class_0', 'class_1']))
```

`classification_report` mencetak precision, recall, F1, dan support per kelas. Ringkasan:

- **Precision**: dari yang diprediksi positif, berapa yang benar-benar positif. Tinggi = sedikit false positive.
- **Recall**: dari yang aktual positif, berapa yang berhasil ditemukan. Tinggi = sedikit false negative.
- **F1**: rata-rata harmonik precision dan recall. Ringkasan satu angka.
- **Support**: jumlah sampel aktual per kelas.

Untuk data tidak seimbang, F1-macro (rata-rata F1 per kelas) lebih informatif daripada akurasi.

### 7.3 ROC-AUC untuk klasifikasi biner

```python
from sklearn.metrics import roc_auc_score, roc_curve

y_proba = model.predict_proba(X_test)[:, 1]   # probabilitas kelas positif
auc = roc_auc_score(y_test, y_proba)
print(f"AUC: {auc:.3f}")   # 0.5 = random, 1.0 = sempurna
```

AUC = 0.5 artinya model tidak lebih baik dari tebakan acak. AUC = 1.0 artinya model memisahkan kelas sempurna. Untuk AUC, kamu butuh `predict_proba` (atau `decision_function` di SVM).

---

## 8. Hyperparameter Penting

### 8.1 Logistic Regression

| Parameter | Default | Efek |
|---|---|---|
| `C` | 1.0 | Inverse regularisasi. Besar = regularisasi lemah (bisa overfit). Kecil = regularisasi kuat (bisa underfit). |
| `max_iter` | 100 | Iterasi maksimum solver. Naikkan kalau muncul ConvergenceWarning. |
| `penalty` | 'l2' | Jenis regularisasi. 'l1' untuk sparsity, 'l2' default. |
| `solver` | 'lbfgs' | Algoritma optimisasi. 'liblinear' untuk dataset kecil atau L1. |

### 8.2 KNN

| Parameter | Default | Efek |
|---|---|---|
| `n_neighbors` | 5 | Jumlah tetangga. Kecil = detail, bisa overfit. Besar = halus, bisa underfit. |
| `weights` | 'uniform' | 'distance' = tetangga lebih dekat bobot lebih besar. |
| `metric` | 'minkowski' | 'euclidean' (p=2) atau 'manhattan' (p=1). |

### 8.3 Decision Tree

| Parameter | Default | Efek |
|---|---|---|
| `max_depth` | None | Kedalaman pohon. None = hafal data train. 3-5 = sweet spot untuk dataset kecil. |
| `min_samples_split` | 2 | Minimum sampel untuk split. Naikkan = regularisasi. |
| `min_samples_leaf` | 1 | Minimum sampel di daun. Naikkan = regularisasi. |
| `criterion` | 'gini' | 'gini' (default, cepat) atau 'entropy' (mirip, sedikit lebih lambat). |

### 8.4 Random Forest

| Parameter | Default | Efek |
|---|---|---|
| `n_estimators` | 100 | Jumlah pohon. Lebih banyak = lebih stabil, tapi diminishing returns setelah 200-500. |
| `max_depth` | None | Kedalaman tiap pohon. Batas lebih ketat = regularisasi. |
| `max_features` | 'sqrt' | Fitur yang dipertimbangkan per split. 'sqrt' default bagus. |
| `n_jobs` | None | -1 = pakai semua core CPU. |
| `oob_score` | False | True = gunakan out-of-bag samples untuk validasi internal. |

---

## 9. Referensi SQL ↔ ML

Pola data tabular yang sudah kamu kenal di chapter 02 punya padanan langsung di ML:

| Operasi Pandas/SQL | Padanan di ML |
|---|---|
| `df.select_dtypes(include='number')` | `X` (fitur numerik) |
| `df['target']` | `y` (target) |
| `df.drop(columns=['target'])` | `X = df.drop(columns=['target'])` |
| `df.fillna(df.mean())` | `SimpleImputer(strategy='mean')` |
| `pd.get_dummies(df['jurusan'])` | `OneHotEncoder().fit_transform(df[['jurusan']])` |
| `df.groupby('jurusan').mean()` | Explorasi sebelum modelling (bukan modelling) |
| `df.merge(df1, df2, on='id')` | Feature engineering sebelum modelling |
| `df.query('age > 18')` | Boolean indexing untuk preprocessing/filtering |
| `df.sample(frac=0.8, random_state=42)` | `train_test_split(test_size=0.2, random_state=42)` |
| `pd.crosstab(df['jurusan'], df['lulus'])` | Confusion matrix (low-dim case) |

---

## 10. Anti-Pattern

### 10.1 Data leakage: scaler di-fit di seluruh data

```python
# JANGAN
scaler.fit(X)              # lihat semua data
X_train, X_test, y_train, y_test = train_test_split(scaler.transform(X), y)

# BENAR
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)
```

Gejala: akurasi di test set terlihat terlalu bagus, gagal di produksi.

### 10.2 Tuning hyperparameter pakai test set

```python
# JANGAN
for k in [3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    print(k, model.score(X_test, y_test))   # bocor!
    model_terbaik = model

# BENAR
from sklearn.model_selection import cross_val_score
for k in [3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(k, scores.mean())
model_terbaik = KNeighborsClassifier(n_neighbors=5)
model_terbaik.fit(X_train, y_train)
akurasi_final = model_terbaik.score(X_test, y_test)   # sentuh sekali
```

Test set adalah "ujian akhir". Kalau kamu pakai untuk tuning, kamu menghafal jawaban ujian, bukan belajar konsepnya.

### 10.3 Akurasi sebagai satu-satunya metrik untuk data tidak seimbang

```python
# JANGAN — untuk dataset 95% kelas 0, 5% kelas 1
print(model.score(X_test, y_test))   # bisa 0.95 dengan model yang selalu tebak kelas 0

# BENAR
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))   # precision, recall, F1 per kelas
```

Untuk kelas minoritas, precision/recall/F1 jauh lebih informatif. Akurasi hanya cocok untuk dataset yang proporsi kelasnya seimbang.

### 10.4 Lupa set random_state

```python
# JANGAN
train_test_split(X, y, test_size=0.2)            # setiap run beda
RandomForestClassifier(n_estimators=100)          # setiap run beda

# BENAR
train_test_split(X, y, test_size=0.2, random_state=42)
RandomForestClassifier(n_estimators=100, random_state=42)
```

Tanpa `random_state`, hasilmu tidak bisa direproduksi. Kamu tidak bisa membuktikan bahwa perubahan kode (misal tambah fitur) benar-benar meningkatkan model, karena perbedaan akurasi bisa jadi hanya noise dari pengacakan.

### 10.5 Cross_val_score pada data yang sudah di-scale

```python
# JANGAN
X_scaled = scaler.fit_transform(X)
cross_val_score(model, X_scaled, y, cv=5)   # scaler lihat test fold → leakage

# BENAR
# Pakai Pipeline
from sklearn.pipeline import Pipeline
pipe = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression())])
cross_val_score(pipe, X, y, cv=5)   # scaling per fold, aman
```

`cross_val_score` memanggil `fit` di tiap fold. Kalau `X` sudah di-scale di luar, setiap fold tetap aman — tapi kalau kamu `fit_transform` di satu tempat lalu split, kamu balik ke leakage. Pipeline menghindari ambiguitas ini.

### 10.6 LogReg tanpa scaling

```python
# JANGAN
model = LogisticRegression()
model.fit(X_train, y_train)   # fitur dengan rentang beda-beda → konvergensi lambat, koefisien tak sebanding

# BENAR
pipe = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(max_iter=1000))])
```

LogReg pakai regularisasi L2 default, yang mensyaratkan fitur dalam skala sebanding. Tanpa scaling, fitur dengan rentang besar mendominasi.

---

## 11. Ringkasan Pola Satu Baris

| Tujuan | Pola |
|---|---|
| Load dataset | `X, y = load_iris(return_X_y=True)` |
| Split stratified | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)` |
| Pipeline klasifikasi | `Pipeline([('s', StandardScaler()), ('c', LogisticRegression(max_iter=1000, random_state=42))])` |
| Fit + akurasi | `pipe.fit(X_train, y_train); pipe.score(X_test, y_test)` |
| Cross-val | `cross_val_score(pipe, X, y, cv=5, scoring='accuracy').mean()` |
| Probabilitas | `pipe.predict_proba(X_test)[:, 1]` (kolom kelas positif) |
| Confusion matrix | `confusion_matrix(y_test, y_pred)` |
| Report lengkap | `classification_report(y_test, y_pred, target_names=names)` |
| Feature importance | `pd.DataFrame({'fitur': names, 'imp': model.feature_importances_}).sort_values('imp', ascending=False)` |
| Regresi metrics | `mean_squared_error(y_test, y_pred, squared=False)`, `mean_absolute_error(...)`, `r2_score(...)` |
| Reproducible | Selalu isi `random_state=42` di estimator dan split |

---

**Penutup:** Babak terbesar di ML adalah memastikan preprocessing benar (tanpa leakage) dan evaluasi jujur (cross-val + test set terpisah). Sintaks estimator sendiri cepat dikuasai. Kalau kamu bingung kapan pakai LogReg vs RF vs KNN, lihat tabel di section 4.1. Kalau kamu bingung kenapa akurasimu tidak sesuai harapan, cek dulu apakah scaler sudah benar.
