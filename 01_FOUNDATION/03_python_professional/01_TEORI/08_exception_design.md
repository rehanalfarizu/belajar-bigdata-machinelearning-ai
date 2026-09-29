# Lesson 8 — Exception Design

## Problem, context, why

Library melempar `ValueError` untuk config, data corruption, dan network response. Caller tidak tahu mana yang dapat diperbaiki, di-retry, atau harus menghentikan job.

## Intuisi dan mental model

Exception taxonomy adalah bahasa failure antar-boundary. Terlalu umum tidak memberi keputusan; terlalu banyak subclasses membuat API rapuh.

## Definition dan internal mechanism

Gunakan built-in bila semantics tepat. Buat domain base exception kecil bila caller perlu membedakan category. Translate infrastructure exception pada boundary sambil mempertahankan cause melalui `raise ... from ...`. Message membawa safe context; exception type membawa handling contract.

## Small example

```python
class SensorError(Exception):
    pass

class InvalidReading(SensorError):
    pass

def validate(value):
    if value < -50:
        raise InvalidReading(f"value out of range: {value}")
```

### Predict/run/observe/explain

Tangkap `SensorError` lalu type spesifik. Prediksi hierarchy matching dan causal chain ketika wrapping parser error.

## Workplace application

API maps domain failure ke 4xx/5xx, job runner menentukan retry/nonretry, dan logs menyertakan correlation context. Retry policy tidak ditentukan hanya oleh class name; operation/idempotency juga penting.

## Common failure dan debugging

Broad catch, exception untuk expected branch biasa, sensitive payload di message, kehilangan cause, dan inconsistent taxonomy. Review caller decisions yang perlu didukung.

## Mini exercise/checkpoint

Rancang tiga failure categories untuk Sensor Package dan mapping CLI exit codes. Hindari satu class per message.

## Penutup

**KAMU BARU BELAJAR:** exception type/message/cause membentuk failure contract.

**KENAPA INI PENTING:** caller harus tahu fail, translate, quarantine, atau retry.

**DI DUNIA KERJA DIPAKAI UNTUK:** API, jobs, libraries, retries, dan incident diagnosis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** failure dan operation perlu event evidence; Lesson 9 membahas logging.
