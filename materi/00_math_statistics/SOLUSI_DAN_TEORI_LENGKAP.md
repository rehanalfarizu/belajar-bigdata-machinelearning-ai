# Teori dan Solusi Lengkap — Level 00

## 1. Mengapa matematika muncul di ML?

Satu baris data adalah vektor fitur `x = [x1, x2, ..., xd]`. Model linear mencari bobot `w` dan bias `b`, lalu menghitung `y_hat = x @ w + b`. Seluruh dataset menjadi matriks `X` dengan shape `(jumlah_sampel, jumlah_fitur)`. Baris adalah observasi, kolom adalah fitur. Konvensi shape ini perlu dikuasai karena hampir semua error NumPy, scikit-learn, dan TensorFlow berasal dari shape yang tidak cocok.

Dot product bukan sekadar operasi sintaksis. Ia memberi kontribusi setiap fitur terhadap satu skor. Jika `w_j` positif, menaikkan `x_j` menaikkan skor dengan fitur lain tetap; jika negatif, ia menurunkan skor. Interpretasi itu hanya valid bila fitur sudah didefinisikan dan diskalakan dengan tepat.

## 2. Solusi latihan dot product

```python
import numpy as np

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [2, 1, 0],
    [0, 1, 2],
], dtype=float)
w = np.array([0.5, -1.0, 2.0])
b = 1.0

y_hat = X @ w + b
print(y_hat)
assert X.shape == (5, 3)
assert w.shape == (3,)
assert y_hat.shape == (5,)
assert y_hat[0] == 1 * 0.5 + 2 * -1.0 + 3 * 2.0 + 1.0
```

Baris pertama menghasilkan `5.5`. Kalau memakai `X * w`, hasilnya matriks `(5, 3)` karena perkalian dilakukan elemen per elemen. Gunakan `@` bila maksudnya kombinasi linear.

## 3. Standardization

Standardization mengubah fitur menjadi rata-rata 0 dan standard deviation 1: `z = (x - mean_train) / std_train`. Statistik **hanya** dihitung dari data train. Bila mean seluruh data dipakai, informasi test ikut memengaruhi proses training; ini disebut data leakage.

```python
x_train = np.array([10., 12., 14., 16.])
x_test = np.array([18., 20.])
mean_train = x_train.mean()
std_train = x_train.std()
z_train = (x_train - mean_train) / std_train
z_test = (x_test - mean_train) / std_train
assert np.isclose(z_train.mean(), 0)
assert np.isclose(z_train.std(), 1)
```

Test mean tidak harus 0. Jika 0 dengan sendirinya, itu hanya kebetulan—bukan target transformasi.

## 4. Gradient descent: solusi lengkap

Kita ingin model `y_hat = w*x + b` mendekati target. MSE adalah rata-rata `(y_hat - y)^2`. Turunan MSE terhadap `w` adalah `2 * mean((y_hat-y) * x)`, sedangkan terhadap `b` adalah `2 * mean(y_hat-y)`. Update dilakukan berlawanan arah gradient karena gradient menunjukkan arah naik tercepat.

```python
rng = np.random.default_rng(42)
x = np.arange(1, 51, dtype=float)
y = 4 * x - 2 + rng.normal(0, 5, size=len(x))

w, b, learning_rate = 0.0, 0.0, 0.0005
losses = []
for _ in range(2_000):
    pred = w * x + b
    error = pred - y
    losses.append(np.mean(error ** 2))
    w -= learning_rate * 2 * np.mean(error * x)
    b -= learning_rate * 2 * np.mean(error)

print(f"w={w:.2f}, b={b:.2f}, final_mse={losses[-1]:.2f}")
assert losses[-1] < losses[0]
```

Jika memakai `learning_rate=1`, parameter dapat melompat jauh dan loss menjadi `inf`/`nan`. Jika memakai `1e-9`, loss turun tetapi sangat lambat. Ini alasan learning rate adalah hyperparameter.

## 5. Probabilitas, sampling, dan interval

Mean sample adalah estimator mean populasi. Karena sample berubah, estimator juga berubah. Bootstrap meniru proses tersebut dengan mengambil sample ulang dari data yang tersedia. Interval bootstrap percentile 95% bukan jaminan bahwa 95% data berada di interval itu; ia mengukur ketidakpastian estimator pada prosedur sampling.

```python
income = np.array([4, 4.2, 4.5, 5, 5.1, 5.5, 6, 6.2, 7, 40])
rng = np.random.default_rng(42)
medians = np.array([
    np.median(rng.choice(income, size=len(income), replace=True))
    for _ in range(5_000)
])
ci_low, ci_high = np.percentile(medians, [2.5, 97.5])
print(f"Median={np.median(income):.2f}, CI 95%=({ci_low:.2f}, {ci_high:.2f})")
```

Median lebih tahan terhadap `40` dibanding mean. Namun “lebih tahan” bukan berarti selalu lebih baik; mean tetap tepat untuk total/rata-rata yang memang menjadi pertanyaan bisnis.

## 6. Korelasi dan kesimpulan

Pearson mengukur hubungan linear dan sensitif terhadap outlier. Spearman menghitung korelasi peringkat dan lebih cocok untuk hubungan monotonic. Keduanya tidak membuktikan sebab-akibat. Sebelum menyimpulkan sebab, pertimbangkan confounder, urutan waktu, selection bias, dan eksperimen terkontrol.
