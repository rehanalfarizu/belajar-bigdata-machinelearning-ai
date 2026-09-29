# Panduan Penulisan Kode — Level 5: Deep Learning

> Dibaca bersamaan dengan `05_deep_learning.ipynb` — jalankan cell, baca panduan ini, lalu pahami arsitektur neural network dari dasar sampai production-grade.

---

## 1. Apa Itu Deep Learning? Kapan Dipakai?

### 1.1 Neural Network vs Machine Learning Klasik

```
Machine Learning Klasik:
  Input (fitur ENGINEERED) → Model (biasanya 1-level) → Output
  Masalah: manusia harus mendefinisikan fitur sendiri

Deep Learning:
  Input (RAW data) → Neural Network (multiple layers) → Output
  Neural network LEARNING fitur sendiri dari data
```

**Kapan pakai Deep Learning?**
- Data sangat besar (>100K sample)
- Input berupa gambar, teks, audio, video
- Fitur sulit di-engineer secara manual
- Sudah punya GPU yang powerful

**Kapan TIDAK perlu Deep Learning?**
- Dataset kecil (<10K sample)
- Tabular data dengan fitur jelas
- Interpretability penting
- Resource terbatas (GPU mahal)

### 1.2 Arsitektur Neural Network

```
Input Layer          Hidden Layers           Output Layer
[3 fitur]  →  [8 neuron]  →  [5 neuron]  →  [1 neuron]
 x1,x2,x3     ReLU(Σw·x+b)  ReLU(Σw·x+b)   Sigmoid/Softmax

Setiap koneksi = bobot (weight) yang belajar dari data
Setiap neuron = ReLU(w·x + b)
```

**Kenapa banyak layer?**
- Layer 1 → belajar fitur sederhana (edges, textures)
- Layer 2 → kombinasi fitur sederhana → fitur lebih kompleks
- Layer 3+ → kombinasi fitur kompleks → pemahaman abstrak

---

## 2. PyTorch — Framework Deep Learning

### 2.1 Tensor — fundamental building block

```python
import torch

# Tensor = array NumPy yang bisa di-GPU-kan dan punya autograd
# NumPy array → CPU-only
# PyTorch Tensor → bisa dipindah ke GPU

# Dari list/NumPy
t = torch.tensor([1, 2, 3])          # float64 default
t = torch.tensor([1, 2, 3], dtype=torch.float32)
t = torch.from_numpy(np.array([1, 2, 3]))

# factory methods
torch.zeros(3, 5)                   # matriks 0
torch.ones(3, 5)                    # matriks 1
torch.rand(3, 5)                    # random uniform 0-1
torch.randn(3, 5)                   # random normal (mean=0, std=1)
torch.arange(0, 10, 2)               # [0, 2, 4, 6, 8]
torch.linspace(0, 1, 10)            # 10 titik sama jarak
torch.eye(5)                        # matriks identitas 5×5

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
t = t.to(device)

# Operasi sama seperti NumPy
t.sum()          # jumlah semua
t.mean()        # rata-rata
t.max()         # max + index
t.argmax()      # index max
t.view(5, 3)    # reshape
t.squeeze()     # hapus dimensi size-1
t.unsqueeze(0)  # tambah dimensi
```

### 2.2 Autograd — Automatic Differentiation

Ini yang membuat PyTorch bisa belajar:

```python
# PyTorch melacak setiap operasi → bisa hitung gradien secara otomatis
x = torch.tensor([2.0], requires_grad=True)  # butuh gradien → aktifkan
y = x ** 2 + 3 * x + 1

y.backward()   # hitung dy/dx untuk semua tensor dengan requires_grad=True
print(x.grad)  # → dy/dx = 2x + 3 = 2(2) + 3 = 7

# Proses training loop (dalam satu langkah):
# 1. Forward pass → hitung output
# 2. Hitung loss
# 3. backward() → hitung gradien
# 4. Optimizer step → update bobot
```

### 2.3 nn.Module — Membuat Neural Network

