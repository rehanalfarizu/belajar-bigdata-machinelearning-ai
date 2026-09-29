# Lesson 10 — Configuration

## Problem, context, why

Code memakai path, threshold, dan port hard-coded. Mengubah environment memerlukan edit source; typo config baru diketahui setelah job memproses data.

## Intuisi dan mental model

Configuration adalah input runtime yang memilih behavior dalam operating envelope yang didukung. Bukan tempat memindahkan semua keputusan design.

```text
defaults < config file < environment < CLI override
                    ↓
             parse + validate once
                    ↓
           immutable config object
```

## Definition dan internal mechanism

Tentukan sources dan precedence eksplisit. Environment/CLI adalah strings yang perlu parse type/range. Validate fail-fast saat startup. Secrets berbeda dari config biasa: referensikan secara aman dan jangan log value.

## Small example

```python
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Config:
    port: int

def load_config():
    port = int(os.getenv("APP_PORT", "8000"))
    if not 1 <= port <= 65535:
        raise ValueError("APP_PORT out of range")
    return Config(port=port)
```

### Predict/run/observe/explain

Uji missing, valid, text invalid, 0, dan 70000. Bedakan source absence, parse failure, dan range failure.

## Workplace application

Configuration memisahkan deploy environments, feature rollout, thresholds, dan endpoints. Version/owner/change audit diperlukan untuk critical config.

## Common failure dan debugging

Boolean string `"false"` dianggap truthy, precedence tidak jelas, validation tersebar, secret logged, reload partial, atau default unsafe. Cetak effective nonsecret config dan provenance bila aman.

## Mini exercise/checkpoint

Rancang config Sensor Package untuk input path, unit, log level, dan threshold dengan precedence serta validation.

## Penutup

**KAMU BARU BELAJAR:** config adalah runtime input berprecedence yang diparse/validasi menjadi object.

**KENAPA INI PENTING:** deploy berbeda tidak boleh memerlukan source edit.

**DI DUNIA KERJA DIPAKAI UNTUK:** environments, endpoints, thresholds, feature flags, dan operations.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** contract config/domain perlu dibuktikan otomatis melalui tests.
