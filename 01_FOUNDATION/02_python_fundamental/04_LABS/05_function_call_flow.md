# Lab 05 — Function Call Flow

## 1. TUJUAN
Melacak argument, parameter, local state, return value, dan caller.

## 2. PREREQUISITE
Baca lesson 09.

## 3. SETUP
Buat fungsi `normalize(value, minimum, maximum)` dan caller yang menyimpan hasilnya.

## 4. PREDICTION BEFORE RUN
Gambar urutan call untuk input 15 pada rentang 10–20; tulis local value setiap langkah.

## 5. LANGKAH PRAKTIKUM
Ketik fungsi dengan print `ENTER`, intermediate, `RETURN`, dan print caller sesudah call.

## 6. OBSERVATION
Bandingkan urutan aktual dengan diagram dan catat kapan control kembali ke caller.

## 7. WHY
Setiap call memiliki local frame; `return` mengirim value dan menghentikan eksekusi fungsi saat itu.

## 8. MODIFICATION
Tambahkan guard untuk rentang terbalik dan fungsi kedua yang memanggil `normalize`.

## 9. FAILURE EXPERIMENT
Hapus `return` pada jalur tertentu lalu lakukan operasi angka pada hasilnya.

## 10. DEBUGGING
Telusuri asal `None` dari caller ke callee, pastikan semua jalur memenuhi contract, dan tambah assertion.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada business logic, pipeline transform, API handler, dan library reusable.

## 12. CHECKPOINT
Buat fungsi dengan dua jalur return, gambar call flow, dan uji kedua jalur tanpa melihat contoh.
