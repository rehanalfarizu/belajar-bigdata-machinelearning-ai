# Lab 02 — Filesystem, Path, dan Working Directory

## 1. TUJUAN

Menjelaskan resolusi relative path dan membuktikan pengaruh current working directory.

## 2. PREREQUISITE

Baca lesson 02. Gunakan terminal dan Python 3.

## 3. SETUP

Buat `lab_path/data/value.txt` berisi satu baris dan `lab_path/read.py` yang membuka `data/value.txt` serta mencetak `os.getcwd()`.

## 4. PREDICTION BEFORE RUN

Prediksi hasil ketika script dijalankan dari dalam `lab_path` dan dari parent directory. Tulis path mana yang sedang di-resolve.

## 5. LANGKAH PRAKTIKUM

Jalankan dari kedua working directory. Gunakan `pwd`, `ls -l`, dan `python -c "from pathlib import Path; print(Path.cwd())"` untuk mengumpulkan bukti.

## 6. OBSERVATION

Catat command yang berhasil, yang gagal, working directory, dan absolute path file sebenarnya.

## 7. WHY

Relative path di-resolve terhadap working directory process, bukan otomatis terhadap lokasi script. Hubungkan fakta ini ke error `FileNotFoundError`.

## 8. MODIFICATION

Perbaiki script memakai `Path(__file__).resolve().parent / "data" / "value.txt"`, lalu ulangi dari dua lokasi.

## 9. FAILURE EXPERIMENT

Ubah nama file menjadi beda kapital atau hilangkan permission baca pada file sementara, kemudian jalankan lagi.

## 10. DEBUGGING

Baca exception paling bawah, cetak path hasil resolusi, verifikasi dengan `exists()` dan `is_file()`, perbaiki satu penyebab, lalu regression test dari dua working directory.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul pada ETL yang membaca dataset, service yang memuat config, test runner, container, dan scheduled job.

## 12. CHECKPOINT

Buat script baru yang selalu menemukan file sibling dari lokasi mana pun dan jelaskan mengapa `cd` dapat mengubah hasil versi lama.
