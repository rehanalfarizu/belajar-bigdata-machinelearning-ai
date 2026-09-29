# Lesson 06 — CNN, Sequence Model, dan Attention Bridge

CNN memakai local receptive field dan shared weights untuk spatial pattern; cocok untuk image/grid. RNN/LSTM membawa state sepanjang sequence dan menangani order, tetapi long dependency sulit.

Attention membiarkan representation menimbang bagian sequence lain secara langsung. Ini menjadi jembatan ke Transformer pada Phase 3, bukan alasan memakai Transformer untuk semua masalah.

Manual convolution kecil dan sequence state dilakukan sebelum framework. Evaluate sesuai modality: classification metric/slice, sequence horizon, latency, memory, and shift.

Why not deep architecture: classical features/model mungkin cukup, lebih murah, dan lebih mudah dipelihara.
