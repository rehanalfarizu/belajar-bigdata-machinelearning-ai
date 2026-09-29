# Lab 04 — Network, Localhost, dan Port

## 1. TUJUAN

Membuktikan bahwa server bind ke address dan port, serta mendiagnosis port kosong dan port bentrok.

## 2. PREREQUISITE

Baca lesson 04. Siapkan dua terminal dan Python 3.

## 3. SETUP

Di Terminal A jalankan `python -m http.server 8765 --bind 127.0.0.1` dalam folder sementara tanpa data sensitif.

## 4. PREDICTION BEFORE RUN

Prediksi hasil koneksi ke port 8765, 8766, dan hasil menjalankan server kedua pada port 8765.

## 5. LANGKAH PRAKTIKUM

Di Terminal B jalankan `python -c "import socket; print(socket.create_connection(('127.0.0.1',8765),2))"`. Periksa listener dengan `lsof -nP -iTCP:8765 -sTCP:LISTEN`, lalu hentikan server.

## 6. OBSERVATION

Catat address lokal, PID listener, koneksi berhasil, dan perubahan hasil setelah server dihentikan.

## 7. WHY

IP memilih host/interface dan port memilih process listener. `localhost` menunjuk mesin sendiri, bukan service tertentu.

## 8. MODIFICATION

Pindahkan server ke port 8877. Sebelum menjalankan, prediksi command mana yang harus ikut berubah.

## 9. FAILURE EXPERIMENT

Saat server pertama aktif, jalankan server kedua pada port sama; lalu coba koneksi ke port tanpa listener.

## 10. DEBUGGING

Bedakan `address already in use` dari `connection refused`. Cari pemilik port, verifikasi konfigurasi client-server, perbaiki, lalu tes ulang.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul pada API lokal, database, Jupyter, Kafka, container port mapping, dan health check.

## 12. CHECKPOINT

Jalankan service di port pilihanmu, buktikan listener dan koneksi, buat satu kegagalan port, lalu diagnosis tanpa menebak.
