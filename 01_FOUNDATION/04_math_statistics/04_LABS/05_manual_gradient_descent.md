# Lab 05 — Manual Gradient Descent

## 1. TUJUAN
Menelusuri update parameter, loss, gradient, dan learning rate.

## 2. PREREQUISITE
Baca lesson 05–06.

## 3. SETUP
Gunakan loss `(w-3)²`, start `w=0`, dan rate 0.25.

## 4. PREDICTION BEFORE RUN
Secara intuitif tentukan arah gerak; hitung manual dua update dengan gradient `2(w-3)`.

## 5. LANGKAH PRAKTIKUM
Jalankan `gradient_descent` dan gambar loss tiap step sebagai bar ASCII.

## 6. OBSERVATION
Bandingkan dua langkah manual dengan kode dan pola loss.

## 7. WHY
Gradient memberi arah kenaikan tercepat; pengurangan gradient menurunkan loss jika step sesuai.

## 8. MODIFICATION
Bandingkan rate 0.05, 0.25, 0.9, dan 1.1; prediksi convergence/oscillation.

## 9. FAILURE EXPERIMENT
Gunakan rate negatif atau terlalu besar hingga loss naik.

## 10. DEBUGGING
Periksa tanda update, magnitude gradient, dan loss per step; kecilkan rate lalu verifikasi tren.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada training model, tuning optimizer, dan diagnosis loss divergen.

## 12. CHECKPOINT
Lakukan tiga update manual, cocokkan kode/visual, ubah rate, dan jelaskan trade-off speed versus stability.
