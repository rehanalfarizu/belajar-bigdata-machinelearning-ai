# Level 5 — Deep Learning

> **Tujuan**: Pahami arsitektur neural network dari perspektif praktisi — apa yang terjadi di balik `.fit()`, kenapa arsitektur tertentu bekerja untuk masalah tertentu, dan kapan deep learning overkill.
> **Asumsi**: Kamu sudah paham ML dasar dan linear algebra dasar (vektor, matriks, perkalian).

---

## 1. Neural Network — Apa yang Sebenarnya Terjadi

### 1.1 Single Neuron — Perseptron

```
Input x₁, x₂, x₃
        ↓
  Σ wᵢ · xᵢ + b  → z (weighted sum)
        ↓
  activation(z) → a (output)
```

### 1.2 Activation Functions

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)

def leaky_relu(z, alpha=0.01):
    return np.where(z > 0, z, alpha * z)

def softmax(z):
    exp_z = np.exp(z - np.max(z))  # subtract max for numerical stability
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)
```

**Kapan pakai yang mana?**

| Activation | Use case | Catatan |
|---|---|---|
| Sigmoid | Output layer binary classification | Vanishing gradient |
| Tanh | Hidden layers | Vanishing gradient |
| ReLU | Hidden layers (default) | Fast, sparse gradient |
| Leaky ReLU | Hidden layers (ReLU variant) | Solves "dying ReLU" |
| Softmax | Output layer multi-class | Probabilitas yang jumlahnya = 1 |

### 1.3 Feedforward — Cara Neural Network Menghitung

```
Input Layer (4 neuron) → Hidden Layer 1 (64 neuron) → Hidden Layer 2 (32 neuron) → Output Layer (3 neuron)

Proses:
1. Input: vector [x₁, x₂, x₃, x₄] shape (4,)
2. Multiply dengan weight matrix W₁ shape (64, 4) → Z₁ shape (64,)
3. Add bias b₁ shape (64,) → Z₁ = W₁·x + b₁
4. Apply ReLU → A₁ = relu(Z₁)
5. Multiply dengan weight matrix W₂ shape (32, 64) → Z₂ = W₂·A₁ + b₂
6. Apply ReLU → A₂ = relu(Z₂)
7. Output → A₃ = softmax(W₃·A₂ + b₃)
```

### 1.4 Loss Function — Mengukur Error

```python
# Binary Cross-Entropy (binary classification)
def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-15  # prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Categorical Cross-Entropy (multi-class)
def categorical_cross_entropy(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_true * np.log(y_pred)) / len(y_true)

# Mean Squared Error (regression)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
```

---

## 2. TensorFlow/Keras — API yang Practically Digunakan di Industri

### 2.1 Sequential API

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization

model = Sequential([
    # Layer 1
    Dense(64, activation='relu', input_shape=(4,)),
    BatchNormalization(),
    Dropout(0.2),

    # Layer 2
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),

    # Layer 3
    Dense(64, activation='relu'),

    # Output layer
    Dense(3, activation='softmax')  # 3 kelas → softmax
])
```

### 2.2 Compile — Konfigurasi Training

```python
model.compile(
    optimizer='adam',          # Adaptive learning rate optimizer
    loss='sparse_categorical_crossentropy',  # untuk integer labels
    # loss='categorical_crossentropy'        # untuk one-hot labels
    # loss='binary_crossentropy'             # untuk binary classification
    metrics=['accuracy']
)
```

### 2.3 Training — .fit()

```python
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,           # samples per gradient update
    validation_split=0.2,    # 20% dari training data untuk validasi
    validation_data=(X_val, y_val),  # jika punya separate val set
    callbacks=[...],
    verbose=1
)
```

### 2.4 Batch Size — Tradeoff

```
Batch size besar:
  ✓ Training lebih cepat (GPU utilization tinggi)
  ✓ Gradient estimate lebih stabil
  ✗ Lebih memory
  ✗ Bisa stuck di local minima (gradient estimate terlalu kasar)

Batch size kecil:
  ✓ More updates per epoch
  ✓ Better generalization (noise membantu escape local minima)
  ✗ Training lebih lambat
  ✗ Gradient estimate noisy

Common choices: 32, 64, 128, 256
```

---

## 3. CNN — Convolutional Neural Network untuk Gambar

### 3.1 Kenapa Convolution untuk Gambar?

Gambar punya struktur spasial — piksel di dekatnya saling terkait. Fully connected (Dense) layer mengabaikan ini:

