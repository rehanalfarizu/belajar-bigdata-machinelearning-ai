# Lesson 02 — Linear dan Logistic Regression

Linear regression mencari coefficient yang meminimalkan residual squared; prediction adalah weighted sum. Hitung slope/intercept kecil dengan tangan, lalu verifikasi `fit_simple_linear` sebelum sklearn.

Logistic regression menerapkan sigmoid pada linear score sehingga output 0–1. Ia mengoptimalkan log loss, bukan langsung accuracy. Threshold menerjemahkan probability menjadi decision dan harus terkait cost.

Asumsi penting: hubungan linear pada target/linear log-odds, independent errors sesuai konteks, dan feature tidak sepenuhnya collinear. Outlier memengaruhi squared loss.

Why not tree? Tree menangkap nonlinearity tetapi prediction discontinuous dan dapat overfit. Why not neural net? Complexity sering tidak dibenarkan pada tabular kecil.

Evidence: residual/error slice, held-out metric, coefficient stability, calibration untuk probability. Debug shape, scale, convergence, leakage, dan feature availability.