```python
import torch.nn as nn
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)   # layer 1: 784 → 256
        self.relu = nn.ReLU()             # aktivasi
        self.fc2 = nn.Linear(256, 128)    # layer 2: 256 → 128
        self.fc3 = nn.Linear(128, 10)      # layer 3: 128 → 10 (output)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

model = Net().to(device)
print(model)

# Xaviers initialization (otomatis)
for m in model.modules():
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        nn.init.zeros_(m.bias)
```

### 2.4 Training Loop

```python
criterion = nn.CrossEntropyLoss()   # untuk classification
criterion = nn.MSELoss()            # untuk regression
criterion = nn.BCEWithLogitsLoss()  # untuk binary classification

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 10
for epoch in range(epochs):
    model.train()  # mode training ( dropout aktif, batch norm update)

    running_loss = 0.0
    correct = 0
    total = 0

    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)

        # Forward pass
        optimizer.zero_grad()          # WAJIB: reset gradien dari batch sebelumnya
        outputs = model(data)
        loss = criterion(outputs, target)

        # Backward pass
        loss.backward()
        optimizer.step()

        # Statistics
        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += target.size(0)
        correct += predicted.eq(target).sum().item()

    acc = 100. * correct / total
    print(f"Epoch {epoch+1}: Loss={running_loss:.4f}, Acc={acc:.2f}%")

# Validation
model.eval()   # mode evaluation ( dropout off, batch norm gunakan statistik training )
with torch.no_grad():
    correct = 0
    total = 0
    for data, target in val_loader:
        data, target = data.to(device), target.to(device)
        outputs = model(data)
        _, predicted = outputs.max(1)
        total += target.size(0)
        correct += predicted.eq(target).sum().item()

print(f"Validation Accuracy: {100. * correct / total:.2f}%")
```

---

## 3. Data Loading — Dataset & DataLoader

### 3.1 torch.utils.data.Dataset

```python
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, X, y, transform=None):
        self.X = torch.FloatTensor(X)  # float32 untuk neural network
        self.y = torch.LongTensor(y)    # int64 untuk cross-entropy
        self.transform = transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x = self.X[idx]
        y = self.y[idx]

        if self.transform:
            x = self.transform(x)

        return x, y

dataset = CustomDataset(X_train, y_train)
dataloader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True,       # random urutan setiap epoch
    num_workers=2,       # parallel data loading
    pin_memory=True,     # GPU transfer lebih cepat
    drop_last=True      # drop batch terakhir jika tidak full
)

for batch_x, batch_y in dataloader:
    print(batch_x.shape)  # torch.Size([64, fitur])
```

### 3.2 torchvision untuk Computer Vision

```python
import torchvision.transforms as transforms
from torchvision import datasets

# Transformasi gambar → tensor + normalisasi
transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),    # augmentasi: crop acak
    transforms.RandomHorizontalFlip(),         # flip horizontal
    transforms.ToTensor(),                     # [0-255] → [0-1], HWC → CHW
    transforms.Normalize((0.5, 0.5, 0.5),     # normalisasi ke [-1, 1]
                    (0.5, 0.5, 0.5))
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Download & load dataset
train_data = datasets.CIFAR10(
    root="./data", train=True, download=True, transform=transform_train
)
test_data = datasets.CIFAR10(
    root="./data", train=False, download=True, transform=transform_test
)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True, num_workers=2)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False, num_workers=2)
```

---

## 4. Convolutional Neural Network (CNN)

### 4.1 Kenapa CNN untuk Gambar?

```
Fully Connected (FC) layer untuk gambar 224×224×3:
  Input = 224 × 224 × 3 = 150,528 neuron
  Jika layer pertama = 1000 neuron → 150,528 × 1000 = 150 JUTA bobot!

Convolutional layer:
  Filter kecil (3×3) → hanya 3×3×channels parameter per filter
  Shared weights → efisien luar biasa!
```

### 4.2 Conv2d — Cara Kerjanya

```python
import torch.nn.functional as F

# Conv2d(in_channels, out_channels, kernel_size, stride, padding)
conv = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)

# Input: batch × 3 × 32 × 32 (CIFAR-10)
# Output: batch × 32 × 32 × 32

# Batch Normalization — menstabilkan training
bn = nn.BatchNorm2d(32)

# Max Pool — turunkan dimensi
pool = nn.MaxPool2d(2, 2)  # 2×2 window, stride=2 → ukuran / 2

# Dropout — regularisasi
dropout = nn.Dropout2d(0.25)  # 25% neuron di-nonaktifkan saat training
```

