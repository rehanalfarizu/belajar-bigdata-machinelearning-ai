# Lab 01 — Association Rules
## 1. TUJUAN
Menghitung support, confidence, lift manual dan executable.
## 2. PREREQUISITE
Lesson 01–02 dan `pattern_lab.py`.
## 3. SETUP
Gunakan lima basket A/B/C dan tabel hitung.
## 4. PREDICTION BEFORE RUN
Hitung metric A→B dan jumlah frequent itemset pada threshold 0.4.
## 5. LANGKAH PRAKTIKUM
Ketik transaksi, jalankan metrics/candidate mining, bandingkan dengan manual.
## 6. OBSERVATION
Catat denominator, candidate, dan rule lift di bawah/atas satu.
## 7. WHY
Base rate membuat confidence saja menyesatkan.
## 8. MODIFICATION
Ubah minimum support dan tambah item sangat umum.
## 9. FAILURE EXPERIMENT
Hitung duplicate item satu basket sebagai dua occurrence.
## 10. DEBUGGING
Periksa grain basket, set normalization, numerator/denominator, lalu regression test.
## 11. WORKPLACE CONNECTION
Muncul pada bundling, recommendation, event/alarm co-occurrence.
## 12. CHECKPOINT
Buat dataset enam basket, manual/code, sensitivity threshold, dan batas causal claim.
