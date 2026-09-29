# Chapter 04 — Machine Learning Advanced

Di chapter 03 kamu sudah membangun, melatih, dan mengevaluasi empat algoritma klasifikasi dan dua regresi dengan scikit-learn. Kamu juga sudah paham alur CRISP-DM, train/test split stratified, dan pipeline sebagai pencegah data leakage. Bab itu menutupi **fondasi ML** yang dipakai di mana-mana.

Chapter ini menaikkan levelnya. Di sini kita akan membahas teknik-teknik yang membedakan praktisi ML yang sudah berpengalaman dari yang baru lulus tutorial. Topiknya bukan algoritma baru (kebanyakan masih pakai keluarga yang sama), tapi **cara menggunakan algoritma itu dengan lebih cerdas dan sadar konteks**: bagaimana membuat fitur baru yang lebih informatif, bagaimana memilih hyperparameter yang optimal, bagaimana menggabungkan banyak model jadi satu ensemble yang lebih kuat, bagaimana menangani data yang tidak seimbang, dan bagaimana memvalidasi time series tanpa membocorkan masa depan ke masa lalu.

Setelah selesai chapter ini, kamu akan bisa mengerjakan project ML skala industri yang sering muncul di lowongan data/ML engineer: dataset tabular dengan ratusan fitur, ribuan baris, distribusi kelas yang tidak seimbang, dan tuntutan deploy model yang stabil. Fondasi ini juga akan menyiapkan kamu untuk chapter 05 (Deep Learning) dan chapter 06 (MLOps & Deployment), di mana kita akan memindahkan model dari laptop ke production.

## Daftar Section

Chapter ini dibagi menjadi delapan section yang saling membangun. Section satu dan dua fokus pada **fitur** — bagaimana membuat fitur baru dari data mentah dan bagaimana menyaring fitur yang benar-benar penting. Section tiga menutupi **hyperparameter tuning** dengan GridSearchCV, RandomizedSearchCV, dan Optuna. Section empat masuk ke **ensemble methods** — Voting, Stacking, dan gradient boosting (XGBoost, LightGBM). Section lima dan enam membahas dua topik yang sering bikin model "tidak berguna" kalau diabaikan: **imbalanced dataset** dan **time series validation**. Section tujuh membahas kurva ROC dan Precision-Recall sebagai alat evaluasi. Section delapan mengikat semuanya dalam mini project end-to-end.

Section satu memperkenalkan feature engineering: membuat fitur interaksi (`luas = panjang × lebar`), transformasi log untuk data skewed, dan polynomial features untuk menangkap hubungan non-linear. Section dua mengajarkan tiga cara feature selection: VarianceThreshold (hapus yang hampir konstan), SelectKBest (pilih K fitur dengan skor statistik tertinggi), dan RFE (eliminasi rekursif dengan model sebagai evaluator). Section tiga membahas hyperparameter tuning — perbedaan GridSearchCV (exhaustive tapi lambat) vs RandomizedSearchCV (sampel acak) vs Optuna (Bayesian optimization, paling efisien untuk ruang pencarian besar). Section empat menjelaskan ensemble: Voting (majority vote), Stacking (meta-classifier di atas base models), dan gradient boosting (XGBoost, LightGBM) yang merupakan standar industri untuk data tabular.

Section lima masuk ke imbalanced data — kasus di mana satu kelas punya 99% data dan kelas lain cuma 1%. Akurasi 99% terlihat bagus tapi modelnya bodoh. Solusinya: `class_weight='balanced'`, SMOTE (synthetic oversampling), dan threshold tuning. Section enam membahas time series — kasus khusus di mana urutan waktu penting dan split random akan membocorkan masa depan. TimeSeriesSplit adalah solusinya. Section tujuh membedakan kurva ROC-AUC (default untuk balanced) dan Precision-Recall (lebih informatif untuk imbalanced) dan mengajarkan threshold tuning. Section kedelapan adalah ujian — kamu akan melatih dan mengevaluasi pipeline end-to-end pada dataset sintetis yang berisi gabungan tantangan dari semua section.

## Prasyarat

Chapter ini mengasumsikan kamu sudah nyaman dengan semua yang diajarkan di chapter 01 (Python dasar), chapter 02 (NumPy, Pandas, matplotlib), dan chapter 03 (scikit-learn, train/test split, pipeline, Logistic Regression, KNN, Decision Tree, Random Forest, Linear/Ridge/Lasso Regression). Kalau kamu masih ragu pada salah satu fondasi itu, disarankan untuk membuka lagi notebook chapter 03 sebentar — chapter 04 akan sangat sering merujuk ke pola-pola yang sudah kita tetapkan di sana.

Library tambahan yang akan kamu temui di chapter ini (dan perlu di-install): `xgboost` dan `lightgbm` untuk gradient boosting, `optuna` untuk Bayesian optimization, dan `imbalanced-learn` (imblearn) untuk SMOTE dan teknik resampling. Semua bisa dipasang dengan satu perintah: `pip install xgboost lightgbm optuna imbalanced-learn`.

## Library yang Dipakai

Chapter ini menggunakan pustaka-pustaka dari chapter sebelumnya (NumPy, Pandas, matplotlib, scikit-learn) ditambah empat pustaka baru. **XGBoost** (`import xgboost as xgb`) adalah implementasi gradient boosting paling populer di dunia — sering jadi pemenang di kompetisi Kaggle. **LightGBM** (`import lightgbm as lgb`) dari Microsoft, secara umum lebih cepat dari XGBoost untuk dataset besar. **Optuna** (`import optuna`) adalah framework hyperparameter tuning dengan Bayesian optimization — jauh lebih efisien dari GridSearch untuk ruang pencarian besar. **Imbalanced-learn** (`import imblearn`) menyediakan SMOTE dan berbagai teknik resampling untuk menangani dataset tidak seimbang.

## Cara Membaca Chapter Ini

Mulai dari `04_ml_advanced.ipynb`. Ikuti setiap cell secara berurutan, ketik ulang kode di code cell, amati output, dan jawab pertanyaan refleksi di akhir setiap section. Setelah selesai (atau saat kamu butuh istirahat), buka `praktikum.ipynb` untuk 8 latihan terstruktur dan satu tantangan end-to-end. Kalau kamu ingin menulis kode dari nol untuk melatih memori otot, buka `typing_practice.ipynb` — 10 soal bertingkat dari manipulasi fitur sampai mini pipeline ML.

## File Pendukung

`PANDUAN_KODE.md` adalah referensi pattern dan anti-pattern. Bukan duplikat notebook — buka hanya saat kamu butuh mengingat idiom tertentu. README ini sengaja tidak menjelaskan sintaksis — semuanya ada di notebook.

## Setelah Chapter Ini

Begitu chapter 04 selesai, kamu akan masuk ke chapter 05: Deep Learning. Di sana kita akan membahas neural network, CNN untuk gambar, RNN/LSTM untuk sequence, dan transfer learning. Setelah itu, chapter 06: MLOps & Deployment — bagaimana membawa model dari notebook ke production dengan FastAPI, Docker, dan MLflow.
