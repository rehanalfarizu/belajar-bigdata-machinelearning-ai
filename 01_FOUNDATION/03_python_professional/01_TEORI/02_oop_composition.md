# Lesson 2 — OOP dan Composition

## Problem, context, why

Dictionary sensor diteruskan ke banyak function dan setiap function mengasumsikan keys berbeda. Atau satu class raksasa menangani parsing, network, domain, dan output. OOP berguna bila state, behavior, dan invariant memang milik concept yang sama.

## Intuisi dan mental model

Object adalah actor kecil dengan state dan responsibility. Composition berarti object memakai object lain (“has-a”), bukan memaksa inheritance (“is-a”) untuk reuse.

## Definition dan internal mechanism

Class mendefinisikan construction dan attribute/method lookup; instance menyimpan state. Method call mengikat instance sebagai `self`. Encapsulation bukan menyembunyikan semua field, melainkan menjaga invariant melalui public operations. Composition memasukkan dependency melalui constructor/parameter.

## Small example

```python
class Sensor:
    def __init__(self, sensor_id):
        if not sensor_id:
            raise ValueError("sensor_id required")
        self.sensor_id = sensor_id

    def label(self):
        return f"sensor:{self.sensor_id}"
```

### Predict/run/observe/explain

Prediksi failure untuk empty ID dan hasil dua instances. Trace class object, instance state, serta bound method.

## Workplace application

Object cocok untuk stateful estimator, registry entity, adapter, dan policy. Function/dataclass lebih sederhana untuk stateless transform/value record.

## Common failure dan debugging

God object, inheritance dalam, hidden mutation, class sebagai namespace functions, dan dependency dibuat di dalam class sehingga sulit diuji. Tanyakan siapa owner invariant dan bisakah dependency diinjeksi.

## Mini exercise/checkpoint

Rancang `SensorService` yang *memiliki* repository interface, bukan mewarisinya. Jelaskan kenapa composition dipilih.

## Penutup

**KAMU BARU BELAJAR:** OOP menggabungkan state/behavior/invariant; composition menjaga hubungan eksplisit.

**KENAPA INI PENTING:** abstraction seharusnya mengikuti responsibility.

**DI DUNIA KERJA DIPAKAI UNTUK:** domain entities, adapters, policies, dan stateful components.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** banyak domain values tidak butuh class manual; dataclass memberi record semantics.
