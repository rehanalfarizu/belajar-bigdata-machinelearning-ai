# Lesson 3 — Terminal, Shell, dan Environment Variable

## Problem

Kamu mengetik `python --version`. Siapa yang membaca teks itu, mencari executable `python`, menentukan working directory, lalu menampilkan output? Bukan terminal sendirian—shell yang melakukannya.

## Context dan why

Confusion antara terminal, shell, dan program menyebabkan salah environment, salah interpreter, secret bocor, atau command bekerja di satu sesi tetapi gagal di sesi lain.

## Intuisi dan mental model

Terminal adalah layar/kanal percakapan. Shell adalah petugas yang membaca perintah, mencari program, menyusun arguments/environment, dan meminta OS membuat process.

```text
kamu mengetik command
        ↓
terminal mengirim teks
        ↓
shell parse command
├── built-in? (`cd`, `export`)
└── executable? cari lewat PATH
        ↓
OS membuat child process
├── arguments
├── working directory
└── salinan environment
```

## Definition dan internal mechanism

**Terminal** adalah interface input/output. **Shell** adalah command interpreter. **Environment variable** adalah pasangan key/value pada process. Child process biasanya mewarisi snapshot environment parent; perubahan child tidak kembali mengubah parent.

`PATH` adalah daftar directory tempat shell mencari executable. `cd` harus menjadi shell built-in karena working directory adalah state process shell; program child tidak bisa mengubah cwd parent setelah exit.

## Small manual example

Jika shell memiliki `APP_MODE=dev`, process Python child dapat membacanya. Jika Python mengubah `os.environ`, hanya Python dan child berikutnya yang melihat perubahan itu; shell parent tetap sama.

## Hands-on experiment

Pada macOS/Linux:

```bash
export COURSE_MODE=foundation
python -c 'import os; print(os.getenv("COURSE_MODE"))'
python -c 'import os; os.environ["COURSE_MODE"]="changed"; print(os.getenv("COURSE_MODE"))'
echo "$COURSE_MODE"
```

### Predict before run

Prediksi tiga output. Apakah command Python kedua mengubah hasil `echo`?

### Observe dan explain

Expected: `foundation`, lalu `changed`, lalu tetap `foundation`. Child menerima environment, tetapi tidak mengubah parent.

## Workplace application

Environment digunakan untuk runtime mode, endpoint, feature flag, dan lokasi credential reference. Secret tidak boleh ditulis ke source, log, screenshot, atau commit. Environment tetap harus divalidasi; string yang ada belum tentu benar.

## Common failures dan debugging

- executable berbeda: inspect path executable dan `PATH`.
- variable kosong: cek apakah diekspor pada shell/process yang benar.
- `.env` dianggap otomatis: file `.env` hanyalah file sampai tool/code memuatnya.
- value string disalahartikan boolean/angka: parse dan validate eksplisit.
- shell quoting salah: pahami ekspansi variable dan spaces.

Debug: identifikasi shell → inspect cwd → cari executable → inspect variable presence tanpa mencetak secret → jalankan minimal child process.

## Problem solving dan checkpoint

1. Mengapa `cd` tidak bisa diimplementasikan sebagai process biasa yang mengubah parent shell?
2. Mengapa package bisa terpasang tetapi `import` gagal jika `pip` dan `python` berasal dari environment berbeda?
3. Rancang startup validation untuk `APP_PORT` dan `APP_MODE`.

## Penutup

**KAMU BARU BELAJAR:** terminal menampilkan interaksi; shell membentuk process dengan cwd, arguments, dan environment.

**KENAPA INI PENTING:** environment menentukan program dan configuration yang benar-benar dipakai.

**DI DUNIA KERJA DIPAKAI UNTUK:** local development, CI, container, job scheduler, dan configuration.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** process sering perlu berbicara dengan process lain; Lesson 4 membangun model IP, port, localhost, dan DNS.
