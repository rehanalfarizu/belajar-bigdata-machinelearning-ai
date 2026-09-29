# Konsep Dasar Data Mining

Data mining mencari struktur berguna dalam data sebagai bagian dari proses KDD: selection, cleaning, transformation, mining, interpretation, dan deployment. CRISP-DM mengingatkan bahwa business understanding dan deployment bersifat iteratif, bukan langkah terakhir kosmetik.

Association rule `A → B` dinilai antara lain dengan support, confidence, dan lift. Confidence tinggi dapat menipu bila `B` memang sangat umum; lift membandingkan dengan base rate tetapi tetap bukan bukti kausal.

Clustering mengelompokkan berdasarkan representation dan distance yang dipilih. Hasil berubah karena scaling, metric, initialization, jumlah cluster, noise, serta bentuk cluster. Label bisnis diberikan setelah audit, bukan diasumsikan dari centroid.

Dimensionality reduction dapat membantu visualisasi/compression tetapi mungkin menghapus sinyal kecil. Outlier adalah observasi tidak biasa menurut reference distribution; anomaly belum tentu fault. Sequential pattern harus menjaga order dan window semantics.

Semakin banyak pola diuji, semakin besar peluang menemukan kebetulan. Gunakan holdout, stability analysis, multiple-testing awareness, dan domain review. “Menarik” harus didefinisikan: statistically unusual, actionable, economically valuable, atau aman—empat hal tersebut tidak identik.
