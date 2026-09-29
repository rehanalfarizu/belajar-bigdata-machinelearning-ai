# Tutorial Penyelesaian — Level 02 Data Analysis

## Urutan EDA yang benar

Setelah memuat data, jangan langsung membuat model atau grafik. Jawab urutannya: berapa baris/kolom, apa tipe kolom, berapa missing/duplicate, apa rentang nilai, dan apa grain satu baris.

```python
df = pd.read_csv("data.csv")
print(df.shape)
display(df.head())
df.info()
print(df.isna().sum())
print(df.duplicated().sum())
```

Jika `info()` menunjukkan angka sebagai `object`, jangan memaksa agregasi; bersihkan/cast dahulu dan catat alasan bisnisnya.

## Filtering dan groupby

Tulis boolean condition secara terpisah supaya mudah diperiksa. Setelah `groupby`, cek apakah agregasi menjawab pertanyaan dan apakah denominator diperlukan.

```python
aktif = (df["status"] == "aktif") & (df["ipk"] >= 3.5)
hasil = df.loc[aktif, ["nama", "jurusan", "ipk"]]
rata = df.groupby("jurusan", as_index=False).agg(rata_ipk=("ipk", "mean"))
```

Kesalahan umum: memakai `and` alih-alih `&`, lupa tanda kurung, atau menganggap `count()` menghitung missing value. Gunakan `size()` untuk jumlah baris dan `count()` untuk nilai non-null.

## Visualisasi dan insight

Satu grafik harus menjawab satu pertanyaan. Beri judul yang menjelaskan temuan, label sumbu dan satuan. Setelah plot, tulis insight berbasis bukti, bukan “grafiknya bagus”. Contoh: “Median IPK jurusan A lebih tinggi 0,18, tetapi distribusinya overlap besar.”

## Mini EDA project

Selesaikan dengan deliverable: data dictionary, cleaning log, tiga grafik, lima insight, dan dua pertanyaan lanjutan. Simpan data asli tanpa perubahan dan tulis data bersih ke file baru.
