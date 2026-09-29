# Lesson 05 — Rolling Validation, Forecast Uncertainty, dan Drift

Rolling-origin validation melatih hanya pada past lalu bergerak maju. Expanding window memakai semua history; sliding window membatasi recent data. Pilihan mencerminkan drift dan cost retrain.

Point forecast tidak menyatakan uncertainty. Interval perlu dievaluasi coverage dan width; interval terlalu lebar tidak actionable, terlalu sempit gagal meliputi outcome.

Concept drift berarti relationship input-target berubah; data drift hanya distribution input. Monitor performance ketika label tersedia dan proxy/feature distribution dengan hati-hati.

Checkpoint: evaluasi naive baseline pada beberapa origin/horizon, plot errors over time, dan tetapkan retraining/investigation trigger.
