# Lesson 1 — Program, Process, CPU, dan Memory

## Problem

Ketika kamu menjalankan:

```bash
python app.py
```

apa sebenarnya yang berjalan? Apakah file `app.py` berjalan? Tidak. File hanya menyimpan instruksi. Operating system membuat sebuah **process** untuk interpreter Python; interpreter membaca dan mengeksekusi instruksi dari file.

## Context dan why

Perbedaan ini menjelaskan mengapa satu file dapat dijalankan dua kali sebagai dua process, mengapa menghentikan terminal dapat menghentikan program, dan mengapa program bisa kehabisan memory walau source code-nya kecil.

## Intuisi dan mental model

Bayangkan resep dan koki. Resep adalah program; koki yang sedang bekerja adalah process. Dua koki dapat memakai resep sama tetapi memiliki meja, bahan, dan progres berbeda.

```text
app.py (instruksi tersimpan)
        ↓ dibaca oleh
Python interpreter
        ↓ dijalankan sebagai
Operating-system process
├── process ID (PID)
├── virtual memory
├── file handles
├── environment
├── network sockets
└── CPU time yang dijadwalkan OS
```

## Definition

**Program** adalah instruksi/data yang tersimpan. **Process** adalah instance program yang sedang dieksekusi dengan identity, memory, dan resource. **CPU** mengeksekusi instruction dalam time slices. **Memory (RAM)** menyimpan code/data aktif; penyimpanan disk mempertahankan data setelah process berhenti.

Thread adalah alur eksekusi di dalam process. Beberapa thread berbagi memory process. Concurrency berarti beberapa pekerjaan mengalami progress dalam periode sama; parallelism berarti benar-benar dieksekusi bersamaan pada core berbeda. Detail ini akan diperdalam di Python Professional.

## How it works internally

Shell meminta OS membuat child process. OS memberi PID dan virtual address space, memuat interpreter/dependency, lalu scheduler memberi CPU time. Saat process meminta file/network, OS memeriksa permission dan mengembalikan handle. Ketika process exit, OS mengambil kembali resource—kecuali resource eksternal yang memang dipersistenkan.

## Small manual example

Jika kamu menjalankan `python app.py` pada dua terminal, terdapat dua PID dan dua variable state. Mengubah variable di process A tidak mengubah process B. Keduanya masih dapat menulis file yang sama; di situlah race/conflict bisa muncul.

## Hands-on experiment

Simpan sebagai `process_demo.py` di area scratch:

```python
import os
import time

data = [0] * 100_000
print("PID:", os.getpid())
print("items:", len(data))
time.sleep(20)
```

### Predict before run

Prediksi: apakah PID tetap sama jika file dijalankan dua kali? Apakah process masih terlihat selama `sleep`? Tulis jawaban sebelum menjalankan.

### Run dan observe

Jalankan di dua terminal, lalu gunakan `ps` atau activity monitor untuk mencari kedua PID. Expected result: dua PID berbeda; masing-masing memiliki state/memory sendiri dan berhenti setelah kira-kira 20 detik.

### Explain result

File source sama tidak berarti runtime state sama. List dibuat di memory masing-masing process. `sleep` tidak menghapus process; process menunggu timer dan hampir tidak memakai CPU.

## Workplace application

API server, background worker, notebook kernel, training job, dan Digital Twin service adalah process. Operator memantau PID/container, CPU, memory, open files, dan exit status untuk memahami kesehatan runtime.

## Common failures dan debugging

- CPU tinggi: loop/komputasi aktif, bukan otomatis “memory penuh”.
- Memory terus naik: object dipertahankan atau input terlalu besar.
- Process hilang: cek exit code, signal, log, dan resource limit.
- Dua process menulis resource sama: periksa concurrency dan ownership.

Debug dengan pertanyaan: process mana? PID berapa? command apa? sejak kapan? CPU/memory berapa? exit atau masih hidup?

## Problem solving dan checkpoint

1. Mengapa mengedit `app.py` tidak otomatis mengubah process yang sudah berjalan?
2. Apa yang dibagi dan tidak dibagi oleh dua process dari file sama?
3. Jelaskan beda “program lambat karena CPU” dan “program menunggu I/O”.

Kamu lulus lesson bila dapat menggambar file→interpreter→process→resource dan membuktikan dua eksekusi mempunyai PID berbeda.

## Penutup

**KAMU BARU BELAJAR:** program bukan process; process memakai CPU, memory, dan resource OS.

**KENAPA INI PENTING:** hampir semua sistem berikutnya berjalan sebagai satu atau lebih process.

**DI DUNIA KERJA DIPAKAI UNTUK:** diagnosis server, worker, notebook, training, dan service crash.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** process perlu membaca file; Lesson 2 menjelaskan bagaimana file ditemukan dan mengapa working directory sering menipu.
