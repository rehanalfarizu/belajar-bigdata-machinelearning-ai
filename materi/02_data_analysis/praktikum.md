# Praktikum — Level 2: Data Analysis

> **Instruksi**: Ketik ulang setiap kode. Pahami kenapa NumPy lebih cepat, kenapa scaler harus di-fit di train saja, dan kenapa visualisasi itu penting untuk memahami data.
> **Waktu**: ~4–6 jam praktikum

---

## Latihan 1: NumPy — Array Fundamentals

**1.1.** Buat array 1D dari 0–20, hanya bilangan genap. Gunakan `np.arange(0, 21, 2)`. Cetak tipe data (`dtype`) dan shape-nya.

**1.2.** Given array `a = np.array([1, 2, 3, 4, 5])`:
- Ambil 3 elemen pertama: `a[:3]`
- Ambil elemen terakhir: `a[-1]`
- Ambil dari index 2 hingga 4: `a[2:5]`
- Reverse array: `a[::-1]`

**1.3.** Buat matriks 3×4 menggunakan `np.arange(12).reshape(3, 4)`. Cetak:
- Elemen baris ke-2, kolom ke-3: `matriks[1, 2]`
- Seluruh baris pertama: `matriks[0, :]`
- Seluruh kolom terakhir: `matriks[:, -1]`
- Submatriks baris 1–2, kolom 2–3: `matriks[1:3, 2:4]`

**1.4.** Challenge: buat matriks identitas 5×5 tanpa hardcode.
Hint: `np.eye(5)`

---

## Latihan 2: NumPy — Operasi Matematika

**2.1.** Dua array `a = np.array([1, 2, 3])` dan `b = np.array([4, 5, 6])`. Hitung:
- `a + b` (element-wise)
- `a - b`
- `a * b`
- `a / b`
- `a ** 2`

**2.2.** Buat array 50 angka random 0–100 (`np.random.randint(0, 101, 50)`). Hitung:
- `np.mean()`, `np.std()`, `np.median()`
- `np.max()`, `np.min()`, `np.sum()`
- `np.cumsum()` — kumulatif jumlah

**2.3.** Dot product: `v1 = [1, 2, 3]` dan `v2 = [4, 5, 6]`.
- Hitung manual dengan loop
- Bandingkan dengan `np.dot(v1, v2)`
- Verifikasi: 1×4 + 2×5 + 3×6 = ?

**2.4.** Broadcasting challenge:
```python
matriks = np.arange(1, 13).reshape(4, 3)  # 4×3 matriks
vec = np.array([10, 20, 30])              # 3 elemen
```
- Tambahkan vector per baris: `matriks + vec` (broadcasting)
- Kalikan scalar 5 ke seluruh matriks
- Normalisasi kolom: kurangi mean kolom dari setiap kolom
  Hint: `matriks - matriks.mean(axis=0)` (axis=0 = per kolom)

---

## Latihan 3: NumPy — Boolean Indexing

**3.1.** Dari `np.arange(1, 51)`:
- Elemen > 30
- Elemen antara 10–25 (inklusif)
- Elemen habis dibagi 7

**3.2.** Matriks random 5×5: `np.random.randint(0, 101, (5, 5))`:
- Temukan posisi (baris, kol) nilai terbesar: `np.unravel_index(mat.argmax(), mat.shape)`
- Semua posisi > 50: `np.where(mat > 50)`
- Ganti nilai < 25 jadi 0: `mat[mat < 25] = 0`

**3.3.** Given: `tinggi = np.array([170, 165, 180, 155, 175])`:
- Filter di atas rata-rata
- Filter di atas median
- Filter di atas 75th percentile: `np.percentile(tinggi, 75)`

---

## Latihan 4: Pandas — DataFrame Dasar

**4.1.** Buat DataFrame:
```python
data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
    'jurusan': ['IF', 'SI', 'IF', 'TK', 'IF'],
    'ipk': [3.2, 3.8, 3.5, 3.1, 3.9],
    'semester': [3, 5, 4, 2, 6]
}
df = pd.DataFrame(data)
```
Cek `shape`, `columns`, `dtypes`, `head()`.

**4.2.** Dari DataFrame di atas:
- Pilih kolom `'nama'` dan `'ipk'` saja
- Pilih baris 0 dan 3: `df.iloc[[0, 3]]`
- Pilih baris 1–3 dengan kolom `'nama'` dan `'jurusan'`: `df.loc[1:3, ['nama', 'jurusan']]`
- Filter IPK ≥ 3.5: `df[df['ipk'] >= 3.5]`
- Filter jurusan == 'IF' DAN semester > 3

---

## Latihan 5: Pandas — Statistik Deskriptif

