# Teori Mendalam — Level 03: Machine Learning Fundamental

## 1. Apa yang sebenarnya dipelajari model?

Machine learning mencari pola statistik dari contoh, bukan memahami sebab atau dunia seperti manusia. Fitur `X` adalah informasi tersedia saat prediksi dibuat; target `y` adalah hasil yang ingin diprediksi. Generalisasi berarti performa pada data baru dari distribusi yang relevan, bukan performa tinggi pada data training. Model yang menghafal noise memiliki training score tinggi tetapi gagal generalisasi: overfitting.

Bias adalah error karena asumsi model terlalu sederhana; variance adalah sensitivitas terhadap sample training. Menambah kompleksitas biasanya menurunkan bias tetapi menaikkan variance. Regularisasi, data lebih banyak, validasi, dan feature design adalah cara mengelola trade-off ini.

## 2. Split, leakage, dan validasi

Train data untuk fit parameter, validation/CV untuk memilih model/hyperparameter, test untuk evaluasi final yang tidak disentuh keputusan. Stratification menjaga proporsi kelas pada klasifikasi. Random state memberi reproduktibilitas, bukan jaminan representatif. Untuk data temporal, split harus menghormati waktu; untuk pengguna/keluarga/dokumen terkait, split berbasis group mungkin diperlukan.

Leakage terjadi bila model melihat informasi yang tidak tersedia pada waktu prediksi: scaler fit pada semua data, target terselubung dalam fitur, data masa depan, duplicate antar split, atau preprocessing sebelum CV. Leakage sering membuat score sangat tinggi dan model production sangat buruk. Pipeline adalah mekanisme untuk menjalankan transform dalam train fold yang tepat.

## 3. Regresi dan klasifikasi

Linear regression memodelkan kombinasi linear fitur dan target kontinu. Koefisien adalah asosiasi kondisional terhadap fitur lain dalam model, bukan sebab-akibat otomatis. Ridge menambah penalti L2 untuk mengecilkan koefisien berkorelasi; Lasso penalti L1 dapat membuat sebagian koefisien nol. Logistic regression memakai sigmoid/softmax untuk probabilitas kelas dan memiliki batas keputusan linear.

KNN memprediksi dari tetangga sehingga scaling dan pilihan jarak penting. Decision tree membuat aturan split yang mudah divisualisasi namun mudah overfit. Random forest menggabungkan banyak tree dengan bootstrap dan random feature subset untuk menurunkan variance. Tidak ada model terbaik universal; baseline sederhana dan data context harus memandu pilihan.

## 4. Metric dan threshold

Metrik harus mewakili dampak keputusan. Accuracy cocok hanya bila kelas/cost relatif seimbang. Precision, recall, F1, ROC-AUC, PR-AUC, log loss, calibration, MAE, RMSE, dan R² menjawab pertanyaan berbeda. Probabilitas yang ranking-nya baik belum tentu calibrated. Threshold 0,5 bukan hukum; pilih berdasarkan biaya false positive/negative, kapasitas operasi, dan validasi.

## 5. Unsupervised learning

Clustering tidak menemukan “kebenaran” otomatis; ia mengelompokkan menurut asumsi distance/density/number of cluster. K-Means mengasumsikan cluster kira-kira bulat dan perlu `k`; DBSCAN menemukan daerah padat tetapi sensitif parameter; hierarchical membantu melihat struktur berjenjang. PCA mereduksi dimensi untuk visualisasi/kompresi tetapi dapat menyembunyikan kelompok minoritas. Validasi cluster memerlukan domain knowledge, stabilitas, dan kegunaan tindakan.
