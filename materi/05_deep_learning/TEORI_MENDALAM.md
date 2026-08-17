# Teori Mendalam — Level 05: Deep Learning

## 1. Representasi berlapis

Deep learning mempelajari representasi bertingkat. Layer awal image dapat mendeteksi tepi/tekstur; layer lebih dalam menggabungkannya menjadi bagian/objek. Ini berbeda dari feature engineering manual, tetapi bukan berarti data preprocessing/domain knowledge tidak perlu. Model tetap bergantung pada label, sampling, objective, dan distribusi data.

Neuron menghitung affine transformation `z = W*x + b`, lalu activation `a = f(z)`. Jika semua activation linear, banyak layer dapat digabung menjadi satu transformasi linear. ReLU menjaga gradient pada sisi positif; sigmoid/tanh dapat saturate sehingga gradient kecil; softmax menghasilkan distribusi multi-kelas dari logit. Pilih activation output dan loss bersama: sigmoid+BCE untuk binary, softmax+cross-entropy untuk multi-class tunggal, output linear+MSE/MAE untuk regression.

## 2. Backpropagation dan optimizer

Forward pass menyimpan intermediate activation, loss membandingkan prediksi dan target, lalu backpropagation menerapkan chain rule dari output menuju parameter awal. Gradient memberi sensitivitas loss terhadap setiap parameter, bukan “tingkat kepentingan fitur”. Mini-batch SGD menambah noise yang dapat membantu eksplorasi; momentum mengakumulasi arah update; Adam menyesuaikan skala update per parameter. Optimizer tidak memperbaiki label salah, leakage, atau validation split buruk.

Initialization yang terlalu kecil dapat menghilangkan signal, terlalu besar dapat membuat activation/gradient eksplosif. Batch normalization menormalkan activation batch dan menambah parameter scale/shift; dropout menonaktifkan sebagian unit ketika training sebagai regularisasi. Keduanya berbeda fungsi dan harus dievaluasi pada validation, bukan dipasang otomatis.

## 3. CNN dan inductive bias image

Convolution menggunakan filter lokal yang dibagi bobotnya di seluruh lokasi. Local connectivity dan translation equivariance adalah inductive bias: pola sama dapat muncul di mana saja. Padding menjaga ukuran spatial, stride menentukan lompatan filter, pooling/downsampling mengurangi resolusi dan biaya. Receptive field bertambah pada layer lebih dalam. CNN efisien untuk image karena menghormati struktur grid; pada data tabular kecil, inductive bias tree sering lebih cocok.

Augmentation menyatakan invariance yang diyakini valid: sedikit crop/flip/cahaya mungkin tetap mewakili kelas sama. Augmentation yang mengubah label adalah data corruption. Preprocessing, augmentation, dan normalisasi harus konsisten antara training dan inference sesuai desainnya.

## 4. Sequence, LSTM, dan Transformer

RNN membawa hidden state tetapi dapat mengalami vanishing/exploding gradient pada sequence panjang. LSTM/GRU memakai gate untuk mempertahankan/melupakan informasi. Mereka tetap sequential sehingga sulit diparalelkan. Transformer memakai self-attention untuk menghubungkan token jauh secara langsung, tetapi biaya attention standar tumbuh kuadrat terhadap panjang sequence. Untuk forecast, future leakage adalah risiko dominan: split, scaling, lag, dan feature calendar harus menghormati waktu.

## 5. Generalisasi, transfer learning, dan evaluasi

Train loss turun tidak menjamin generalisasi. Pantau train/validation curve, error per kelas, calibration, contoh salah, serta performa pada slice penting. Transfer learning memakai feature dari pretraining besar; freeze backbone untuk data sedikit, fine-tune perlahan dengan learning rate kecil. Dataset pretraining membawa bias dan batas domain. Simpan seed, augmentasi, split, hardware, library, checkpoint, dan config agar eksperimen bisa diulang.
