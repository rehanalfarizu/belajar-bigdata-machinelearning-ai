# Lesson 04 — Forecast Horizon, Baseline, dan Models

Horizon menentukan difficulty dan information availability. Baseline wajib: last value, seasonal naive, atau moving average.

Exponential smoothing memberi bobot lebih besar pada observation baru; ARIMA memodelkan differenced autoregressive/moving-average structure. Temporal-feature ML dapat menangkap nonlinear/exogenous signal tetapi mudah leakage.

Why not complex model? Bila seasonal naive setara, model kompleks menambah failure/maintenance tanpa value.

Evidence: rolling-origin metric by horizon, comparison to baseline, residual diagnostics, and runtime.
