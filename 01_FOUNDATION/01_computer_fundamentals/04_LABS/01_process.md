# Lab 01 — Process, PID, CPU, dan Memory

## 1. TUJUAN

Membedakan program dari process serta mengamati PID, status hidup, CPU, dan memory sebuah process.

## 2. PREREQUISITE

Baca lesson 01. Siapkan dua terminal dan Python 3.

## 3. SETUP

Buat folder sementara, lalu ketik file `worker.py` yang mencetak PID dengan `os.getpid()` dan melakukan `time.sleep(60)`.

## 4. PREDICTION BEFORE RUN

Tulis: apakah dua eksekusi file yang sama mempunyai PID dan memory yang sama? Apa yang terjadi sesudah process dihentikan?

## 5. LANGKAH PRAKTIKUM

Jalankan `python worker.py` di Terminal A. Di Terminal B, cari PID itu dengan `ps -p <PID> -o pid,ppid,state,%cpu,%mem,command`. Jalankan instance kedua, bandingkan keduanya, lalu hentikan salah satu dengan `Ctrl-C`.

## 6. OBSERVATION

Catat dua PID, PPID, state, dan status setelah penghentian. Ambil bukti bahwa file program tetap ada walaupun process sudah tidak ada.

## 7. WHY

File adalah instruksi pasif; process adalah eksekusi aktif dengan identity dan resource sendiri. Jelaskan mengapa satu program dapat melahirkan beberapa process.

## 8. MODIFICATION

Ubah sleep menjadi loop perhitungan selama lima detik. Prediksi dan bandingkan `%CPU` sebelum dan sesudah perubahan.

## 9. FAILURE EXPERIMENT

Ganti alokasi kecil dengan list yang jauh lebih besar hingga penggunaan memory terlihat naik; jangan memakai ukuran yang berisiko menghabiskan RAM.

## 10. DEBUGGING

Jika PID tidak ditemukan, cek apakah process sudah selesai, apakah PID tersalin benar, dan apakah kamu menjalankan Terminal B sebelum 60 detik. Perbaiki lalu ulangi observasi.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul saat mencari worker macet, memory leak, job training berat, atau service yang mati sebelum health check.

## 12. CHECKPOINT

Tanpa panduan, jalankan dua process dari satu file, tunjukkan identity berbeda, hentikan satu, dan jelaskan program-versus-process dalam tiga kalimat.
