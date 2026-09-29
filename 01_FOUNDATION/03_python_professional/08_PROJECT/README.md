# Mini-Project — Installable Sensor Package

## Problem

Ubah Sensor Log CLI menjadi package kecil yang dapat diinstall, diuji, dikonfigurasi, dan didiagnosis.

## Milestones

1. Tentukan public behavior dan freeze baseline samples.
2. Susun `src/sensor_tool` dengan domain/io/cli dependency satu arah.
3. Buat dataclasses dan typed function contracts.
4. Gunakan generator untuk input lines dan context manager untuk resources.
5. Buat exception taxonomy kecil dan CLI exit-code mapping.
6. Tambah named logging tanpa secret.
7. Buat validated config dan precedence.
8. Tulis unit/integration tests.
9. Tambah `pyproject.toml`, build/install locally, dan test clean import.
10. Dokumentasikan architecture, run, test, failure, limitations, dan change evidence.

## Acceptance criteria

Domain dapat diimport tanpa I/O/CLI side effects; invalid data tidak menjadi zero; config invalid fail-fast; logs contextual; tests mencakup boundaries; install tidak bergantung pada cwd; package tidak melakukan network nyata.

## Stretch, bukan syarat

Simulasikan async processing hanya setelah sequential behavior benar. Batasi concurrency dan dokumentasikan cancellation/failure semantics.
