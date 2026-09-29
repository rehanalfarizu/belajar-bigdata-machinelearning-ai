# Teori dan Solusi Lengkap — Level 02 Data Analysis

## 1. NumPy: vectorization dan broadcasting

NumPy menyimpan array homogen dan menjalankan operasi dalam kode teroptimasi. `nilai + 5` menambah semua elemen tanpa loop Python. Broadcasting memperluas dimensi berukuran 1 agar operasi shape kompatibel. Ia kuat, tetapi salah shape dapat menghasilkan jawaban salah tanpa error.

```python
nilai = np.array([[70, 80, 90], [60, 75, 85]])
bobot = np.array([0.2, 0.3, 0.5])
nilai_akhir = nilai @ bobot
assert np.allclose(nilai_akhir, [83, 77.5])
```

`nilai.mean(axis=0)` berarti rata-rata ke bawah per kolom; `axis=1` berarti rata-rata ke samping per baris. Selalu tulis bentuk hasil yang diharapkan sebelum memilih axis.

## 2. Pandas: solusi cleaning yang dapat diaudit

```python
df = df.copy()
df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
df["pendapatan"] = pd.to_numeric(df["pendapatan"], errors="coerce")
df = df.drop_duplicates(subset=["id_transaksi"])
invalid = df["pendapatan"].lt(0) | df["tanggal"].isna()
data_bersih = df.loc[~invalid].copy()
```

Jangan langsung `dropna()` untuk semua kolom. Tentukan apakah missing berarti tidak diketahui, tidak berlaku, atau kesalahan ingest. Simpan jumlah baris sebelum/sesudah setiap aturan agar cleaning dapat dipertanggungjawabkan.

## 3. Groupby: solusi pertanyaan bisnis

Pertanyaan “jurusan mana memiliki IPK rata-rata tertinggi?” membutuhkan groupby dan mean, bukan sorting seluruh data.

```python
ringkasan = (data_bersih.groupby("jurusan", as_index=False)
             .agg(jumlah_mahasiswa=("nama", "size"), rata_ipk=("ipk", "mean"))
             .sort_values("rata_ipk", ascending=False))
```

`size` menghitung seluruh baris; `count` hanya nilai yang tidak missing. Pilih yang sesuai denominator yang ingin kamu laporkan.

## 4. Visualisasi: jawaban harus berupa insight

Histogram menjawab bentuk distribusi, boxplot membandingkan distribusi kelompok, scatterplot mengecek hubungan dua numerik, dan line chart mengecek perubahan waktu. Korelasi tinggi pada scatterplot tidak berarti salah satu variabel menyebabkan yang lain.

Solusi mini EDA harus menyertakan data dictionary, cleaning log, tiga grafik, lima insight berbukti, dan pertanyaan lanjutan. “Ada korelasi 0,7” belum insight sebelum unit, outlier, dan konteks diperiksa.
