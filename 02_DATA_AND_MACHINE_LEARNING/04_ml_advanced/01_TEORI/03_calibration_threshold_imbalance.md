# Lesson 03 — Calibration, Threshold, dan Imbalance

Ranking baik tidak menjamin probability benar. Calibration bertanya apakah sekitar 70% event dengan skor 0.7 benar-benar positive. Brier/log loss dan reliability plot menilai ini.

Threshold adalah decision policy. Pilih pada validation dari FN/FP cost atau capacity; test hanya mengevaluasi pilihan final.

Pada imbalance, accuracy dapat dikuasai majority. Gunakan PR, recall/precision, cost, dan stratified/group/temporal evaluation. SMOTE hanya pada training fold; ia mengasumsikan interpolation minority bermakna dan dapat membuat sample tidak realistis.

Alternatives: class weight, threshold, anomaly framing, targeted data collection. Debug prevalence shift, label bias, leakage, dan calibration per slice.
