# Lesson 03 — KNN, Naive Bayes, dan SVM Intuition

KNN memprediksi dari tetangga berdasarkan distance. Scaling diperlukan karena magnitude menentukan distance. K kecil sensitif noise; k besar menghaluskan boundary. Prediction mahal karena menyimpan data.

Naive Bayes menggabungkan prior dan likelihood dengan asumsi conditional independence. Asumsi “naive” sering salah tetapi model tetap menjadi baseline cepat untuk text/count data.

SVM mencari boundary dengan margin besar; kernel memungkinkan nonlinear similarity. Ia sensitif scale dan parameter, probability tidak native, serta sulit dijelaskan pada dataset besar.

Manual: hitung distance dua titik, satu update Bayes, dan margin sederhana. Lalu gunakan library pipeline.

Debug: periksa scale, distance metric, class prior, zero probabilities/smoothing, convergence, dan split. Pilih dari data/cost, bukan leaderboard.
