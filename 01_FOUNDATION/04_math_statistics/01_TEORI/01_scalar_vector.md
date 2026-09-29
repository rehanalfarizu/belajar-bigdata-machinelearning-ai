# Lesson 1 — Scalar dan Vector

## Problem, context, why

Satu sensor memberi suhu 27°C—satu quantity. Satu asset memberi suhu, getaran, dan tekanan—beberapa quantities yang harus diperlakukan bersama.

## Intuisi visual dan mental model

Scalar adalah satu posisi pada garis angka. Vector adalah panah/daftar terurut dengan magnitude dan direction dalam ruang fitur.

```text
scalar:  27
vector: [temperature, vibration, pressure] = [27, 3, 10]
         └──────────── shape (3,)
```

## Definition

Scalar adalah satu bilangan. Vector `x = [x₁,...,xₙ]` adalah ordered components pada coordinate system/basis. Urutan dan unit adalah bagian makna; `[27,3]` tidak bermakna tanpa feature contract.

## Small manual calculation

Untuk `a=[1,2]` dan `b=[3,-1]`:

- addition: `a+b=[4,1]`;
- scalar multiplication: `2a=[2,4]`;
- displacement dari a ke b: `b-a=[2,-3]`.

## Python experiment

```python
a = [1, 2]
b = [3, -1]
result = [x + y for x, y in zip(a, b)]
print(result)
```

### Predict → run → observe → explain

Prediksi result dan apa yang terjadi bila lengths berbeda. Observe bahwa `zip` diam-diam berhenti pada input terpendek; validation shape diperlukan.

## Workplace application

Feature vectors, coordinates, embeddings, sensor state, dan model parameters. Standardization/unit handling dibutuhkan sebelum membandingkan dimensions berbeda.

## Common failure dan debugging

Shape mismatch, feature order berubah, units tercampur, list concatenation dianggap addition, dan magnitude didominasi scale besar. Tulis shape/feature names/units sebelum operasi.

## Mini exercise/checkpoint

Representasikan tiga assets sebagai vectors dengan schema eksplisit; jelaskan mengapa menukar component positions merusak meaning.

## Penutup

**KAMU BARU BELAJAR:** scalar satu quantity; vector ordered quantities pada basis/schema.

**KENAPA INI PENTING:** data multifeature memerlukan representation konsisten.

**DI DUNIA KERJA DIPAKAI UNTUK:** features, state, coordinates, parameters, embeddings.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** banyak vectors disusun menjadi matrix dan ditransformasi.
