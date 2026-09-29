# Chapter 11 — IoT, Telemetry, dan Connectivity

Tujuan chapter ini bukan sekadar mengirim angka melalui broker. Tujuannya membangun **evidence pipeline**: observation dari dunia nyata tiba dengan identity, time, unit, quality, provenance, dan semantics yang cukup agar twin state dapat diperbarui secara benar.

## 1. Dari fenomena ke event

Rantai pengukuran:

```text
physical phenomenon → transducer/sensor → signal conditioning → sampling
→ device/PLC → edge/gateway → protocol/broker → validation → storage/state
```

- **Sensor** mengubah fenomena menjadi signal/reading. Ia memiliki range, resolution, accuracy, precision, bias, drift, response time, dan calibration history.
- **Actuator** mengubah command menjadi pengaruh fisik. Command acknowledgement belum membuktikan aksi berhasil; perlu observation balik.
- **PLC/controller** menjalankan logic deterministik dekat process. Twin bukan pengganti safety PLC.
- **Edge device** melakukan filtering, aggregation, buffering, local inference, atau protocol translation dekat aset.
- **Gateway** menjadi boundary jaringan/protokol/identity. Ia tidak boleh diam-diam mengubah unit atau timestamp.

Observation harus dibaca bersama metadata. `temperature=42` tanpa unit, lokasi sensor, timestamp, quality, dan calibration status bukan fakta yang cukup.

## 2. Kontrak telemetry

Schema minimum:

```json
{
  "event_id": "01J...",
  "asset_id": "motor-17",
  "metric": "bearing_temperature",
  "value": 78.2,
  "unit": "Cel",
  "event_time": "2026-09-26T08:15:31.125Z",
  "ingest_time": "2026-09-26T08:15:31.410Z",
  "sequence_number": 92841,
  "schema_version": 2,
  "quality": "good",
  "source": "sensor-B-17"
}
```

Bedakan:

- **event time**: kapan fenomena diukur;
- **ingest time**: kapan platform menerima event;
- **processing time**: kapan stage tertentu memprosesnya;
- **state effective time**: waktu yang diwakili snapshot state;
- **freshness**: `now - event_time`, bukan sekadar cepatnya query.

Sequence number membantu menemukan duplicate, gap, dan reordering, tetapi perlu scope yang jelas: per device, per metric, atau per boot session. Setelah device restart, counter bisa kembali nol; sertakan boot/session identity bila ini mungkin.

## 3. Late, out-of-order, duplicate, dan missing

Jaringan terdistribusi tidak menjamin arrival order sama dengan event order.

- **Duplicate**: event yang sama diproses lagi. Idempotency key mencegah state/aggregate dihitung dua kali.
- **Out-of-order**: event sequence lebih kecil datang setelah sequence baru. Jangan menimpa latest state secara buta.
- **Late event**: event time lebih lama dari watermark/kebijakan lateness. Ia mungkin tetap masuk historian tetapi tidak mengubah operational state.
- **Missing**: gap sequence atau expected sample tidak hadir. Missing bukan nol.
- **Stale**: event valid tetapi terlalu tua untuk keputusan sekarang.

Strategi harus berbeda untuk dua jalur:

```text
raw immutable log ── menerima apa yang benar-benar tiba untuk audit/replay
curated/state path ── menerapkan schema, unit, ordering, freshness, quality
quarantine/DLQ     ── menyimpan event gagal + alasan + retry policy
```

Dead-letter queue bukan tempat sampah abadi. Pantau volume/reason, batasi retry, sediakan replay setelah parser/schema diperbaiki, dan cegah poison message membuat loop.

## 4. MQTT, OPC UA, dan event streaming

### MQTT

MQTT adalah protocol publish/subscribe ringan. Topic memisahkan routing dari payload. QoS 0/1/2 mengatur pertukaran delivery antara client dan server pada scope protocol; QoS tidak otomatis memberi exactly-once business processing dari sensor sampai database. Retained message berguna untuk last known value tetapi harus dibedakan dari event history. Persistent session, Last Will, authentication, authorization topic, dan TLS perlu dirancang eksplisit.

Contoh topic yang stabil:

```text
site/{site_id}/asset/{asset_id}/telemetry/{metric}
```

