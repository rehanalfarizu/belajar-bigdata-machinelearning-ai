# Broken Cases — Data Mining

1. Duplicate item satu basket menggelembungkan support.
2. Confidence tinggi hanya karena consequent sangat umum.
3. Apriori candidate explosion karena threshold terlalu rendah.
4. K-Means didominasi feature ber-scale besar.
5. Cluster labels diperlakukan sebagai ground truth.
6. Event sequence salah karena tidak sort per entity.
7. Dari ribuan pattern hanya hasil “signifikan” dilaporkan.

Setiap fix harus menunjukkan before/after metric, stability/holdout, dan batas causation.
