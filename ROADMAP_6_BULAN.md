# Roadmap 6 Bulan — 26 Minggu

Roadmap memberi ritme, bukan izin melewati gate. Satu minggu diasumsikan 6 hari belajar dan 1 hari review; sesuaikan durasi tanpa menghapus evidence.

```text
Weeks 01–04  FOUNDATION              → Month 1 Capstone
Weeks 05–09  DATA + ML CORE          → Month 2 Capstone
Weeks 10–13  AI + DATA SYSTEMS       → Month 3 Capstone
Weeks 14–17  CONNECTED DIGITAL TWIN  → Month 4 Capstone
Weeks 18–21  PREDICTIVE/PRESCRIPTIVE → Month 5 Capstone
Weeks 22–26  INTELLIGENT/PROFESSIONAL→ Final Capstone
```

## Week 1 — Computer Fundamentals

| Day | Theory/tutorial | Hands-on | Problem solving / deliverable | Checkpoint |
|---|---|---|---|---|
| 1 | program, process, CPU, memory | inspect two processes/PIDs | explain program vs process | draw runtime mental model |
| 2 | filesystem, path, cwd, permission | run same path from two cwd | diagnose FileNotFoundError | predict resolved path |
| 3 | terminal, shell, environment; network basics | environment inheritance; localhost/port | distinguish no listener/DNS/port | explain process context |
| 4 | TCP, HTTP, request/response, JSON, API | local JSON server and requests | layer failure classification | explain 200/404/connect error |
| 5 | Git working tree/staging/commit/branch/remote | branch and merge conflict | defend resolution intent | read status/diff/log |
| 6 | debugging mental model | solve two broken cases | full symptom→prevention narrative | evidence review |
| 7 | review | build `system-check` | mini-project deliverable | [chapter checkpoint](01_FOUNDATION/01_computer_fundamentals/09_CHECKPOINT/CHECKPOINT.md) |

## Week 2 — Python Fundamental

| Day | Theory/tutorial | Hands-on | Problem solving / deliverable | Checkpoint |
|---|---|---|---|---|
| 1 | execution, variable, type, value | trace state/type/conversion | predict before run | explain name binding |
| 2 | operator, string | expression tree and parser | invalid text cases | explain precedence/immutability |
| 3 | list/tuple/set/dict | aliasing and records | choose collection from invariants | preserve order/duplicates/meaning |
| 4 | condition/loop | decision table and loop trace | empty/invalid input | boundaries and termination |
| 5 | function/scope/exception | extract and test functions | broad-catch failure | return/failure contract |
| 6 | file/module/import/CLI | JSONL module + CLI | import/path broken case | input→domain→output |
| 7 | notebook run-all and review | Sensor Log CLI | Level 4 problem | [chapter checkpoint](01_FOUNDATION/02_python_fundamental/09_CHECKPOINT/CHECKPOINT.md) |

## Week 3 — Python Professional

| Day | Theory/tutorial | Hands-on | Problem solving / deliverable | Checkpoint |
|---|---|---|---|---|
| 1 | module/package, OOP/composition | package boundaries | dependency direction | import without side effect |
| 2 | dataclass, type hints | typed domain values | validation vs annotation | invariant tests |
| 3 | iterator/generator, decorator, context manager | micro-lab lazy/resource lifecycle | generator/context broken cases | explain timing/cleanup |
| 4 | exception design, logging, configuration | error taxonomy/log/config | redaction and precedence | effective config evidence |
| 5 | testing | unit + integration tests | regression design | behavior coverage |
| 6 | packaging, async, concurrency | clean install and async experiment | race/cancellation reasoning | choose concurrency model |
| 7 | guided refactor | Installable Sensor Package | Level 4/5 design | [chapter checkpoint](01_FOUNDATION/03_python_professional/09_CHECKPOINT/CHECKPOINT.md) |

## Week 4 — Math, Statistics, dan Month 1 Capstone

| Day | Theory/tutorial | Hands-on | Problem solving / deliverable | Checkpoint |
|---|---|---|---|---|
| 1 | scalar/vector/matrix/dot/norm | manual + Python transform | shape/unit case | explain representation |
| 2 | eigen/SVD/PCA; derivative/gradient | projection and finite difference | scale/leakage/gradient case | explain assumptions |
| 3 | gradient descent; probability/Bayes | rate sweep and count table | base-rate problem | diagnose convergence |
| 4 | expectation/variance; sample/CLT/CI | sampling simulation | dependence/bias case | interpret interval |
| 5 | testing; correlation/regression | multiple-test and correlation experiments | causal claim challenge | limit conclusions |
| 6 | uncertainty mini-project | report and broken cases | Level 4 design | [math checkpoint](01_FOUNDATION/04_math_statistics/09_CHECKPOINT/CHECKPOINT.md) |
| 7 | integration | finish [Month 1 Sensor Simulator](06_PROJECTS/month_01_python_engineering/README.md) | demo + reasoning defense | Phase 1 gate |

