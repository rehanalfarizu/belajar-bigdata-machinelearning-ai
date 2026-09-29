# Tutorial Penyelesaian — Level 00

## Linear algebra: selalu mulai dari shape

Untuk soal `X @ w`, tulis `X.shape` dan `w.shape` di kertas. Jika `X` berukuran `(5, 3)`, maka `w` harus `(3,)` atau `(3, 1)`. Hasilnya satu prediksi per baris, yaitu `(5,)` atau `(5, 1)`.

```python
import numpy as np

X = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
w = np.array([0.5, -1.0, 2.0])
b = 1.0
y_hat = X @ w + b
assert y_hat.shape == (2,)
print(y_hat)
```

Verifikasi elemen pertama secara manual: `1*0.5 + 2*(-1) + 3*2 + 1`. Jika hasil berbeda, jangan lanjut ke model yang lebih rumit.

## Gradient descent

Pecah solusi menjadi data, prediksi, loss, gradient, update. Pastikan `x`, `y`, dan prediksi semuanya 1D; bentuk `(n, 1)` dikurangi `(n,)` dapat membuat broadcasting menjadi matriks `(n, n)` tanpa error.

```python
prediction = weight * x + bias
error = prediction - y
loss = np.mean(error ** 2)
d_weight = 2 * np.mean(error * x)
d_bias = 2 * np.mean(error)
```

Simpan `loss` setiap epoch. Solusi benar harus memiliki loss akhir jauh lebih kecil daripada loss awal. Jika loss naik atau `nan`, kecilkan learning rate; jika nyaris tidak berubah, naikkan sedikit atau tambah epoch.

## Statistik dan bootstrap

Untuk confidence interval, jangan menghitung ulang statistik yang sama pada data asli. Ambil sample **dengan replacement**, hitung statistik pada setiap sample, lalu ambil percentile.

```python
rng = np.random.default_rng(42)
medians = [np.median(rng.choice(data, size=len(data), replace=True)) for _ in range(2_000)]
low, high = np.percentile(medians, [2.5, 97.5])
print(low, high)
```

Tuliskan interpretasi yang benar: interval adalah rentang estimasi parameter dari prosedur sampling ini, bukan rentang tempat 95% data berada.

## Checklist jawaban

- Bentuk array dan satuan data sudah diperiksa.
- Seed dipakai bila ada random process.
- Plot memiliki judul dan label sumbu.
- Kesimpulan menyebut asumsi serta keterbatasan.
