# Tutorial Penyelesaian — Level 04 Machine Learning Advanced

## Sebelum tuning

Jangan menjalankan GridSearch sebelum punya baseline, split yang benar, metric, dan alasan parameter yang dicoba. Tuning bukan pengganti data understanding.

```python
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    estimator=pipeline,
    param_grid={"clf__max_depth": [3, 5, None], "clf__n_estimators": [100, 300]},
    scoring="f1_macro", cv=5, n_jobs=-1,
)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

Parameter pipeline selalu memakai prefix nama langkah, misalnya `clf__max_depth`. Jika muncul `Invalid parameter`, cetak `pipeline.get_params().keys()`.

## Imbalanced data

Split stratified dahulu. Terapkan SMOTE **hanya di train fold**, idealnya memakai `imblearn.Pipeline`. Jangan melakukan oversampling sebelum cross-validation karena sampel sintetis dapat bocor.

## Time series

Urutkan waktu, buat feature lag dari masa lalu, dan gunakan `TimeSeriesSplit`. Jangan memakai random split atau scaler yang di-fit pada seluruh periode. Evaluasi dengan baseline naïf: prediksi besok sama dengan nilai terakhir.

## Error analysis

Setelah tuning, kumpulkan baris salah prediksi. Kelompokkan berdasarkan kelas, rentang nilai, wilayah, atau waktu. Pertanyaan yang harus dijawab: data apa yang tidak terwakili, apakah label salah, dan apakah threshold perlu diubah.
