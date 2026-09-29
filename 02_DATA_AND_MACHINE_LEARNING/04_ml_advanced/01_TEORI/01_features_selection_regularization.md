# Lesson 01 — Feature Engineering, Selection, dan Regularization

Feature mengubah raw signal menjadi representation yang dapat dipakai model. Setiap feature harus tersedia pada decision time dan dihitung hanya dari past/train context.

Selection mengurangi noise/cost; filter cepat tetapi tidak melihat interaction, wrapper mahal, embedded mengikuti model. Regularization mengubah objective menjadi prediction error + complexity penalty. L1 dapat membuat coefficient nol; L2 mengecilkan secara halus.

Failure: feature time-window menyentuh masa depan, selection dilakukan sebelum CV, atau proxy membocorkan target. Gunakan pipeline fold-local dan feature availability audit.

Evidence: validation stability, ablation, latency/memory, dan error slice—bukan jumlah feature semata.
