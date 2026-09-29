# Lab 03 — Type Hints dan Static Check

## 1. TUJUAN
Menangkap mismatch kontrak sebelum runtime dan membedakannya dari validasi runtime.

## 2. PREREQUISITE
Baca lesson 04. Aktifkan type checker editor atau siapkan environment lab dengan `python -m pip install mypy`.

## 3. SETUP
Buat `typed_lab.py` dengan fungsi `average(values: list[float]) -> float` dan caller benar.

## 4. PREDICTION BEFORE RUN
Prediksi hasil pemeriksaan dan runtime bila caller memberi `["1", "2"]` atau bila fungsi lupa return.

## 5. LANGKAH PRAKTIKUM
Ketik dua mismatch, jalankan `python -m mypy --strict typed_lab.py`, lalu jalankan Python dan bandingkan temuannya.

## 6. OBSERVATION
Catat diagnostic statis, baris, runtime result, dan bug yang hanya ditemukan salah satu mekanisme.

## 7. WHY
Hint adalah kontrak yang dibaca checker; Python tidak otomatis menegakkannya ketika runtime.

## 8. MODIFICATION
Terima `Sequence[float]` alih-alih `list[float]` dan uji tuple. Nilai apakah kontrak menjadi lebih fleksibel.

## 9. FAILURE EXPERIMENT
Gunakan `Any` untuk membungkam error lalu masukkan object yang gagal saat operasi.

## 10. DEBUGGING
Telusuri sumber `Any`, perketat boundary dengan parsing/narrowing, dan jalankan static check plus test runtime.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada review, refactor, IDE, library API, dan pipeline CI.

## 12. CHECKPOINT
Buat module yang lolos mode strict, sengaja munculkan satu mismatch, perbaiki, dan jelaskan trade-off presisi versus fleksibilitas.