### 4.3 CNN Architecture Pattern

```
Convolutional Block (ulang 2-3x):
  Conv2d → BatchNorm → ReLU → Conv2d → BatchNorm → ReLU → MaxPool

Classifier:
  Flatten → Dense → ReLU → Dropout → Dense → Output
```

```python
class CNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        # Block 1: 3→32 channel, 32×32 → 16×16
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        # Block 2: 32→64 channel, 16×16 → 8×8
        self.block2 = nn.Sequential(
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        # Classifier
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.classifier(x)
        return x
```

---

## 5. NLP — Pemrosesan Teks dengan Neural Network

### 5.1 Tokenisasi dan Vocabulary

```python
# Tokenisasi dasar (word-level)
def tokenize(text):
    return text.lower().split()

vocab = set()
for sentence in corpus:
    vocab.update(tokenize(sentence))

word2idx = {word: idx for idx, word in enumerate(vocab)}
idx2word = {idx: word for word, idx in word2idx.items()}

# Encode
encoded = [word2idx[word] for word in tokenize("halo dunia")]

# Padding (semua kalimat harus sama panjang)
from torch.nn.utils.rnn import pad_sequence
padded = pad_sequence([torch.tensor(seq) for seq in sequences], batch_first=True)
```

### 5.2 Embedding Layer

```python
# Embedding: mapping word → vector
# Training dari nol: belajar representasi dari data sendiri
embedding = nn.Embedding(num_embeddings=10000,   # ukuran vocabulary
                         embedding_dim=128)       # dimensi vector per kata

# Pre-trained embedding (Word2Vec, GloVe, FastText)
import gensim.downloader as api
word_vectors = api.load("glove-wiki-gigaword-100")

# Gunakan pre-trained weights
pretrained = torch.FloatTensor(word_vectors.vectors)
embedding = nn.Embedding.from_pretrained(pretrained, freeze=False)
# freeze=False → fine-tune saat training
# freeze=True → tetap pre-trained, tidak ikut update
```

### 5.3 RNN — Recurrent Neural Network

```python
# Vanilla RNN
rnn = nn.RNN(input_size=128, hidden_size=256, num_layers=2, batch_first=True)

# input: (batch, seq_len, input_size)
# output: (batch, seq_len, hidden_size) — setiap timestep
# hidden: (num_layers, batch, hidden_size) — final hidden state

# LSTM — Long Short-Term Memory (lebih baik dari RNN biasa)
lstm = nn.LSTM(input_size=128, hidden_size=256, num_layers=2,
               batch_first=True, dropout=0.3, bidirectional=True)

# Bidirectional: information dari masa lalu DAN masa depan
# output[0] → forward hidden state
# output[1] → backward hidden state

# Contoh forward pass
outputs, (hidden_state, cell_state) = lstm(input_tensor)
# outputs: semua timestep
# hidden_state: timestep terakhir (atau rata-rata jika bidirectional)
```

### 5.4 Attention Mechanism

Attention = neural network belajar **mana yang penting** di setiap langkah.

```python
class Attention(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn = nn.Linear(hidden_size * 2, 1)  # *2 karena bidirectional

    def forward(self, encoder_outputs):
        # encoder_outputs: (batch, seq_len, hidden_size*2)
        attn_weights = F.softmax(self.attn(encoder_outputs), dim=1)
        # attn_weights: (batch, seq_len, 1)
        context = torch.sum(attn_weights * encoder_outputs, dim=1)
        return context, attn_weights

attention = Attention(256)
context, weights = attention(encoder_outputs)
# context: weighted sum dari semua encoder output
```

---

## 6. Transfer Learning — Pakai Model yang Sudah Ada

### 6.1 Dua Strategi Transfer Learning

```
Strategi 1: Fine-tune seluruh model
  → Pretrained model → replace last layer → train semua layer
  → Untuk: dataset BESAR dan similar ke ImageNet

Strategi 2: Freeze + Train classifier saja
  → Pretrained model → extract features → train classifier baru
  → Untuk: dataset KECIL atau berbeda jauh dari ImageNet
```

