# Research Methodology dan Reproducible Evidence

Research dimulai dari pertanyaan yang falsifiable dan gap yang didukung literature review, bukan dari keinginan memakai algoritma tertentu.

## Literature review

Tentukan scope, database/index, query string, search date, inclusion/exclusion, screening, quality assessment, extraction table, dan synthesis. Bedakan standard, peer-reviewed evidence, benchmark, vendor documentation, dan marketing claim. Simpan DOI/URL dan alasan exclusion.

## Pertanyaan, hypothesis, dan baseline

Pertanyaan yang baik membandingkan baseline dan outcome terukur. Contoh: “Apakah residual hybrid mengurangi median detection delay tanpa menaikkan false alarms per asset-day dibanding EWMA pada tiga operating modes?” Klaim “AI meningkatkan Digital Twin” terlalu luas untuk diuji.

## Experimental design

- definisikan unit of analysis dan independent test assets/time;
- pilih baseline dan oracle/upper bound bila ada;
- nyatakan factors, confounders, seeds, serta data/model/config version;
- gunakan train/validation/test chronology yang cocok;
- justify sample size/power atau uncertainty;
- rencanakan ablation, sensitivity, dan failure tests;
- tetapkan primary metric sebelum melihat semua hasil bila stakes tinggi.

Reproducibility membutuhkan code, environment, data provenance/hash, configuration, seed, run command, raw results, dan analysis script. Exact numerical equality tidak selalu mungkin pada distributed/GPU computation; dokumentasikan tolerance dan nondeterminism.

## Validity dan pelaporan

Bahas internal validity (confounding/leakage), construct validity (metric mewakili tujuan?), external validity (transfer lintas asset/domain/season), dan conclusion validity (uncertainty/multiple comparison). Laporkan negative result, failed run, excluded data, deviation dari plan, dan limitations.

Metric Digital Twin perlu melampaui accuracy: freshness/lag, loss/duplicate/reject rate, estimation error dan coverage, simulation error/conservation, detection delay dan false alarm per asset-time, RUL calibration, optimization infeasibility, availability/recovery/replay correctness, constraint violation, operator override, dan outcome decision.
