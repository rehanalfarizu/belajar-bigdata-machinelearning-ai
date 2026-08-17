# Praktikum — Level 5: Deep Learning

> **Instruksi**: Ketik ulang setiap kode. Jangan copy-paste. Pastikan GPU available (`nvidia-smi` atau `tf.config.list_physical_devices('GPU')`). Jika tidak ada GPU, training akan lambat — tetap bisa试验 tapi预期waktu lebih lama.
> **Waktu**: ~8–10 jam praktikum

---

## Latihan 1: TensorFlow/Keras Setup

**1.1.** Cek TensorFlow version dan apakah GPU available.
```python
import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")
print(f"GPU available: {tf.config.list_physical_devices('GPU')}")

# Alternative: tf.test.is_gpu_available() — deprecated tapi masih jalan
```

**1.2.** Buat neural network sederhana untuk klasifikasi:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # 4 fitur (Iris)
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')  # 3 kelas
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
```

**1.3.** Train 50 epoch dengan `validation_split=0.2`, simpan history.
- Plot training vs validation accuracy dan loss.

---

## Latihan 2: MLP untuk Fashion-MNIST

**2.1.** Load Fashion-MNIST dari keras.datasets.
```python
from tensorflow.keras.datasets import fashion_mnist

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
print(f"Train shape: {X_train.shape}")  # (60000, 28, 28)
print(f"Test shape: {X_test.shape}")   # (10000, 28, 28)

# Label mapping
labels = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
          'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
```

**2.2.** Preprocessing:
- Normalisasi pixel ke [0, 1]: `X_train / 255.0`
- Flatten gambar 28×28 jadi 784: `X_train.reshape(-1, 784)`

**2.3.** Arsitektur MLP:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
    Dense(512, activation='relu', input_shape=(784,)),
    Dropout(0.2),
    Dense(256, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])
```

**2.4.** Compile: adam, sparse_categorical_crossentropy, accuracy.
- Train: 20 epoch, batch=64, validation_split=0.1

**2.5.** Evaluasi model di test set: `model.evaluate(X_test, y_test)`
- Classification report dan confusion matrix.

---

## Latihan 3: CNN untuk CIFAR-10

**3.1.** Load CIFAR-10, normalisasi pixel ke [0, 1].
```python
from tensorflow.keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0  # Normalize
print(f"Train shape: {X_train.shape}")  # (50000, 32, 32, 3)
```

**3.2.** Arsitektur CNN:
```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
```

**3.3.** Compile: adam, sparse_categorical_crossentropy, accuracy.
- Train: 20 epoch, batch=64

**3.4.** Bandingkan dengan MLP sederhana (Dense layer tanpa Conv). Berapa selisih accuracy?

---

## Latihan 4: ImageDataGenerator + Data Augmentation

**4.1.** Gunakan ImageDataGenerator untuk augmentasi:
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    zoom_range=0.1
)
```

**4.2.** Train CNN CIFAR-10 dengan augmentasi:
```python
train_datagen.fit(X_train)
model.fit(
    train_datagen.flow(X_train, y_train, batch_size=64),
    epochs=20,
    validation_data=(X_test, y_test)
)
```
Bandingkan accuracy vs tanpa augmentasi.

---

## Latihan 5: Callbacks

**5.1.** Buat callbacks:
```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

callbacks = [
    EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    ModelCheckpoint(
        'best_model.keras',
        monitor='val_accuracy',
        save_best_only=True
    ),
    ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=3,
        min_lr=1e-6
    )
]
```

**5.2.** Train ulang model dengan callbacks. Cek apakah model yang disimpan adalah yang terbaik.

**5.3.** Challenge: buat custom callback yang setiap epoch print epoch number dan validation accuracy.
```python
from tensorflow.keras.callbacks import Callback

class PrintAccuracy(Callback):
    def on_epoch_end(self, epoch, logs=None):
        print(f"Epoch {epoch+1}: val_accuracy={logs['val_accuracy']:.4f}")
```

---

## Latihan 6: LSTM untuk Time Series

**6.1.** Generate synthetic time series data:
```python
import numpy as np

t = np.arange(1000)
y = np.sin(0.05 * t) + np.random.randn(1000) * 0.1  # sin + noise
```

**6.2.** Buat sequences: window_size=20 → tiap sample: 20 timestep → prediksi timestep 21.
```python
def create_sequences(data, window_size=20):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

