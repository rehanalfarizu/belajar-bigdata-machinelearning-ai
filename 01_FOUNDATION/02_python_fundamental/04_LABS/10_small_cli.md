# Lab 10 — Small CLI

## 1. TUJUAN
Membangun CLI kecil dengan input, domain logic, output, error message, dan exit code.

## 2. PREREQUISITE
Baca lesson 14 dan selesaikan lab function serta exception.

## 3. SETUP
Buat `convert.py` dengan `argparse` untuk mengonversi Celsius ke Fahrenheit.

## 4. PREDICTION BEFORE RUN
Prediksi output dan exit code untuk input valid, argumen hilang, serta value bukan angka.

## 5. LANGKAH PRAKTIKUM
Ketik parser, fungsi domain terpisah, `main(argv=None)`, dan `raise SystemExit(main())`. Jalankan tiga skenario dan cek `echo $?`.

## 6. OBSERVATION
Catat stdout, stderr, usage, dan exit code setiap skenario.

## 7. WHY
CLI adalah contract proses: arguments masuk, output/error keluar, exit code memberi sinyal mesin.

## 8. MODIFICATION
Tambahkan pilihan pembulatan dan unit kebalikan; prediksi behavior kombinasi argumen.

## 9. FAILURE EXPERIMENT
Campur parsing dan logic, lalu panggil `sys.exit` dari fungsi domain sehingga sulit diuji.

## 10. DEBUGGING
Pisahkan parse/domain/render, kembalikan exit code dari `main`, dan uji logic tanpa subprocess.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada automation, data migration, admin tool, scheduled job, dan pipeline CI.

## 12. CHECKPOINT
Dari file kosong, buat CLI satu command dengan help, validation, dua exit code, dan minimal tiga uji manual.
