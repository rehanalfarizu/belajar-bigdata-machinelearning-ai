# Panduan Kode — Chapter 02: NumPy & Pandas

> Cheat sheet idiom + anti-pattern untuk chapter 2. Bukan duplikat notebook — buka ini saat kamu butuh mengingat kapan pakai A vs B, atau apa jebakan umum yang harus dihindari.

---

## 1. NumPy: Idiom Penting

### 1.1 Vectorization — Operasi Tanpa Loop

**Kenapa ini ada:** NumPy menjalankan operasi di kode C, bukan di Python interpreter. Untuk data besar, loop Python 50–100x lebih lambat dari operasi NumPy element-wise.

```python
# JANGAN — loop Python untuk operasi numerik
hasil = []
for x in data:
    hasil.append(x * 2 + 1)

# LAKUKAN — biarkan NumPy yang loop
hasil = np.array(data) * 2 + 1
```

**Kapan hindari:** kalau logikanya benar-benar conditional dan sulit di-vectorize (misalnya butuh `if x > 0` yang berbeda untuk tiap elemen), `np.where` atau list comprehension kadang lebih jelas.

### 1.2 `np.where` — Conditional Element-wise

```python
# Klasifikasi nilai
nilai = np.array([60, 75, 80, 55, 90])
kategori = np.where(nilai >= 75, 'Lulus', 'Tidak Lulus')
# array(['Tidak Lulus', 'Lulus', 'Lulus', 'Tidak Lulus', 'Lulus'], dtype='<U11')
```

**Kapan hindari:** kalau kondisinya cuma dua (true/false), boolean indexing kadang lebih langsung: `nilai[nilai >= 75]`.

### 1.3 `axis` — Arah Operasi

**Aturan:** `axis=0` artinya operasi dilakukan per kolom (bergerak ke bawah). `axis=1` artinya per baris (bergerak ke samping).

```python
mat = np.arange(12).reshape(4, 3)
mat.sum(axis=0)   # array([18, 22, 26]) — jumlah per kolom
mat.sum(axis=1)   # array([3, 12, 21, 30]) — jumlah per baris
```

**Cara mengingat:** `axis=0` adalah "collapse row 0", jadi hasilnya punya shape seperti row. `axis=1` adalah "collapse column 1", hasilnya punya shape seperti kolom.

---

## 2. Pandas: Memilih Data

### 2.1 Empat Sistem Selecting

| Situasi | Pakai | Contoh |
|---|---|---|
| Satu kolom | `df['kolom']` (Series) | `df['nama']` |
| Banyak kolom | `df[['a', 'b']]` (DataFrame) | `df[['nama', 'ipk']]` |
| Baris by posisi | `df.iloc[0:3]` | `df.iloc[0]` |
| Baris by label | `df.loc['Andi']` | `df.loc[0:2, ['nama']]` |
| Filter kondisi | `df[df['ipk'] > 3.5]` | `df[(df['jurusan']=='IF') & (df['semester']>=5)]` |

**Jebakan umum:**
- `df['kolom']` → Series, bukan DataFrame. Kalau mau DataFrame, pakai `df[['kolom']]`.
- `df[0:3]` slicing tanpa `.iloc`/`.loc` → ambigu, lebih baik pakai `df.iloc[0:3]`.
- `df.loc[0:3]` → slicing INklusif di akhir (ambil 0, 1, 2, 3). `df.iloc[0:3]` → eksklusif di akhir (0, 1, 2).

### 2.2 Boolean Indexing — Filter dengan Kondisi

```python
# Tunggal
df[df['ipk'] > 3.5]

# AND
df[(df['ipk'] > 3.5) & (df['jurusan'] == 'IF')]

# OR
df[(df['jurusan'] == 'IF') | (df['jurusan'] == 'SI')]

# NOT
df[~(df['ipk'] > 3.5)]   # IPK <= 3.5
```

**Aturan wajib:** setiap kondisi **wajib** di dalam kurung. `&` dan `|` (bukan `and`/`or`).

### 2.3 `df.query()` — Boolean Indexing Versi SQL