X, y = create_sequences(y, window_size=20)
X = X.reshape(-1, 20, 1)  # reshape untuk LSTM: (samples, timesteps, features)
```

**6.3.** Split: 80% train, 20% test. Normalisasi.

**6.4.** Arsitektur LSTM:
```python
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(20, 1)),
    LSTM(30),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
```

**6.5.** Train 50 epoch. Plot: actual vs predicted.

---

## Latihan 7: Transfer Learning — VGG16 / MobileNet

**7.1.** Download VGG16 pretrained ImageNet weights, tanpa top layer:
```python
from tensorflow.keras.applications import VGG16

base_model = VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
base_model.trainable = False  # Freeze semua layer
base_model.summary()
```

**7.2.** Buat model:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])
```

**7.3.** Compile: adam (learning rate kecil: 1e-4), binary_crossentropy.
- Train 10 epoch.

**7.4.** Unfreeze layer terakhir VGG16 → fine-tune 5 epoch lagi.
```python
base_model.trainable = True
# Freeze semua layer KECUALI 4 layer terakhir
for layer in base_model.layers[:-4]:
    layer.trainable = False

model.compile(optimizer=Adam(1e-5), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_generator, epochs=5, validation_data=val_generator)
```

---

## Latihan 8: Batch Normalization & Dropout Comparison

**8.1.** Buat 4 model untuk Fashion-MNIST:
- Model A: tanpa BatchNorm, tanpa Dropout
- Model B: dengan BatchNorm, tanpa Dropout
- Model C: tanpa BatchNorm, dengan Dropout(0.3)
- Model D: dengan BatchNorm + Dropout(0.3)

```python
from tensorflow.keras.layers import BatchNormalization

def build_model(norm=False, dropout=0.0):
    model = Sequential([Flatten(input_shape=(28, 28))])
    for units in [256, 128, 64]:
        model.add(Dense(units, activation='relu'))
        if norm: model.add(BatchNormalization())
        if dropout: model.add(Dropout(dropout))
    model.add(Dense(10, activation='softmax'))
    return model
```

**8.2.** Train semua model 15 epoch dengan learning rate sama.

**8.3.** Analisis: model mana yang paling bagus? Mana yang paling cepat konvergen?

---

## Latihan 9: Multi-GPU Training (jika ada)

**9.1.** Cek apakah multi-GPU tersedia:
```python
strategy = tf.distribute.MirroredStrategy()
print(f"Number of devices: {strategy.num_replicas_in_sync}")
```

**9.2.** Bangun dan train model dalam strategy scope.

**9.3.** Bandingkan waktu training dengan dan tanpa multi-GPU.

---

## Tantangan Akhir — CNN untuk Batu-Gunting-Kertas (RPS)

**Tantangan: End-to-End Deep Learning Pipeline**

Unduh dataset RPS: https://www.kaggle.com/datasets/dat判定files/rock-paper-scissors-dataset

### Langkah:

1. **Load dan explore dataset**. Tampilkan 1 contoh dari tiap kelas.
2. **Preprocessing**: resize 150×150, normalisasi, augmentasi
3. **Arsitektur CNN** yang kamu desain sendiri
4. **Compile**: adam, categorical_crossentropy, accuracy
5. **Train** dengan EarlyStopping dan ModelCheckpoint
6. **Plot** training history (accuracy + loss)
7. **Evaluasi** di test set: classification report, confusion matrix
8. **Prediksi** beberapa gambar acak → tampilkan gambar + prediksi + aktual
9. **Simpan** model terbaik
10. **Load** model, cek apakah bisa memprediksi gambar baru

---

## Challenge Tambahan: Neural Network dari Nol (Tanpa Keras)

**Tujuan**: Pahami apa yang terjadi DI BALAKANG layer — bukan black box.

Implementasikan single neuron dengan NumPy saja:

```python
import numpy as np

class Neuron:
    def __init__(self, n_inputs):
        # Inisialisasi weight random kecil
        self.weights = np.random.randn(n_inputs) * 0.01
        self.bias = 0

    def forward(self, x):
        # z = w·x + b
        z = np.dot(self.weights, x) + self.bias
        # Sigmoid activation
        return 1 / (1 + np.exp(-z))

# Test
neuron = Neuron(3)
x = np.array([0.5, -0.2, 0.1])
output = neuron.forward(x)
print(f"Neuron output: {output:.4f}")
```

**Challenge**: extend ke Layer (banyak neuron) dan Neural Network lengkap dengan forward pass, loss function (MSE), dan backpropagation dari scratch!
