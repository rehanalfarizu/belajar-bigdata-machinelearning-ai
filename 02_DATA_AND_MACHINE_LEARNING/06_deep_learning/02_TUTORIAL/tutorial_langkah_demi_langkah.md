# Tutorial Penyelesaian — Level 05 Deep Learning

## Aturan sebelum `.fit()`

Tulis empat hal: bentuk input, bentuk label, activation output, dan loss. Untuk Fashion-MNIST, input `(batch, 28, 28)`, label integer `0–9`, output `Dense(10, softmax)`, dan loss `sparse_categorical_crossentropy`. Jika label one-hot, gunakan `categorical_crossentropy`—jangan mencampur keduanya.

## MLP dari nol

Ikuti cell gradient descent di notebook secara berurutan. Cek bahwa `prediction`, `error`, dan `y` memiliki shape sama. Loss harus turun; bila naik, kurangi learning rate. Jangan menilai hanya dari prediksi terakhir—plot seluruh loss history.

## Cara membangun model Keras

```python
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
```

Lihat `model.summary()` sebelum training. Jumlah parameter yang sangat besar terhadap data kecil adalah sinyal risiko overfitting.

## Membaca history

- Train dan validation sama-sama rendah: underfitting; cek data, tambah kapasitas secara terbatas, atau train lebih lama.
- Train naik tetapi validation stagnan/turun: overfitting; tambah data/augmentation, regularisasi, atau early stopping.
- Loss `nan`: cek learning rate, data `nan/inf`, normalisasi, dan label.

Untuk CNN, tambah channel dengan `x[..., np.newaxis]`, sehingga shape menjadi `(batch, 28, 28, 1)`. Untuk LSTM, jangan mengacak waktu dan hitung normalisasi hanya dari periode train.

## Evaluasi akhir

Tampilkan confusion matrix dan contoh prediksi salah. Jangan mengatakan CNN “lebih baik” hanya dari satu run; gunakan seed sama, data split sama, serta budget epoch yang sebanding.
