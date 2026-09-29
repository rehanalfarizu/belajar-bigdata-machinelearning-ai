# Lesson 03 — TensorFlow Autograd dan Training Loop

TensorFlow/Keras dipilih sebagai framework primer repository. Tensor menyimpan data; GradientTape mencatat operation; optimizer mengubah variables dari gradient.

Training loop: batch→forward→loss→gradient→update→metric. State berubah pada weights dan optimizer slots. Evaluation harus memakai inference mode dan data unseen.

High-level `model.fit` produktif, tetapi custom loop dipelajari sekali agar callback, masking, debug, dan failure dapat dijelaskan.

Precondition: split valid, shapes/dtypes benar, seed/config dicatat. Postcondition: checkpoint, history, evaluation, and metadata.
