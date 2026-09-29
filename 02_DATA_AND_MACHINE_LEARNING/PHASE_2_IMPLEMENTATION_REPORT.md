# Phase 2 Implementation Report

Tanggal: 29 September 2026. Referensi: [audit](PHASE_2_PEDAGOGICAL_AUDIT.md), [plan](PHASE_2_IMPLEMENTATION_PLAN.md), dan [review](PHASE_2_PEDAGOGICAL_REVIEW.md).

## Kondisi awal dan gap

Phase 2 bermula dengan 49 file. Dua chapter hanya empat file; teori lain terlalu ringkas atau terlalu padat; lab dominan notebook; tidak ada broken-case ladder; empat checkpoint hilang; Month 2 belum milestone; Week 5–9 belum harian; Deep Learning mencampur framework.

## Files added

- 32 sequential lesson: Data 6, Mining 4, ML Fundamental 6, ML Advanced 5, Time Series 5, Deep Learning 6.
- 14 lab guides dengan 12 bagian wajib.
- Messy local dataset tiga tabel dan DuckDB SQL.
- Lima lightweight executable modules plus TensorFlow custom training-loop script.
- Enam lightweight test modules.
- Problems, broken cases, mini-project, dan checkpoint untuk keenam chapter.
- Phase audit, implementation plan, pedagogical review, dan report.
- GitHub Actions lightweight workflow.

Phase 2 kini memiliki 132 file; materi lama dipertahankan sebagai reference/laboratory.

## Files modified

- Phase/chapter README menjadi navigable maps dengan prerequisite, effort, lesson, practice, workplace, gate.
- `requirements.txt` menambahkan DuckDB.
- Month 2 project menjadi M1–M10.
- Global data/ML problems menjadi Level 1–5.
- Roadmap Week 5–9 menjadi tabel harian.
- Repository audit memeriksa Phase 2 lab count/contract, lesson minimum, artifact directories, project milestones, dan problem levels.

## Labs

- Data: profile messy data; clean/validate/curate; DuckDB JOIN/CTE/window.
- Mining: association rules; cluster/sequence/spurious pattern.
- ML Fundamental: split/baseline/leakage; from-scratch→sklearn; metrics/error analysis.
- ML Advanced: calibration/cost threshold; comparison under constraints.
- Time Series: future leakage; rolling forecast/drift.
- Deep Learning: manual neuron/gradient; Keras loop/overfitting/checkpoint.

## Tests

23/23 lightweight unit tests lulus:

- data quality 4;
- pattern mining 4;
- ML mechanics 4;
- decision/calibration 3;
- temporal mechanics 4;
- neural mechanics 4.

## Debugging dan problems

Tiap chapter mempunyai 7–9 broken cases. Chapter/global problem sets memakai Recall→Apply→Analyze→Design→Workplace serta tidak memberi tool sebagai jawaban untuk open-ended problem.

## Project milestones

Month 2: inspect raw; grain/schema; clean/validate; SQL; EDA/baseline; feature pipeline; candidates; evaluation; error/constraints; reproducibility/report.

## Verification

- structure, Markdown/local links, notebook JSON/static syntax, Python syntax: PASS;
- Phase 1+2 lab contract: PASS;
- Phase 2 structural contract: PASS;
- generated artifacts: none;
- lightweight tests: 23/23 PASS;
- Week 5–9: daily theory, lab, problem/debug, deliverable/checkpoint;
- lightweight CI: configured.

## Limitations

- DuckDB, scikit-learn, dan TensorFlow tidak terpasang pada execution environment ini; library-heavy labs dan TensorFlow script diverifikasi secara statis, bukan dieksekusi. `requirements.txt` menyediakan dependency path.
- Notebook lama lolos JSON/Python static validation tetapi tidak seluruhnya dieksekusi ulang karena heavy/download workload.
- Visual experiments membutuhkan learner menjalankan environment lengkap; CI default sengaja tidak mengunduh dataset atau memakai GPU.
- Local datasets kecil mengajarkan mechanism, bukan benchmark performance.
- Checkpoint defense manusia tetap diperlukan untuk membuktikan learning outcome.

## Gate

**PHASE 2 PEDAGOGICAL/LIGHTWEIGHT ENGINEERING GATE: PASS.**

Scope wajib, navigation, labs, reasoning, debugging, project, roadmap, static validation, dan lightweight behavior evidence tersedia. Heavy execution tetap menjadi explicit environment-specific verification, bukan klaim tersembunyi.