```python
# Boolean indexing klasik
df[(df['ipk'] >= 3.5) & (df['jurusan'] == 'IF')]

# Query — lebih mudah dibaca untuk kondisi kompleks
df.query("ipk >= 3.5 and jurusan == 'IF'")
df.query("ipk >= 3.5 and jurusan in ['IF', 'SI']")
```

**Kapan pakai:** kalau kondisi kamu panjang dan melibatkan banyak kolom, `query` lebih bersih. Kalau cuma satu kondisi, boolean indexing biasa sudah cukup.

### 2.4 `df.loc[kondisi, kolom]` — Filter + Pilih Sekaligus

```python
# Filter baris + pilih kolom
df.loc[df['ipk'] > 3.5, ['nama', 'jurusan']]

# Pilih semua baris, kolom tertentu
df.loc[:, ['nama', 'ipk']]

# Pilih baris by label index
df.set_index('nama').loc['Andi':'Citra', 'ipk']
```

---

## 3. Pandas: Transformasi

### 3.1 Tambah Kolom Baru

```python
# Dari kolom yang ada
df['nilai_akhir'] = (df['uts'] + df['uas']) / 2

# Konstanta
df['lulus'] = True

# Hasil apply fungsi
df['predikat'] = df['ipk'].apply(lambda x: 'Cum Laude' if x >= 3.7 else 'Memuaskan')

# np.where untuk dua kategori
import numpy as np
df['kategori'] = np.where(df['ipk'] >= 3.5, 'Tinggi', 'Rendah')
```

**Kapan hindari `apply`:** kalau operasinya sederhana, vectorize lebih cepat: `df['ipk'] * 4` vs `df['ipk'].apply(lambda x: x*4)`. Apply cocok untuk logika kompleks yang tidak bisa di-vectorize.

### 3.2 `inplace=True` — Modiﬁkasi Langsung atau Return Baru?

```python
# Tanpa inplace — return DataFrame baru, df asli tidak berubah
df_new = df.dropna()
df_new = df.rename(columns={'nama': 'Nama'})

# Dengan inplace — modifikasi df langsung
df.dropna(inplace=True)
df.rename(columns={'nama': 'Nama'}, inplace=True)
```

**Jebakan:** `inplace=True` itu **bukan** optimasi — dia menghapus referensi ke objek lama dan assign objek baru ke variabel yang sama. Hasilnya: `df` lama tidak bisa diakses lagi. Mulai sekarang, **hindari `inplace=True`** — lebih mudah di-debug kalau kamu pakai `df = df.dropna()`. Versi terbaru Pandas (3.x) akan deprecate `inplace`.

### 3.3 `df.append()` — Sudah Deprecated

```python
# JANGAN — sudah deprecated
df = df.append({'nama': 'Budi', 'ipk': 3.5}, ignore_index=True)

# LAKUKAN — pakai concat
df = pd.concat([df, pd.DataFrame([{'nama': 'Budi', 'ipk': 3.5}])], ignore_index=True)
```

### 3.4 Sorting

```python
# Satu kolom
df.sort_values('ipk', ascending=False)

# Multi-kolom dengan arah berbeda
df.sort_values(['jurusan', 'ipk'], ascending=[True, False])
# jurusan ascending (A→Z), ipk descending (tinggi→rendah)
```

---

## 4. Pandas: Group By dan Agregasi

### 4.1 Tiga Bentuk Group By

```python
# 1. Tunggal dengan satu fungsi
df.groupby('jurusan')['ipk'].mean()

# 2. Tunggal dengan banyak fungsi
df.groupby('jurusan')['ipk'].agg(['mean', 'min', 'max'])

# 3. Multi-kolom dengan dictionary
df.groupby('jurusan').agg({
    'ipk'      : ['mean', 'max', 'count'],
    'nilai_uts': 'mean',
    'nilai_uas': ['mean', 'std']
})
```

**Output bentuk 3** punya MultiIndex di kolom — agak ribet di awal, tapi sangat powerful untuk analisis multi-dimensi.

