# Teori Mendalam — Level 00: Matematika, Statistik, dan Eksperimen

## 1. Bahasa untuk menyatakan data

Matematika ML bukan kumpulan rumus untuk dihafal. Ia adalah bahasa ringkas untuk menyatakan data, asumsi, transformasi, dan ketidakpastian. Skalar adalah satu nilai, vektor adalah urutan nilai berarah, matriks adalah tabel atau transformasi linear, sedangkan tensor adalah array berdimensi lebih dari dua. Dalam dataset tabular, `X` lazim berbentuk `(n, d)`: `n` observasi dan `d` fitur. Target `y` lazim berbentuk `(n,)` untuk satu target per observasi.

Periksa shape sebelum menjalankan rumus. Misalnya `X @ w` hanya valid bila jumlah kolom `X` sama dengan panjang `w`. Hasilnya satu skor per baris. Kesalahan penting adalah mengira `X * w` sama dengan `X @ w`; operator pertama perkalian elemen-per-elemen, sedangkan kedua menjumlahkan kontribusi fitur menjadi prediksi.

## 2. Aljabar linear sebagai transformasi

Vektor dapat dibaca sebagai titik di ruang fitur atau arah. Dot product `x @ w` mengukur keselarasan tertimbang antara dua arah. Norma L2 mengukur panjang; cosine similarity membandingkan arah dan banyak dipakai pada embedding teks. Matriks dapat dilihat sebagai transformasi: rotasi, skala, proyeksi, atau kombinasi fitur. Transpose membalik orientasi baris/kolom dan penting saat menurunkan rumus regresi atau menghitung covariance.

Rank menyatakan banyaknya arah independen. Jika dua kolom persis berkorelasi, informasi keduanya tidak independen dan matriks dapat singular. Inverse hanya ada untuk matriks persegi yang full-rank; di data nyata pseudo-inverse lebih aman. Eigenvector adalah arah yang tetap searah setelah transformasi, dan eigenvalue menyatakan skala pada arah itu. PCA memakai arah variance besar untuk mereduksi dimensi, tetapi tidak memahami target atau sebab-akibat; komponen utama bukan otomatis fitur “paling penting” bagi keputusan bisnis.

## 3. Kalkulus, loss, dan optimisasi

Turunan menjawab: jika input diubah sangat kecil, seberapa cepat output berubah? Partial derivative melakukan itu untuk satu parameter sambil parameter lain tetap. Gradient mengumpulkan seluruh partial derivative dan menunjuk arah kenaikan fungsi paling cepat. Karena tujuan training adalah menurunkan loss, gradient descent bergerak ke arah kebalikannya: `theta_baru = theta_lama - learning_rate * gradient`.

Loss adalah fungsi objektif, bukan metrik bisnis. MSE menghukum error besar secara kuadrat sehingga sensitif outlier; MAE linear sehingga lebih robust tetapi gradiennya tidak mulus pada nol. Cross-entropy cocok untuk probabilitas kelas karena menghukum prediksi percaya diri yang salah. Landscape loss pada deep learning non-convex; minimum lokal, saddle point, skala fitur, initialization, dan noise mini-batch memengaruhi training. Learning rate terlalu besar dapat divergen, terlalu kecil lambat. Momentum dan Adam menambahkan memory/scaling pada update, bukan sihir yang menggantikan data bagus.

## 4. Probabilitas sebagai model ketidakpastian

Random variable memetakan hasil acak ke angka. Distribution menjelaskan peluang nilai; expectation adalah rata-rata jangka panjang; variance mengukur penyebaran sekitar expectation. Conditional probability `P(A|B)` menyatakan peluang A setelah B diketahui. Bayes membalik kondisi: posterior sebanding dengan likelihood dikali prior. Dalam klasifikasi, probabilitas model adalah estimasi berdasarkan data/model/asumsi, bukan kepastian dunia nyata.

Distribusi normal berguna karena banyak rata-rata proses mendekatinya, bukan karena semua data nyata normal. Binomial memodelkan jumlah sukses dari trial Bernoulli independen; Poisson memodelkan count kejadian dalam interval dengan rate tertentu. Cek asumsi independensi, stationarity, dan parameter sebelum memakai distribusi. Memakai uji statistik secara mekanis pada data yang tidak memenuhi asumsi memberi angka yang tampak ilmiah tetapi menyesatkan.

## 5. Statistik deskriptif dan inferensial

Mean merangkum pusat tetapi peka outlier; median lebih robust pada distribusi skewed. Quantile/IQR membantu memeriksa sebaran dan outlier. Standard deviation mengukur sebaran, bukan “kesalahan” secara otomatis. Korelasi Pearson mengukur hubungan linear; Spearman mengukur hubungan monotonic berbasis peringkat. Korelasi tidak membuktikan sebab-akibat karena confounder, selection bias, reverse causality, dan kebetulan dapat menciptakan hubungan.

Sample adalah bagian populasi. Estimator berubah jika sample berubah; standard error mengukur variasi estimator. Central Limit Theorem menjelaskan mengapa distribusi mean sample dapat mendekati normal saat sample cukup besar dalam kondisi tertentu. Confidence interval bukan peluang parameter berada di rentang setelah data terlihat; secara frequentist, prosedurnya akan mencakup parameter pada proporsi pengulangan tertentu. P-value adalah peluang melihat data setidak-ekstrem ini jika null hypothesis benar—bukan peluang null benar.

## 6. Eksperimen dan keputusan

A/B test harus menentukan metric, unit randomization, hipotesis, minimum detectable effect, sample size, duration, stopping rule, dan guardrail sebelum melihat hasil. Statistical significance tidak menjamin practical significance; perbedaan 0,01% dapat signifikan pada data sangat besar tetapi tidak bernilai bisnis. Multiple testing menaikkan peluang false positive. Gunakan effect size, interval, segment analysis, dan pemahaman proses bisnis bersama p-value.

Di ML, eksperimen yang baik mengubah satu hal, memakai split/seed yang dicatat, membandingkan baseline, dan menyimpan hasil gagal. Hindari “p-hacking” dan memilih metric setelah melihat hasil. Ketidakpastian harus dilaporkan, bukan disembunyikan.
