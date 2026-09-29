# Lesson 02 — Ensemble, Boosting, dan Search

Bagging melatih model relatif independen lalu merata-ratakan untuk mengurangi variance. Boosting menambah learner yang fokus pada residual/error sebelumnya sehingga kuat tetapi sensitif noise/tuning.

Random Forest adalah bagging tree. Gradient boosting, XGBoost, dan LightGBM memakai strategi boosting berbeda untuk efisiensi/regularization.

Hyperparameter search adalah experiment budget. Grid exhaustif pada ruang kecil; random sering lebih efisien; Optuna memilih trial adaptif. Semua keputusan memakai validation/CV, bukan test.

Trade-off wajib: quality, latency, memory, training cost, maintainability. Early stopping harus memakai validation yang sah. Evidence adalah comparison table dengan uncertainty dan constraints.
