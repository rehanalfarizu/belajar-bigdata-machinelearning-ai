# Chapter 13 — Simulation, Physics-Based, Data-Driven, dan Hybrid Twin

Simulation menjawab “apa yang mungkin terjadi bila…”. Digital Twin membuat initial state, parameter, input, dan validation terikat pada entity/process nyata. Chapter ini mengajarkan simulator sebagai model yang dapat salah, bukan oracle.

## 1. Pilih paradigma dari mekanisme masalah

| Paradigma | Clock/state | Cocok untuk | Contoh |
|---|---|---|---|
| Continuous | differential equation | dynamics fisik kontinu | tank, motor, battery, thermal HVAC |
| Discrete-time | state per timestep | sampled control/signal | estimator, digital controller |
| Discrete-event | event mengubah state | queue/resource/process | manufacturing line, warehouse, hospital flow |
| Agent-based | banyak agent + rule | interaction/emergence | traffic, logistics, crowd |
| System dynamics | stock-flow-feedback | kebijakan agregat jangka panjang | energy/resource planning |
| Monte Carlo | repeated random samples | uncertainty/risk | failure probability, demand scenarios |

Deterministic model memberi keluaran sama untuk input/parameter sama. Stochastic model memasukkan random variables/processes; seed dibutuhkan untuk reproducibility tetapi satu seed bukan bukti robustness.

## 2. Continuous model dan numerical integration

Tangki berpenampang konstan:

```text
dV/dt = q_in - q_out
V = A h
q_out = c sqrt(max(h, 0))
dh/dt = (q_in - c sqrt(h)) / A
```

Explicit Euler:

```text
h_(k+1) = h_k + Δt f(h_k, u_k, θ)
```

Euler mudah dipahami tetapi error/stability bergantung timestep. Uji convergence: jalankan `dt`, `dt/2`, `dt/4`; jika keputusan berubah drastis, discretization belum dipercaya. Solver adaptif di SciPy cocok untuk model lebih sulit, tetapi toleransi solver tidak memperbaiki persamaan/parameter yang salah.

Model di [`simulation.py`](../10_digital_twin/src/digital_twin_lab/simulation.py) melakukan clamp level. Clamp mencegah state tak fisik, tetapi juga dapat menyembunyikan timestep/model buruk; log setiap boundary hit.

## 3. Verification, calibration, validation

- **Code verification**: apakah persamaan diimplementasikan benar? Gunakan unit test, conservation check, analytic solution bila ada, dan timestep convergence.
- **Calibration/identification**: cari parameter agar model cocok dengan data calibration. Pisahkan data validation.
- **Validation**: apakah model cukup akurat untuk intended use pada operating envelope?
- **Uncertainty quantification**: bagaimana input/parameter/model uncertainty memengaruhi output?

Jangan hanya melaporkan RMSE rata-rata. Periksa transient, steady state, boundary, operating modes, conservation, residual pattern, sensitivity, dan extrapolation.

## 4. Physics versus data versus hybrid

### Physics-based

Kelebihan: structure/explainability, constraints, dapat bekerja dengan data lebih sedikit. Kekurangan: simplification, unknown parameter, mahal pada high-fidelity, discrepancy terhadap real system.

### Data-driven

Kelebihan: belajar pola kompleks dari data. Kekurangan: leakage, distribution shift, constraint violation, ketergantungan coverage training, uncertainty yang sering buruk.

### Hybrid/grey-box

Pola residual correction:

```text
physics_prediction = f_physics(state, input, parameters)
residual_target = observation - physics_prediction
final_prediction = physics_prediction + ML(features)
```

Train residual model hanya dari prediction yang dibuat tanpa future leakage. Batasi correction agar tidak melanggar physics/safety, dan bandingkan dengan physics-only serta ML-only baseline.

Pola online calibration:

```text
sensor → estimator(parameter/state) → calibrated physics model → prediction
```

- **System identification** mengestimasi dynamics/parameter dari input-output.
- **Surrogate model** meniru simulator mahal untuk mempercepat exploration/optimization.
- **Reduced-order model** mempertahankan behavior dominan dengan dimension lebih kecil.
- **Physics-informed ML** memasukkan equation/constraint ke learning; ini bukan jaminan benar bila physics/prior salah.

## 5. Sensitivity dan uncertainty propagation

Local sensitivity mengubah satu parameter kecil; global sensitivity menjelajah distribution/range parameter dan interaction. Monte Carlo:

1. definisikan distribution parameter/input berdasarkan bukti;
2. sample scenario dengan seed tercatat;
3. jalankan simulator;
4. laporkan distribution outcome, interval, tail risk;
5. cek convergence jumlah sample.

Jangan memberi distribution yang nyaman tanpa dasar. Bedakan aleatoric variability dari epistemic uncertainty akibat pengetahuan/model terbatas.

## 6. Contoh lintas domain

- **Tank**: mass balance, leak/clog, pump policy.
- **Motor**: thermal/electromechanical dynamics, bearing degradation.
- **HVAC/building**: RC thermal network, occupancy/weather uncertainty.
- **Battery**: equivalent circuit, state of charge/health, temperature.
- **Manufacturing line**: discrete-event queue, breakdown, scheduling.
- **Traffic/logistics/fleet**: agent/network flow, routing, demand.
- **Energy**: generation/load/storage balance, forecast scenarios.

Domain berubah, workflow tetap: use case → boundary → state/input/output → assumptions → solver → verification → calibration → validation → uncertainty → safe decision.

## 7. Praktikum dan mini project

1. Lakukan timestep convergence pada tank.
2. Estimasi outlet coefficient dari noisy telemetry; validasi pada periode lain.
3. Buat 1.000 Monte Carlo run dengan uncertainty coefficient/noise; plot maximum level distribution.
4. Buat SimPy conceptual model dua mesin dan satu buffer; ukur throughput/wait time dan warm-up bias.
5. Train regression sederhana untuk residual physics; gunakan temporal split.
6. What-if tiga inflow policy; jangan terapkan ke plant, hanya buat recommendation beserta uncertainty.

## Gate

Lulus bila dapat memilih paradigma simulation, membedakan verification/calibration/validation, menguji timestep/sensitivity/uncertainty, dan membuktikan hybrid mengalahkan baseline pada data temporal yang terpisah.

## Referensi lanjutan

- [SciPy integration and ODE solvers](https://docs.scipy.org/doc/scipy/reference/integrate.html)
- [SimPy documentation](https://simpy.readthedocs.io/)
- [NIST Digital Twins for Advanced Manufacturing](https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing)

Berikutnya: [`14_anomaly_predictive_maintenance_rul`](../14_anomaly_predictive_maintenance_rul/README.md).
