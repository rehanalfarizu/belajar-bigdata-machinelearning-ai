# Optimization dan Decision Intelligence

Predictive twin mengatakan apa yang mungkin terjadi. Prescriptive twin membandingkan tindakan di bawah constraints. Recommendation tetap bukan command.

```text
minimize/maximize  f(x; state, forecast, scenario)
subject to         g_i(x) ≤ 0
                   h_j(x) = 0
                   x ∈ domain
```

Definisikan decision variables, objective, hard/soft constraints, parameters, state, dan uncertainty. Linear programming cocok untuk bentuk linear; mixed-integer untuk on/off/assignment/scheduling; nonlinear optimization untuk dynamics nonlinear; routing/scheduling memiliki solver khusus. Heuristic membantu ruang sulit tetapi tidak memberi optimality guarantee.

Multi-objective decision tidak boleh disembunyikan dalam weighted sum tanpa stakeholder justification. Tampilkan Pareto trade-off. Solver output harus melaporkan feasibility, status, gap, time limit, scaling, sensitivity, dan alternative yang dipertimbangkan.

## What-if dan robustness

```text
state + uncertainty
→ candidate actions
→ simulate scenarios/disturbances
→ buang hard-constraint violations
→ bandingkan objective + risk + robustness
→ recommendation + rationale + validity window
```

Simulation optimization membutuhkan replications dan variance reduction seperti common random numbers bila sesuai. Jangan memilih action dari satu stochastic run. Uji worst-case dan plausible scenarios, bukan hanya mean forecast.

Recommendation object menyertakan state/model version, data freshness, assumptions, alternatives, predicted outcome range, constraint margins, expiry, dan rationale. Sistem penerima harus dapat menolak recommendation stale atau incompatible.

Reinforcement learning dapat dipertimbangkan untuk sequential decisions dan delayed outcomes, tetapi wajib dibandingkan dengan rule, control, dan mathematical optimization. Sim-to-real gap, reward hacking, partial observability, unsafe exploration, serta distribution shift sering membuat RL tidak layak. Governed feedback dan actuation dipelajari pada [chapter 09](../../09_intelligent_digital_twin/README.md).
