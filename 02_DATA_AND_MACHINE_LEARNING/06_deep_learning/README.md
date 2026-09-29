# Mulai dari sini — Deep Learning

## Pertanyaan utama

Bagaimana linear transformation, activation, loss, dan gradient menjadi training loop yang dapat diuji, serta kapan kompleksitas ini layak?

## Framework, prerequisite, effort

TensorFlow/Keras adalah framework primer karena sudah menjadi dependency repository. NumPy digunakan untuk mechanics; PyTorch hanya comparison appendix. Lulus ML Fundamental; estimasi 20–28 jam.

## Lesson map

1. [Neuron, activation, loss](01_TEORI/01_neuron_linear_activation_loss.md)
2. [Gradient, backprop, NumPy](01_TEORI/02_gradient_backprop_numpy.md)
3. [TensorFlow autograd/training loop](01_TEORI/03_tensorflow_autograd_training_loop.md)
4. [Dataset, batch, checkpoint, reproducibility](01_TEORI/04_dataset_batch_reproducibility.md)
5. [Overfitting, regularization, curves](01_TEORI/05_overfitting_regularization_curves.md)
6. [CNN, sequence, attention bridge](01_TEORI/06_cnn_sequence_attention_bridge.md)

## Practice path

[Manual neuron/gradient](04_LABS/01_manual_neuron_gradient.md) → [Keras training loop](04_LABS/02_keras_training_loop.md) → notebook comparison/reference → [exercises](05_EXERCISES/exercises.md) → [problems](06_PROBLEM_SOLVING/problems.md) → [broken cases](07_DEBUGGING/broken_cases.md) → [project](08_PROJECT/README.md) → [checkpoint](09_CHECKPOINT/CHECKPOINT.md).

## Gate dan navigasi

Lulus bila dapat menjelaskan gradient update, membuat loop/checkpoint/evaluation, membaca learning curve, dan membenarkan DL terhadap baseline klasik.

- Previous: [05 Time Series](../05_time_series/README.md)
- Next: [Phase 3 — Computer Vision](../../03_AI_AND_DATA_SYSTEMS/01_computer_vision/README.md)