```
Dense layer pada gambar 224×224×3:
  Input = 224 × 224 × 3 = 150,528 neuron
  Layer pertama 512 neuron → 150,528 × 512 = 77 juta parameter!

Convolutional layer:
  Kernel 3×3 → hanya 9 × channels × filters parameter
  Output: H × W × filters
```

### 3.2 Convolution Operation

```
Input (5×5):     Kernel (3×3):
[[1,2,3,4,5],    [[1,0,-1],
 [6,7,8,9,10],    [1,0,-1],
 [1,2,3,4,5],    [1,0,-1]]
 [6,7,8,9,10],
 [1,2,3,4,5]]

Output (3×3):
[[-?, -?, -?],
 [-?, -?, -?],
 [-?, -?, -?]]

Setiap output = sum(element-wise multiply) dari kernel × patch input
```

### 3.3 Padding dan Stride

```
Padding 'same':
  → Output sama size dengan input
  → Tambah 0了一圈 di sekeliling

Stride:
  → Step size kernel saat scan
  → stride=2 → output size setengah dari input
```

### 3.4 Pooling — Downsampling

```python
# Max Pooling (paling umum) — ambil nilai maksimum di setiap region
# [[1,5], [[9,3]] → [[9,3]] (2×2 pool, stride 2)
# [[9,3]]

# Average Pooling — rata-rata
# [[1,5], [[9,3]] → [[4.5, 4]] → [[4.5, 4]]
```

### 3.5 Arsitektur CNN Umum

```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten

model = Sequential([
    # Block 1: Conv → Conv → Pool
    Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),  # 28×28 → 14×14

    # Block 2
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),  # 14×14 → 7×7

    # Block 3
    Conv2D(128, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),  # 7×7 → 3×3

    # Classifier
    Flatten(),              # 3×3×128 = 1152 → flatten ke 1D
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')  # 10 kelas
])
```

### 3.6 Data Augmentation — Lebih Data dari Data yang Ada

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rotation_range=15,        # rotasi random ±15°
    width_shift_range=0.1,    # shift horizontal ±10%
    height_shift_range=0.1,   # shift vertical ±10%
    horizontal_flip=True,     # flip horizontal
    zoom_range=0.1,           # zoom ±10%
    fill_mode='nearest'       # cara fill pixel kosong
)

# Augmentation tidak mengubah jumlah data di disk
# Tapi memberi variasi baru setiap epoch
model.fit(train_datagen.flow(X_train, y_train, batch_size=64),
          epochs=20, validation_data=(X_test, y_test))
```

---

## 4. CNN untuk CIFAR-10 — Contoh Lengkap

```python
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0  # Normalize

# Model
model = Sequential([
    # Block 1
    Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    # Block 2
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    # Block 3
    Conv2D(128, (3, 3), activation='relu', padding='same'),
    MaxPooling2D((2, 2)),

    # Classifier
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Callbacks
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint('best_cnn_model.keras', monitor='val_accuracy', save_best_only=True)
]

# Train
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=64,
    validation_split=0.1,
    callbacks=callbacks
)

# Evaluate
model.evaluate(X_test, y_test)
```

---

## 5. Transfer Learning — Leverage Pretrained Model

Transfer learning = pakai knowledge yang sudah dipelajari model dari dataset besar (ImageNet 1.2jt gambar, 1000 kelas) untuk tugas kamu dengan dataset kecil.

### 5.1 Pretrained Models yang Umum

| Model | Input Size | Parameters | ImageNet Top-5 Acc |
|---|---|---|---|
| VGG16 | 224×224 | 138M | 89% |
| ResNet50 | 224×224 | 25.6M | 93% |
| MobileNetV2 | 224×224 | 3.5M | 95% |
| EfficientNetB0 | 224×224 | 5.3M | 97% |
| InceptionV3 | 299×299 | 23.9M | 94% |

### 5.2 Dua Strategi Transfer Learning

```
Strategi A — Feature Extraction (cepat, murah):
  1. Ambil pretrained model (tanpa top layer)
  2. Freeze semua layer (weight tidak berubah)
  3. Tambah classifier baru (train hanya classifier)
  → Cocok untuk dataset kecil (< 1000 gambar per kelas)

Strategi B — Fine-tuning (lebih powerful, lebih lama):
  1. Ambil pretrained model (tanpa top layer)
  2. Train seluruh model (unfreeze sebagian layer)
  3. Learning rate kecil (lr = 1e-4 atau 1e-5)
  → Cocok untuk dataset medium (> 1000 gambar per kelas)
