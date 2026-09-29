# Lesson 11 — Testing

## Problem, context, why

Perubahan parser memperbaiki satu input tetapi merusak empty file. Manual demo hanya membuktikan sample yang dipilih; test menyimpan expectation dan mencegah regression.

## Intuisi dan mental model

Test adalah executable claim: dengan arrangement tertentu, action menghasilkan observable outcome. Ia bukan bukti tidak ada bug.

## Definition dan internal mechanism

Unit test memeriksa behavior kecil dengan dependency terkontrol; integration test memeriksa boundary nyata; end-to-end memeriksa workflow. Pola Arrange→Act→Assert menjaga intent. Test sebaiknya deterministic, isolated, meaningful, dan membaca public behavior.

## Small example

```python
import unittest

def normalize(value):
    if value < 0:
        raise ValueError("negative")
    return value / 100

class NormalizeTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(normalize(0), 0)

    def test_negative_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize(-1)
```

### Predict/run/observe/explain

Mutasi comparison menjadi `<=`. Prediksi test mana gagal dan gap apa masih ada. Tambah boundary 100.

## Workplace application

Tests mendukung refactor, CI, compatibility, incident regression, dan release confidence. Mock hanya external boundary yang tidak deterministik/mahal; over-mocking menguji implementation.

## Common failure dan debugging

Test hanya happy path, bergantung waktu/network/order, assert lemah, shared state, atau test code internals. Reproduce failure sendiri, periksa fixture, dan pertahankan test terkecil yang membuktikan behavior.

## Mini exercise/checkpoint

Tulis table-driven tests parser untuk valid, empty, malformed, wrong type, out-of-range, dan unknown unit.

## Penutup

**KAMU BARU BELAJAR:** test adalah claim behavior otomatis pada boundary tertentu.

**KENAPA INI PENTING:** perubahan aman membutuhkan regression evidence.

**DI DUNIA KERJA DIPAKAI UNTUK:** CI, refactor, releases, incident fixes, dan contracts.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** code+tests perlu didistribusikan secara reproducible; Lesson 12 membahas packaging.
