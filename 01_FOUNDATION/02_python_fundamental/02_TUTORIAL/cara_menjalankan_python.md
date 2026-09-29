# Cara Menjalankan Python dan Notebook

Panduan ini menganggap terminal dibuka pada root repository.

## 1. Buat environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Prompt terminal biasanya menampilkan `(.venv)`. Pastikan interpreter benar:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

Jika import gagal, jangan langsung memasang ulang package. Periksa apakah terminal dan notebook memakai environment yang sama.

## 2. Jalankan script

Buat file latihan di luar materi solusi, misalnya `learning_journal/scratch.py`, lalu jalankan dari root:

```bash
python learning_journal/scratch.py
```

Working directory memengaruhi relative path. Untuk code project, utamakan path yang diberikan lewat configuration/argument; jangan mengandalkan lokasi file source secara diam-diam.

## 3. Jalankan notebook

```bash
jupyter lab
```

Buka salah satu lab:

- `01_FOUNDATION/02_python_fundamental/04_LABS/praktikum.ipynb`
- `01_FOUNDATION/02_python_fundamental/04_LABS/typing_practice.ipynb`

Pilih kernel dari environment project. Jalankan cell berurutan dengan `Shift+Enter`. Setelah selesai, lakukan restart kernel dan run-all untuk membuktikan notebook tidak bergantung pada state tersembunyi.

## 4. Saat terjadi error

1. Baca traceback dari baris paling bawah.
2. Catat exception type, file, line, input, dan working directory.
3. Buat contoh gagal terkecil.
4. Ubah satu hypothesis saja.
5. Tambahkan test atau catatan agar error tidak terulang.

Kasus umum:

- `ModuleNotFoundError`: interpreter/environment atau package path salah.
- `FileNotFoundError`: working directory atau input path salah.
- `PermissionError`: process tidak memiliki akses atau file sedang dikunci.
- kernel tidak muncul: environment belum terdaftar/terpilih di Jupyter.

## 5. Urutan belajar

Kembali ke [README chapter](../README.md): konsep → tutorial → examples → labs → exercise → mini-project/checkpoint. Jangan membuka `99_SOLUTIONS` sebelum mencoba minimal 20–30 menit.
