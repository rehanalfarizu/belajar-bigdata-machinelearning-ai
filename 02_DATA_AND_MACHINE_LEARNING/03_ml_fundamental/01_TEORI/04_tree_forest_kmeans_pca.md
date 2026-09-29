# Lesson 04 — Tree, Random Forest, K-Means, dan PCA

Decision tree memilih threshold yang mengurangi impurity. Tree tidak memerlukan feature scaling karena memakai order/split, tetapi mudah overfit.

Random Forest melatih banyak tree pada bootstrap sample dan subset feature; averaging menurunkan variance dengan trade-off latency/memory/interpretability.

K-Means dan PCA tidak memakai target. K-Means mencari centroid; PCA mencari direction variance. Scaling penting untuk keduanya. Cluster bukan class alami dan component bukan causal factor.

Manual: hitung satu split impurity, satu assignment centroid, dan satu projection kecil. Library dipakai sesudah mechanism dipahami.

Evidence: held-out supervised metric, tree depth curve, seed stability, cluster usefulness, reconstruction/explained variance. Debug label leakage, scale, arbitrary cluster label, dan false interpretation.
