# Lesson 04 — Interpretability dan Uncertainty

Global explanation merangkum model; local explanation menerangkan satu prediction. Feature importance tidak membuktikan causation dan correlated features dapat membagi/menukar importance.

Uncertainty dapat berasal dari noise data, limited sample, model choice, atau distribution shift. Prediction interval berbeda dari confidence interval parameter.

Gunakan simple coefficients/tree, permutation importance, partial dependence, atau SHAP sesuai kebutuhan dan cost. Explanation harus diuji dengan sanity check serta dibandingkan domain knowledge.

Abstention masuk akal ketika uncertainty/OOD tinggi dan human review tersedia. Evidence: coverage-risk curve, calibration, interval coverage, and failure slices.
