# Lesson 7 — Debugging Mental Model

## Problem

Program “tidak jalan”. Kamu mengganti path, memasang ulang package, mengubah port, lalu error berubah tetapi akar masalah tidak diketahui. Banyak perubahan sekaligus menghapus evidence.

## Context dan why

Debugging adalah proses mencari penjelasan yang konsisten dengan observasi, bukan koleksi trik. Skill ini lebih tahan lama daripada hafalan tools.

## Intuisi dan mental model

Seperti dokter: gejala bukan diagnosis. Ukur vital signs, susun kemungkinan, lakukan test yang membedakan, baru berikan treatment dan verifikasi.

```text
SYMPTOM
  ↓ reproduce secara konsisten
OBSERVATIONS (error, input, cwd, env, time, version)
  ↓
HYPOTHESES A / B / C
  ↓ cheapest discriminating test
ROOT CAUSE
  ↓ minimal fix
VERIFY original + edge cases
  ↓
PREVENT test / validation / log / documentation
```

## Definition dan internal mechanism

**Symptom** adalah behavior terlihat. **Root cause** adalah kondisi yang jika diperbaiki menghilangkan failure pada causal chain. **Hypothesis** adalah penjelasan yang dapat diuji. **Minimal reproduction** menghapus variable yang tidak diperlukan agar signal jelas.

Traceback dibaca dari exception akhir lalu naik ke code path milik kita. Log adalah event evidence, bukan dump semua value. Debugger/print membantu mengamati state tetapi observasi dapat mengubah timing pada concurrency case.

## Small manual example

Symptom `FileNotFoundError` memiliki hypotheses: cwd salah, nama salah, file belum dibuat, permission path parent, atau environment memilih data root lain. Test `Path.cwd()` dan resolved path membedakan beberapa hypothesis sekaligus.

## Hands-on experiment

Pilih satu case di [broken cases](../07_DEBUGGING/broken_cases.md). Sebelum fix, isi tabel:

| Item | Catatan |
|---|---|
| Symptom | |
| Langkah reproduce | |
| Observasi | |
| 3 hypotheses | |
| Test pembeda termurah | |
| Root cause | |
| Fix | |
| Verification | |
| Prevention | |

### Predict before run

Untuk tiap test, tulis hasil yang diharapkan jika hypothesis benar dan jika salah.

### Observe dan explain

Jangan menerima “sekarang berhasil” sebagai penjelasan. Expected evidence adalah perubahan behavior yang dapat dihubungkan ke satu root cause dan tetap lulus pada rerun.

## Workplace application

Dipakai untuk incident, flaky test, performance regression, data-quality issue, model drift, dan integration failure. Timeline, version, correlation ID, metrics, logs, dan traces membantu boundary diagnosis.

## Common failures dalam debugging

- mengubah banyak variable sekaligus;
- hanya menguji happy path setelah fix;
- menghapus error dengan `except Exception: pass`;
- menganggap error terakhir selalu root cause;
- restart/reinstall tanpa mengumpulkan state;
- berhenti setelah symptom hilang tanpa prevention.

## Problem solving dan checkpoint

1. Buat hypothesis tree untuk “API timeout”.
2. Test apa yang membedakan wrong port dari server overload?
3. Mengapa retry dapat memperburuk outage?

Lulus bila satu debugging narrative memuat seluruh flow dan orang lain dapat mereproduksi diagnosisnya.

## Penutup

**KAMU BARU BELAJAR:** debugging adalah eksperimen terkontrol dari symptom menuju root cause dan prevention.

**KENAPA INI PENTING:** sistem nyata gagal pada boundary, timing, data, dan konfigurasi yang tidak terlihat dari source saja.

**DI DUNIA KERJA DIPAKAI UNTUK:** development, production incident, data/ML pipeline, dan service operation.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Python Fundamental memakai model ini untuk menelusuri variable, type, flow, function, file, import, dan exception.
