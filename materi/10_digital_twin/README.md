# Chapter 10 — Digital Twin Fundamental

Chapter ini menjawab pertanyaan paling dasar sebelum memilih cloud, dashboard, 3D engine, atau model AI: **representasi apa yang dibuat, realitas mana yang direpresentasikan, bagaimana keduanya disinkronkan, untuk keputusan apa, dan seberapa besar kita dapat mempercayainya?**

## Tujuan dan gate

Setelah selesai, kamu harus mampu:

- menjelaskan sejarah dan alasan Digital Twin muncul tanpa mengubah sejarah menjadi mitos tunggal;
- membedakan physical entity, virtual entity, observation, state, model, synchronization, prediction, dan action;
- menjelaskan mengapa 3D, dashboard, IoT, dan simulation masing-masing tidak otomatis menjadi twin;
- mengklasifikasikan model, shadow, connected/predictive/prescriptive/adaptive twin dengan menyebut taxonomy yang dipakai;
- menjalankan reference implementation tangki dan menjelaskan setiap boundary;
- menolak klaim “real-time” tanpa angka frequency, latency, freshness, dan fidelity.

Gate lulus: jalankan 10 test, ubah noise/dropout/fault pada simulator, lalu jelaskan mengapa MAE rendah belum membuktikan twin aman.

## 1. Sejarah: masalahnya lebih tua dari istilahnya

Engineer sudah lama memakai model, simulator, telemetry, dan replika untuk memahami sistem yang mahal atau berbahaya disentuh langsung. Program antariksa menunjukkan nilai kombinasi model dan data operasi; product lifecycle management kemudian menekankan hubungan antara produk fisik dan informasi digital sepanjang lifecycle. Literatur awal 2000-an membentuk konsep, sementara istilah “digital twin” populer pada dekade berikutnya. Sejarah ini bukan garis lurus dari satu produk menuju satu definisi universal.

Mengapa konsep berkembang:

1. sensor dan konektivitas membuat kondisi aset dapat diamati lebih sering;
2. storage dan compute membuat histori, simulation, dan inference lebih murah;
3. sistem makin kompleks sehingga dashboard variabel tunggal tidak cukup;
4. keputusan maintenance/design perlu diuji tanpa merusak aset;
5. lifecycle data terpecah antara engineering, operation, maintenance, dan business system.

Digital Twin menyatukan kemampuan-kemampuan itu di sekitar **identitas real-world entity/process dan use case**. Ia bukan nama baru untuk setiap model komputer.

## 2. Mental model: map bukan territory

Setiap model menyederhanakan realitas. Twin yang baik bukan replika sempurna; ia cukup faithful untuk keputusan tertentu dan menyatakan batasnya.

```text
real-world entity/process
        │ menghasilkan fenomena
        ▼
sensor / records ── observation + metadata ──► quality gate
                                                     │
input/command ─► process model ─► prediction         ▼
                       ▲                       estimated state
                       └──── calibration ◄───────────┤
                                                    ▼
                                      analysis / what-if / decision
                                                    │
                              recommendation → approval → command
```

- **Physical entity/process**: subjek di dunia nyata; tidak harus satu mesin. Bisa gedung, armada, jaringan energi, workflow, atau ekosistem.
- **Virtual entity**: representasi digital beridentitas, schema, state, model, histori, dan relationships yang relevan.
- **Observation**: pembacaan/record tentang state; selalu punya uncertainty dan provenance.
- **State**: variabel minimum yang dibutuhkan untuk memprediksi evolusi sistem. State dapat teramati langsung, tersembunyi, atau hanya dapat diestimasi.
- **Model**: aturan yang memetakan state/input menuju prediction. Model bisa physics-based, data-driven, logical, geometric, semantic, atau gabungan.
- **Synchronization**: mekanisme memperkecil divergence physical–digital pada frequency dan fidelity yang dinyatakan.
- **Lifecycle**: design, commissioning, operation, maintenance, upgrade, sampai decommissioning; model dan identity berubah di sepanjangnya.

## 3. Definisi kerja dan batas taxonomy

ISO/IEC 30173 membahas konsep, terminology, lifecycle, stakeholders, types, dan functional view secara general-purpose. Digital Twin Consortium mendefinisikan twin sebagai virtual representation berbasis data yang terintegrasi dengan real-world entities/processes dan memiliki synchronized interaction pada frequency serta fidelity tertentu. Keduanya menekankan konteks dan sinkronisasi; tidak berarti setiap use case harus memberi autonomous command ke actuator.

