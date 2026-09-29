# Restructure Plan

Tanggal rencana: 28 September 2026. Dokumen ini dibuat sebelum perpindahan path. Prinsip migrasi: content existing dipindahkan, bukan dibuat ulang; file generated/internal dikeluarkan dari learning path; semua link lokal diuji setelah migrasi.

## Mapping chapter

| Old path | New path | Action | Reason | Links yang diperbarui |
|---|---|---|---|---|
| `materi/00_math_statistics` | `01_FOUNDATION/04_math_statistics` | move + struktur internal | matematika adalah foundation gate | root, curriculum, guide, tracker, tutorial index |
| `materi/01_python_fundamental` | `01_FOUNDATION/02_python_fundamental` | move + struktur internal | urutan belajar Python beginner | root dan semua navigasi chapter |
| — | `01_FOUNDATION/01_computer_fundamentals` | tambah content nyata | prerequisite process/memory/files/network/HTTP | phase README dan breadcrumbs |
| — | `01_FOUNDATION/03_python_professional` | tambah content nyata | typing/testing/packaging/async dipisahkan dari syntax dasar | phase README dan breadcrumbs |
| `materi/02_data_analysis` | `02_DATA_AND_MACHINE_LEARNING/01_data_analysis_sql` | move + struktur internal | fase data | root dan semua navigasi chapter |
| — | `02_DATA_AND_MACHINE_LEARNING/02_data_mining` | tambah content nyata | KDD/CRISP-DM/pattern mining eksplisit | phase README dan breadcrumbs |
| `materi/03_ml_fundamental` | `02_DATA_AND_MACHINE_LEARNING/03_ml_fundamental` | move + struktur internal | fase Data/ML | root dan navigasi |
| `materi/04_ml_advanced` | `02_DATA_AND_MACHINE_LEARNING/04_ml_advanced` | move + struktur internal | fase Data/ML | root dan navigasi |
| — | `02_DATA_AND_MACHINE_LEARNING/05_time_series` | tambah content nyata | fondasi temporal sebelum predictive twin | phase README dan breadcrumbs |
| `materi/05_deep_learning` | `02_DATA_AND_MACHINE_LEARNING/06_deep_learning` | move + struktur internal | fase Data/ML | root dan navigasi |
| — | `03_AI_AND_DATA_SYSTEMS/01_computer_vision` | tambah content nyata | track AI modality yang belum eksplisit | phase README dan breadcrumbs |
| `materi/08_nlp_transformers` | `03_AI_AND_DATA_SYSTEMS/02_nlp_transformers` | move + struktur internal | fase AI systems | root dan navigasi |
| `materi/07_big_data_data_engineering` | `03_AI_AND_DATA_SYSTEMS/03_big_data_data_engineering` | move + struktur internal | fase data systems | root dan navigasi |
| `materi/06_mlops_deployment` | `03_AI_AND_DATA_SYSTEMS/04_mlops` | move + struktur internal | fase production AI | root dan navigasi |
| `materi/09_ai_systems_cloud` | `03_AI_AND_DATA_SYSTEMS/05_ai_systems_cloud` | move + struktur internal | fase production AI | root dan navigasi |
| `materi/10_digital_twin` | `04_DIGITAL_TWIN_ENGINEERING/01_digital_twin_fundamentals` | move + struktur internal; pertahankan `src/tests` | awal track DT | seluruh cross-link DT dan commands |
| `materi/11_iot_telemetry_connectivity` | `04_DIGITAL_TWIN_ENGINEERING/02_iot_telemetry_connectivity` | move + struktur internal | connected twin | seluruh cross-link DT |
| `materi/12_time_series_state_estimation` | `04_DIGITAL_TWIN_ENGINEERING/03_time_series_state_estimation` | move + struktur internal | connected twin | notebook source path dan cross-link |
| `materi/13_simulation_physics_hybrid` | `04_DIGITAL_TWIN_ENGINEERING/04_simulation_physics_hybrid` | move + struktur internal | predictive twin | cross-link DT |
| `materi/14_anomaly_predictive_maintenance_rul` | `04_DIGITAL_TWIN_ENGINEERING/05_anomaly_predictive_maintenance_rul` | move + struktur internal | predictive twin | cross-link DT |
| `materi/15_architecture_semantics_spatial` | `04_DIGITAL_TWIN_ENGINEERING/06_architecture_semantics_graph` + `07_spatial_gis_3d` | split by subject | architecture/semantics dan spatial punya gate berbeda | cross-link DT |
| `materi/16_optimization_intelligent_twin` | `04_DIGITAL_TWIN_ENGINEERING/08_optimization_decision_intelligence` + `09_intelligent_digital_twin` | split by subject | optimization dan governed intelligence punya gate berbeda | cross-link DT |
| `materi/17_domains_research_capstone` | `05_PROFESSIONAL_AND_RESEARCH/04_research_methodology` + `05_domain_case_studies` | split; capstone specification ke project | professional/research phase | root, roadmap, project links |
| — | `05_PROFESSIONAL_AND_RESEARCH/01_workplace_software_engineering` | tambah content nyata | workplace engineering gap | phase README |
| — | `05_PROFESSIONAL_AND_RESEARCH/02_system_design` | tambah content nyata | architecture trade-off gap | phase README |
| — | `05_PROFESSIONAL_AND_RESEARCH/03_security_safety_governance` | tambah content nyata dari track | cross-cutting professional gate | phase README |

