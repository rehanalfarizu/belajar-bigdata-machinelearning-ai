# Lesson 06 — EDA, Visualization, dan Validation

## Problem dan why

EDA bukan mencari chart menarik; EDA menguji bentuk, quality, relationships, dan assumptions sebelum klaim atau model.

## Causal chain

Question → grain/schema → profile → quality failures → distribution/groups/time → hypothesis → targeted visualization → validation → bounded conclusion.

Univariate plot mengungkap shape/outlier; grouped comparison mengungkap heterogeneity; time plot mengungkap drift/seasonality. Correlation tidak membuktikan causation dan aggregate dapat menyembunyikan subgroup reversal.

## Manual example

Untuk delapan readings, hitung count, missing, min, median, max, dan group mean dengan tangan. Tandai apakah outlier error, rare valid event, atau signal penting sebelum memilih handling.

## Alternatives dan trade-off

Histogram sensitif bin; boxplot ringkas tetapi menyembunyikan multimodality; scatter memperlihatkan hubungan tetapi overplot pada data besar. Sample mempercepat visualisasi tetapi bisa melewatkan rare event.

## Failure/debugging/evidence

Chart tanpa unit/grain, truncated axis, post-treatment filtering, atau silent missing dapat menyesatkan. Reconcile chart count, label unit, tampilkan denominator, dan simpan query/code.

## Workplace dan checkpoint

Dipakai dalam analysis request, incident, experiment, dan dataset review. Hasilkan tiga insight yang masing-masing menyertakan evidence, limitation, dan next test.
