# Mulai dari sini — Digital Twin Fundamentals

Hari pertama: baca [konsep dasar](01_TEORI/konsep_dasar.md), ikuti [tutorial](02_TUTORIAL/tutorial_langkah_demi_langkah.md), jalankan notebook, lalu jalankan test package `digital_twin_lab`.

Jangan membuka [solution](99_SOLUTIONS/solusi_dan_teori_lengkap.md) sebelum mencoba minimal 20–30 menit.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m digital_twin_lab.demo --steps 500 --fault-step 300
```

## Target dan gate

Bedakan digital model, shadow, dan twin; pisahkan plant truth, observation, estimated state, simulation, recommendation, dan command. Lulus bila core dapat dijelaskan, diuji, dan failure assumptions dinyatakan.

Mini-project: tank shadow. Bukti fase: [Month 4 Capstone](../../06_PROJECTS/month_04_connected_digital_twin/README.md).

## Navigasi

- Previous: [05 AI Systems & Cloud](../../03_AI_AND_DATA_SYSTEMS/05_ai_systems_cloud/README.md)
- Current: **01 Digital Twin Fundamentals**
- Next: [02 IoT, Telemetry & Connectivity](../02_iot_telemetry_connectivity/README.md)
