# Learning Protocol — Cara Belajar Setiap Lesson

## Siklus utama

```text
PREDICT → RUN → OBSERVE → EXPLAIN → MODIFY → VERIFY
```

1. **Predict:** tulis output atau behavior yang kamu perkirakan beserta alasannya.
2. **Run:** jalankan persis satu eksperimen dari environment dan working directory yang diketahui.
3. **Observe:** catat output, error type, state, timing, atau file yang berubah—bukan hanya “berhasil/gagal”.
4. **Explain:** hubungkan observasi dengan mental model lesson.
5. **Modify:** ubah satu variabel saja.
6. **Verify:** prediksi ulang, jalankan test, dan bandingkan dengan baseline.

Jika prediksi salah, itu data belajar paling berharga. Jangan hapus prediksi awal; koreksi penjelasannya.

## Flow debugging

```text
SYMPTOM → REPRODUCE → OBSERVE → HYPOTHESIS → TEST
→ ROOT CAUSE → FIX → VERIFY → PREVENT
```

- Salin pesan error lengkap dan langkah reproduksi minimal.
- Pisahkan fakta dari dugaan.
- Buat beberapa hypothesis, lalu pilih test termurah yang membedakannya.
- Jangan mengubah banyak hal sekaligus.
- Setelah fix, jalankan kasus awal dan edge case.
- Tambahkan test, validation, log, atau dokumentasi yang mencegah regresi.

## Bukti yang disimpan

Untuk setiap chapter, simpan: catatan prediksi, command/input, hasil, satu error yang didiagnosis, solution alternatif, trade-off, test evidence, dan jawaban checkpoint dengan kata sendiri.

## Menggunakan AI

Minta AI memberi pertanyaan, hint bertahap, counterexample, atau review reasoning. Jangan meminta full solution sebelum mencoba. Jangan menyalin output yang tidak dapat kamu jelaskan. Selalu verifikasi terhadap eksperimen dan dokumentasi resmi.
