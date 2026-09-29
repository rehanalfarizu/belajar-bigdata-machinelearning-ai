# Teori Mendalam — Level 04: Machine Learning Advanced

## 1. Feature engineering sebagai knowledge yang dapat diuji

Feature engineering menerjemahkan proses domain menjadi representasi model: rasio, log transform, interaction, bucket, lag, aggregate historis, atau embedding. Feature yang bagus harus tersedia saat inference, stabil, dapat dihitung ulang, dan tidak menyandikan target/masa depan. Simpan definisi feature dan window waktunya agar training-serving consistency terjaga.

Feature selection mengurangi noise/biaya tetapi mudah bocor. Filter statistic, RFE, dan embedded importance harus dilakukan dalam pipeline/CV. Importance model bukan causal effect, dapat bias pada fitur berkardinalitas tinggi, dan tidak menggantikan pemeriksaan fairness/robustness.

## 2. Hyperparameter search dan estimasi jujur

Parameter dipelajari dari data; hyperparameter dipilih oleh manusia/search. Grid search menyapu kombinasi tetap, randomized search lebih efisien untuk ruang besar, Bayesian optimization memakai hasil sebelumnya untuk memilih trial berikut. Semua search dapat overfit validation ketika eksperimen terlalu banyak. Gunakan budget, ruang pencarian berdasarkan hipotesis, CV yang sesuai, seed, dan test final terpisah. Nested CV memberi estimasi lebih jujur bila data kecil dan keputusan model banyak.

## 3. Ensemble

Bagging melatih model pada bootstrap lalu merata-ratakan/voting untuk menurunkan variance; random forest adalah contoh. Boosting melatih model lemah berurutan untuk memperbaiki residual/error sebelumnya, sehingga kuat tetapi dapat sensitif noise/hyperparameter. Stacking memakai model meta untuk menggabungkan base learner dan memerlukan out-of-fold prediction agar tidak leakage. Ensemble tidak menggantikan baseline, feature quality, dan interpretability requirement.

## 4. Imbalance, calibration, dan decision policy

Resampling mengubah distribusi train, bukan prevalensi dunia nyata. Class weight memberi cost lebih tinggi pada kelas minoritas; undersampling membuang data mayoritas; oversampling/SMOTE membuat contoh tambahan tetapi berisiko memperbesar noise/overlap. Terapkan hanya dalam train fold. Setelah model, pilih threshold berdasarkan policy dan periksa calibration. Dua model dengan ROC-AUC sama dapat memiliki keputusan operasional sangat berbeda.

## 5. Time series

Observasi temporal autocorrelated; masa depan tidak boleh mencampur masa lalu. Feature lag, rolling, seasonality, holiday, dan exogenous variable harus dihitung tanpa look-ahead. Gunakan walk-forward validation dan baseline naïf/seasonal naïf. Error dapat berubah menurut horizon; laporan satu RMSE global sering menyembunyikan kegagalan pada periode penting. Distribution shift, missing interval, dan revisi data historis harus masuk desain pipeline.
