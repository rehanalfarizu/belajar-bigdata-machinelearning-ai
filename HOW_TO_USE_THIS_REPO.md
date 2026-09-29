# Cara Menggunakan Repository Ini

Mulai dari [START_HERE](START_HERE.md), pilih fase berdasarkan gate kompetensi, lalu ikuti urutan bernomor di README chapter. Bulan adalah ritme yang disarankan; evidence tetap menjadi syarat lulus.

## Siklus belajar satu chapter

1. Baca `01_TEORI/konsep_dasar.md`, lalu teori mendalam bila tersedia.
2. Ikuti `02_TUTORIAL`, ketik ulang contoh, dan jelaskan setiap keputusan.
3. Jalankan `04_LABS` atau script yang tersedia.
4. Kerjakan exercise sekurangnya 20–30 menit tanpa membuka `99_SOLUTIONS`.
5. Selesaikan problem, debugging case, mini-project, dan checkpoint yang tersedia.
6. Catat bukti, kegagalan, dan keputusan di [learning journal](learning_journal/README.md).
7. Kerjakan capstone bulan terkait di [06_PROJECTS](06_PROJECTS/README.md).

Tidak semua chapter memerlukan semua subfolder. Folder hanya ada jika berisi pekerjaan nyata.

## Notebook dan project Python

Aktifkan environment dari root repository, lalu buka Jupyter agar path data konsisten:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Untuk notebook: baca narasi, prediksi hasil cell, jalankan berurutan, lalu ubah satu variabel dan catat dampaknya. Restart kernel dan jalankan semua cell sebelum menyimpan evidence.

Untuk project `.py`: baca README chapter, jalankan test terlebih dahulu, ubah satu hal kecil, lalu jalankan test lagi. Pisahkan input/output, domain logic, configuration, dan state. Jangan menyimpan credential, model generated, cache, atau data sensitif ke Git.

## Cara memecahkan latihan

Tuliskan: diketahui, ditanya, constraints, asumsi, dan contoh terkecil. Pecah masalah, pilih baseline, ukur hasil, lalu uji edge case. Jika buntu, kecilkan kasus dan baca error dari penyebab paling bawah. Solusi baru boleh dibuka setelah usaha nyata minimal 20–30 menit; setelah itu tutup solusi dan tulis ulang dari ingatan.

## Cara memakai AI

Gunakan AI sebagai reviewer dan sparring partner: minta petunjuk bertahap, test case, kritik asumsi, atau pertanyaan Socratic. Jangan meminta jawaban final sebelum mencoba. Verifikasi keluaran terhadap kode, eksperimen, dokumentasi resmi, dan batas domain. Jangan kirim secrets atau data sensitif.

## Definisi bukti lulus

- **Project:** artefak dapat dijalankan ulang dari petunjuk tertulis.
- **Tests:** happy path, edge case, dan satu failure mode relevan lulus.
- **Reasoning challenge:** keputusan dan trade-off dapat dijelaskan tanpa menyalin materi.
- **Checkpoint:** memenuhi kriteria chapter.
- **Date:** dicatat di [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md).

Jika ada link atau notebook rusak setelah perubahan, jalankan `python tools/audit_repository.py` dan laporkan path serta pesan errornya.