## Weeks 5–26 — Chapter map

Phase berikutnya tetap pada scope sebelumnya; detail hariannya akan dikembangkan saat phase tersebut diaudit.

| Week | Fokus | Chapter/project |
|---|---|---|
| 5 | Data Analysis & SQL I | [Data Analysis & SQL](02_DATA_AND_MACHINE_LEARNING/01_data_analysis_sql/README.md) |
| 6 | Data Analysis & SQL II; Data Mining | [Data Mining](02_DATA_AND_MACHINE_LEARNING/02_data_mining/README.md) |
| 7 | ML Fundamental | [ML Fundamental](02_DATA_AND_MACHINE_LEARNING/03_ml_fundamental/README.md) |
| 8 | ML Advanced; Time Series | [ML Advanced](02_DATA_AND_MACHINE_LEARNING/04_ml_advanced/README.md), [Time Series](02_DATA_AND_MACHINE_LEARNING/05_time_series/README.md) |
| 9 | Deep Learning + integration | [Deep Learning](02_DATA_AND_MACHINE_LEARNING/06_deep_learning/README.md), [Month 2](06_PROJECTS/month_02_data_ml_system/README.md) |
| 10 | Computer Vision | [Computer Vision](03_AI_AND_DATA_SYSTEMS/01_computer_vision/README.md) |
| 11 | NLP & Transformers | [NLP & Transformers](03_AI_AND_DATA_SYSTEMS/02_nlp_transformers/README.md) |
| 12 | Big Data & Data Engineering | [Big Data](03_AI_AND_DATA_SYSTEMS/03_big_data_data_engineering/README.md) |
| 13 | MLOps; AI Systems/Cloud | [MLOps](03_AI_AND_DATA_SYSTEMS/04_mlops/README.md), [Month 3](06_PROJECTS/month_03_ai_data_platform/README.md) |
| 14 | Digital Twin Fundamentals | [DT Fundamentals](04_DIGITAL_TWIN_ENGINEERING/01_digital_twin_fundamentals/README.md) |
| 15 | IoT, Telemetry & Connectivity | [Telemetry](04_DIGITAL_TWIN_ENGINEERING/02_iot_telemetry_connectivity/README.md) |
| 16 | Time Series & State Estimation | [State Estimation](04_DIGITAL_TWIN_ENGINEERING/03_time_series_state_estimation/README.md) |
| 17 | Connected Twin integration | [Month 4](06_PROJECTS/month_04_connected_digital_twin/README.md) |
| 18 | Simulation, Physics & Hybrid Models | [Simulation](04_DIGITAL_TWIN_ENGINEERING/04_simulation_physics_hybrid/README.md) |
| 19 | Anomaly, Predictive Maintenance & RUL | [PdM/RUL](04_DIGITAL_TWIN_ENGINEERING/05_anomaly_predictive_maintenance_rul/README.md) |
| 20 | Architecture, Semantics, Spatial | [Architecture](04_DIGITAL_TWIN_ENGINEERING/06_architecture_semantics_graph/README.md), [Spatial](04_DIGITAL_TWIN_ENGINEERING/07_spatial_gis_3d/README.md) |
| 21 | Optimization + Predictive Twin integration | [Optimization](04_DIGITAL_TWIN_ENGINEERING/08_optimization_decision_intelligence/README.md), [Month 5](06_PROJECTS/month_05_predictive_digital_twin/README.md) |
| 22 | Intelligent Digital Twin | [Intelligent Twin](04_DIGITAL_TWIN_ENGINEERING/09_intelligent_digital_twin/README.md) |
| 23 | Workplace Software Engineering | [Workplace Engineering](05_PROFESSIONAL_AND_RESEARCH/01_workplace_software_engineering/README.md) |
| 24 | System Design; Security/Safety/Governance | [Professional phase](05_PROFESSIONAL_AND_RESEARCH/README.md) |
| 25 | Research; Domain Case Studies | [Research](05_PROFESSIONAL_AND_RESEARCH/04_research_methodology/README.md), [Domains](05_PROFESSIONAL_AND_RESEARCH/05_domain_case_studies/README.md) |
| 26 | Final capstone, workplace simulation, defense | [Month 6](06_PROJECTS/month_06_intelligent_digital_twin/README.md) |
