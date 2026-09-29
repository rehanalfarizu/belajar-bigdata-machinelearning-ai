# Chapter 02 — Data Analysis dengan NumPy & Pandas

Sekarang fondasi Python sudah kamu kuasai. Saatnya bertemu dua library yang akan kamu pakai hampir setiap hari sebagai data/ML engineer: **NumPy** untuk komputasi numerik, dan **Pandas** untuk mengolah data tabular. Chapter ini adalah jembatan dari "bisa menulis program Python" ke "bisa menganalisis data nyata" — misalnya CSV dari Kaggle, log dari server, atau dataset yang dikirimkan rekan kerja.

Kalau kamu sudah familiar dengan Excel atau SQL, banyak konsep di sini akan terasa seperti versi yang lebih eksplisit dan bisa diotomasi. Kalau belum, jangan khawatir — kita mulai dari analogi yang sama sekali tidak butuh pengalaman spreadsheet. Yang kamu butuhkan hanya chapter 01: variabel, list, dict, loop, dan fungsi.

## Daftar Section

Chapter ini dibagi menjadi delapan section. Section satu sampai empat adalah dunia NumPy — kita akan paham kenapa komputasi numerik di Python hampir selalu pakai NumPy, dan bagaimana array bekerja sebagai blok bangunan utama. Section lima sampai tujuh masuk ke Pandas — di sini kamu mulai bekerja dengan tabel, dan merasa familiar karena struktur DataFrame mirip tabel di spreadsheet. Section kedelapan adalah mini project: kita akan menggabungkan semua yang sudah dipelajari untuk melakukan EDA (Exploratory Data Analysis) pada dataset Iris yang legendaris itu.

Section satu membahas kenapa NumPy lebih cepat dari list Python untuk komputasi numerik, dan bagaimana cara membuat array. Section dua mendalami shape, reshape, dan cara mengambil elemen dari array multi-dimensi. Section tiga membawa kita ke kekuatan terbesar NumPy: operasi vektor dan agregasi yang berjalan tanpa loop. Section empat menutup dunia NumPy dengan dua fitur yang paling sering kamu pakai di dunia kerja: broadcasting (operasi antara array dengan bentuk berbeda) dan boolean indexing (menyaring data dengan kondisi).

Section lima memperkenalkan Pandas dan DataFrame — struktur data tabular dengan kolom bernama. Kita juga akan belajar cara membaca file CSV, karena hampir semua data di industri datang dalam format itu. Section enam fokus pada cara mengambil dan menyaring data dari DataFrame dengan `.loc`, `.iloc`, dan boolean indexing ala Pandas. Section tujuh adalah trio transformasi data yang paling penting di industri: group by untuk agregasi, merge untuk menggabungkan tabel, dan penanganan missing values. Section kedelapan adalah ujian: kita analisis dataset Iris dari awal sampai akhir dan menarik insight.

## Prasyarat

Chapter ini mengasumsikan kamu sudah paham variabel, list, dict, tuple, control flow, fungsi, dan cara import modul dari chapter 01. Kalau kamu merasa ragu pada bagian mana pun, tidak ada salahnya membuka lagi `01_python_fundamental/01_python_fundamental.ipynb` untuk mengingat. NumPy dan Pandas akan terasa jauh lebih ringan kalau fondasimu sudah kuat.

## Library yang Dipakai

Chapter ini menggunakan tiga library utama. Yang pertama adalah **NumPy** (diimpor sebagai `np`) — untuk komputasi numerik dan array multi-dimensi. Yang kedua adalah **Pandas** (diimpor sebagai `pd`) — untuk DataFrame dan manipulasi data tabular. Yang ketiga adalah **Matplotlib** (diimpor sebagai `plt`) — untuk visualisasi dasar, dipakai di section terakhir. Semua tiga dipasang dengan satu perintah: `pip install numpy pandas matplotlib`. Di chapter 04 kamu akan bertemu Seaborn, dan di chapter 05 kamu akan bertemu Scikit-learn.

## Cara Membaca Chapter Ini

Mulai dari `02_data_analysis.ipynb`. Notebook itu adalah pengalaman utama — ikuti setiap cell secara berurutan, ketik ulang kode di code cell, amati outputnya, dan jawab pertanyaan refleksi yang muncul di akhir setiap section. Setelah selesai (atau kalau kamu butuh istirahat), buka `praktikum.ipynb` untuk menguji pemahamanmu dengan soal-soal bertingkat. Kalau kamu ingin menulis kode dari nol untuk melatih memori otot, buka `typing_practice.ipynb` — itu akan memaksamu membangun solusi NumPy dan Pandas dari baris pertama.

## File Pendukung

`PANDUAN_KODE.md` adalah referensi pattern dan anti-pattern yang akan kamu temui di chapter ini. File itu bukan duplikat notebook — buka hanya saat kamu butuh mengingat idiom tertentu (misalnya cara paling idiomatik untuk melakukan group by, atau kapan pakai `.loc` vs `.iloc`). README ini sengaja tidak menjelaskan sintaksis atau konsep — semuanya ada di notebook.

## Setelah Chapter Ini

Begitu chapter 02 selesai, kamu sudah punya bekal yang cukup untuk chapter 03: Machine Learning Fundamental. Di sana kita akan menggunakan Pandas untuk menyiapkan data, dan NumPy untuk operasi matematis yang mendasari algoritma ML. Chapter 03 adalah saat di mana semua yang kamu pelajari di 01 dan 02 akan dipakai dalam konteks yang lebih besar.