### 4.2 `as_index=False` — Hasil sebagai Default Index

```python
# Default — index adalah nilai jurusan
df.groupby('jurusan')['ipk'].mean()
# jurusan
# IF    3.75
# SI    3.55

# Dengan as_index=False — hasilnya DataFrame dengan index 0, 1, 2
df.groupby('jurusan', as_index=False)['ipk'].mean()
#   jurusan    ipk
# 0       IF  3.75
# 1       SI  3.55
```

**Kapan pakai:** kalau kamu mau hasil `groupby` di-merge atau di-filter lagi, `as_index=False` lebih mudah.

### 4.3 Pivot Table — Group By 2D

```python
# Baris = jurusan, kolom = semester, nilai = mean IPK
df.pivot_table(values='ipk', index='jurusan', columns='semester', aggfunc='mean')
```

**Kapan ganti ke `pivot_table`:** kalau kamu mau output yang langsung berbentuk matrix 2D (baris × kolom), `pivot_table` lebih cocok dari `groupby().unstack()`.

---

## 5. Pandas: Missing Values

### 5.1 `dropna` — Hapus Missing

```python
df.dropna()                  # hapus baris dengan missing value
df.dropna(axis=1)            # hapus kolom dengan missing value
df.dropna(thresh=3)          # baris yang punya < 3 non-null dihapus
df.dropna(subset=['ipk'])    # hanya cek kolom 'ipk'
```

### 5.2 `fillna` — Isi Missing

```python
df['ipk'].fillna(0)                        # dengan skalar
df['ipk'].fillna(df['ipk'].mean())         # dengan mean kolom
df['ipk'].fillna(method='ffill')          # forward fill (dari baris sebelumnya)
df['ipk'].fillna(method='bfill')          # backward fill
df.fillna({'ipk': 0, 'jurusan': 'Unknown'})  # per kolom
```

**Kapan hindari `fillna(0)`:** untuk kolom seperti IPK, gaji, atau data yang **tidak mungkin** bernilai 0, mengisinya dengan 0 akan mendistorsi analisis. Pilih mean/median/forward fill sesuai konteks.

---

## 6. Pandas: Merge dan Concat

### 6.1 `pd.merge` — SQL JOIN

```python
# Inner join (hanya match di kedua tabel)
pd.merge(df1, df2, on='key', how='inner')

# Left join (semua baris df1, NaN untuk yang tidak match)
pd.merge(df1, df2, on='key', how='left')

# Multi-key
pd.merge(df1, df2, on=['key1', 'key2'], how='inner')

# Key berbeda nama
pd.merge(df1, df2, left_on='id_left', right_on='id_right', how='left')
```

### 6.2 `pd.concat` — Stack Vertikal/Horizontal

```python
# Vertikal (tambah baris) — sumbu default 0
pd.concat([df1, df2], ignore_index=True)

# Horizontal (tambah kolom) — sumbu 1
pd.concat([df1, df2], axis=1)
```

**Bedanya dengan `merge`:** `concat` cuma tempel, tidak ada logika pencocokan key. `merge` melakukan JOIN dengan key.

---

## 7. Matplotlib: Idiom Penting

### 7.1 OO Style vs pyplot Style

```python
# pyplot style (stateful, lebih simpel untuk plot cepat)
plt.plot(x, y)
plt.title('Plot')
plt.show()

# OO style (lebih eksplisit, recommended untuk subplot)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Plot')
plt.show()
```

**Kapan pakai OO:** kalau kamu punya subplot atau mau kontrol presisi tiap elemen. Untuk plot cepat, pyplot cukup.

### 7.2 Subplots Layout

```python
# Grid 2x2
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data)

# Flat akses
axes[0, 0]   # baris 0, kolom 0
axes[0, 1]   # baris 0, kolom 1
axes[1, 0]   # baris 1, kolom 0
axes[1, 1]   # baris 1, kolom 1

# Flatten kalau kamu mau loop
axes = axes.flatten()
for ax in axes:
    ax.plot(x, y)
```

### 7.3 `plt.tight_layout()` — Anti-Overlap

