# Level 10 — Digital Twin

Digital twin adalah representasi digital dari aset, proses, atau sistem nyata yang terus diperbarui oleh data dan dipakai untuk memahami kondisi, memprediksi perilaku, menguji skenario, atau membantu keputusan. Dashboard sensor saja bukan digital twin; model statis tanpa sinkronisasi data juga bukan digital twin. Twin yang berguna menghubungkan **entitas fisik**, **data observasi**, **state model**, **simulasi/prediksi**, dan **aksi yang terkontrol**.

## 1. Konsep dasar

Contoh aset adalah tangki air, pompa, mesin, gedung, kendaraan, atau lini produksi. Sistem fisik memiliki state: tinggi air, suhu, tekanan, kecepatan, getaran, atau status komponen. Sensor hanya mengamati sebagian state dengan noise, delay, dropout, dan bias. Twin menyimpan estimasi state terbaik yang tersedia saat ini.

Secara ringkas:

```text
aset fisik → sensor/event → ingest & quality → state twin → model/simulasi
     ↑                                                        ↓
     └──────────── operator/controller ← rekomendasi/alarm ──┘
```

Jangan membalik arah ini: aksi ke aset fisik harus melalui kontrol yang aman, otorisasi, limit, dan manusia bila konsekuensinya tinggi.

## 2. Tingkat kematangan twin

1. **Digital model**: model 3D/fisika tanpa sinkronisasi otomatis.
2. **Digital shadow**: data fisik mengalir satu arah ke representasi digital.
3. **Digital twin**: data memperbarui twin dan twin dapat memberi rekomendasi atau aksi balik yang terkontrol.
4. **Fleet twin**: banyak aset dipantau bersama untuk optimisasi dan pembelajaran lintas aset.

Mulailah dari shadow dan validasi nilainya sebelum memberi twin hak mengontrol apa pun.

## 3. Jenis model

**Physics-based** memakai hukum domain, misalnya neraca massa tangki atau persamaan panas. Model ini lebih dapat dijelaskan dan dapat bekerja saat data sedikit, tetapi parameter harus dikalibrasi. **Data-driven** mempelajari pola dari histori menggunakan statistik/ML; ia kuat pada perilaku kompleks tetapi dapat gagal saat kondisi keluar dari data training. **Hybrid** menggabungkan keduanya: fisika memberi struktur, data mengoreksi residual atau memperbarui parameter.

Untuk tangki sederhana, state tinggi air `h` berubah melalui neraca massa:

```text
h(t+1) = max(0, h(t) + dt / area * (inflow(t) - outflow(t)))
outflow(t) = coefficient * sqrt(h(t))
```

Formula tersebut adalah model, bukan kebenaran absolut. Koefisien, batas sensor, kebocoran, dan delay harus divalidasi terhadap aset nyata.

## 4. Data dan state synchronization

Setiap event sensor wajib memiliki `asset_id`, `timestamp`, `metric`, `value`, `unit`, `quality_flag`, dan sebaiknya `sequence_number`. Bedakan event time dari ingest time. Simpan data mentah yang immutable; buat tabel curated untuk nilai tervalidasi; simpan state twin terbaru terpisah agar query cepat.

Quality check minimal: schema, unit, range fisik, timestamp future/stale, duplicate, missing, sensor calibration status, dan ordering. Nilai yang gagal tidak boleh diam-diam dipakai controller; tandai kualitas dan gunakan fallback yang eksplisit.

## 5. Arsitektur referensi

```text
Sensor/PLC/IoT → gateway → broker/event stream → validation → time-series store
                                                          ├→ twin state service
                                                          ├→ simulator / ML model
                                                          └→ alert, dashboard, historian
Control plane ← authorization + safety rule + audit log ← recommendation service
```

MQTT umum untuk telemetry IoT ringan; OPC UA umum di industri; Kafka/Event Hubs umum untuk stream skala besar. Pilih protokol dari latensi, reliability, lingkungan perangkat, dan integrasi—bukan popularitas.

## 6. Prediksi, anomaly detection, dan what-if

Residual adalah selisih observasi sensor dan prediksi twin. Residual besar dapat berarti sensor rusak, parameter model salah, kondisi operasi berubah, atau aset mengalami fault. Karena itu anomaly detector hanya memberi hipotesis, bukan diagnosis final. What-if menjalankan model dengan input/skenario alternatif tanpa mengubah aset fisik.

Evaluasi prediksi dengan MAE/RMSE serta error per mode operasi. Evaluasi alarm dengan precision, recall, false alarm rate, time-to-detect, dan dampak operator. Jangan memakai random split untuk data temporal.

## 7. Safety, security, dan governance

Digital twin OT/industrial menyentuh dunia fisik. Terapkan network segmentation, asset identity, mutual authentication, least privilege, encrypted telemetry, audit log, command allowlist, rate/limit guard, manual override, fail-safe mode, dan incident runbook. Simulasi tidak menggantikan prosedur keselamatan atau engineer domain.

## Urutan belajar chapter

1. Jalankan `10_digital_twin.ipynb` untuk melihat plant, sensor, twin, dan residual.
2. Baca `PANDUAN_KODE.md` untuk pattern implementasi.
3. Kerjakan `praktikum.md` tanpa melihat jawaban.
4. Buka `SOLUSI_DAN_TEORI_LENGKAP.md` untuk teori/solusi setelah mencoba.
5. Buat proyek twin pilihan: tangki, HVAC, motor, energi, atau produksi.
