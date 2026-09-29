# Lesson 11 — Error dan Exception

## Problem, context, why

Input invalid membuat program berhenti. Menangkap semua exception membuat program tampak “aman”, tetapi data salah diteruskan tanpa diketahui. Kita perlu membedakan bug, expected invalid input, dan recoverable boundary failure.

## Intuisi dan mental model

Exception seperti alarm yang membawa type, message, dan call path. Menutup alarm tanpa menangani bahaya bukan recovery.

```text
function gagal → raise exception
→ stack unwinds
→ handler spesifik ditemukan?
   yes: recovery/translate
   no: traceback + process exit/caller failure
```

## Definition dan internal mechanism

Syntax error terjadi sebelum execution normal. Runtime exception seperti `ValueError` atau `FileNotFoundError` muncul saat operation gagal. `try` membatasi code berisiko; `except` menangani type spesifik; `else` untuk success path; `finally` untuk cleanup; `raise` menyatakan invalid state/contract.

## Small manual example

```python
def parse_temperature(text):
    try:
        value = float(text)
    except ValueError as error:
        raise ValueError(f"invalid temperature: {text!r}") from error
    return value
```

### Predict → run → observe → explain

Uji `"27.5"` dan `"hot"`. Baca traceback dari baris terakhir dan causal chain. Jelaskan mengapa message menambah context tanpa menghapus cause.

## Hands-on experiment

Bandingkan dengan `except Exception: return 0`. Tunjukkan bagaimana fallback 0 mencampur invalid input dengan real zero.

## Workplace application

Exception diterjemahkan pada boundary: parser→domain error, domain→API response, infrastructure→retry/degraded mode. Log sekali pada owner boundary, bukan di setiap layer.

## Common failure dan debugging

Broad catch, empty handler, retry semua error, logging secret, atau memakai exception sebagai flow normal. Reproduce input, baca full traceback, dan tangani hanya failure yang benar-benar dapat dipulihkan/diterjemahkan.

## Mini exercise dan checkpoint

Tulis parser positive integer dengan error type/message jelas. Buat test untuk valid, zero, negative, decimal text, dan empty.

## Penutup

**KAMU BARU BELAJAR:** exception membawa failure melalui call stack dan harus ditangani pada boundary yang memahami recovery.

**KENAPA INI PENTING:** silent corruption lebih berbahaya daripada failure jelas.

**DI DUNIA KERJA DIPAKAI UNTUK:** input validation, API errors, file/network failure, dan operational diagnosis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** file I/O adalah boundary yang sering gagal dan membutuhkan cleanup; Lesson 12 mempraktikkannya.
