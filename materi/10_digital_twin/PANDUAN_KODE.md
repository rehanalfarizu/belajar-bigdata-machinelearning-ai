# Panduan Kode — Level 10 Digital Twin

## 1. Kontrak event telemetry

Gunakan schema eksplisit sejak awal. Unit dan quality flag bukan aksesori; keduanya menentukan apakah data aman dipakai.

```python
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class TelemetryEvent:
    asset_id: str
    timestamp: datetime
    metric: str
    value: float
    unit: str
    quality: str = "good"

def validate_event(event: TelemetryEvent) -> TelemetryEvent:
    if event.timestamp.tzinfo is None:
        raise ValueError("timestamp harus memiliki timezone")
    if event.metric == "tank_level_m" and not 0 <= event.value <= 10:
        raise ValueError("level tangki di luar batas fisik")
    return event
```

Simpan raw event yang gagal ke dead-letter/quarantine dengan alasan penolakan. Jangan membuangnya tanpa jejak, karena mungkin menunjukkan sensor atau integrasi rusak.

## 2. Pisahkan plant, sensor, dan twin

Plant simulator menghasilkan state “sebenarnya”. Sensor memberi observasi berisik. Twin memperbarui state estimasi. Memisahkan ketiganya mencegah simulasi terlihat sempurna hanya karena twin membaca state internal plant langsung.

```python
def next_level(level: float, inflow: float, coefficient: float, area: float, dt: float) -> float:
    outflow = coefficient * level ** 0.5
    return max(0.0, level + dt / area * (inflow - outflow))

def update_twin(previous: float, predicted: float, measured: float | None, gain: float = 0.35) -> float:
    if measured is None:
        return predicted
    return predicted + gain * (measured - predicted)
```

`gain` besar membuat twin cepat mengikuti sensor tetapi lebih sensitif noise. Gain kecil lebih halus tetapi lambat menangkap perubahan nyata.

## 3. Residual bukan diagnosis

```python
residual = measured_level - predicted_level
is_anomaly = abs(residual) > residual_threshold
```

Residual besar bisa berupa sensor bias, unit salah, delay event, parameter fisika salah, kebocoran, atau perubahan operasi. Tambahkan context: mode operasi, kualitas sensor, periode maintenance, dan sensor lain sebelum mengirim alarm.

## 4. Anti-pattern penting

- Menggunakan `datetime.now()` tanpa timezone dan tanpa event time.
- Menggabungkan meter dengan centimeter atau Celsius dengan Fahrenheit tanpa konversi eksplisit.
- Menjalankan command fisik langsung dari output model.
- Menghitung threshold dari seluruh data termasuk periode fault tanpa label.
- Menghapus raw telemetry sehingga hasil twin tidak dapat diaudit.
- Memakai random split untuk forecast/anomaly temporal.
