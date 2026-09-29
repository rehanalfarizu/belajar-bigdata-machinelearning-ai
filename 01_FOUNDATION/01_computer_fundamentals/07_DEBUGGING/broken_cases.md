# Broken Cases — Computer Fundamentals

Gunakan flow `SYMPTOM → REPRODUCE → OBSERVE → HYPOTHESIS → TEST → ROOT CAUSE → FIX → VERIFY → PREVENT`. Jangan membaca bagian “observasi awal” sebagai jawaban; root cause harus dibuktikan.

## Case 1 — FileNotFoundError

Symptom: `open("config.json")` gagal walau file terlihat di editor. Observasi awal: command dijalankan dari directory lain. Buktikan resolved path dan perbaiki contract, bukan sekadar menambah `../` secara coba-coba.

## Case 2 — Wrong working directory

Symptom: program menulis output tetapi file “hilang”. Temukan actual output path, jelaskan cwd, lalu rancang output path eksplisit.

## Case 3 — Wrong environment variable

Symptom: `APP_PORT` terbaca kosong pada child process. Bedakan variable shell lokal, exported environment, typo key, dan process yang sudah berjalan sebelum perubahan.

## Case 4 — Port already in use

Symptom: server gagal bind. Identifikasi address/port dan owner process. Jangan menghentikan process sebelum tahu milik siapa dan dampaknya. Pilih reuse atau port baru berdasarkan requirement.

## Case 5 — Invalid JSON

Symptom: parse error pada line/column tertentu. Simpan raw sample aman, kecilkan input, bedakan syntax JSON dari schema/type error, lalu tambah validation.

## Case 6 — Git merge conflict

Symptom: merge berhenti dengan marker. Baca history dan intent kedua branch, pilih/gabung behavior, jalankan verification, stage resolution, dan dokumentasikan keputusan.

## Case 7 — Import menggunakan environment salah

Symptom: package “sudah diinstall” tetapi Python tidak menemukannya. Bandingkan executable `python`, installer yang dipakai, environment aktif, dan import path. Fix environment ownership; jangan memasang berulang ke interpreter acak.
