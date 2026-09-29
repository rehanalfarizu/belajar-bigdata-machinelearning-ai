# Lesson 02 — Association Rules: Support, Confidence, Lift

## Problem

Transaksi dapat menunjukkan item yang sering muncul bersama, tetapi “sering bersama” perlu denominator yang jelas.

## Manual mechanism

Dari 5 basket: A muncul 4, B muncul 3, A∩B muncul 2. Support(A→B)=2/5. Confidence=2/4. Lift=(2/5)/((4/5)(3/5))=0.833. Lift < 1 berarti co-occurrence lebih rendah daripada independence expectation.

Apriori memanfaatkan sifat: jika itemset frequent, semua subset-nya frequent. FP-Growth mengompres transaksi agar tidak menghasilkan semua candidate secara eksplisit.

## Why not dan trade-off

Apriori transparan untuk data kecil tetapi candidate explosion; FP-Growth lebih efisien tetapi kurang mudah dipelajari. High confidence dapat menipu bila consequent sangat umum; lift dapat ekstrem pada support kecil.

## Failure/debug/evidence

Periksa transaction grain, duplicate item dalam basket, minimum support sensitivity, holdout stability, dan multiple testing. Association ≠ causation.

## Workplace dan checkpoint

Dipakai pada recommendation, bundling, alarm co-occurrence. Hitung tiga metric manual, implementasikan count sederhana, lalu jelaskan satu keputusan yang tidak boleh dibuat dari rule.
