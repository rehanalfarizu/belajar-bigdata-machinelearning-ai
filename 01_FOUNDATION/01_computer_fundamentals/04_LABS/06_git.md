# Lab 06 — Git Snapshot, Branch, dan Conflict

## 1. TUJUAN

Melacak perubahan melalui working tree, staging area, commit, branch, dan penyelesaian conflict.

## 2. PREREQUISITE

Baca lesson 06. Git harus tersedia; gunakan repository sementara, bukan repository utama.

## 3. SETUP

Buat folder sementara, jalankan `git init`, atur identity lokal bila perlu, buat `notes.txt`, stage, dan commit awal.

## 4. PREDICTION BEFORE RUN

Sebelum setiap command, prediksi hasil `git status --short` setelah edit, `git add`, commit, dan perpindahan branch.

## 5. LANGKAH PRAKTIKUM

Buat branch `feature` dan ubah baris pertama. Kembali ke branch awal, ubah baris yang sama secara berbeda, commit, lalu merge `feature`.

## 6. OBSERVATION

Catat status pada setiap state, marker conflict, hasil `git log --oneline --graph --all`, dan isi final.

## 7. WHY

Commit adalah snapshot yang terhubung; branch adalah pointer. Conflict terjadi karena Git tidak dapat memilih dua perubahan pada region sama secara aman.

## 8. MODIFICATION

Ulangi dengan perubahan pada baris berbeda. Prediksi apakah merge tetap conflict dan jelaskan hasilnya.

## 9. FAILURE EXPERIMENT

Saat conflict aktif, coba commit sebelum menghapus semua marker atau sebelum staging hasil resolusi.

## 10. DEBUGGING

Gunakan `git status` sebagai sumber kebenaran, baca tiga bagian marker, susun isi yang benar, `git add`, commit, lalu periksa graph dan file.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul pada code review, kolaborasi branch, hotfix, release, dan investigasi perubahan penyebab regresi.

## 12. CHECKPOINT

Tanpa melihat langkah, buat conflict aman, selesaikan dengan isi yang mempertahankan intent kedua branch, dan jelaskan setiap state Git.
