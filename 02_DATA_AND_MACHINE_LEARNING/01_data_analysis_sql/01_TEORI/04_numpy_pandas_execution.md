# Lesson 04 — NumPy, Pandas, dan Execution Model

## Problem dan why

Loop Python per row mudah ditulis tetapi lambat dan rawan state mutation. Array/table operations menyatakan transformasi pada sekumpulan nilai.

## Mental model dan mechanism

NumPy array biasanya homogeneous dan contiguous/strided; vectorized operation memindahkan loop ke implementasi teroptimasi. Pandas menambah label index, nullable data, alignment, group, dan relational operations.

Alignment adalah kekuatan sekaligus failure source: dua Series dengan index berbeda dijumlah berdasarkan label, bukan posisi.

## Manual experiment

Hitung mean `[10, 20, 30]` manual. Bandingkan loop, NumPy, dan Pandas. Prediksi hasil penjumlahan Series ber-index `a,b` dengan `b,c` sebelum run.

## When not to use

Gunakan Python/SQL streaming bila data tidak muat memory, logic benar-benar sequential, atau dependency berat tidak diperlukan. Vectorization dapat memakai memory besar karena temporary arrays.

## Failure/debugging/evidence

Periksa `shape`, `dtype`, index uniqueness/alignment, null count, dan copy/view behavior. Benchmark hanya dengan data representatif.

## Workplace dan checkpoint

Dipakai untuk profiling, feature engineering, batch analytics. Implementasikan transformasi dengan loop dan vectorization, ukur, lalu jelaskan trade-off clarity/memory/speed.
