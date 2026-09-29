# Lesson 05 — Overfitting, Regularization, dan Learning Curves

Jika training loss turun sementara validation naik, model mempelajari detail yang tidak generalize. Lihat curve, bukan epoch final saja.

Alternatives: more representative data, augmentation yang label-preserving, weight decay, dropout, smaller model, early stopping. Batch normalization bukan universal regularizer.

Eksperimen ubah satu variable, ulangi seeds bila mampu, dan simpan baseline. Evidence harus mencakup train/validation gap, held-out result, cost, serta failure slice.
