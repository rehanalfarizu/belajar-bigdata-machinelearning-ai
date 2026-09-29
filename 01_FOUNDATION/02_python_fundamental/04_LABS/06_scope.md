# Lab 06 — Scope dan Name Resolution

## 1. TUJUAN
Membedakan local, enclosing, global, dan efek mutation object.

## 2. PREREQUISITE
Baca lesson 10.

## 3. SETUP
Buat global `threshold = 10` dan fungsi yang memiliki local `threshold = 5`.

## 4. PREDICTION BEFORE RUN
Prediksi nilai di dalam dan luar fungsi, lalu prediksi efek append ke list global.

## 5. LANGKAH PRAKTIKUM
Ketik eksperimen shadowing, nested function, dan mutation list; cetak pada boundary call.

## 6. OBSERVATION
Catat name mana yang ditemukan oleh aturan LEGB dan object mana yang termutasi.

## 7. WHY
Rebinding name dan mutating object adalah operasi berbeda; scope menentukan pencarian name.

## 8. MODIFICATION
Ubah desain agar fungsi menerima threshold dan list sebagai parameter serta mengembalikan hasil baru.

## 9. FAILURE EXPERIMENT
Baca lalu assign global name dalam fungsi tanpa deklarasi sehingga muncul `UnboundLocalError`.

## 10. DEBUGGING
Identifikasi assignment yang membuat name lokal, hilangkan hidden dependency, lalu test bahwa global tidak berubah.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada config global, test isolation, callback, closure, dan shared mutable state.

## 12. CHECKPOINT
Jelaskan satu contoh rebinding dan mutation, lalu refactor fungsi agar pure tanpa global.
