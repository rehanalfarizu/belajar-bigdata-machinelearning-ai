# Lesson 01 — KDD, CRISP-DM, dan Pattern Discovery

## Problem dan why

Dataset besar memiliki banyak regularity; tidak semuanya berguna. Data mining mencari pattern yang cukup kuat, valid, dan actionable—bukan sekadar menjalankan clustering.

## Mental model

KDD bergerak selection→preprocessing→transformation→mining→interpretation. CRISP-DM menambahkan business understanding, evaluation, deployment, dan iterasi. Mining adalah satu tahap, bukan keseluruhan pekerjaan.

Pattern descriptive menjelaskan structure; predictive memperkirakan outcome. Interestingness statistik tidak otomatis bernilai operasional dan tidak membuktikan causation.

## Assumptions, alternatives, trade-off

Eksplorasi tanpa hypothesis dapat menemukan kejadian kebetulan karena banyak comparison. Domain rule lebih mudah diaudit; supervised learning cocok bila target tersedia; causal study diperlukan untuk intervensi.

## Failure/debug/evidence

Tanyakan: data-generating process apa, selection bias apa, berapa pattern diuji, apakah pattern stabil pada holdout/time/site, dan apakah ada plausible mechanism?

## Workplace dan checkpoint

Dipakai pada basket analysis, operating mode, fraud triage, dan alarm sequence. Tulis satu objective CRISP-DM, success metric, risiko spurious pattern, dan deployment decision.
