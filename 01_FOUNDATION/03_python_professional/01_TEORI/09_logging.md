# Lesson 9 — Logging

## Problem, context, why

Production failure tidak dapat direproduksi saat itu juga. `print("error")` tanpa time/context tidak menjawab asset, operation, version, atau cause.

## Intuisi dan mental model

Log adalah event record untuk diagnosis, bukan transcript semua variable. Setiap event harus membantu pertanyaan operasional.

## Definition dan internal mechanism

Python logging membuat `LogRecord` dengan level, logger name, message, time, exception, dan optional context; handlers memformat/mengirim. Library sebaiknya memakai logger bernama dan tidak mengonfigurasi global output secara paksa. Level: DEBUG detail diagnosis, INFO lifecycle, WARNING degraded/unusual, ERROR operation failed.

## Small example

```python
import logging

logger = logging.getLogger(__name__)

def process(sensor_id):
    logger.info("processing sensor_id=%s", sensor_id)
```

### Predict/run/observe/explain

Tanpa basic configuration, prediksi level yang tampil. Tambah configuration di entrypoint dan ubah level. Gunakan lazy formatting arguments.

## Workplace application

Logs dikaitkan dengan metrics/traces/correlation ID. Redact secrets/PII dan hindari payload besar. Log failure pada boundary owner agar tidak terduplikasi tiap layer.

## Common failure dan debugging

Semua INFO/ERROR, duplicate handlers, log tanpa context, exception hilang, secret tercetak, atau logging di hot loop. Inspect logger/handler/level propagation.

## Mini exercise/checkpoint

Definisikan lima events Sensor CLI beserta level, fields, dan redaction. Lulus bila log membedakan startup, rejected event, file failure, summary, dan shutdown.

## Penutup

**KAMU BARU BELAJAR:** logging merekam event berlevel dan bercontext melalui logger/handler.

**KENAPA INI PENTING:** runtime jauh dari debugger membutuhkan evidence.

**DI DUNIA KERJA DIPAKAI UNTUK:** operations, incident, audit, dan performance diagnosis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** log level dan endpoint berasal dari configuration yang harus tervalidasi.