### 6.2 torchvision pretrained models

```python
from torchvision import models

# ════ Strategi 2: Feature extraction (freeze) ════
model = models.resnet18(pretrained=True)

# Freeze semua layer
for param in model.parameters():
    param.requires_grad = False

# Ganti classifier terakhir
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)  # 10 kelas output

# Hanya classifier yang trainable
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)

# ════ Strategi 1: Fine-tune ════
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(num_features, 10)

# Semua layer trainable
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# Learning rate scheduler
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
```

### 6.3 Hugging Face Transformers

```python
from transformers import AutoTokenizer, AutoModel

# Load pretrained model + tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
bert = AutoModel.from_pretrained(model_name)

# Tokenisasi
text = "Deep learning is amazing"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Forward pass
outputs = bert(**inputs)
last_hidden_state = outputs.last_hidden_state  # semua token
pooled_output = outputs.pooler_output          # [CLS] token representation

# Fine-tune untuk classification
class BertClassifier(nn.Module):
    def __init__(self, model_name, num_classes):
        super().__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        self.classifier = nn.Linear(768, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled = outputs.pooler_output
        return self.classifier(pooled)
```

---

## 7. Regularisasi Deep Learning

```python
# 1. Dropout — nonaktifkan neuron secara acak saat training
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Dropout(0.3),    # 30% neuron di-nonaktifkan
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(128, 10)
)

# 2. Early stopping
from pytorch_lightning import LightningModule, Trainer

# 3. L2 regularization → weight_decay di optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)

# 4. BatchNorm → stabilisasi distribusi input per layer
bn = nn.BatchNorm1d(256)
bn(x)  # normalisasi output layer sebelumnya
```

---

## 8. GPU Training & Mixed Precision

```python
# Check GPU
print(f"GPU available: {torch.cuda.is_available()}")
print(f"GPU name: {torch.cuda.get_device_name(0)}")

# Move model & data ke GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Jika GPU memory terbatas → mixed precision
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in train_loader:
    data, target = data.to(device), target.to(device)

    optimizer.zero_grad()

    with autocast():   # float16 untuk forward pass, float32 untuk backward
        outputs = model(data)
        loss = criterion(outputs, target)

    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

---

## Ringkasan Pola Penulisan

| Topik | Pola Kunci |
|---|---|
| Tensor | `torch.tensor()`, `torch.zeros()`, `.to(device)` |
| Model | `nn.Module.__init__()` + `forward()` |
| Optimizer | `optim.Adam()`, `zero_grad()`, `step()`, `scheduler` |
| DataLoader | `DataLoader(dataset, batch_size, shuffle)` |
| CNN | `Conv2d → BatchNorm → ReLU → MaxPool` × N → FC |
| NLP | `Embedding → LSTM/GRU → Attention → FC` |
| Transfer | `models.resnet18(pretrained=True)`, freeze, replace FC |
| Training | `model.train()` → forward → `zero_grad()` → backward → `step()` |
| GPU | `device = torch.device("cuda")`, `.to(device)` |

---

`★ Insight ─────────────────────────────────────`
**1. Autograd di PyTorch**: `requires_grad=True` adalah toggle yang mengaktifkan tracking operasi. Saat `backward()` dipanggil, PyTorch menghitung gradien melalui computational graph. Ini bukan magic — PyTorch benar-benar tahu persis operasi apa yang dilakukan setiap tensor, jadi bisa hitung turunan secara simbolis/differensial.

**2. Transfer Learning intuition**: Model ImageNet sudah belajar 1000 kategori dengan 1.2 juta gambar. Filter konvolusional layer pertama belajar hal universal (edges, textures, colors) yang valid untuk hampir semua gambar. Freeze + train classifier = pakai fitur universal + belajar mapping ke kategori baru. Fine-tune = adaptasi filter generik ke domain spesifik.
`─────────────────────────────────────────────────`

---

**Lanjut:** Buka `05_deep_learning.ipynb` — bangun CNN untuk CIFAR-10, RNN untuk teks, dan transfer learning dengan pretrained model.