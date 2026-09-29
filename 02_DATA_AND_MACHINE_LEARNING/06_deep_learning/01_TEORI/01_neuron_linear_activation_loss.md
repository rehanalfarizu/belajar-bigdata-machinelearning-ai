# Lesson 01 — Neuron, Linear Transformation, Activation, Loss

Neuron menghitung weighted sum + bias lalu activation. Tanpa nonlinear activation, tumpukan layer linear tetap satu transformasi linear.

Loss mengubah “salah” menjadi objective numerik. MSE cocok pada error kontinu tertentu; cross-entropy pada probability classification. Metric bisnis tidak selalu differentiable sehingga loss dan metric dapat berbeda.

Hitung manual satu neuron dan cross-entropy sebelum framework. Periksa shape, scale, saturation, dan target encoding.

Why not deep learning? Data tabular kecil sering lebih baik dengan baseline linear/tree: lebih murah, cepat, dan mudah diaudit.
