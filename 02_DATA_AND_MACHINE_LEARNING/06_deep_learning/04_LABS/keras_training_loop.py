"""Tiny local TensorFlow training loop; no download or GPU required."""

from __future__ import annotations

import tempfile
from pathlib import Path

import tensorflow as tf


def build_dataset() -> tuple[tf.data.Dataset, tf.data.Dataset]:
    features = tf.reshape(tf.range(0, 40, dtype=tf.float32), (-1, 1)) / 40.0
    labels = 3.0 * features + 0.5
    train = (
        tf.data.Dataset.from_tensor_slices((features[:32], labels[:32]))
        .shuffle(32, seed=42, reshuffle_each_iteration=True)
        .batch(8)
    )
    validation = tf.data.Dataset.from_tensor_slices(
        (features[32:], labels[32:])
    ).batch(8)
    return train, validation


def mean_loss(model: tf.keras.Model, dataset: tf.data.Dataset) -> float:
    losses = [
        tf.reduce_mean(tf.square(model(inputs, training=False) - targets))
        for inputs, targets in dataset
    ]
    return float(tf.reduce_mean(losses))


def run(epochs: int = 20) -> tuple[float, float]:
    tf.keras.utils.set_random_seed(42)
    train, validation = build_dataset()
    model = tf.keras.Sequential([tf.keras.layers.Input((1,)), tf.keras.layers.Dense(1)])
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
    initial_validation_loss = mean_loss(model, validation)

    for epoch in range(epochs):
        for inputs, targets in train:
            with tf.GradientTape() as tape:
                predictions = model(inputs, training=True)
                loss = tf.reduce_mean(tf.square(predictions - targets))
            gradients = tape.gradient(loss, model.trainable_variables)
            if any(gradient is None for gradient in gradients):
                raise RuntimeError("missing gradient")
            optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        print(f"epoch={epoch + 1:02d} validation_loss={mean_loss(model, validation):.6f}")

    final_validation_loss = mean_loss(model, validation)
    with tempfile.TemporaryDirectory() as directory:
        checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
        saved_path = checkpoint.save(str(Path(directory) / "checkpoint"))
        before_reload = model(tf.constant([[0.25]]), training=False)
        restored = tf.keras.Sequential(
            [tf.keras.layers.Input((1,)), tf.keras.layers.Dense(1)]
        )
        tf.train.Checkpoint(model=restored).restore(saved_path).expect_partial()
        after_reload = restored(tf.constant([[0.25]]), training=False)
        tf.debugging.assert_near(before_reload, after_reload)
    return initial_validation_loss, final_validation_loss


if __name__ == "__main__":
    before, after = run()
    print(f"validation_loss: {before:.6f} -> {after:.6f}")