Selalu panggil sebelum `plt.show()` atau `plt.savefig()`. Fungsi ini menyesuaikan spasi antar subplot dan elemen plot agar tidak saling tumpang tindih.

```python
fig, axes = plt.subplots(2, 2)
# ... plotting ...
plt.tight_layout()
plt.show()
```

---

## 8. SQL ↔ Pandas Reference

Paling sering ditanyakan pemula yang sudah kenal SQL.

| SQL | Pandas |
|---|---|
| `SELECT *` | `df` |
| `SELECT a, b` | `df[['a', 'b']]` |
| `WHERE a > 5` | `df[df['a'] > 5]` |
| `AND`/`OR` | `&` / `\|` |
| `GROUP BY a` | `df.groupby('a')` |
| `ORDER BY a DESC` | `df.sort_values('a', ascending=False)` |
| `LIMIT 10` | `df.head(10)` |
| `DISTINCT` | `df['a'].unique()` |
| `COUNT(*)` | `len(df)` |
| `AVG(a)` | `df['a'].mean()` |
| `SUM(a)` | `df['a'].sum()` |
| `INNER JOIN` | `pd.merge(df1, df2, on='k', how='inner')` |
| `LEFT JOIN` | `how='left'` |
| `GROUP BY ... HAVING` | `df.groupby('a').filter(lambda x: x['b'].mean() > 5)` |

---

## 9. Anti-Pattern yang Harus Dihindari

### Loop untuk Hal yang Bisa Di-vectorize

```python
# JANGAN
hasil = []
for i in range(len(df)):
    if df.iloc[i]['ipk'] > 3.5:
        hasil.append(df.iloc[i]['nama'])

# LAKUKAN
hasil = df.loc[df['ipk'] > 3.5, 'nama'].tolist()
```

### `inplace=True` Berlebihan

```python
# JANGAN — `inplace` deprecated di Pandas 3.x
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# LAKUKAN — reassign lebih jelas
df = df.dropna()
df = df.reset_index(drop=True)
```

### `df.append()` (Deprecated)

```python
# JANGAN
df = df.append(row, ignore_index=True)

# LAKUKAN
df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
```

### `df[0]` atau `df[0:3]` Tanpa `.iloc`

```python
# JANGAN — ambigu, bisa berubah makna di versi Pandas mendatang
df[0:3]

# LAKUKAN
df.iloc[0:3]
```

### `df.sort()` (Deprecated — ganti `sort_values`)

```python
# JANGAN
df.sort('ipk')

# LAKUKAN
df.sort_values('ipk')
```

### Lupa `inplace=False` (Default) → DataFrame Tidak Berubah

```python
# JANGAN — banyak pemula mengira ini sudah cukup
df.dropna()

# LAKUKAN
df = df.dropna()
# atau
df.dropna(inplace=True)
```

### Menggabungkan `.apply` untuk Hal Sederhana

```python
# JANGAN
df['ipk_x2'] = df['ipk'].apply(lambda x: x * 2)

# LAKUKAN
df['ipk_x2'] = df['ipk'] * 2
```

---

## 10. Ringkasan Pola Satu Baris

| Tujuan | Pola |
|---|---|
| Filter + pilih kolom | `df.loc[kondisi, [kolom]]` |
| Agregat per grup | `df.groupby(kolom)[target].agg(['mean', 'std'])` |
| Hitung missing | `df.isnull().sum()` |
| Cek tipe data | `df.dtypes` atau `df.info()` |
| Korelasi | `df[numerik_cols].corr()` |
| Baca CSV | `pd.read_csv('file.csv')` |
| Tulis CSV | `df.to_csv('file.csv', index=False)` |
| Plot 1 variabel | `df['x'].hist()` atau `plt.hist(df['x'])` |
| Save figure | `plt.savefig('plot.png', dpi=150, bbox_inches='tight')` |
| Konfirmasi perubahan | `print(df.shape)` atau `df.head()` |

---

**Lanjut:** Buka `praktikum.ipynb` untuk latihan, atau `typing_practice.ipynb` untuk uji memori otot.
