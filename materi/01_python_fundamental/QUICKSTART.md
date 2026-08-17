# Quick Start — Chapter 01

File ini memandumu menyiapkan environment Python dari nol. Kalau kamu sudah pernah install Python dan Jupyter sebelumnya, sebagian langkah ini bisa dilewati. Tapi kalau ini pertama kalinya, ikuti saja urutannya. Total waktu setup sekitar 15 sampai 30 menit.

## Sebelum Mulai: Pahami Apa yang Akan Diinstall

Kamu butuh dua hal utama: Python 3 sebagai bahasa pemrograman yang akan kita pakai, dan Jupyter Notebook sebagai tempat menulis dan menjalankan kode. Jupyter bukan satu-satunya pilihan — Google Colab dan VS Code juga bisa — tapi untuk chapter ini kita pakai Jupyter karena format notebook-nya paling cocok untuk materi yang penuh dengan narasi dan cell kode.

Cara berpikirnya sederhana: Python adalah mesin yang mengeksekusi kode, Jupyter adalah buku tulis interaktif tempat kamu mengetik kode dan melihat hasilnya di tempat yang sama. Setiap "cell" di Jupyter bisa berisi narasi (markdown) atau kode (Python) yang bisa dijalankan.

## Cek Apakah Python Sudah Terinstall

Buka terminal di Mac atau Linux, atau Command Prompt di Windows. Ketik `python3 --version` dan tekan Enter. Kalau muncul tulisan seperti `Python 3.11.5` atau versi 3.x lainnya, berarti Python sudah ada di sistemmu dan kamu bisa lanjut ke langkah berikutnya.

Kalau muncul pesan `command not found` atau `python3 is not recognized`, Python belum terinstall. Jangan panik — buka browser, pergi ke [python.org/downloads](https://www.python.org/downloads/), dan unduh installer untuk sistem operasimu. Untuk Windows, pastikan mencentang opsi "Add Python to PATH" di halaman pertama installer — ini sering terlewat dan menyebabkan Python tidak terdeteksi di terminal.

## Cek Apakah Jupyter Sudah Terinstall

Di terminal yang sama, ketik `jupyter --version`. Kalau muncul daftar versi untuk beberapa komponen (notebook, kernel, dll), berarti Jupyter sudah siap. Kalau tidak, install dengan satu perintah: `pip install jupyter`. Tunggu sampai proses selesai, lalu cek lagi dengan `jupyter --version` untuk memastikan.

## Buka Notebook Chapter Ini

Navigasi ke folder `materi/01_python_fundamental/` lewat terminal. Kalau folder materi ada di home directory, perintahnya seperti `cd ~/Documents/belajar-bigdata-machinelearning-ai/materi/01_python_fundamental` (sesuaikan dengan lokasimu). Setelah berada di folder yang benar, ketik `jupyter notebook` dan tekan Enter.

Tunggu beberapa detik. Browser akan terbuka otomatis menampilkan daftar file di folder itu. Klik `01_python_fundamental.ipynb` untuk membuka notebook utama chapter ini. Tampilan Jupyter memang terasa ramai di awal — ada toolbar di atas, sidebar di kiri, dan deretan cell di tengah. Itu normal.

## Cara Kerja Notebook

Setiap cell di notebook punya dua mode: cell markdown (berwarna abu-abu) berisi narasi penjelasan, dan cell code (berwarna putih dengan label `In []`) berisi kode yang bisa dijalankan. Untuk menjalankan satu cell, klik cell itu lalu tekan `Shift + Enter`. Setelah dijalankan, cell code akan menampilkan output di bawahnya, dan fokus berpindah ke cell berikutnya. Untuk menjalankan semua cell dari atas sampai bawah sekaligus, gunakan menu `Cell > Run All`.

Kebiasaan baik: jalankan cell satu per satu dari atas ke bawah saat pertama kali membuka notebook. Ini memastikan kamu membaca setiap narasi sebelum melihat output. Kalau kamu menjalankan cell di tengah tanpa menjalankan cell di atasnya dulu, kemungkinan besar akan muncul error karena variabel atau modul yang dibutuhkan belum ada.

## Kalau Ada Error

Error di Python terasa menakutkan di awal, tapi sebenarnya ia memberitahumu dengan tepat apa yang salah dan di mana. Pesan error selalu dimulai dengan `Traceback`, lalu menunjukkan file dan nomor baris, dan diakhiri dengan jenis error dan penjelasan singkat. Contoh paling umum saat setup:

Kalau muncul `ModuleNotFoundError: No module named 'jupyter'`, artinya Jupyter belum terinstall di Python yang sedang kamu pakai. Solusinya: jalankan `pip install jupyter` di terminal. Kalau muncul `python3: command not found`, artinya Python belum terinstall atau tidak ada di PATH. Solusi: install ulang Python dan pastikan centang opsi "Add to PATH" (Windows) atau pakai installer resmi dari python.org (Mac).

Kalau Jupyter bisa dibuka tapi cell code pertama langsung error, kemungkinan besar ada masalah dengan instalasi Python itu sendiri. Coba buka terminal dan ketik `python3` saja (tanpa argumen). Kalau masuk ke prompt interaktif Python (ditandai dengan `>>>`), ketik `print("Halo")` dan tekan Enter. Kalau `Halo` muncul, Python bekerja. Ketik `exit()` untuk keluar, lalu coba lagi jalankan cell di Jupyter.

## Cara Membaca Notebook Chapter Ini

Setelah Jupyter terbuka dan notebook chapter sudah dimuat, jangan langsung scroll ke bawah. Cell pertama adalah narasi pembuka. Baca dulu. Cell kedua adalah ajakan untuk mengetik kode tertentu di cell berikutnya. Cell ketiga berisi kode yang bisa langsung dijalankan. Cell keempat menjelaskan apa yang terjadi di balik layar. Cell kelima adalah modifikasi kecil dari kode sebelumnya. Dan di akhir setiap section, ada satu atau dua pertanyaan refleksi terbuka yang mengundangmu berpikir.

Kebiasaan paling penting: jangan copy-paste kode. Ketik ulang. Proses mengetik membuat koneksi di otak yang tidak terjadi kalau kamu hanya menempel. Kalau kode error, baca pesan error-nya — itu memberitahu baris mana dan kenapa. Kalau masih bingung, coba pecah jadi beberapa baris dan jalankan satu per satu untuk melihat di mana persisnya masalah muncul.

## Kalau Sudah Selesai

Setelah menyelesaikan chapter ini, kamu akan paham tipe data Python, operator, struktur data, control flow, fungsi, dan error handling. Untuk chapter berikutnya, kamu akan masuk ke NumPy, Pandas, dan visualisasi data. Pastikan Jupyter dan Python masih bisa berjalan di sistemmu — kalau perlu uninstal sesuatu di kemudian hari, ingat bahwa Jupyter adalah paket Python biasa dan mengikuti konvensi uninstall yang sama.

Kalau di tengah jalan ada masalah yang tidak bisa diselesaikan sendiri, simpan pesan error-nya dan tanyakan di sesi berikutnya. Pesan error adalah informasi paling berharga saat debugging — tanpa itu, masalahnya cuma "kok tidak jalan" tanpa tahu kenapa.

**Lanjut**: Setelah Jupyter terbuka dan notebook chapter ini sudah di depanmu, kerjakan section 1 sampai 8 secara berurutan. Setelah selesai, pindah ke `praktikum.ipynb` untuk melatih pemahamanmu — buka file itu juga di Jupyter, lalu ketik kode jawabanmu langsung di cell kosong yang sudah disediakan.
