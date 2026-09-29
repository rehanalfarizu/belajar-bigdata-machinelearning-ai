# Lesson 2 — Matrix, Dot Product, Norm, dan Transformation

## Problem, context, why

Kita ingin menghitung weighted score dari features dan menerapkan operasi sama ke banyak rows. Matrix membuat transform linear terlihat dan dapat dihitung efisien.

## Intuisi visual dan mental model

Matrix dapat dilihat sebagai table data atau mesin transformasi yang memutar, meregangkan, mencampur, atau memproyeksikan vector.

```text
x (input vector) → A @ x → y (transformed vector)

[2 0] [3] = [6]
[0 1] [4]   [4]
```

## Definition

Matrix mempunyai shape rows×columns. Dot product `a·b = Σ aᵢbᵢ` mengukur weighted alignment. Norm L2 `||x||₂ = sqrt(Σxᵢ²)` mengukur magnitude. Matrix-vector multiplication valid bila inner dimensions cocok.

## Small manual calculation

Untuk `a=[1,2]`, `b=[3,4]`: dot = `1×3+2×4=11`; norm a = `√5`. Matrix `[[2,0],[0,1]]` mengubah `[3,4]` menjadi `[6,4]`.

## Python experiment

```python
import math

a = [1, 2]
b = [3, 4]
dot = sum(x * y for x, y in zip(a, b))
norm = math.sqrt(sum(x * x for x in a))
print(dot, norm)
```

### Predict/run/observe/explain

Prediksi dot vectors tegak lurus `[1,0]` dan `[0,5]`. Visualisasikan sebagai arrows di grid manual.

## Workplace application

Linear models, similarity, projection, transformations, graphics, PCA, dan state transition. Dot product tinggi bisa berasal dari magnitude, bukan hanya direction—cosine normalization menjawab pertanyaan berbeda.

## Common failure dan debugging

Shape mismatch, transpose salah, row/column ambiguity, scale/unit dominance, dan menganggap matrix multiplication elementwise. Tulis shapes di setiap panah.

## Mini exercise/checkpoint

Hitung manual matrix 2×2 pada tiga vectors dan jelaskan geometric effect. Lulus bila dapat memprediksi output shape.

## Penutup

**KAMU BARU BELAJAR:** matrix mentransformasi vectors; dot dan norm mengukur interaction/magnitude.

**KENAPA INI PENTING:** banyak model adalah composition transformasi.

**DI DUNIA KERJA DIPAKAI UNTUK:** linear models, similarity, coordinates, dan dimensionality reduction.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** eigen/SVD/PCA mengungkap arah struktur penting dalam transformation/data.
