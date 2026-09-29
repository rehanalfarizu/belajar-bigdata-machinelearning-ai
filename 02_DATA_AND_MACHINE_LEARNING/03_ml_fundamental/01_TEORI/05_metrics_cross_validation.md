# Lesson 05 — Metrics dan Cross-Validation

Confusion matrix memisahkan TP/FP/TN/FN. Precision menjawab “dari alarm, berapa benar?” Recall menjawab “dari kasus nyata, berapa ditemukan?” F1 menyeimbangkan keduanya; PR lebih informatif pada positive rare. ROC mengukur ranking across thresholds tetapi dapat terlihat baik pada imbalance.

Regression: MAE mudah diterjemahkan dan robust relatif; RMSE menghukum error besar; R² membandingkan dengan mean baseline dan dapat negatif pada test.

Satu validation split dapat kebetulan. Cross-validation mengukur variability antar-sample, tetapi gunakan temporal/group-aware split bila struktur menuntutnya. CV lebih mahal dan bukan pengganti independent test.

Checkpoint: dari cost FN/FP, pilih metric/threshold; hitung confusion manual; desain CV yang menghormati entity/time.
