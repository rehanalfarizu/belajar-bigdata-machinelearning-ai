# Lesson 04 — Dataset, Batch, Checkpoint, dan Reproducibility

Dataset pipeline memisahkan storage dari batching/shuffle/prefetch. Shuffle hanya training; validation/test deterministic. Batch size memengaruhi gradient noise, memory, throughput, dan batch-normalization behavior.

Reproducibility memerlukan code, data/version, split, seed, environment, config, dan hardware note. Seed tidak menjamin bit-identical semua accelerator operation.

Checkpoint menyimpan state untuk recovery/best validation, bukan bukti model bagus. Uji load→predict equivalence dan jangan menyimpan secret/path lokal.
