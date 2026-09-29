# Lesson 3 — Dataclass dan Data Model

## Problem, context, why

Event dictionary mudah salah key/type dan sulit dibandingkan di test. Menulis `__init__`/`__repr__`/`__eq__` berulang juga menambah noise.

## Intuisi dan mental model

Dataclass seperti formulir bernama dengan fields eksplisit. Ia membantu value object, tetapi validation dan semantics tetap tanggung jawab desain.

## Definition dan internal mechanism

`@dataclass` menghasilkan methods berdasarkan annotations/fields. `frozen=True` mencegah assignment attribute biasa, bukan membuat nested object otomatis immutable. `__post_init__` dapat menjaga invariant. Bedakan value object (equality dari fields) dari entity (identity/lifecycle).

## Small example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float
    unit: str

    def __post_init__(self):
        if not self.sensor_id:
            raise ValueError("sensor_id required")
```

### Predict/run/observe/explain

Prediksi equality dua readings sama dan behavior assignment. Uji nested mutable field untuk memahami batas frozen.

## Workplace application

Dipakai untuk commands/events/config/result yang kecil dan typed. Jangan langsung serialize internal dataclass sebagai stable external API tanpa version contract.

## Common failure dan debugging

Mutable default, validation terlambat, entity dianggap value, serta field internal bocor ke API. Gunakan `field(default_factory=...)` dan tests invariant.

## Mini exercise/checkpoint

Buat dataclass `Summary` dengan count/min/max/mean dan invariant count nonnegative/no-data explicit.

## Penutup

**KAMU BARU BELAJAR:** dataclass mengurangi boilerplate record tetapi tidak menggantikan domain design.

**KENAPA INI PENTING:** explicit fields memudahkan review/test.

**DI DUNIA KERJA DIPAKAI UNTUK:** domain values, config, events, dan results.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** annotations dataclass membawa kita ke type hints dan batas static contract.
