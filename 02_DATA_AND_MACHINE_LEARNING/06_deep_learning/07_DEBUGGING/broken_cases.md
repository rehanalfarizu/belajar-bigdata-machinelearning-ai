# Broken Cases — Deep Learning

1. Input/label shape mismatch.
2. Loss-target encoding mismatch.
3. Update sign/rate membuat divergence.
4. Validation augmentation/shuffle salah.
5. Evaluation masih training mode.
6. Test memilih epoch.
7. Checkpoint tidak dapat reload equivalently.
8. Seed dicatat tetapi data split berubah.
9. DL tidak mengalahkan simple baseline.

Gunakan tiny batch overfit, gradient check, curve, shape/dtype, checkpoint equivalence, dan baseline.
