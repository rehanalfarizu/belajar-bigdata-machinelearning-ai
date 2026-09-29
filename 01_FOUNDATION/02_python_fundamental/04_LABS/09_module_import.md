# Lab 09 — Module dan Import

## 1. TUJUAN
Memahami namespace, import-time execution, dan entry-point guard.

## 2. PREREQUISITE
Baca lesson 13.

## 3. SETUP
Buat `temperature.py` dengan fungsi konversi dan satu print di top level; buat `app.py` yang mengimpornya.

## 4. PREDICTION BEFORE RUN
Prediksi output saat menjalankan `temperature.py` langsung dan saat menjalankan `app.py`.

## 5. LANGKAH PRAKTIKUM
Ketik kedua file, jalankan dua cara, lalu tambahkan `if __name__ == "__main__":` pada demo.

## 6. OBSERVATION
Catat nilai `__name__` dan side effect yang terjadi saat import sebelum/sesudah guard.

## 7. WHY
Import mengeksekusi top level sekali dan membuat namespace module; guard memisahkan library dari program.

## 8. MODIFICATION
Pindahkan module ke package `sensors/` dengan `__init__.py` dan import public function.

## 9. FAILURE EXPERIMENT
Ubah nama file menjadi `json.py` lalu import standard-library `json` untuk memicu shadowing.

## 10. DEBUGGING
Cetak `module.__file__`, inspeksi `sys.path`, ganti nama collision, hapus cache lokal bila ada, lalu uji ulang.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada reusable package, test discovery, CLI entry point, dan struktur service.

## 12. CHECKPOINT
Buat package dua module tanpa import side effect dan demonstrasikan pemakaian public API.
