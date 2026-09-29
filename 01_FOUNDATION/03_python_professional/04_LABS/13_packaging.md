# Lab 13 — Packaging dengan pyproject

## 1. TUJUAN
Membuat package installable dengan metadata, layout, import, dan CLI entry point yang dapat diverifikasi.

## 2. PREREQUISITE
Baca lesson 12 dan selesaikan Lab 01.

## 3. SETUP
Buat folder sementara dengan `pyproject.toml`, layout `src/sensor_tools/`, test sederhana, dan virtual environment khusus lab.

## 4. PREDICTION BEFORE RUN
Prediksi import sebelum instalasi, setelah editable install, dan ketika nama package berbeda dari distribution.

## 5. LANGKAH PRAKTIKUM
Aktifkan venv, jalankan `python -m pip install --no-deps -e .`, import dari directory lain, dan jalankan console script.

## 6. OBSERVATION
Catat metadata instalasi, `module.__file__`, version, dan executable yang dibuat.

## 7. WHY
Packaging memisahkan source tree dari mekanisme distribusi; editable install menunjuk source untuk development.

## 8. MODIFICATION
Tambahkan dependency internal antar-module dan bump version; verifikasi metadata berubah.

## 9. FAILURE EXPERIMENT
Hapus `__init__.py` atau salah tulis package discovery/entry point.

## 10. DEBUGGING
Periksa layout, metadata, environment Python/pip, reinstall, lalu uji dari directory di luar project.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada library tim, CLI internal, artifact CI, deployment, dan reproducible environment.

## 12. CHECKPOINT
Buat package kecil installable di venv bersih dan jelaskan trade-off editable install versus artifact release.