## Mapping file internal chapter

| Existing filename | Destination |
|---|---|
| `README.md` yang berisi teori | `01_TEORI/konsep_dasar.md`; diganti README navigasi |
| `TEORI_MENDALAM.md` | `01_TEORI/teori_mendalam.md` |
| `TUTORIAL_PENYELESAIAN.md`, `QUICKSTART.md` | `02_TUTORIAL/` |
| `PANDUAN_KODE.md` | `03_EXAMPLES/contoh.md` |
| `*.ipynb` | `04_LABS/` |
| `praktikum.md` | `05_EXERCISES/exercises.md` |
| `SOLUSI_DAN_TEORI_LENGKAP.md` | `99_SOLUTIONS/solusi_dan_teori_lengkap.md` |
| `src/`, `tests/`, `pyproject.toml` | tetap di root chapter engineering |

Folder `06_PROBLEM_SOLVING`, `07_DEBUGGING`, `08_PROJECT`, dan `09_CHECKPOINT` hanya dibuat bila ada content yang benar-benar dapat dikerjakan. Monthly capstone berada terpisah di `06_PROJECTS`.

## Mapping root dan internal

| Old path | New path/action |
|---|---|
| `STUDY_GUIDE.md` | basis `HOW_TO_USE_THIS_REPO.md`, ditulis ulang untuk struktur baru |
| `ROADMAP_TRACKER.txt` | basis `PROGRESS_TRACKER.md`, dibuat hierarchical |
| `TUTORIAL.md` | `01_FOUNDATION/02_python_fundamental/02_TUTORIAL/cara_menjalankan_python.md` |
| `CARA_MENGERJAKAN_LATIHAN.md` | content diintegrasikan ke `HOW_TO_USE_THIS_REPO.md` dan `07_PROBLEM_SOLVING/README.md` |
| `GAP_ANALYSIS.md` | `.ai_context/audits/GAP_ANALYSIS.md` |
| `materi/TEMPLATE_CHAPTER.md` | `.ai_context/TEMPLATE_CHAPTER.md` |
| `scripts/audit_repository.py` | `tools/audit_repository.py` |
| `CURRICULUM_LENGKAP.md` | tetap sementara sebagai curriculum detail; semua path diperbarui |

## Content baru yang bukan placeholder

- Delapan phase README dengan WHY, LEARN, ORDER, OUTPUT, GATE, PROJECT, NEXT.
- `START_HERE.md`, `ROADMAP_6_BULAN.md`, `PROGRESS_TRACKER.md`, `HOW_TO_USE_THIS_REPO.md`.
- Enam monthly capstone briefs dengan acceptance criteria dan evidence.
- Unscaffolded problem sets untuk programming, math/statistics, data, ML, systems, dan Digital Twin.
- Workplace tickets, debugging cases, reviews, incidents, architecture/PR/interview cases.
- Learning journal template dan repository audit tool.

## Validation setelah migrasi

1. Tidak ada file belajar tersisa di `materi/` dan tidak ada orphan content.
2. Semua local Markdown links resolve.
3. Semua Python fences, `.py`, dan notebook code cells lolos parse statis.
4. Unit tests `digital_twin_lab` lulus dari path baru.
5. Notebook state estimation dieksekusi dengan kernel project bila dependency tersedia.
6. Root README mengarahkan first-time learner ke `START_HERE.md`.
7. Setiap phase/chapter README menjawab posisi, urutan, gate, project, dan next step.

## Hasil migrasi — 28 September 2026

- [x] Seluruh learning content dipindahkan dari `materi/` ke fase kompetensi; folder legacy telah dihapus.
- [x] Materi campuran dipisah menjadi Architecture/Semantics, Spatial/GIS/3D, Optimization, Intelligent Twin, Research, Domain Cases, dan Final Capstone.
- [x] Root, roadmap, curriculum, guide, tracker, README fase, serta breadcrumbs chapter memakai path baru.
- [x] Semua solution existing berada di `99_SOLUTIONS`; README mengharuskan usaha 20–30 menit sebelum membukanya.
- [x] Enam monthly capstone, enam problem-solving tracks, tujuh workplace cases, dan learning journal berisi brief nyata.
- [x] `python tools/audit_repository.py` melaporkan structure, Markdown, notebook, Python, dan artifact: OK.
- [x] Tiga belas unit test `digital_twin_lab` lulus dari path baru.
- [x] Notebook state-estimation berhasil dieksekusi dengan kernel `python311`; hasil verifikasi disimpan di temporary directory, bukan repository.
- [x] `git diff --check` lulus dan tidak ada folder kosong atau generated artifacts tersisa.