Gunakan definisi kerja repository ini:

> Digital Twin adalah representasi virtual beridentitas dari entity atau process dunia nyata, yang disinkronkan melalui observations/records pada frequency dan fidelity yang ditetapkan, memakai model untuk memahami atau memprediksi state, dan menghasilkan keluaran yang dapat divalidasi terhadap use case.

Istilah berikut adalah **taxonomy pedagogis**, bukan urutan normatif tunggal yang disepakati semua standar:

| Bentuk | Sinkronisasi | Model/analitik | Keluaran |
|---|---|---|---|
| Digital model | manual atau tidak ada | geometri/fisika/logika | dokumentasi/simulasi offline |
| Digital shadow | physical → digital otomatis | monitoring/analytics | visibility; tidak mengirim keputusan balik |
| Connected twin | physical ↔ digital terintegrasi | state + behavior | insight/recommendation/command sesuai use case |
| Predictive twin | data masuk | forecast/failure probability/RUL | prediksi + uncertainty |
| Prescriptive twin | prediction + constraints | optimization/what-if | rekomendasi yang dapat dijelaskan |
| Adaptive/intelligent twin | feedback hasil + governance | online adaptation/AI | berubah terkendali, versioned, rollback-able |

Sumbu scale berbeda dari capability:

- **component/asset twin** merepresentasikan satu komponen/aset;
- **system twin** merepresentasikan interaksi banyak komponen;
- **fleet twin** membandingkan banyak instance sejenis;
- **system-of-systems twin** menggabungkan sistem dengan owner/tujuan berbeda;
- **federated twin** membuat beberapa twin berinteroperasi tanpa harus menjadi satu database/owner.

Sebuah fleet twin bisa hanya descriptive; sebuah asset twin bisa predictive. Jangan mencampur sumbu scale dengan kecerdasan.

## 4. Empat miskonsepsi penting

### 3D model bukan otomatis Digital Twin

3D menjawab bentuk dan lokasi. Ia menjadi salah satu view twin bila terhubung ke identity, state, time, dan use case. Banyak twin—misalnya battery health estimator—tidak memerlukan 3D.

### Dashboard bukan otomatis Digital Twin

Dashboard adalah user interface. Grafik temperature tanpa entity model, state semantics, synchronization contract, dan validation tetap dashboard telemetry.

### IoT dashboard bukan otomatis Digital Twin

IoT menyalurkan data; twin memberi konteks dan model. Sebaliknya, IoT network tidak selalu wajib: inspeksi manual harian dapat menyinkronkan twin bangunan bila frequency itu memadai untuk use case. Yang wajib adalah synchronization contract yang jujur.

### Simulation saja bukan otomatis Digital Twin

Simulation memprediksi behavior dari initial condition dan parameter. Tanpa kaitan terpelihara ke instance dunia nyata, ia adalah simulator/digital model. Setelah telemetry mengkalibrasi state/parameter dan hasil divalidasi terhadap instance, simulation dapat menjadi capability twin.

## 5. Maturity model berbasis bukti

| Maturity | Pertanyaan | Bukti minimum | Failure mode khas |
|---|---|---|---|
| M0 model | “Seperti apa/berperilaku bagaimana?” | model tervalidasi offline | model diperlakukan sebagai realitas |
| M1 observed/shadow | “Apa yang terjadi?” | identity + timestamp + telemetry quality | reading disamakan dengan state |
| M2 synchronized | “Apa state terbaik sekarang?” | estimator + freshness + uncertainty | late event merusak state |
| M3 diagnostic | “Mengapa menyimpang?” | residual + hypotheses + context | anomaly disebut diagnosis |
| M4 predictive | “Apa yang mungkin terjadi?” | temporal validation + interval/calibration | point forecast tanpa uncertainty |
| M5 prescriptive | “Apa pilihan terbaik?” | objective + constraints + what-if | objective salah/constraint hilang |
| M6 adaptive | “Bagaimana sistem belajar aman?” | monitored update + approval + rollback | silent model update |
| M7 federated | “Bagaimana banyak twin bekerja bersama?” | identity/semantics/access contracts | global ID collision dan semantic drift |

Naik maturity hanya bila outcome dapat diuji. Menambah neural network atau 3D tidak otomatis menaikkan maturity.

## 6. Frequency, fidelity, dan fitness for purpose

