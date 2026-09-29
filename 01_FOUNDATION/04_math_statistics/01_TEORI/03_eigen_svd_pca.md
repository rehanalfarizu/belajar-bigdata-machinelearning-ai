# Lesson 3 — Eigen Concept, SVD, dan PCA

## Problem, context, why

Dataset memiliki banyak features yang saling berkorelasi. Kita ingin menemukan directions yang paling menjelaskan variasi tanpa hanya memilih columns asli.

## Intuisi visual dan mental model

Eigenvector adalah direction yang tidak berbelok di bawah transform tertentu—hanya diskalakan. SVD memecah matrix menjadi rotate→scale→rotate. PCA memilih directions variance terbesar pada data yang sudah dicenter.

```text
data cloud memanjang diagonal
        ↗ principal direction 1 (variance besar)
       ↖ direction 2 (variance kecil)
```

## Definition

`Av=λv` mendefinisikan eigenvector/value untuk square matrix. SVD `A=UΣVᵀ` berlaku lebih umum; singular values mengukur strength directions. PCA biasanya memakai eigen decomposition covariance atau SVD centered data. PCA tidak mengetahui target dan bukan bukti feature importance kausal.

## Small manual example

Points `(1,1),(2,2),(3,3)` setelah centering berada pada garis direction `[1,1]`; variance orthogonal hampir nol. Satu component mempertahankan struktur utama.

## Python experiment

Gunakan points kecil dan hitung centered coordinates serta projection ke unit vector `[1/√2,1/√2]`. Verifikasi reconstruction dan residual manual sebelum memakai library.

### Predict/run/observe/explain

Prediksi effect jika tidak centering atau feature kedua memiliki unit 1.000×. Observe bahwa scale mengubah direction.

## Workplace application

Compression, denoising, visualization, latent factors, conditioning diagnostics. PCA fit hanya pada training data dalam ML pipeline untuk mencegah leakage.

## Common failure dan debugging

Tidak centering/scaling, leakage, menafsirkan component sebagai causal factor, memilih components hanya karena plot, dan sign ambiguity dianggap bug. Laporkan explained variance bersama reconstruction/error/use case.

## Mini exercise/checkpoint

Jelaskan kapan PCA merusak signal low-variance tetapi penting. Lulus bila dapat membedakan eigen concept, SVD, dan PCA scope.

## Penutup

**KAMU BARU BELAJAR:** eigen/SVD mengurai transform; PCA mencari variance directions pada centered data.

**KENAPA INI PENTING:** structure berdimensi tinggi dapat diringkas tetapi informasi bisa hilang.

**DI DUNIA KERJA DIPAKAI UNTUK:** compression, visualization, denoising, dan diagnostics.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** setelah representation, kita memerlukan bahasa perubahan—function, slope, dan derivative.
