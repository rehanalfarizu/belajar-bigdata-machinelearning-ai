# Lab 04 — Numeric Derivative

## 1. TUJUAN
Memperkirakan slope lokal dan memahami pengaruh step size.

## 2. PREREQUISITE
Baca lesson 04.

## 3. SETUP
Gunakan `f(x)=x²` pada `x=3` dan dua titik di sekitar x.

## 4. PREDICTION BEFORE RUN
Dengan intuisi grafik prediksi slope positif; hitung manual derivative analitik `2x=6`.

## 5. LANGKAH PRAKTIKUM
Panggil `numeric_derivative(f, 3, h)` untuk beberapa h dan buat bar ASCII besar error absolut.

## 6. OBSERVATION
Catat estimasi, error terhadap 6, dan pola saat h mengecil.

## 7. WHY
Central difference memakai perubahan output di lingkungan kecil; h terlalu besar bias, terlalu kecil terkena floating-point.

## 8. MODIFICATION
Uji `x³` atau `sin(x)` dan ubah x/h sebelum menginterpretasikan.

## 9. FAILURE EXPERIMENT
Gunakan h nol dan h sangat kecil.

## 10. DEBUGGING
Validasi h positif, bandingkan beberapa skala, dan jangan menganggap h terkecil selalu terbaik.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada optimisasi, gradient checking, sensitivity analysis, dan simulation.

## 12. CHECKPOINT
Pilih fungsi, berikan intuisi/manual, kode, visual error, variasi h, dan interpretasi keterbatasan.
