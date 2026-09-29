# Mulai dari sini — Python Professional

## Saya sedang belajar apa?

Kamu akan mengubah script menjadi software kecil yang modular, reusable, typed, testable, configurable, observable, dan dapat dipaketkan. Async/concurrency dipelajari sebagai mental model, bukan sebagai trik membuat semuanya cepat.

## Kenapa penting?

Code data/ML/AI hidup lebih lama dari notebook pertama. Tim perlu menguji perubahan, membaca log, mengelola config, memakai ulang package, dan memahami behavior saat banyak pekerjaan berjalan.

## Prerequisite dan effort

Lulus [Python Fundamental](../02_python_fundamental/README.md). Estimasi 22–30 jam untuk 14 lesson, guided refactor, 13 lab, exercises, broken cases, mini-project, dan checkpoint.

## Lesson map

| # | Lesson | Output mental model |
|---|---|---|
| 1 | [Module & Package](01_TEORI/01_module_package.md) | namespace, package boundary, public API |
| 2 | [OOP & Composition](01_TEORI/02_oop_composition.md) | object responsibility dan has-a relationship |
| 3 | [Dataclass & Data Model](01_TEORI/03_dataclass_data_model.md) | typed record, invariant, identity/value |
| 4 | [Type Hints](01_TEORI/04_type_hints.md) | static contract vs runtime validation |
| 5 | [Iterator & Generator](01_TEORI/05_iterator_generator.md) | lazy stream dan stateful iteration |
| 6 | [Decorator](01_TEORI/06_decorator.md) | function wrapping dan metadata |
| 7 | [Context Manager](01_TEORI/07_context_manager.md) | acquire/use/release |
| 8 | [Exception Design](01_TEORI/08_exception_design.md) | taxonomy, translation, causal chain |
| 9 | [Logging](01_TEORI/09_logging.md) | event, level, context, redaction |
| 10 | [Configuration](01_TEORI/10_configuration.md) | validated runtime input dan precedence |
| 11 | [Testing](01_TEORI/11_testing.md) | behavior, boundaries, regression |
| 12 | [Packaging / pyproject](01_TEORI/12_packaging_pyproject.md) | build/install metadata dan dependency |
| 13 | [Async / await](01_TEORI/13_async_await.md) | cooperative I/O concurrency |
| 14 | [Concurrency Mental Model](01_TEORI/14_concurrency_mental_model.md) | task/thread/process, race, cancellation |

## Urutan praktik

```text
Lesson 1–4 → guided refactor
Lesson 5–10 → micro-lab patterns
Lesson 11–12 → test + package
Lesson 13–14 → concurrency experiments
→ exercises → debugging → problems
→ mini-project → checkpoint → Math & Statistics
```

- [Guided refactor](02_TUTORIAL/guided_refactor.md)
- Praktikum: [module/package](04_LABS/01_module_package.md),
  [dataclass](04_LABS/02_dataclass.md),
  [typing + static check](04_LABS/03_typing_static_check.md),
  [generator streaming](04_LABS/04_generator_streaming.md),
  [context manager](04_LABS/05_context_manager.md),
  [decorator](04_LABS/06_decorator.md),
  [exception design](04_LABS/07_exception_design.md),
  [logging](04_LABS/08_logging.md),
  [configuration](04_LABS/09_configuration.md),
  [unit test](04_LABS/10_unit_test.md),
  [integration test](04_LABS/11_integration_test.md),
  [async I/O](04_LABS/12_async_io.md), dan
  [packaging](04_LABS/13_packaging.md).
- [Micro-lab executable dan cara menjalankannya](04_LABS/README.md)
- [Exercises](05_EXERCISES/exercises.md)
- [Problem-solving ladder](06_PROBLEM_SOLVING/problems.md)
- [Broken cases](07_DEBUGGING/broken_cases.md)
- [Mini-project — Sensor Package](08_PROJECT/README.md)
- [Checkpoint](09_CHECKPOINT/CHECKPOINT.md)

## Dunia kerja

Module/package memungkinkan reuse; composition menjaga boundaries; typing/review menangkap mismatch lebih awal; logging/config/test membantu operasi; packaging memastikan delivery; concurrency menentukan correctness dan capacity.

## Navigasi

- Previous: [02 Python Fundamental](../02_python_fundamental/README.md)
- Current: **03 Python Professional**
- Next: [04 Math & Statistics](../04_math_statistics/README.md)
