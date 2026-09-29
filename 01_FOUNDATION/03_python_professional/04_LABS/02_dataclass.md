# Lab 02 — Dataclass dan Invariant

## 1. TUJUAN
Memodelkan record typed dengan equality, representation, dan invariant.

## 2. PREREQUISITE
Baca lesson 02–03.

## 3. SETUP
Gunakan `Reading` pada `patterns_lab.py` sebagai referensi, lalu ketik versi sendiri dari kosong.

## 4. PREDICTION BEFORE RUN
Prediksi hasil equality dua instance dan assignment pada dataclass `frozen=True`.

## 5. LANGKAH PRAKTIKUM
Tambahkan unit, timestamp, `__post_init__`, dan method konversi yang mengembalikan instance baru.

## 6. OBSERVATION
Catat `repr`, equality, validasi, dan efek frozen.

## 7. WHY
Dataclass mengurangi boilerplate record; invariant menjaga object valid sejak konstruksi.

## 8. MODIFICATION
Bandingkan desain mutable dan frozen untuk update value.

## 9. FAILURE EXPERIMENT
Buat reading dengan ID kosong atau unit tidak dikenal dan coba mutasi instance frozen.

## 10. DEBUGGING
Pisahkan invalid domain data dari `FrozenInstanceError`, perbaiki constructor/caller, lalu tambah regression test.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada event, DTO, config, feature record, dan hasil query.

## 12. CHECKPOINT
Buat model domain dengan dua invariant dan jelaskan trade-off dataclass frozen dibanding dictionary.
