# Lab 01 — Module dan Package Boundary

## 1. TUJUAN
Membentuk package dengan public API jelas dan import tanpa side effect.

## 2. PREREQUISITE
Baca lesson 01 dan selesaikan lab import fundamental.

## 3. SETUP
Buat package `sensor_tools` berisi `parser.py`, `stats.py`, dan `__init__.py` serta satu `demo.py` di luar package.

## 4. PREDICTION BEFORE RUN
Prediksi namespace untuk `import sensor_tools` versus `from sensor_tools.parser import parse`.

## 5. LANGKAH PRAKTIKUM
Ketik fungsi kecil, ekspor public function dari `__init__.py`, jalankan demo, lalu inspeksi `dir(sensor_tools)`.

## 6. OBSERVATION
Catat nama publik, lokasi module, dan urutan import.

## 7. WHY
Package boundary mengurangi coupling; `__init__.py` dapat mendefinisikan API yang stabil.

## 8. MODIFICATION
Pindahkan implementasi internal tanpa mengubah import di `demo.py`.

## 9. FAILURE EXPERIMENT
Buat circular import antara `parser` dan `stats`.

## 10. DEBUGGING
Baca pesan partially initialized module, gambar dependency direction, pindahkan shared model ke module netral, lalu uji lagi.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada library internal, service layer, reusable feature engineering, dan SDK.

## 12. CHECKPOINT
Buat package tiga module dengan satu public API dan buktikan refactor internal tidak merusak caller; jelaskan trade-off facade.
