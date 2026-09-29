# Lesson 02 — Lag, Rolling Feature, dan Future Leakage

Lag memakai past value untuk menjelaskan future. Rolling statistic merangkum window; feature pada time t hanya boleh memakai informasi tersedia sebelum/at decision time.

Centered rolling, backward fill dari masa depan, random split, atau scaling pada seluruh series menyebabkan leakage. Metric naik tetapi deployment gagal.

Manual: untuk [10,12,15,14], lag-1 targets adalah (10→12),(12→15),(15→14). Rolling mean dua untuk target 15 harus memakai 10 dan 12, bukan 12 dan 15 bila prediction dibuat sebelum 15.

Debug dengan timestamp lineage setiap feature dan “latest source time” assertion.
