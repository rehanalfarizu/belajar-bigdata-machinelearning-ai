# Lab 07 — Bayes Update

## 1. TUJUAN
Memperbarui keyakinan dari prior dan kualitas evidence.

## 2. PREREQUISITE
Baca lesson 08.

## 3. SETUP
Gunakan prior defect 1%, sensitivity 90%, dan false-positive rate 5%.

## 4. PREDICTION BEFORE RUN
Secara intuitif tebak P(defect|positive), lalu hitung manual tabel 10.000 item.

## 5. LANGKAH PRAKTIKUM
Panggil `bayes_positive` dan tampilkan true-positive versus false-positive sebagai bar ASCII.

## 6. OBSERVATION
Bandingkan tebakan, tabel frekuensi, dan hasil kode.

## 7. WHY
Posterior menimbang likelihood bersama base rate; akurasi test saja tidak menentukan posterior.

## 8. MODIFICATION
Ubah prior dan false-positive rate; prediksi parameter mana paling berpengaruh.

## 9. FAILURE EXPERIMENT
Tukar P(positive|defect) dengan P(defect|positive).

## 10. DEBUGGING
Tulis numerator/denominator dengan label kejadian, cek probabilitas 0–1, lalu verifikasi via tabel.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada alert anomaly, diagnosis, fraud, spam, dan predictive maintenance.

## 12. CHECKPOINT
Bangun kasus Bayes baru: intuisi, hitung manual, kode, visual, ubah prior, dan interpretasikan.
