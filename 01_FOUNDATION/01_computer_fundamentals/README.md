# Mulai dari sini — Computer Fundamentals

## Saya sedang belajar apa?

Kamu akan membangun mental model tentang apa yang terjadi di bawah program: process, CPU, memory, file/path, shell/environment, network, HTTP/JSON/API, Git, dan debugging.

## Kenapa penting?

Kelak FastAPI server, Kafka consumer, Spark worker, ML training job, dan Digital Twin service semuanya berjalan sebagai process, membaca file/config, memakai network port, dan harus dapat di-debug. Tanpa fondasi ini, error lingkungan terasa acak.

## Prerequisite dan effort

Tidak perlu bisa Python. Kamu hanya perlu terminal dan editor. Estimasi 10–14 jam: tujuh lesson, enam lab, exercise, broken cases, mini-project, dan checkpoint.

## Urutan belajar

```text
START HERE
  ↓
01 Program, Process, CPU, Memory
  ↓
02 Filesystem, File, Path, Working Directory, Permission
  ↓
03 Terminal, Shell, Environment Variable
  ↓
04 Network, IP, Port, Localhost, DNS
  ↓
05 TCP, HTTP, Request/Response, JSON, API
  ↓
06 Git Mental Model
  ↓
07 Debugging Mental Model
  ↓
LABS → EXERCISES → BROKEN CASES → PROBLEM SOLVING
  ↓
MINI-PROJECT → CHECKPOINT → NEXT CHAPTER
```

## Lesson map

| # | Lesson | Pertanyaan pembuka | Praktik utama |
|---|---|---|---|
| 1 | [Program, Process, CPU, Memory](01_TEORI/01_program_process_cpu_memory.md) | Saat `python app.py` dijalankan, apa yang benar-benar berjalan? | inspect process dan memory |
| 2 | [Filesystem, Path, Working Directory, Permission](01_TEORI/02_filesystem_path_permission.md) | Mengapa file yang ada bisa “tidak ditemukan”? | relative vs absolute path |
| 3 | [Terminal, Shell, Environment](01_TEORI/03_terminal_shell_environment.md) | Siapa yang membaca command dan memberi environment? | variable scope dan child process |
| 4 | [Network, IP, Port, Localhost, DNS](01_TEORI/04_network_ip_port_dns.md) | Bagaimana satu process menemukan process lain? | port dan DNS inspection |
| 5 | [TCP, HTTP, JSON, API](01_TEORI/05_tcp_http_json_api.md) | Bagaimana bytes menjadi request yang bermakna? | local HTTP request dan JSON parse |
| 6 | [Git Mental Model](01_TEORI/06_git_mental_model.md) | Di mana perubahan berada sebelum menjadi commit? | branch dan merge conflict |
| 7 | [Debugging Mental Model](01_TEORI/07_debugging_mental_model.md) | Bagaimana berhenti menebak dan menemukan akar masalah? | hypothesis-driven diagnosis |

## Lab, exercise, dan problem solving

- [Lab 1 — Process, PID, CPU, dan memory](04_LABS/01_process.md)
- [Lab 2 — Filesystem, path, dan working directory](04_LABS/02_filesystem_path.md)
- [Lab 3 — Shell dan environment variable](04_LABS/03_environment_variable.md)
- [Lab 4 — Network, localhost, dan port](04_LABS/04_network_port.md)
- [Lab 5 — HTTP request/response dan JSON](04_LABS/05_http_json.md)
- [Lab 6 — Git snapshot, branch, dan conflict](04_LABS/06_git.md)
- [Exercises bertingkat](05_EXERCISES/exercises.md)
- [Problem-solving ladder](06_PROBLEM_SOLVING/problems.md)
- [Broken cases](07_DEBUGGING/broken_cases.md)

## Mini-project dan checkpoint

Buat [`system-check`](08_PROJECT/README.md), lalu kerjakan [checkpoint](09_CHECKPOINT/CHECKPOINT.md). Evidence wajib: output project, satu conflict yang diselesaikan, satu diagnosis error, dan penjelasan lisan/tertulis dengan kata sendiri.

Jangan membuka solution chapter lain untuk menjawab checkpoint. Bila gagal, kembali ke lesson dan eksperimen yang terkait.

## Navigasi

- Previous: [Start Here](../../START_HERE.md)
- Current: **01 Computer Fundamentals**
- Next: [02 Python Fundamental](../02_python_fundamental/README.md)
