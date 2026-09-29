# Broken Cases — Math & Statistics

## Case 1 — Shape mismatch tersembunyi

`zip` vectors berbeda length diam-diam membuang tail. Tambah shape invariant dan test.

## Case 2 — Unit mismatch

Temperature Celsius dan Fahrenheit digabung dalam satu mean. Temukan melalui metadata/range, konversi dengan provenance, dan cegah lewat contract.

## Case 3 — Gradient salah sign

Loss meningkat setiap step. Bandingkan analytic dengan finite difference, inspect sign/rate/scaling, lalu verify curve.

## Case 4 — Numerical cancellation

Finite difference h sangat kecil memberi derivative buruk. Sweep h dan jelaskan truncation vs floating-point error.

## Case 5 — Base-rate fallacy

Sensitivity 95% dilaporkan sebagai probability failure setelah alarm. Bangun count table dengan prevalence.

## Case 6 — Pseudoreplication

10.000 readings dari 10 assets dianggap n=10.000 independent units. Tetapkan cluster/unit dan uncertainty method yang sesuai scope.

## Case 7 — Multiple testing

100 metrics diuji dan hanya yang p<0.05 dilaporkan. Audit analysis plan dan false discoveries.

## Case 8 — Correlation causal claim

Time trend/confounder membuat correlation. Plot per regime/time, tulis causal alternatives, dan batasi claim.
