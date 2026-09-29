# Lab 03 — List, Dictionary, dan Mutation

## 1. TUJUAN
Mengamati alias, mutation, shallow copy, dan perubahan nested data.

## 2. PREREQUISITE
Baca lesson 05–06; pahami assignment dasar.

## 3. SETUP
Buat list record sensor, lalu bind `alias = sensors` dan `copied = sensors.copy()`.

## 4. PREDICTION BEFORE RUN
Prediksi isi ketiga name setelah append ke alias dan setelah mengubah field dictionary pertama.

## 5. LANGKAH PRAKTIKUM
Ketik operasi satu per satu; cetak data dan `id` container/nested dictionary setiap tahap.

## 6. OBSERVATION
Catat perubahan mana yang menembus alias dan shallow copy.

## 7. WHY
Shallow copy membuat container baru tetapi mempertahankan reference ke object nested.

## 8. MODIFICATION
Bandingkan list comprehension yang menyalin setiap dictionary dengan `copy.deepcopy`; prediksi dahulu.

## 9. FAILURE EXPERIMENT
Hapus key yang tidak ada dan akses key hilang dengan indexing.

## 10. DEBUGGING
Bedakan `KeyError` dari mutation tak disengaja; gunakan `get` hanya jika missing memang valid, lalu tambah test.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul saat membersihkan batch record, caching, payload request, dan shared test fixture.

## 12. CHECKPOINT
Buat transformasi yang mengubah hasil tanpa memutasi input dan buktikan dengan assertion.
