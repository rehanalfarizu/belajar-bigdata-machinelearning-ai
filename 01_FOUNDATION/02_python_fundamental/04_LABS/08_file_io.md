# Lab 08 — File I/O

## 1. TUJUAN
Membaca, memvalidasi, dan menulis file dengan lifecycle resource yang benar.

## 2. PREREQUISITE
Baca lesson 12 dan Lab path.

## 3. SETUP
Buat `readings.txt` berisi satu angka per baris termasuk satu baris invalid.

## 4. PREDICTION BEFORE RUN
Prediksi hasil `read`, `readline`, iterasi file, dan posisi failure konversi.

## 5. LANGKAH PRAKTIKUM
Ketik program dengan `with open(..., encoding="utf-8")`, nomor baris, parsing, lalu tulis hanya data valid ke file output.

## 6. OBSERVATION
Catat baris valid/invalid, isi output, dan bukti file tertutup setelah blok.

## 7. WHY
Context manager menjamin cleanup; validasi per baris memberi lokasi error yang dapat ditindaklanjuti.

## 8. MODIFICATION
Ubah format menjadi CSV sederhana dua kolom dan tambahkan header.

## 9. FAILURE EXPERIMENT
Coba path salah, encoding salah, dan directory sebagai file—satu per satu.

## 10. DEBUGGING
Klasifikasikan `FileNotFoundError`, `UnicodeDecodeError`, atau `IsADirectoryError`; periksa path/input lalu regression test.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada log ingestion, dataset, config, export report, dan checkpoint pipeline.

## 12. CHECKPOINT
Buat converter file yang melaporkan nomor baris rusak dan tidak meninggalkan output setengah benar.
