# Lesson 06 — Bias, Variance, dan Error Analysis

Underfitting terjadi ketika train dan validation sama-sama buruk: representation/model terlalu sederhana atau signal lemah. Overfitting terjadi ketika train baik tetapi validation buruk: model menyesuaikan noise/specific sample.

Learning curve terhadap data/complexity membantu membedakan. Regularization, lebih banyak representative data, dan simplification dapat membantu tetapi bukan resep universal.

Aggregate metric menyembunyikan failure group. Error analysis memeriksa slice site/device/time/range, false positive/negative examples, label quality, dan uncertainty.

Requirement change harus kembali ke target/cost/split, bukan hanya tuning. Evidence berikutnya dapat berupa data collection, feature fix, threshold, atau bahkan tidak memakai ML.

Checkpoint: diagnosis satu gap train-validation, buat tiga hypothesis, eksperimen pembeda, dan keputusan dengan trade-off.
