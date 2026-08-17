# Chapter 01 — Python Fundamental

Selamat datang di chapter pertama. Ini adalah fondasi dari semua yang akan kita pelajari setelahnya — dari variabel dan tipe data, sampai fungsi dan error handling. Chapter ini bukan hanya tentang sintaksis Python, tapi tentang membangun cara berpikir bagaimana Python bekerja di balik layar. Setelah menyelesaikannya, kamu akan bisa membaca dan menulis program Python sendiri, memahami ekosistem library Python, dan punya pijakan yang cukup kuat untuk masuk ke data analysis, machine learning, dan deployment.

Python dipilih bukan karena popularitasnya, tapi karena filosofi desainnya yang menomor-satukan keterbacaan. Kode Python dibaca hampir seperti kalimat bahasa Inggris, bukan seperti instruksi mesin. Ini membuat learning curve lebih landai untuk pemula, dan kolaborasi antar engineer jadi lebih ringan. Di dunia data science dan machine learning, hampir semua algoritma dan library utama tersedia dalam Python. NumPy, Pandas, scikit-learn, TensorFlow, dan PyTorch semuanya adalah library Python. Ekosistem ini adalah alasan utama kenapa data engineer dan machine learning engineer nyaris selalu memulai perjalanan mereka dari Python.

## Apa yang Akan Kamu Kuasai?

Chapter ini terdiri dari 8 section yang dibangun secara bertahap. Setiap section dirancang untuk diikuti secara berurutan, karena konsep di section belakang selalu dibangun di atas section sebelumnya. Jangan meloncat. Berikut adalah peta section dan apa yang akan kamu bisa lakukan setelah masing-masing selesai.

**Section 1 — Variabel dan Tipe Data.** Setelah section ini kamu akan bisa menyimpan angka, teks, dan nilai benar/salah dalam variabel, dan kamu akan paham kenapa Python memperlakukan variabel sebagai "label" yang menunjuk ke objek, bukan kotak penyimpanan. Pemahaman ini akan menjelaskan banyak perilaku Python yang terasa aneh di awal, seperti kenapa satu list bisa berubah di dua tempat sekaligus.

**Section 2 — Operator dan String.** Setelah section ini kamu akan bisa melakukan operasi matematika, perbandingan, dan logika pada data. Kamu juga akan mahir memotong string dengan indexing dan slicing, memformat teks dengan f-string, dan memakai method string yang paling sering dipakai seperti `upper`, `replace`, dan `split`.

**Section 3 — Struktur Data.** Ini adalah section terpadat. Kamu akan menguasai empat struktur utama: `list` untuk kumpulan data yang bisa berubah, `dict` untuk pasangan kunci-nilai, `tuple` untuk kumpulan data yang tidak boleh berubah, dan `set` untuk koleksi unik tanpa urutan. Kamu juga akan belajar list comprehension — cara Pythonic untuk membangun list baru dari list lama dalam satu baris.

**Section 4 — Control Flow.** Setelah section ini kamu akan bisa membuat program yang mengambil keputusan dengan `if/elif/else`, mengulang pekerjaan dengan `for` loop saat kamu tahu berapa kali harus mengulang, dan `while` loop saat pengulangan bergantung pada kondisi. Kamu juga akan paham kapan harus memakai `break` untuk keluar lebih awal dan `continue` untuk melewati satu iterasi.

**Section 5 — Fungsi.** Setelah section ini kamu akan bisa membungkus logika yang berulang menjadi blok yang bisa dipanggil berulang kali. Kamu akan paham parameter, return value, default argument, dan konsep scope — kapan sebuah variabel bisa diakses dan kapan tidak.

**Section 6 — Error Handling.** Setelah section ini kamu akan terbiasa membaca pesan error Python tanpa panik, dan kamu akan bisa menangani error yang bisa diprediksi dengan `try/except` supaya program tidak crash di tengah jalan. Kamu juga akan belajar kapan error handling benar-benar diperlukan dan kapan ia malah membuat kode lebih membingungkan.

**Section 7 — Modul dan Import.** Setelah section ini kamu akan bisa menggunakan library dari standard library (seperti `math`, `random`, `datetime`) dan memasang library eksternal dengan `pip`. Ini adalah gerbang masuk ke ekosistem Python yang sangat luas.