Jangan menaruh data sensitif atau schema berubah-ubah di nama topic. Version-kan payload/schema dan batasi publish/subscribe per identity.

### OPC UA

OPC UA bukan hanya transport. Ia menyediakan information modeling—Objects, Variables, Methods, relationships—serta services dan security model. Companion specifications dapat memberi semantics domain. Gunakan OPC UA ketika interoperability industrial dan information model penting; jangan mengubah seluruh address space menjadi topic tanpa mempertahankan identity/semantics.

### Kafka/event streaming

Kafka-style log cocok untuk throughput, replay, partitioned ordering, dan banyak consumer. Ordering biasanya hanya dijamin dalam partition; pilih partition key dari kebutuhan ordering, misalnya `asset_id`. At-least-once delivery memerlukan idempotent consumer. “Exactly once” pada satu platform tidak menghapus side effect duplikat di database/API eksternal.

Pilihan bukan kompetisi satu pemenang. Pola umum: OPC UA di cell/plant, gateway menerjemahkan data terpilih, MQTT untuk device telemetry, dan log streaming untuk platform data.

## 5. Schema evolution, units, calibration, provenance

- Tambah field optional secara backward-compatible sebelum mewajibkannya.
- Jangan ubah makna field lama sambil mempertahankan nama/version.
- Gunakan canonical unit di curated layer, tetapi pertahankan raw value/unit.
- Calibration menghasilkan coefficient, valid interval, method, reference, dan uncertainty—bukan hanya boolean “calibrated”.
- Provenance mencatat device/firmware/gateway/parser/schema serta transformasi.
- Quality flag sebaiknya reasoned: `good`, `uncertain`, `bad` ditambah cause code.

Sensor disagreement tidak selalu berarti satu sensor rusak: posisi, response time, sampling phase, dan operating condition mungkin berbeda.

## 6. Implementasi lokal

[`TelemetryValidator`](../../01_digital_twin_fundamentals/src/digital_twin_lab/telemetry.py) menerapkan timezone, schema version, finite value, canonical unit, physical range, future/stale time. `EventLedger` memisahkan raw, accepted, dan quarantine serta mendeteksi duplicate/order. Ini demonstrasi in-memory; produksi perlu persistence, transaction/idempotency, partition policy, observability, dan retention.

Latihan:

1. Tambah rule motor temperature dan converter Kelvin→Celsius.
2. Simulasikan duplicate, sequence gap, reboot counter, delay acak, dan clock drift.
3. Definisikan watermark 10 detik: late event masuk historian tetapi tidak menimpa current state.
4. Tulis contract test untuk schema v1→v2 dengan field `calibration_id` optional.
5. Buat adapter conceptual `MQTT message → TelemetryEvent`; labeli test broker sebagai integration test.

## 7. Observability dan debugging

Pantau ingestion rate, valid/rejected rate per reason, duplicate rate, out-of-order rate, event-time lag percentiles, sequence gaps, DLQ age, schema versions, dan per-device silence. Debug dari satu `event_id` melintasi gateway, broker, validator, store, dan state update. Log tidak boleh membocorkan credentials atau data sensitif.

Anti-pattern:

- memakai server receive time sebagai event time;
- QoS tinggi dianggap menjamin data benar;
- membuang bad event tanpa raw audit;
- retry tanpa idempotency;
- satu global ordering untuk semua asset;
- auto unit conversion tanpa menyimpan sumber;
- controller menerima telemetry `uncertain` tanpa fallback.

## Gate

Lulus bila dapat menjelaskan QoS vs business semantics, membuat event contract versioned, menguji duplicate/out-of-order/stale/unit mismatch, serta menunjukkan bahwa invalid event tidak mengubah twin state.

## Referensi lanjutan

- [OASIS MQTT Version 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
- [OPC UA specifications](https://opcfoundation.org/developer-tools/specifications-unified-architecture)
- [OPC UA Part 1 — Overview and Concepts](https://reference.opcfoundation.org/Core/Part1/)
- [OPC UA Part 3 — Address Space Model](https://reference.opcfoundation.org/Core/Part3/)
- [OGC SensorThings API](https://www.ogc.org/standards/sensorthings/) untuk observation/tasking yang geospatial-enabled.

Berikutnya: [Time Series & State Estimation](../../03_time_series_state_estimation/README.md).
