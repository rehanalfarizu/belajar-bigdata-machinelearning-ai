# Chapter 16 — Optimization, Intelligent Twin, Human Control, Safety, dan Security

Predictive twin mengatakan apa yang mungkin terjadi. Prescriptive twin membandingkan tindakan di bawah constraints. Intelligent twin menutup learning/decision feedback secara governed. Tidak satu pun berarti AI boleh langsung mengontrol physical system.

## 1. Operational optimization

Formulasi dasar:

```text
minimize/maximize  f(x; state, forecast, scenario)
subject to         g_i(x) ≤ 0
                   h_j(x) = 0
                   x ∈ domain
```

- **Decision variables**: apa yang boleh diubah.
- **Objective**: cost, energy, throughput, lateness, emissions, risk.
- **Constraints**: physics, capacity, safety, crew, inventory, regulation.
- **Parameters/state**: estimate dari twin beserta uncertainty.

Linear programming cocok bila objective/constraints linear; mixed-integer programming untuk on/off/assignment/scheduling; nonlinear optimization untuk dynamics nonlinear; routing/scheduling punya solver khusus; heuristic/metaheuristic membantu ruang sulit tetapi tidak memberi optimality guarantee. Multi-objective bukan sekadar weighted sum tanpa stakeholder justification; tampilkan Pareto trade-off.

Simulation optimization mengevaluasi candidate decision lewat stochastic simulator. Gunakan common random numbers/replications dan uncertainty; jangan memilih candidate dari satu random run.

Tools setelah formulasi manual: `scipy.optimize` untuk continuous optimization dan OR-Tools untuk routing/scheduling/constraint programming. Solver status, feasibility, gap, time limit, scaling, dan sensitivity harus dilaporkan.

## 2. What-if ke recommendation

```text
estimated state + uncertainty
→ candidate actions
→ simulate scenarios/disturbances
→ discard hard-constraint violations
→ compare objective + risk + robustness
→ recommendation + rationale + validity window
```

Recommendation bukan command. Sertakan assumptions, alternatives, predicted outcome range, model version, data freshness, constraint margin, and expiry.

## 3. Reinforcement learning secara proporsional

RL mendefinisikan agent, environment, state, action, reward, policy, value. Q-learning belajar action value; DQN mengaproksimasi value dengan neural network; PPO adalah policy-gradient family; model-based RL memakai/learns dynamics.

Twin/simulator dapat menjadi environment untuk training/evaluation, tetapi sim-to-real gap, reward hacking, partial observability, unsafe exploration, distribution shift, dan verification tetap ada. Gunakan RL jika sequential decisions dan delayed outcomes memang penting serta baseline control/optimization tidak cukup. Bandingkan dengan rule, PID/MPC, dan mathematical optimization. Jangan melakukan online exploration pada hazardous asset.

## 4. Intelligent twin loop

```text
Physical System → Telemetry → Quality → State Estimation → Twin State
→ Diagnosis/Prediction → What-if/Optimization → Recommendation
→ Policy + Human Decision → Validated Command → Physical System
→ Outcome/Feedback → evaluation and controlled learning
```

Capability:

- descriptive: state/history;
- diagnostic: hypotheses and evidence;
- predictive: future distribution;
- prescriptive: constrained alternatives;
- adaptive: update policy/model dengan monitoring, approval, version, canary/shadow, rollback.

Model update tanpa audit bukan intelligence; itu uncontrolled change.

## 5. Pisahkan monitoring, recommendation, decision, command, actuation

- **Monitoring**: observe dan alert.
- **Recommendation**: proposed action, belum authorized.
- **Decision**: actor/policy memilih/menolak.
- **Command**: authenticated instruction dengan idempotency/expiry.
- **Actuation**: physical execution; harus dikonfirmasi lewat independent observation bila perlu.

[`CommandGuard`](../10_digital_twin/src/digital_twin_lab/safety.py) menunjukkan safety envelope, delta limit, uncertainty limit, freshness, emergency reject, operator approval, dan audit record. Ini pedagogis; real safety function harus dirancang/verified sesuai domain/regulation oleh engineer kompeten dan tidak bergantung pada demo Python/cloud availability.

## 6. Safety engineering

Definisikan hazard, severity, exposure, controllability, safe state, safety envelope, hard constraints, interlocks, rate limit, manual override, emergency stop, watchdog, fallback/degraded mode, and recovery. Fail-safe tidak selalu “mati”; pada aircraft/medical/chemical system, safe action kontekstual.

Safety case menghubungkan claim → argument → evidence. ML metric saja bukan evidence cukup untuk actuation. Uji sensor stuck, bias, loss, contradictory sensors, delayed state, optimizer infeasible, model timeout, operator absent, network partition, repeated command, and rollback.

## 7. Security dan trust

IT berfokus confidentiality/integrity/availability; OT sering menempatkan safety/availability/determinism sangat tinggi. Terapkan segmentation, device/workload identity, mutual authentication bila sesuai, least privilege, encryption, secure boot/update, key rotation, allowlisted commands, rate limiting, signed/versioned artifacts, audit, backup/recovery, and incident response.

Threats khusus twin:

- spoofed/replayed sensor menggeser state;
- data poisoning/backdoor merusak model;
- stolen operator identity menyetujui command;
- model/ontology tampering mengubah meaning;
- simulator/optimization manipulation memilih action berbahaya;
- confidentiality leak mengungkap layout/capacity/weakness aset.

Trust juga mencakup accuracy, provenance, uncertainty, availability, explainability, and human factors. Security control tidak membuktikan model benar; model accuracy tidak membuktikan system aman.

## 8. Praktikum

1. Formulasikan tank scheduling: minimum energy dengan level bounds dan demand scenario.
2. Bandingkan greedy rule, linear program, dan simulation optimization.
3. Tambahkan uncertainty margin; ukur cost vs violation risk.
4. Buat recommendation object dengan expiry/model version/rationale.
5. Test command guard untuk stale state, high uncertainty, emergency, out-of-envelope, repeated command.
6. Buat threat model data flow dan mitigasi replay/spoofing/poisoning.
7. Jika mencoba Q-learning pada simulator, bandingkan baseline dan larang unsafe actions di environment serta policy boundary.

## Gate

Lulus bila dapat memformulasikan objective/constraints, mengevaluasi robustness, membedakan recommendation hingga actuation, menulis test hard constraint, dan membuat threat/safety analysis. Label “intelligent” hanya dipakai bila feedback learning dan governance benar-benar ada.

## Referensi lanjutan

- [SciPy optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Google OR-Tools](https://developers.google.com/optimization)
- [NIST IR 8356 — Security and Trust Considerations for Digital Twin Technology](https://csrc.nist.gov/pubs/ir/8356/final)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — periksa status/revisi terbaru sebelum mengadopsi profile; AI RMF 1.0 sedang direvisi pada saat audit.
- [ISO/IEC 42001 — AI management systems](https://www.iso.org/standard/81230.html)
- [OPC UA Part 2 — Security Model](https://reference.opcfoundation.org/Core/Part2/)

Berikutnya: [`17_domains_research_capstone`](../17_domains_research_capstone/README.md).
