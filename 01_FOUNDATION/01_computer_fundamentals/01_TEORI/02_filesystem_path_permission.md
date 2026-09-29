# Lesson 2 — Filesystem, File, Path, Working Directory, dan Permission

## Problem

Kamu melihat `config.json` di editor, tetapi program berkata `FileNotFoundError`. Apakah Python salah? Sering kali tidak. Program mencari relative path dari **working directory**, bukan otomatis dari folder source file.

## Context dan why

Data pipeline membaca CSV, model service membaca artifact, dan application membaca config. Path yang hanya bekerja dari satu terminal akan gagal di test runner, scheduler, container, atau komputer rekan.

## Intuisi dan mental model

Filesystem seperti alamat kota. Nama `config.json` adalah “rumah di sekitar sini”; `/project/config.json` adalah alamat lengkap. Working directory adalah posisi “kamu berdiri” saat menafsirkan alamat relatif.

```text
process
├── working directory: /project
├── relative path: data/input.csv
│   └── resolved: /project/data/input.csv
└── absolute path: /project/data/input.csv

open(path)
→ resolve path
→ traverse directories
→ check existence/type
→ check permission
→ return file handle atau error
```

## Definition dan internal mechanism

**File** adalah sequence bytes plus metadata. **Directory** memetakan nama ke entries. **Path** menunjuk lokasi; absolute path berakar dari filesystem root, relative path bergantung pada working directory. Permission mengatur siapa dapat read/write/execute; keberadaan file tidak menjamin process boleh mengaksesnya.

OS melakukan path resolution komponen demi komponen. `.` berarti current directory, `..` parent. Symbolic link dapat mengarah ke lokasi lain. Process menerima file descriptor/handle setelah `open`; file dapat berubah atau hilang setelah dibuka, sehingga I/O tetap dapat gagal.

## Small manual example

Jika working directory `/project`, path `data/a.txt` berarti `/project/data/a.txt`. Jika command dijalankan dari `/project/scripts`, path sama berarti `/project/scripts/data/a.txt`—lokasi berbeda.

## Hands-on experiment

```python
from pathlib import Path

print("cwd:", Path.cwd())
relative = Path("sample.txt")
print("resolved:", relative.resolve())
print("exists:", relative.exists())
```

### Predict before run

Jalankan file yang sama dari dua working directory. Prediksi nilai `cwd`, `resolved`, dan `exists`.

### Run, observe, explain

Expected result: `Path.cwd()` mengikuti lokasi terminal saat command dijalankan. `resolve()` berubah. Ini membuktikan path relatif adalah input yang membutuhkan context.

## Workplace application

Dipakai saat membaca configuration, dataset, checkpoint/model, certificate, template, dan output. Production code biasanya menerima path lewat argument/config dan memvalidasinya saat startup.

## Common failures dan debugging

- `FileNotFoundError`: cetak/inspect `cwd` dan resolved path.
- `PermissionError`: cek owner/mode dan identity process; jangan asal memakai hak admin.
- “Is a directory” atau “Not a directory”: cek type tiap komponen.
- output ada tetapi bukan di tempat yang diharapkan: cari resolved output path.
- perbedaan huruf besar/kecil: jangan mengandalkan behavior filesystem tertentu.

Debug flow: reproduce → catat cwd → resolve path → cek exists/type → cek permission → coba minimal read/write → perbaiki contract.

## Problem solving dan checkpoint

1. Mengapa path yang sukses di notebook dapat gagal di scheduler?
2. Kapan absolute path membantu, dan kapan membuat project tidak portable?
3. Rancang function yang menerima input/output path tanpa bergantung pada cwd tersembunyi.

Lulus bila dapat memprediksi resolved path dan menjelaskan error path tanpa mencoba lokasi secara acak.

## Penutup

**KAMU BARU BELAJAR:** file memiliki lokasi/metadata; relative path ditafsirkan dari working directory.

**KENAPA INI PENTING:** hampir semua pipeline membaca/menulis resource.

**DI DUNIA KERJA DIPAKAI UNTUK:** config, data, model artifact, log, certificate, dan deployment.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** command dan working directory datang dari shell; Lesson 3 menjelaskan terminal, shell, dan environment variable.