**Section 8 — Mini Project.** Section terakhir menyatukan semua konsep dari section 1 sampai 7 dalam satu proyek: aplikasi CLI untuk mengelola to-do list. Kamu akan membangunnya dari nol sebagai sintesis.

## Library dan Tools

Chapter ini hanya memakai Python standard library — tidak perlu instalasi tambahan. Ini disengaja supaya fokus kamu adalah bahasa Python itu sendiri, bukan library eksternal.

| Library | Kapan Dipakai | Cara Import |
|---|---|---|
| `math` | Fungsi matematika (sqrt, pow, log, sin, cos) | `import math` |
| `random` | Generate angka atau pilihan acak | `import random` |
| `statistics` | Mean, median, stdev, variance | `import statistics` |
| `datetime` | Manipulasi tanggal dan waktu | `import datetime` |
| `collections` | Struktur data tambahan seperti `Counter` | `from collections import Counter` |
| `csv` | Baca dan tulis file CSV | `import csv` |

## Prasyarat

Chapter ini adalah chapter pertama dan tidak membutuhkan pengetahuan programming sebelumnya. Yang perlu disiapkan hanya beberapa hal teknis: Python 3 terinstall di sistem, Jupyter Notebook atau Jupyter Lab untuk membuka file `.ipynb`, text editor untuk menulis file `.py`, dan terminal atau command line untuk menjalankan perintah dasar. Detail setup ada di `QUICKSTART.md` — baca file itu dulu kalau ini pertama kalinya kamu menyentuh Python.

## Cara Mengikuti Chapter Ini

Ada 4 file utama di folder ini, dan masing-masing punya peran berbeda. Jangan baca semuanya sekaligus — ikuti urutan yang disarankan supaya pengalaman belajar tetap terstruktur.

Mulailah dengan `QUICKSTART.md` untuk setup environment. Kalau Python dan Jupyter sudah terinstall, langkah ini bisa dilewati. Lalu buka `01_python_fundamental.ipynb` di Jupyter Notebook atau Jupyter Lab, dan ikuti 8 section secara berurutan. Setiap section mengikuti pola 5-cell: narasi pendek, ajakan untuk mengetik, kode mini, breakdown, dan modifikasi. Jangan cuma membaca — jalankan setiap cell, amati outputnya, ubah kode, dan amati perubahannya. Saat kamu lupa sintaksis atau ingin tahu cara Pythonic untuk melakukan sesuatu, rujuk `PANDUAN_KODE.md`. Setelah menyelesaikan notebook, kerjakan latihan di `praktikum.ipynb` untuk menguji pemahamanmu — format notebook supaya kamu bisa langsung mengetik kode latihan di cell kosong yang sudah disediakan.

## Estimasi Waktu

Pemula total biasanya butuh 8 sampai 12 jam untuk menyelesaikan chapter ini secara menyeluruh. Ini termasuk membaca notebook, menjalankan semua cell, mengerjakan latihan, dan membangun mini project. Jangan terburu-buru. Lebih baik dua sampai tiga hari dengan pemahaman mendalam daripada satu hari dengan hafalan sintaksis tanpa pemahaman konsep.

Kalau di tengah jalan kamu merasa stuck atau bingung, itu normal. Programming bukan tentang menghafal — programming tentang mengenali pola dan memecahkan masalah. Semakin sering kamu mengeksekusi kode, memodifikasi, membaca error, dan men-debug, semakin cepat pola itu terbentuk di kepalamu.

## File Lain di Folder Ini

`QUICKSTART.md` berisi setup environment dari nol. `01_python_fundamental.ipynb` adalah notebook utama dengan 8 section. `PANDUAN_KODE.md` adalah referensi ringkas pattern Pythonic dan anti-pattern. `praktikum.ipynb` berisi latihan bertingkat per section (cell markdown berisi soal + cell kode kosong yang siap kamu ketik) dan satu tantangan mini project di akhir.

**Lanjut**: Buka `QUICKSTART.md` untuk setup, atau langsung ke `01_python_fundamental.ipynb` kalau environment sudah siap.
