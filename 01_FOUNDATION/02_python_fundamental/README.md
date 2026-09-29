# Mulai dari sini — Python Fundamental

## Saya sedang belajar apa?

Kamu akan belajar bagaimana Python mengeksekusi program dan merepresentasikan state: variable, value/type, operator, string, collections, condition, loop, function, scope, exception, file, module, dan CLI.

## Kenapa penting?

Python adalah alat utama untuk automation, data analysis, ML, API, dan Digital Twin di repository ini. Tujuan chapter bukan menghafal syntax, tetapi dapat menelusuri state dan menulis program kecil dari file kosong.

## Prerequisite dan effort

Lulus [Computer Fundamentals](../01_computer_fundamentals/README.md). Estimasi 18–24 jam: 14 lesson, sepuluh lab, dua notebook sintesis, exercises, broken cases, mini-project, dan checkpoint.

## Urutan belajar

```text
Lesson 01–04: execution, value/type, operator, string
        ↓
Lesson 05–08: collections, dictionary, condition, loop
        ↓
Lesson 09–11: function, scope, exception
        ↓
Lesson 12–14: file, module/import, small CLI
        ↓
LABS → EXERCISES → DEBUGGING → PROBLEM SOLVING
        ↓
MINI-PROJECT → CHECKPOINT → Python Professional
```

## Lesson map

| # | Lesson | Fokus |
|---|---|---|
| 1 | [Program execution & variable](01_TEORI/01_execution_variable.md) | statement, object, name, state tracing |
| 2 | [Type & value](01_TEORI/02_type_value.md) | `int`, `float`, `bool`, `None`, conversion |
| 3 | [Operator](01_TEORI/03_operator.md) | arithmetic, comparison, boolean, precedence |
| 4 | [String](01_TEORI/04_string.md) | Unicode text, indexing, slicing, formatting |
| 5 | [List, tuple, set](01_TEORI/05_list_tuple_set.md) | order, mutability, uniqueness |
| 6 | [Dictionary](01_TEORI/06_dictionary.md) | key→value lookup dan records |
| 7 | [Condition](01_TEORI/07_condition.md) | branching, truthiness, decision tables |
| 8 | [Loop](01_TEORI/08_loop.md) | iteration, state update, termination |
| 9 | [Function](01_TEORI/09_function.md) | parameter, return, contract |
| 10 | [Scope](01_TEORI/10_scope.md) | local/global name resolution dan mutability |
| 11 | [Error & exception](01_TEORI/11_error_exception.md) | traceback, expected failure, recovery boundary |
| 12 | [File I/O](01_TEORI/12_file_io.md) | context manager, text/JSON, validation |
| 13 | [Module & import](01_TEORI/13_module_import.md) | reuse, namespace, import path |
| 14 | [Small CLI](01_TEORI/14_small_cli.md) | arguments, input→domain→output, exit code |

## Tutorial, lab, dan reference

1. Setup melalui [quickstart](02_TUTORIAL/quickstart.md) dan [cara menjalankan Python](02_TUTORIAL/cara_menjalankan_python.md).
2. Gunakan [tutorial problem solving](02_TUTORIAL/tutorial_langkah_demi_langkah.md).
3. Kerjakan sepuluh lab berikut dengan siklus predict → run → observe → explain → modify:
   [state tracing](04_LABS/01_variable_state_tracing.md),
   [type conversion](04_LABS/02_type_conversion.md),
   [list/dict mutation](04_LABS/03_list_dict_mutation.md),
   [loop tracing](04_LABS/04_loop_tracing.md),
   [function flow](04_LABS/05_function_call_flow.md),
   [scope](04_LABS/06_scope.md),
   [exception](04_LABS/07_exception_handling.md),
   [file I/O](04_LABS/08_file_io.md),
   [module/import](04_LABS/09_module_import.md), dan
   [small CLI](04_LABS/10_small_cli.md).
4. Gunakan [notebook utama](04_LABS/praktikum.ipynb) dan [typing practice](04_LABS/typing_practice.ipynb) sebagai sintesis setelah lab terkait.
5. [Reference contoh](03_EXAMPLES/contoh.md) dipakai untuk lookup, bukan dibaca 1.198 baris sekaligus.

## Practice map

- [Exercises bertingkat](05_EXERCISES/exercises.md)
- [Problem-solving ladder](06_PROBLEM_SOLVING/problems.md)
- [Broken cases](07_DEBUGGING/broken_cases.md)
- [Mini-project — Sensor Log CLI](08_PROJECT/README.md)
- [Checkpoint](09_CHECKPOINT/CHECKPOINT.md)

Jangan membuka [solutions](99_SOLUTIONS/solusi_dan_teori_lengkap.md) sebelum mencoba minimal 20–30 menit. Setelah membaca solution, tutup file dan tulis ulang tanpa melihat.

## Dunia kerja

Skill chapter dipakai untuk script automation, parser data, validation, CLI internal, ETL sederhana, test setup, serta domain logic awal pada API/ML/Digital Twin.

## Navigasi

- Previous: [01 Computer Fundamentals](../01_computer_fundamentals/README.md)
- Current: **02 Python Fundamental**
- Next: [03 Python Professional](../03_python_professional/README.md)
