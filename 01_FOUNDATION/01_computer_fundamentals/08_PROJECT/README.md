# Mini-Project — System Check

## Problem

Tim sering menerima laporan “program tidak jalan” tanpa context. Buat CLI kecil yang mengumpulkan evidence lingkungan dengan aman.

## Requirements

Program menerima optional config path dan target `host:port`, lalu melaporkan:

- Python version/executable dan PID;
- working directory;
- raw dan resolved config path, existence, serta file type;
- keberadaan required environment keys tanpa menampilkan value secret;
- hasil parse JSON dan field wajib;
- hasil connection attempt dengan timeout singkat bila target diberikan;
- exit code nonzero bila check penting gagal.

## Constraints

Gunakan standard library. Pisahkan collection, validation, formatting, dan CLI. Jangan mengubah system state, scan network, mencetak secret, atau memberi full traceback untuk user biasa tanpa debug mode.

## Milestones

1. Cetak interpreter, PID, dan cwd.
2. Resolve dan validasi path.
3. Parse JSON dengan error yang actionable.
4. Periksa environment presence.
5. Tambah optional host/port check.
6. Kembalikan exit code bermakna.
7. Tambah tests untuk success dan tiga failures.
8. Dokumentasikan sample run, limitations, dan safe usage.

## Acceptance criteria

Output cukup untuk membedakan wrong cwd, missing file, invalid JSON, missing environment, dan unavailable port. Test tidak bergantung pada internet. Error tidak membocorkan secrets.
