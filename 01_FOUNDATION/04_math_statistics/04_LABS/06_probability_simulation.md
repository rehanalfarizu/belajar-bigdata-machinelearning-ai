# Lab 06 — Probability Simulation

## 1. TUJUAN
Menghubungkan peluang teoritis dengan frekuensi jangka panjang dan variasi acak.

## 2. PREREQUISITE
Baca lesson 07.

## 3. SETUP
Pilih Bernoulli dengan `p=0.3` dan seed tetap.

## 4. PREDICTION BEFORE RUN
Secara intuitif prediksi jumlah sukses dari 10 dan 10.000 trial; hitung ekspektasi `n×p`.

## 5. LANGKAH PRAKTIKUM
Panggil `bernoulli_rate` untuk beberapa n dan tampilkan deviasi dari p sebagai bar ASCII.

## 6. OBSERVATION
Catat rate tiap n dan perbedaan antar-seed.

## 7. WHY
Frekuensi sample berfluktuasi; law of large numbers menstabilkan rate, bukan menjamin hasil exact.

## 8. MODIFICATION
Ubah p dan seed; prediksi arah, jalankan, lalu interpretasikan.

## 9. FAILURE EXPERIMENT
Reset seed di dalam setiap trial sehingga hasil tidak merepresentasikan trial independen.

## 10. DEBUGGING
Inspeksi lokasi RNG dibuat, verifikasi rentang p/n, dan bandingkan beberapa seed.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada reliability, A/B simulation, risk, queue, dan Monte Carlo.

## 12. CHECKPOINT
Jelaskan intuisi, ekspektasi manual, kode, visualisasi, variasi parameter, dan arti selisih sample.
