# Chapter 03 — Machine Learning Fundamental

Ini adalah chapter yang paling transformatif di repo ini. Di chapter 01 kamu belajar menulis program Python, di chapter 02 kamu belajar mengolah data tabular dengan NumPy dan Pandas, dan di chapter ini kamu akan menggunakan semuanya untuk **membuat komputer belajar dari data**. Setelah selesai, kamu akan bisa membangun, melatih, dan mengevaluasi model machine learning (ML) untuk masalah klasifikasi dan regresi — keterampilan inti yang diminta di hampir semua lowongan data/ML engineer.

Chapter ini sengaja tidak mengajarkan deep learning dulu. Justru karena supervised learning klasik (Logistic Regression, KNN, Decision Tree, Random Forest) jauh lebih sederhana, kamu bisa benar-benar paham **kenapa** sebuah model bekerja, **kapan** ia gagal, dan **apa** yang harus diwaspadai saat melatihnya. Deep learning di chapter 04 akan terasa lebih natural setelah fondasi ini kuat.

## Daftar Section

Chapter ini dibagi menjadi delapan section. Section satu dan dua membangun fondasi konseptual: apa itu ML, jenis-jenisnya, alur kerja CRISP-DM, dan keputusan paling kritis di ML — train/test split. Section tiga membahas preprocessing: scaling, encoding, dan pipeline sebagai alat pencegah data leakage. Section empat sampai enam adalah empat algoritma klasifikasi inti yang akan kamu pakai berulang di industri: Logistic Regression, K-Nearest Neighbors, Decision Tree, dan Random Forest. Section tujuh bergeser ke regresi (Linear, Ridge, Lasso) dan metrik evaluasinya. Section kedelapan adalah ujian — kamu akan membangun pipeline end-to-end pada dataset Iris dari awal sampai akhir.

Section satu memperkenalkan supervised, unsupervised, dan reinforcement learning dengan analogi dunia nyata, lalu membedakan posisi `X` (2D) dan `y` (1D) di scikit-learn. Section dua menjelaskan alur CRISP-DM dan melatih train/test split stratified dengan `random_state` untuk reproduktifitas — keputusan kecil yang menentukan apakah evaluasimu jujur atau tidak. Section tiga menutup preprocessing: kenapa scaling wajib untuk algoritma berbasis jarak, kenapa `LabelEncoder` berbeda dari `OneHotEncoder`, dan bagaimana `Pipeline` + `ColumnTransformer` mencegah data leakage secara sistematis.

Section empat masuk ke Logistic Regression — algoritma yang elegan dengan sigmoid function, `predict_proba` untuk probabilitas, dan koefisien yang bisa diinterpretasi. Section lima melatih K-Nearest Neighbors dan cara memilih K optimal dengan cross-validation. Section enam menutup trio klasifikasi dengan Decision Tree (gampang dijelaskan, gampang overfit) dan Random Forest (ensemble yang stabil). Section tujuh membahas regresi Linear, Ridge (L2), dan Lasso (L1) dengan metrik MAE, RMSE, dan R². Section delapan mengikat semuanya dalam mini project end-to-end.

## Prasyarat

Chapter ini mengasumsikan kamu sudah paham variabel, list, dict, control flow, fungsi dari chapter 01, dan NumPy/Pandas/matplotlib dari chapter 02. Kalau kamu merasa ragu pada bagian mana pun, tidak ada salahnya membuka lagi notebook chapter sebelumnya untuk mengingat. Scikit-learn akan terasa jauh lebih ringan kalau kamu sudah nyaman dengan operasi array NumPy dan DataFrame Pandas.

## Library yang Dipakai

Chapter ini menggunakan empat library utama. **NumPy** (diimpor sebagai `np`) dan **Pandas** (diimpor sebagai `pd`) dari chapter sebelumnya — dipakai untuk manipulasi data. **Matplotlib** (diimpor sebagai `plt`) untuk visualisasi confusion matrix dan feature importance. Yang baru adalah **Scikit-learn** (diimpor dengan submodule, misalnya `from sklearn.linear_model import LogisticRegression`) — library ML paling populer di Python, dengan API yang konsisten untuk fit/predict dan banyak algoritma siap pakai. Semua dipasang dengan satu perintah: `pip install numpy pandas matplotlib scikit-learn`.

## Cara Membaca Chapter Ini

Mulai dari `03_ml_fundamental.ipynb`. Notebook itu adalah pengalaman utama — ikuti setiap cell secara berurutan, ketik ulang kode di code cell, amati outputnya, dan jawab pertanyaan refleksi di akhir setiap section. Setelah selesai (atau kalau kamu butuh istirahat), buka `praktikum.ipynb` untuk menguji pemahamanmu dengan soal-soal bertingkat — ada 8 latihan, satu tantangan end-to-end, dan 3 bonus. Kalau kamu ingin menulis kode dari nol untuk melatih memori otot, buka `typing_practice.ipynb` — 10 soal bertingkat dari train/test split manual sampai mini pipeline.

## File Pendukung

`PANDUAN_KODE.md` adalah referensi pattern dan anti-pattern yang akan kamu temui di chapter ini. File itu bukan duplikat notebook — buka hanya saat kamu butuh mengingat idiom tertentu (misalnya cara paling idiomatik untuk menggunakan `Pipeline`, atau kapan pakai `cross_val_score` vs `train_test_split`). README ini sengaja tidak menjelaskan sintaksis atau konsep — semuanya ada di notebook.

## Setelah Chapter Ini

Begitu chapter 03 selesai, kamu sudah punya bekal untuk chapter 04: ML Advanced. Di sana kita akan membahas hyperparameter tuning otomatis (GridSearchCV, RandomizedSearchCV), menangani dataset tidak seimbang (SMOTE, class weight), time series forecasting, dan ensemble methods lanjutan (XGBoost, LightGBM). Deep learning dengan PyTorch/TensorFlow juga akan kita singgung di chapter 05.
