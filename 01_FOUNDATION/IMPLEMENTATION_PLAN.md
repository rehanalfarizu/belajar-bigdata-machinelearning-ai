# Phase 1 Implementation Plan

Plan ini dibuat setelah audit dan sebelum perubahan lesson. Struktur `01_FOUNDATION` serta fase besar lain dipertahankan.

## IMPLEMENTATION_PLAN

### 1. Shared learning contract

- Buat `LEARNING_PROTOCOL.md` untuk predict/run/observe/explain, debugging loop, evidence, dan penggunaan AI.
- Ubah README Phase 1 menjadi peta empat minggu dan definition of done.

### 2. Computer Fundamentals

- Ganti ringkasan tunggal dengan 7 lesson berurutan.
- Tambah empat lab: process/memory, filesystem/environment, localhost HTTP/JSON, dan Git conflict.
- Tambah exercise ladder, problem-solving ladder, tujuh broken cases, mini-project `system-check`, dan checkpoint evidence.
- Ubah README menjadi chapter map lengkap.

### 3. Python Fundamental

- Buat 14 lesson dari execution/variable sampai small CLI.
- Pertahankan notebook dan referensi contoh yang sudah bernilai, tetapi tempatkan sebagai pendamping setelah lesson terkait.
- Tambah basic/intermediate/advanced exercises, problem ladder, broken cases, mini-project, dan checkpoint.
- Perbaiki semua nama/path lama di narasi Phase 1.

### 4. Python Professional

- Buat 14 lesson: module/package sampai concurrency mental model.
- Tambah micro-lab standard-library yang dapat dijalankan tanpa dependency baru.
- Tambah exercise ladder, problem ladder, broken cases, package mini-project, dan checkpoint berbasis test/log/config evidence.

### 5. Math & Statistics

- Buat 13 lesson kecil: tiga aljabar linear, tiga kalkulus/optimisasi, tiga probabilitas, dan empat statistik.
- Setiap lesson memakai manual calculation sebelum formula dan Python experiment.
- Tambah lab visual/numerik, reasoning ladder, debugging cases, mini-project uncertainty report, dan checkpoint.

### 6. Integrasi Phase 1

- Perjelas `ROADMAP_6_BULAN.md` menjadi 26 minggu; hanya Week 1–4 dijabarkan per hari pada iterasi ini.
- Pecah Month 1 Sensor Simulator menjadi 10 milestone tanpa full solution.
- Ubah programming problems menjadi difficulty ladder Level 1–5.
- Sesuaikan hanya link/reference di luar Phase 1 yang benar-benar terdampak.

### 7. Verification

- Jalankan audit struktur/link/sintaks/artifact.
- Parse dan jalankan seluruh script lab Phase 1.
- Jalankan notebook Python Foundation bila dependency tersedia.
- Jalankan `git diff --check`; pastikan tidak ada folder kosong/generated artifact.
- Lakukan navigation test delapan pertanyaan dari README → lesson → lab → problem → project → checkpoint → next.

## Urutan implementasi dan acceptance gate

| Tahap | Acceptance gate sebelum lanjut |
|---|---|
| Computer Fundamentals | 7 lesson dapat diikuti dan 4 lab runnable |
| Python Fundamental | 14 lesson terpetakan; exercise/debug/project/checkpoint jelas |
| Python Professional | 14 lesson + micro-lab dan tests runnable |
| Math & Statistics | seluruh konsep minimum tercakup dengan manual example dan experiment |
| Integrasi | Week 1–4, Month 1 milestones, dan Level 1–5 konsisten |
| Final QA | audit dan runtime checks lulus |

## Agent approval

Plan disetujui untuk implementasi karena langsung menutup gap audit, tidak mengubah struktur fase besar, tidak menambah teknologi baru, dan membatasi perubahan luar Phase 1 pada roadmap, Month 1 project, serta Foundation problem ladder yang diminta eksplisit.
