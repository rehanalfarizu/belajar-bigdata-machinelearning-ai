# Panduan Belajar dan Problem Solving

## Urutan yang benar

Jangan lompat ke deep learning sebelum mampu membuat pipeline scikit-learn sendiri. Ikuti urutan ini dan hanya lanjut jika kriteria selesai terpenuhi.

| Tahap | Materi di repository | Bukti bahwa kamu siap lanjut |
|---|---|---|
| 0 | `TUTORIAL.md`, `01_python_fundamental` | Bisa membaca traceback dan menulis fungsi kecil tanpa melihat contoh. |
| 1 | `02_data_analysis` | Bisa memuat CSV, membersihkan missing value, membuat tiga grafik, dan menulis insight. |
| 2 | `03_ml_fundamental` | Bisa menjelaskan `X`, `y`, split, leakage, metrik, dan membuat `Pipeline`. |
| 3 | `04_ml_advanced` | Bisa membandingkan model dengan cross-validation tanpa memakai test set untuk tuning. |
| 4 | `05_deep_learning` | Bisa memilih MLP/CNN/LSTM berdasarkan bentuk data dan membaca kurva train/validation. |
| 5 | `06_mlops_deployment` | Bisa menyimpan pipeline, menguji API lokal, dan menjelaskan versi model/data. |
| 6 | `10_digital_twin` | Bisa memisahkan state aset, sensor, dan twin; mendeteksi residual tanpa memberi command fisik langsung. |

Setelah tahap 3, pilih spesialisasi: ML engineer, data scientist, atau data engineer. Untuk jalur Big Data, selesaikan SQL terlebih dahulu, kemudian PySpark, Spark SQL/MLlib, orchestration, streaming, dan warehouse. Teori dan latihan pengantar tersedia di `materi/07_big_data_data_engineering`; checklist terperinci tersedia di `ROADMAP_TRACKER.txt`.

## Siklus belajar setiap topik

1. Baca `README.md` chapter untuk tujuan dan istilah.
2. Ketik ulang notebook, jalankan satu cell, lalu jelaskan outputnya dengan kalimat sendiri.
3. Kerjakan `praktikum` tanpa melihat solusi.
4. Ubah satu asumsi: seed, ukuran data, hyperparameter, atau fitur. Catat dampaknya.
5. Buat ulang mini proyek dari file kosong pada hari berikutnya.

Jika kode gagal, jangan langsung mengganti banyak hal. Baca traceback dari baris terakhir, buat contoh terkecil yang masih gagal, periksa `type`, `shape`, nilai yang hilang, lalu perbaiki satu hipotesis dan jalankan ulang. Untuk ML, periksa juga target leakage, pembagian data, dan metrik sebelum menyimpulkan modelnya buruk.

## Aturan teknis yang wajib diingat

- Split data sebelum `fit` scaler, encoder, imputer, selector, atau SMOTE.
- Gunakan validation/CV untuk memilih model; gunakan test set sekali untuk evaluasi akhir.
- Simpan pipeline utuh, seed, versi package, data source, metrik, dan keputusan threshold.
- Akurasi saja tidak cukup untuk kelas timpang; cek precision, recall, F1, serta PR-AUC bila relevan.
- Untuk time series, jangan mengacak urutan dan jangan memakai statistik dari masa depan.

## Portofolio bertahap

1. EDA: analisis dataset publik, tiga grafik, lima insight, dan keputusan pembersihan data.
2. ML tabular: pipeline klasifikasi/regresi dengan baseline, CV, metrik, dan error analysis.
3. Deep learning: klasifikasi gambar kecil dengan CNN dan laporan overfitting/augmentasi.
4. MLOps: API FastAPI untuk pipeline yang sama, test request, Dockerfile, metadata model.
5. Big Data: setelah menguasai SQL dan PySpark, proses dataset besar dengan partitioning, quality check, dan tabel hasil yang dapat di-query.

Untuk setiap proyek, tulis: masalah bisnis, data dan batasannya, baseline, eksperimen, metrik, failure case, serta cara menjalankan. Itu yang membedakan notebook latihan dari portofolio profesional.
