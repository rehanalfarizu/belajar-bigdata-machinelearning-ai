# Praktikum — Level 10 Digital Twin

## Latihan 1 — Kontrak telemetry

Buat dataclass event untuk suhu motor, tambahkan `asset_id`, timestamp UTC, unit Celsius, quality flag, dan validasi range -40 sampai 180. Uji event valid, timestamp tanpa timezone, dan suhu 500.

## Latihan 2 — Tank shadow

Buat plant tangki dengan inflow sinusoidal, outflow akar tinggi air, sensor noise, dan kemungkinan dropout 5%. Simpan state fisik, observasi, serta timestamp dalam DataFrame. Buat grafik level fisik versus sensor.

## Latihan 3 — State estimator

Implementasikan twin yang memprediksi level dari input pompa lalu mengoreksi prediksi dengan sensor jika kualitas `good`. Bandingkan MAE model tanpa koreksi, gain 0.1, 0.35, dan 0.8. Jelaskan trade-off noise versus respons.

## Latihan 4 — Fault dan anomaly

Pada langkah 300, tambahkan bias sensor +0.8 meter atau ubah coefficient outflow untuk mensimulasikan clog. Hitung residual, rolling mean/std dari periode normal, lalu buat alarm. Ukur berapa langkah setelah fault alarm pertama muncul dan berapa false alarm sebelum fault.

## Latihan 5 — What-if dan controller aman

Simulasikan tiga skenario inflow: normal, tinggi, dan pompa mati. Buat rekomendasi “naikkan inflow”, “turunkan inflow”, atau “minta inspeksi” dengan batas hard minimum/maksimum level. Rekomendasi tidak boleh langsung mengubah state plant.

## Tantangan proyek

Pilih satu aset nyata: motor, panel surya, HVAC, conveyor, gudang dingin, atau armada kendaraan. Buat asset model, schema telemetry, quality rules, state twin, satu what-if, satu alarm, dashboard/plot, dan dokumen safety. Jelaskan data mana simulasi dan data mana observasi nyata.