- **Synchronization frequency**: seberapa sering update dibutuhkan. Millisecond untuk protection loop berbeda dari satu jam untuk energy planning.
- **Temporal fidelity**: kemampuan menangkap dynamics yang relevan, bukan hanya banyak sample.
- **Model fidelity**: detail behavior pada operating envelope tertentu.
- **Spatial fidelity**: ketelitian bentuk/lokasi bila keputusan memang spasial.
- **Semantic fidelity**: ketepatan identity, unit, relationship, dan meaning.
- **Decision fitness**: apakah error/latency masih dapat diterima untuk keputusan dan konsekuensinya.

Tulis service-level objective, misalnya: 99% telemetry level diterima dalam 3 detik; state age < 10 detik; 95% interval prediction memiliki empirical coverage 90–98%; command di luar envelope selalu ditolak.

## 7. Reference implementation

Kode di [`src/digital_twin_lab`](src/digital_twin_lab) sengaja kecil dan terpisah menjadi:

- `telemetry.py`: schema, timezone, unit conversion, freshness, duplicate, sequence, raw/quarantine;
- `estimation.py`: Kalman Filter skalar dan multi-sensor fusion berdasarkan variance;
- `simulation.py`: plant tangki, noisy/missing sensor, model mismatch, uncertainty;
- `anomaly.py`: residual detector streaming tanpa future leakage;
- `safety.py`: safety envelope, freshness/uncertainty guard, operator approval, audit;
- `demo.py`: experiment runner dan metric summary.

Jalankan tanpa dependency eksternal:

```bash
cd materi/10_digital_twin
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m digital_twin_lab.demo --steps 500 --fault-step 300
```

Eksperimen:

1. naikkan `sensor_std_m`; amati variance dan MAE;
2. naikkan dropout; pastikan uncertainty membesar saat correction hilang;
3. kecilkan perubahan coefficient saat fault; ukur detection delay;
4. ubah threshold; gambarkan trade-off false alarm vs missed/delayed detection;
5. coba melewati `CommandGuard`; hard constraint harus tetap menolak meski operator menyetujui.

## 8. Kesalahan umum dan debugging

- **Twin membaca ground truth simulator**: hasil sempurna adalah leakage. Sensor adapter hanya boleh memberi observation.
- **Residual dihitung setelah correction**: residual mengecil karena measurement sudah diserap. Gunakan prediction sebelum update.
- **Timestamp naive**: ordering lintas zona menjadi ambigu. Gunakan UTC aware datetime dan simpan timezone sumber bila diperlukan.
- **Mencampur Celsius/Fahrenheit atau cm/m**: normalisasi sebelum range rule, simpan original di raw log.
- **Random split pada time series**: masa depan bocor ke training. Gunakan rolling/expanding evaluation.
- **Alarm dianggap fault diagnosis**: residual besar hanya membuktikan mismatch, bukan akar penyebab.
- **Output AI langsung ke actuator**: pisahkan recommendation, decision, command, dan actuation.

## 9. Checkpoint

1. Apakah twin tanpa IoT dapat sah? Jelaskan use case dan synchronization contract-nya.
2. Kapan satu CAD model berubah dari digital model menjadi bagian twin?
3. Apa beda state level tangki dengan reading sensor level?
4. Jika data tiba terlambat 30 detik, apakah latest-arrival sama dengan latest-event-time?
5. Mengapa state uncertainty harus naik ketika sensor hilang?
6. Apa bukti bahwa predictive twin lebih baik daripada threshold sederhana?
7. Siapa yang berhak mengubah model, menerima rekomendasi, dan mengeksekusi command?

## Referensi lanjutan

- [ISO/IEC 30173 — Digital twin: concepts and terminology](https://www.iso.org/standard/81442.html)
- [ISO 23247-1 — Digital twin framework for manufacturing](https://www.iso.org/standard/75066.html) — domain manufacturing, bukan batas definisi general-purpose.
- [Digital Twin Consortium — definition](https://www.digitaltwinconsortium.org/initiatives/the-definition-of-a-digital-twin/)
- [NASA — history and uses of digital twins](https://science.nasa.gov/biological-physical/why-does-the-world-and-nasa-need-digital-twins/)
- Grieves & Vickers, *Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems*, DOI `10.1007/978-3-319-38756-7_4`.
- [NIST IR 8356 — Security and Trust Considerations for Digital Twin Technology](https://csrc.nist.gov/pubs/ir/8356/final)

Lanjutkan ke [`11_iot_telemetry_connectivity`](../11_iot_telemetry_connectivity/README.md) setelah gate chapter ini lulus.
