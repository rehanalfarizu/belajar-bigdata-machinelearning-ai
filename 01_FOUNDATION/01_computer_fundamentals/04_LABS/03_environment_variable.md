# Lab 03 — Shell dan Environment Variable

## 1. TUJUAN

Mengamati environment inheritance dan membedakan shell variable, exported variable, serta default aman.

## 2. PREREQUISITE

Baca lesson 03. Siapkan terminal dan Python 3.

## 3. SETUP

Tulis `show_env.py` yang membaca `APP_MODE` dengan `os.getenv("APP_MODE", "development")` tanpa mencetak secret lain.

## 4. PREDICTION BEFORE RUN

Prediksi output tanpa variable, setelah `APP_MODE=production`, dan setelah `export APP_MODE=production`.

## 5. LANGKAH PRAKTIKUM

Jalankan ketiga kondisi pada shell yang sama. Buka shell baru dan ulangi. Coba pula `APP_MODE=testing python show_env.py` untuk assignment satu command.

## 6. OBSERVATION

Catat nilai yang terlihat oleh shell dan child process pada setiap kondisi. Jangan merekam nilai environment sensitif.

## 7. WHY

Child process menerima salinan environment yang diekspor saat diluncurkan; assignment biasa hanya state internal shell.

## 8. MODIFICATION

Tambahkan parsing `APP_DEBUG` menjadi boolean eksplisit. Uji nilai `1`, `true`, `0`, dan kosong.

## 9. FAILURE EXPERIMENT

Hapus default `APP_MODE` lalu akses dengan `os.environ["APP_MODE"]` ketika variable tidak disetel.

## 10. DEBUGGING

Identifikasi `KeyError`, cek keberadaan key tanpa menampilkan seluruh environment, pilih fail-fast atau default, lalu uji kedua jalur.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul untuk URL database, feature flag, mode deployment, credential injection, dan konfigurasi container.

## 12. CHECKPOINT

Tanpa panduan, buat program yang mewajibkan satu variable, memberi default untuk variable lain, dan tidak pernah mencetak secret.
