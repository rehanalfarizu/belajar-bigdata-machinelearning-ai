# Teori dan Solusi Lengkap — Level 05 Deep Learning

## 1. Dari neuron ke jaringan

Satu neuron menghitung `z = w @ x + b`, lalu activation mengubahnya menjadi `a`. Tanpa activation non-linear, tumpukan Dense layer tetap setara satu transformasi linear. ReLU, `max(0, z)`, umum dipakai di hidden layer karena murah dan mengurangi vanishing gradient. Sigmoid lazim untuk probabilitas biner; softmax mengubah 10 logit menjadi distribusi 10 kelas yang totalnya 1.

Forward pass menghasilkan prediksi. Loss mengukur ketidakcocokan target/prediksi. Backpropagation menggunakan chain rule untuk menghitung gradient loss terhadap setiap parameter. Optimizer Adam memperbarui parameter memakai estimasi momentum dan skala gradient. Epoch berarti seluruh data train telah dilihat sekali; batch adalah sebagian data sebelum satu update.

## 2. Solusi MLP Fashion-MNIST

Fashion-MNIST memiliki image grayscale 28×28 dan label integer 0–9. Pixel 0–255 perlu dinormalisasi menjadi 0–1. Karena label masih integer, gunakan sparse categorical cross-entropy; bila `to_categorical` dipakai, loss harus categorical cross-entropy.

```python
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

mlp = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax"),
])
mlp.compile(optimizer=keras.optimizers.Adam(1e-3),
            loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = mlp.fit(x_train, y_train, validation_split=0.1, epochs=15, batch_size=128,
                  callbacks=[keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)])
loss, accuracy = mlp.evaluate(x_test, y_test)
```

Gunakan `validation_split` hanya pada training data. Test tidak boleh menjadi validation selama eksperimen karena keputusan architecture/epoch akan menyesuaikan test secara tidak langsung.

## 3. Mengapa CNN lebih tepat untuk image?

MLP `Flatten` kehilangan informasi bahwa dua pixel bertetangga. `Conv2D` menggunakan kernel kecil yang sama pada banyak lokasi, sehingga parameter lebih sedikit dan pola tepi/tekstur dapat dideteksi di mana saja. Pooling mengurangi resolusi feature map. CNN bukan selalu lebih baik: untuk data tabular kecil, tree-based model sering lebih tepat.

```python
cnn = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),
    keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax"),
])
cnn.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
cnn.fit(x_train[..., None], y_train, validation_split=0.1, epochs=15, batch_size=128)
```

## 4. Regularisasi dan diagnosis

Jika train accuracy terus naik tetapi validation accuracy stagnan/turun, model overfit. Coba tambah data, valid augmentation, dropout, weight decay, atau early stopping. Jika keduanya rendah, model underfit atau data/label/preprocessing bermasalah. Batch normalization menstabilkan training tetapi bukan obat universal.

Data augmentation hanya boleh menghasilkan variasi yang tetap valid: flip horizontal mungkin valid untuk foto baju, tetapi dapat mengubah makna pada teks atau angka. Jangan augment test/validation data.

## 5. LSTM dan time series

LSTM membawa state untuk sequence, tetapi tidak dapat melihat masa depan. Buat window dari masa lalu, split berdasarkan waktu, dan scale memakai train period saja. Baseline naïf (`prediksi[t] = nilai[t-1]`) harus dikalahkan sebelum memakai LSTM. Banyak time series tabular lebih baik ditangani model statistik/tree dengan lag feature.

## 6. Transfer learning

Backbone pretrained membawa fitur generik. Mulai dengan backbone dibekukan dan classifier head baru. Setelah baseline stabil, unfreeze sebagian layer terakhir dengan learning rate sangat kecil. Fine-tuning besar dengan data kecil dapat menghancurkan fitur pretrained (catastrophic forgetting). Laporkan dataset asal pretraining dan batas domainnya.
