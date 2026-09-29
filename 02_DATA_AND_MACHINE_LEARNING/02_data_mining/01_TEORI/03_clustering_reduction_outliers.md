# Lesson 03 — Clustering, Dimensionality Reduction, dan Outlier Mining

## Problem dan mental model

Tanpa label, kita dapat mencari grouping, low-dimensional structure, atau observation yang tidak sesuai mayoritas. Ketiganya menjawab pertanyaan berbeda.

K-Means meminimalkan squared distance ke centroid dan mengasumsikan cluster relatif bulat serta scale bermakna. Hierarchical clustering membangun dendrogram. DBSCAN memakai density dan dapat menandai noise. PCA mencari arah variance terbesar; ia bukan jaminan class separation.

## Why scaling dan alternatives

Distance sensitif magnitude. Scaling penting untuk K-Means/PCA/LOF, sedangkan business-rule segmentation mungkin lebih interpretable. DBSCAN menangani bentuk irregular tetapi sensitif epsilon/density dan dimensi tinggi.

## Failure/debug/evidence

Visualisasi bukan cukup: cek stability terhadap seed/sample/scaling, silhouette bersama domain meaning, cluster size, dan outlier inspection. Outlier dapat berupa error, rare valid event, atau signal.

## Workplace dan checkpoint

Dipakai untuk segmentasi, operating regime, compression, dan triage anomaly. Bandingkan dua scaling, ubah parameter, dan pertahankan interpretasi cluster dengan evidence.
