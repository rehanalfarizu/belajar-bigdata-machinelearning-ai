# Level 00 — Matematika, Statistik, dan Eksperimen

Level ini menjembatani Python dengan machine learning. Jangan menghafal rumus tanpa memahami bentuk data, asumsi, dan interpretasinya.

## Aljabar linear

Skalar adalah satu angka, vektor adalah array 1D, matriks adalah array 2D, dan tensor memiliki lebih banyak dimensi. Dataset tabular biasanya `X.shape == (n_samples, n_features)`. Dot product menjumlahkan hasil kali pasangan elemen; `X @ w` menghasilkan satu skor per sampel. Norma mengukur panjang, dan cosine similarity mengukur arah.

Pahami juga transpose, rank, inverse versus pseudo-inverse, eigenvector, dan SVD. PCA memusatkan data, mencari arah variance terbesar, lalu memproyeksikan data ke arah tersebut. Scaling penting karena satuan fitur menentukan jarak dan variance.

## Kalkulus dan optimisasi

Turunan fungsi loss terhadap parameter disebut gradient. Gradient descent memindahkan parameter berlawanan arah gradient. Batch gradient memakai semua data, stochastic gradient satu sampel, dan mini-batch kompromi yang umum dipakai deep learning. Learning rate, initialization, dan conditioning sangat memengaruhi konvergensi.

## Statistik

Pelajari mean/median/quantile, variance dan standard deviation, outlier, distribusi normal/binomial/Poisson, conditional probability, Bayes, sampling, CLT, confidence interval, hypothesis test, effect size, power, bootstrap, korelasi Pearson/Spearman, dan regresi.

Bedakan statistik deskriptif (meringkas data) dari inferensial (menyimpulkan populasi). P-value bukan probabilitas hipotesis benar. Korelasi bukan sebab-akibat. Selalu tulis asumsi dan unit analisis.

## Praktik utama

1. Implementasikan dot product, MSE, gradient descent linear, dan standardization dengan NumPy.
2. Simulasikan distribusi dan Central Limit Theorem.
3. Buat bootstrap confidence interval untuk median.
4. Rancang A/B test dengan effect size dan power sederhana.
5. Bandingkan Pearson dan Spearman pada data dengan outlier.

Lulus jika dapat menjelaskan bentuk setiap array, arti setiap metrik, dan mengapa sebuah kesimpulan statistik bisa salah.
