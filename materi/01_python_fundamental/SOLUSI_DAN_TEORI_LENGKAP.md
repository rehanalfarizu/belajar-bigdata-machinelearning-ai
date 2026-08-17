# Teori dan Solusi Lengkap — Level 01 Python

## 1. Model mental Python

Variabel adalah nama yang merujuk ke object, bukan kotak yang menyimpan nilai. `a = [1, 2]` dan `b = a` membuat dua nama menunjuk list yang sama. Perubahan melalui `b` terlihat melalui `a`. Integer dan string immutable; list, dictionary, dan set mutable. Ini menjelaskan banyak bug pemula.

```python
a = [1, 2]
b = a
b.append(3)
assert a == [1, 2, 3]

c = a.copy()
c.append(4)
assert a == [1, 2, 3]
assert c == [1, 2, 3, 4]
```

## 2. Solusi pola input–proses–output

Untuk setiap praktikum, pecah masalah menjadi input, validasi, proses, lalu output. Contoh program nilai:

```python
def hitung_status(nilai_teori: float, nilai_praktik: float) -> str:
    rata_rata = (nilai_teori + nilai_praktik) / 2
    if rata_rata >= 75:
        return f"Lulus, rata-rata {rata_rata:.1f}"
    return f"Belum lulus, rata-rata {rata_rata:.1f}"

assert hitung_status(80, 70) == "Lulus, rata-rata 75.0"
assert hitung_status(60, 70) == "Belum lulus, rata-rata 65.0"
```

`return` mengembalikan nilai dan menghentikan function. `print` hanya menampilkan nilai. Function yang hanya `print` sulit diuji dan dipakai ulang.

## 3. List, dict, dan loop

List dipakai untuk urutan; dict dipakai saat nilai diakses melalui nama key. Jangan mengubah list saat sedang diiterasi, karena indeks dapat bergeser. Buat list hasil baru atau iterasi salinannya.

```python
mahasiswa = [
    {"nama": "Ani", "nilai": 80},
    {"nama": "Budi", "nilai": 65},
    {"nama": "Cici", "nilai": 90},
]
lulus = [m["nama"] for m in mahasiswa if m["nilai"] >= 75]
assert lulus == ["Ani", "Cici"]
```

List comprehension adalah sintaks ringkas untuk loop yang menghasilkan list. Bila logika memiliki banyak cabang atau side effect, gunakan loop biasa agar lebih mudah dibaca.

## 4. Error handling: solusi input umur

```python
def baca_umur(teks: str) -> int:
    try:
        umur = int(teks)
    except ValueError as exc:
        raise ValueError("Umur harus berupa bilangan bulat") from exc
    if umur < 0 or umur > 130:
        raise ValueError("Umur harus berada antara 0 dan 130")
    return umur

assert baca_umur("20") == 20
```

Tangkap exception yang spesifik. `except Exception: pass` menyembunyikan bug sehingga program terlihat jalan tetapi menghasilkan data salah.

## 5. Mini proyek: ringkasan pengeluaran

Simpan transaksi sebagai list dict, validasi nominal positif, hitung total per kategori, lalu tampilkan kategori terbesar. Tambahkan test untuk list kosong, nominal nol, dan kategori baru. Inilah transisi dari latihan sintaks ke program yang dapat dipercaya.
