# Lesson 02 — Gradient, Backpropagation, dan NumPy Network

Gradient menunjukkan perubahan loss terhadap parameter. Chain rule mengalirkan sensitivity dari loss ke layer sebelumnya; backprop menyimpan intermediate lalu menghitung gradient secara efisien.

Manual finite difference memverifikasi gradient tetapi mahal. Implementasi NumPy satu hidden layer memperlihatkan forward→loss→backward→update tanpa magic.

Failure: sign salah, shape broadcasting diam-diam, exploding/vanishing gradient, learning rate terlalu besar. Debug dengan tiny batch, gradient check, loss before/after one update, dan norm gradient.