**5.1.** `df = pd.DataFrame({'nilai': np.random.randint(40, 100, 50)})`.
Hitung manual count, mean, std, min, 25%, 50%, 75%, max. Bandingkan dengan `df.describe()`.

**5.2.** DataFrame dengan nama, nilai_uts, nilai_uas, ipk (10 data random).
- Cari student nilai_uts tertinggi
- Rata-rata IPK
- Student dengan IPK di atas mean

**5.3.** Korelasi: `df = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])`.
Hitung korelasi: `df.corr()`. Visualisasikan heatmap korelasinya.

---

## Latihan 6: Pandas — Manipulasi Data

**6.1.** Tambahkan kolom:
- `predikat`: ipk≥3.5 → 'Cum Laude', else → 'Memuaskan'
- `kategori_nilai`: derived dari nilai_uts

**6.2.** Sort DataFrame:
- IPK descending: `df.sort_values('ipk', ascending=False)`
- Semester ascending: `df.sort_values('semester', ascending=True)`

**6.3.** Rename kolom: `'nama'` → `'Nama'`, `'ipk'` → `'IPK'`.
Hint: `df.rename(columns={'nama': 'Nama', 'ipk': 'IPK'})`

---

## Latihan 7: Pandas — Group By

**7.1.** Group by `jurusan`:
- Rata-rata IPK: `df.groupby('jurusan')['ipk'].mean()`
- Jumlah mahasiswa: `df.groupby('jurusan').size()`
- IPK max & min

**7.2.** Group by `jurusan` DAN `semester`:
- Rata-rata nilai_uts
- Max nilai_uas
- Count

**7.3.** Pivot table: baris=jurusan, kolom=semester, nilai=rata-rata IPK.
Hint: `df.pivot_table(values='ipk', index='jurusan', columns='semester', aggfunc='mean')`

---

## Latihan 8: Pandas — Missing Values

**8.1.**
```python
df = pd.DataFrame({
    'nama': ['A', 'B', 'C', 'D'],
    'nilai': [80, None, 75, 90],
    'ipk': [3.5, 3.2, None, 3.8]
})
```
- Cek missing: `df.isnull().sum()`
- Isi `nilai` dengan mean: `df['nilai'].fillna(df['nilai'].mean())`
- Isi `ipk` dengan median

**8.2.** Drop semua baris dengan missing. Bandingkan jumlah baris sebelum dan sesudah.

---

## Latihan 9: Visualisasi — Matplotlib

**9.1.** Line chart: x=tahun 2015–2024, y=jumlah mahasiswa (random 1000–5000).
```python
import matplotlib.pyplot as plt

tahun = list(range(2015, 2025))
mahasiswa = np.random.randint(1000, 5001, 10)

plt.figure(figsize=(10, 6))
plt.plot(tahun, mahasiswa, marker='o', linestyle='--', color='steelblue', label='Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa 2015-2024', fontsize=14)
plt.xlabel('Tahun')
plt.ylabel('Jumlah')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

**9.2.** 4 subplot (2×2): line chart, bar chart, scatter plot, histogram.

**9.3.** Histogram 50 bins dari `np.random.randn(1000)`. Overlay kurva normal menggunakan `scipy.stats.norm.pdf`. Simpan ke PNG: `plt.savefig('histogram.png')`.

---

## Latihan 10: Visualisasi — Seaborn

**10.1.** Pair plot: buat DataFrame 4 kolom numerik, lalu `sns.pairplot(df)`.

**10.2.** Heatmap korelasi dengan `cmap='coolwarm'` dan anotasi.

**10.3.** Box plot distribusi nilai_uts per jurusan + violin plot overlay.

---

## Tantangan: Mini EDA Project

Gunakan dataset Iris dari sklearn:
```python
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
```

Lakukan:
1. Load → cek shape, columns, info, describe
2. Missing values → cek `df.isnull().sum()`
3. Statistik per species: `df.groupby('species').mean()`
4. Histogram setiap kolom numerik
5. Box plot setiap fitur, di-group per species
6. Scatter plot 2 fitur paling berkorelasi
7. Korelasi heatmap
8. Simpan cleaned dataset ke CSV
9. Cetak 5 insight utama yang kamu dapat dari EDA

---

## Tantangan Tambahan: Pandas + NumPy Gabungan

```python
np.random.seed(42)
df = pd.DataFrame({
    'tanggal': pd.date_range('2024-01-01', periods=100),
    'harga': np.random.randint(1000, 5000, 100),
    'volume': np.random.randint(100, 1000, 100)
})
```

- Rata-rata harga per minggu: `df.set_index('tanggal').resample('W')['harga'].mean()`
- Harga tertinggi & terendah per bulan
- Moving average 7 hari: `df['harga'].rolling(window=7).mean()`
- Volatilitas (std) harga per bulan
- Line chart: harga + moving average + volume (dual axis)