```

### 5.3 Implementasi

```python
from tensorflow.keras.applications import VGG16

# Strategy A: Feature Extraction
base_model = VGG16(weights='imagenet', include_top=False,
                   input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_generator, epochs=10, validation_data=val_generator)

# Strategy B: Fine-tuning
base_model = VGG16(weights='imagenet', include_top=False,
                   input_shape=(224, 224, 3))

# Unfreeze block5 saja (4 layer terakhir)
base_model.trainable = True
for layer in base_model.layers[:-4]:
    layer.trainable = False

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Learning rate lebih kecil untuk fine-tuning
from tensorflow.keras.optimizers import Adam
model.compile(optimizer=Adam(1e-5), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_generator, epochs=15, validation_data=val_generator)
```

---

## 6. LSTM — Memproses Data Sekuensial

### 6.1 RNN — Dasar Masalahnya

```
RNN: h_t = f(W·x_t + U·h_{t-1} + b)
Problem: vanishing gradient — untuk sequence panjang, gradient
         yang propagate back sangat kecil → tidak bisa belajar
         long-range dependencies

LSTM (Long Short-Term Memory): khusus designed untuk solve ini
  → Gates: input, forget, output
  → Cell state: "memory" yang bisa store info untuk lama
```

### 6.2 LSTM untuk Time Series Forecasting

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Buat sequences
def create_sequences(data, window_size=20):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

X, y = create_sequences(harga, window_size=20)
X = X.reshape(-1, 20, 1)  # (samples, timesteps, features)

# Split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Normalize
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train.reshape(-1, 1)).reshape(X_train.shape)
X_test = scaler.transform(X_test.reshape(-1, 1)).reshape(X_test.shape)

# Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(20, 1)),
    LSTM(30),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32,
          validation_data=(X_test, y_test))
```

---

## 7. Batch Normalization & Dropout

### 7.1 Batch Normalization

Normalisasi input ke setiap layer (bukan hanya ke input network):
- Mengurangi internal covariate shift
- Mempercepat training
- Regularization effect (mengurangi overfitting sedikit)

```python
# Di dalam layer:
# 1. Hitung mean dan std batch
# 2. Normalisasi: (x - mean) / sqrt(var + epsilon)
# 3. Scale dan shift: γ·x̂ + β

from tensorflow.keras.layers import BatchNormalization

model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    BatchNormalization(),  # setelah activation atau sebelum? Boleh dua-duanya
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dense(10, activation='softmax')
])
```

### 7.2 Dropout — Regularization untuk Neural Network

```python
model = Sequential([
    Dense(512, activation='relu', input_shape=(784,)),
    Dropout(0.3),   # 30% neuron "dimatikan" saat training
    Dense(256, activation='relu'),
    Dropout(0.3),   # Saat inference (evaluasi), semua neuron aktif
    Dense(10, activation='softmax')
])
```

### 7.3 Comparison Experiment

| Model | Accuracy | Notes |
|---|---|---|
| Dense only | ~87% | Overfitting |
| Dense + Dropout | ~88.5% | Better generalization |
| Dense + BatchNorm | ~89% | Faster convergence |
| Dense + BatchNorm + Dropout | ~90%+ | Best combination |

---

## Ringkasan — Level 5

`★ Insight ─────────────────────────────────────`
**1. Deep learning adalah alat, bukan solusi universal**: Untuk dataset tabular kecil/medium, Gradient Boosting (XGBoost/LightGBM) hampir selalu lebih baik dari Neural Network. DL unggul untuk: gambar, teks, audio, video, sequence data panjang. Untuk 80% masalah ML di industri, DL overkill — investasi waktu lebih baik di feature engineering.

**2. Transfer learning adalah game-changer**: Dengan pretrained model, kamu bisa dapat akurasi 85%+ di banyak image classification tasks dengan hanya 100 gambar per kelas. Tanpa transfer learning, kamu butuh 10,000+ gambar. Selalu cek pretrained model yang tersedia sebelum training dari nol.

**3. Callbacks dan checkpointing bukan luxury**: Training deep learning model bisa makan waktu 2–24 jam. Tanpa EarlyStopping dan ModelCheckpoint, kamu bisa kehilangan semua progress jika ada crash. Minimal pakai EarlyStopping + save_best_only.
`─────────────────────────────────────────────────`

---

**Lanjut**: ke [06_mlops_deployment/README.md](../06_mlops_deployment/README.md) — Deployment, MLflow, Docker, Monitoring.
