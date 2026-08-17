# Panduan Penulisan Kode — Level 1: Python Fundamental

> File ini menjelaskan pola penulisan kode yang benar untuk Level 1.
> Dibaca bersamaan dengan `01_python_fundamental.ipynb` — jalankan cell, baca panduan ini, lalu pahami kenapa penulisannya seperti itu.

---

## 1. Cara Kerja Dasar Python

### 1.1 Interpreter Membaca Baris-demi-Baris

Python itu seperti membaca buku — dari atas ke bawah, kiri ke kanan. Interpreter tidak menyusun program terlebih dahulu (tidak ada tahap "compile"), tapi langsung jalan sambil baca.

```python
# Baris 1: Interpreter lihat "x = 10"
#           → Python membuat objek integer bernilai 10
#           → Menempelkan label "x" ke objek itu

# Baris 2: Interpreter lihat "y = x + 5"
#           → Cek nilai x → 10
#           → Hitung 10 + 5 → 15
#           → Simpan 15 dengan label "y"

# Baris 3: Interpreter lihat "print(x + y)"
#           → x = 10, y = 15
#           → 10 + 15 = 25
#           → Cetak: 25

x = 10
y = x + 5
print(x + y)   # Output: 25
```

**Kesimpulan:** Urutan baris MATTER. Kalau kamu tulis `print(x)` di atas `x = 10`, akan error karena `x` belum ada.

### 1.2 Semua adalah Objek

Di Python, **tidak ada yang namanya "variabel primitif"** seperti di C/Java. Semua adalah objek.

```python
nama = "Rehan"
```

Artinya:
```
"Rehan" → adalah sebuah objek string
nama    → adalah sebuah label (reference/pointer) yang menunjuk ke objek itu
```

Buktinya, kamu bisa cek tipe datanya:

```python
nama = "Rehan"
print(type(nama))   # → <class 'str'>
```

Kalau `nama` adalah variabel primitif (seperti di C), `type()` tidak masuk akal. Tapi karena `nama` adalah label yang menunjuk ke objek string, Python bisa cek: "label ini menunjuk ke objek bertipe apa?"

### 1.3 Immutable vs Mutable — Konsep Penting

Ini bagian yang sering bikin bingung:

| Tipe | Sifat | Penjelasan |
|---|---|---|
| `int`, `float`, `str`, `bool`, `tuple` | **Immutable** | Tidak bisa diubah setelah dibuat |
| `list`, `dict`, `set` | **Mutable** | Bisa diubah setelah dibuat |

**Immutable — tidak bisa diubah:**

```python
nama = "Rehan"
nama[0] = "r"   # ← TypeError! String tidak bisa diubah

# Yang terjadi: "Rehan" tidak berubah
# Tapi "r" + "ehan" membuat objek BARU → nama menunjuk ke objek baru
nama = "rehan"   # ← Ini LEGAL, tapi bukan mengubah, tapi MENGGANTI
```

**Mutable — bisa diubah:**

```python
buah = ["apel", "mangga", "jeruk"]
buah[0] = "anggur"     # ← LEGAL! List memang bisa diubah
print(buah)            # → ['anggur', 'mangga', 'jeruk']
```

**Kenapa ini penting?**

```python
# Immutable: efeknya tidak terduga bagi pemula
x = 10
y = x     # y menunjuk ke objek yang SAMA dengan x
x = x + 5  # x sekarang menunjuk objek BARU (15), y tetap menunjuk 10

print(f"x = {x}, y = {y}")   # → x = 15, y = 10 (bukan keduanya 15!)

# Mutable: efeknya juga tidak terduga
a = [1, 2, 3]
b = a          # b menunjuk ke objek yang SAMA dengan a
b.append(4)     # Ubah objeknya → a juga ikut berubah!

print(f"a = {a}, b = {b}")   # → a = [1, 2, 3, 4], b = [1, 2, 3, 4] (keduanya sama!)
```

---

## 2. Variabel dan Tipe Data

### 2.1 Variabel itu Label, Bukan Kotak Penyimpanan

**Gaya berpikir yang SALAH:**
```
Bayangkan variabel seperti KOTAK:
┌─────────┐
│ nama    │ ← kotak bernama "nama"
└─────────┘
"Rehan" ← disimpan di dalam kotak
```

**Gaya berpikir yang BENAR:**
```
Bayangkan variabel seperti STIKER:
"Rehan" ──────────────────╗
         ← stiker "nama" ──╝ menunjuk ke objek ini

nama = "Rehan"
nama = "Ani"  → stiker "nama" dicabut, ditempel ke objek baru "Ani"
               objek "Rehan" tidak ada yang menunjuk → garbage collected
```

Kenapa ini penting? Karena kalau kamu paham ini, semua behavior Python jadi masuk akal.

### 2.2 Aturan Penamaan Variabel

```python
# ✓ BENAR: snake_case (standar Python)
nama_lengkap = "Rehan"
ipk_mahasiswa = 3.85
jumlah_mahasiswa = 50

# ✗ SALAH:campur case
NamaLengkap = "Rehan"    # PascalCase untuk variabel = tidak standar
Nama_Lengkap = "Rehan"   # Underscore di tengah = tidak konsisten

# ✓ BENAR: boleh angka di akhir
mahasiswa1 = "Andi"
mahasiswa2 = "Budi"

# ✗ SALAH: tidak boleh angka di awal
# 1mahasiswa = "Andi"  → SyntaxError

# ✓ BENAR: underscore di awal untuk private
_private_var = 10
__special__ = "magic"   # reserved untuk Python internals
```

### 2.3 Tipe Data — Kapan Pakai Yang Mana

```python
# INTEGER (int) → untuk bilangan bulat
umur = 21           # ✓
jumlah_item = 150   # ✓
jarak = 0           # ✓

# FLOAT (float) → untuk bilangan desimal
ipk = 3.85         # ✓
harga = 15000.50   # ✓
pi = 3.14159       # ✓

# STRING (str) → untuk teks
nama = "Rehan"     # ✓
alamat = 'Jakarta'  # ✓
kalimat = "IPK saya 3.85"  # ✓ (campur teks dan angka sebagai teks)

# BOOLEAN (bool) → untuk True/False
aktif = True       # ✓
lulus = False      # ✓

# Kapan pilih int vs float?
# - Umur → int (tidak ada ".5 tahun")
# - IPK → float (bisa 3.75)
# - Harga → float (Rp 15.500,50)
# - Koordinat → float (latitude = -6.2088)
```

### 2.4 Casting — Mengubah Tipe Data

Casting artinya mengubah tipe data satu ke tipe lainnya:

```python
# str → int
nim = "2021001"
nim_int = int(nim)   # "2021001" → 2021001

# int → str
nomor = 99
nomor_str = str(nomor)   # 99 → "99"

# float → int (bagian desimal dibuang; menuju nol)
ipk = 3.85
ipk_int = int(ipk)    # 3.85 → 3 (bukan 4!)
# int(-3.85) → -3, jadi ini BUKAN floor untuk bilangan negatif

# str → float
harga_str = "15000.50"
harga = float(harga_str)  # "15000.50" → 15000.5

# KAPAN CASTING DIPERLUKAN?
# print("Umur: " + 21)          → TypeError! str + int tidak bisa
# print("Umur: " + str(21))     → ✓ "Umur: 21"
```

---

## 3. Operator Aritmatika — Rinci

### 3.1 Tabel Operator

```python
a, b = 17, 5

a + b    # 22   → Penjumlahan
a - b    # 12   → Pengurangan
a * b    # 85   → Perkalian
a / b    # 3.4  → Pembagian (SELALU float di Python 3!)
a // b   # 3    → Floor division (dibulatkan ke bawah)
a % b    # 2    → Modulo (sisa bagi)
a ** b   # 1419857 → Perpangkatan (17 pangkat 5)
```

### 3.2 Penjelasan Detail Tiap Operator

**`/` — Pembagian selalu menghasilkan float:**

```python
x = 10 / 2
print(x)      # → 5.0 (float! bukan 5!)
print(type(x))  # → <class 'float'>

# Bandingkan dengan // (floor division):
y = 10 // 2
print(y)      # → 5 (integer)
print(type(y))  # → <class 'int'>
```

**`//` — Floor Division (Pembagian Bulat):**

```python
# Floor = bulatkan ke bawah (SELALU ke arah bilangan lebih kecil)
print(7 // 2)    # → 3 (7/2 = 3.5 → bulatkan ke bawah → 3)
print(-7 // 2)   # → -4 (-7/2 = -3.5 → bulatkan ke bawah → -4)
print(7 // -2)   # → -4 (7/-2 = -3.5 → bulatkan ke bawah → -4)
print(8 // 3)    # → 2 (8/3 = 2.66 → bulatkan ke bawah → 2)
```

**`%` — Modulo (Sisa Bagi):**

```python
# Modulo = sisa dari pembagian bulat
print(17 % 5)    # → 2 (17 = 3×5 + 2 → sisa 2)
print(10 % 2)    # → 0 (10 = 5×2 + 0 → habis, sisa 0)
print(9 % 4)     # → 1 (9 = 2×4 + 1 → sisa 1)

# Kegunaan modulo:
# 1. Cek genap/ganjil
for i in range(10):
    if i % 2 == 0:
        print(f"{i} → genap")
    else:
        print(f"{i} → ganjil")

# 2. Cek kelipatan
for i in range(1, 51):
    if i % 7 == 0:
        print(f"{i} adalah kelipatan 7")

# 3. Looping siklis (array circular)
warna = ["merah", "hijau", "biru"]
for i in range(10):
    print(f"{i} → {warna[i % 3]}")
    # i=0 → warna[0%3=0] = merah
    # i=1 → warna[1%3=1] = hijau
    # i=2 → warna[2%3=2] = biru
    # i=3 → warna[3%3=0] = merah  (restart!)
    # i=4 → warna[4%3=1] = hijau
```

**`**` — Perpangkatan:**

```python
print(2 ** 10)   # → 1024 (2 pangkat 10)
print(5 ** 2)    # → 25 (5 kuadrat)
print(10 ** -2)  # → 0.01 (10 pangkat -2 = 1/100)
print(3 ** 0)    # → 1 (angka pangkat 0 = 1)
```

---

## 4. String — Lebih dari Sekadar Teks

### 4.1 String itu Array Karakter

Di Python, string adalah **urutan karakter** yang disimpan berurutan di memori:

```
"H e l l o"
0 1 2 3 4  → Index (mulai dari 0)
```

```python
teks = "Hello"
print(teks[0])    # → 'H' (karakter pertama, index 0)
print(teks[1])    # → 'e' (karakter kedua, index 1)
print(teks[-1])   # → 'o' (karakter terakhir)
print(teks[-2])   # → 'l' (karakter kedua dari belakang)
```

### 4.2 Slicing — Mengambil Bagian String

Format: `string[start:stop:step]`

```python
kalimat = "Belajar Python itu seru"

# [start:stop] — stop TIDAK inclusif
print(kalimat[0:7])     # → 'Belajar' (index 0-6)
print(kalimat[8:14])    # → 'Python' (index 8-13)
print(kalimat[8:])      # → 'Python itu seru' (dari index 8 sampai akhir)
print(kalimat[:7])      # → 'Belajar' (dari awal sampai index 6)

# [start:stop:step] — lompati karakter
print(kalimat[::2])     # → 'Bajr hyo t us' (setiap 2 karakter)
print(kalimat[::-1])    # → 'ures ti nohtyP nrajalB' (dibalik!)
print(kalimat[::-2])   # → 'uesi ohyp nrle' (dibalik, setiap 2)

# Negative slicing
print(kalimat[-4:])     # → 'seru' (4 karakter terakhir)
print(kalimat[:-5])     # → 'Belajar Python itu' (semua kecuali 5 terakhir)
```

### 4.3 f-string — Cara Modern Memformat String

f-string adalah cara tercepat dan paling readable untuk menyisipkan variabel ke dalam string:

```python
nama = "Rehan"
umur = 21
ipk = 3.85

# f-string (Python 3.6+)
print(f"Nama: {nama}, Umur: {umur}")
print(f"IPK: {ipk:.2f}")         # 2 desimal → "3.85"
print(f"IPK: {ipk:.1f}")         # 1 desimal → "3.9"
print(f"IPK: {ipk:.0f}")         # 0 desimal → "4"
print(f"{nama.upper()}")         # → "REHAN"
print(f"{nama.lower()}")         # → "rehan"

# Format angka besar
harga = 1500000
print(f"Rp {harga:,}".replace(",", "."))
# → "Rp 1.500.000"

# Format percentage
persen = 0.85
print(f"{persen:.0%}")   # → "85%"

# Aritmatika dalam f-string
x, y = 10, 3
print(f"{x} + {y} = {x+y}")   # → "10 + 3 = 13"
print(f"{x} / {y} = {x/y:.2f}") # → "10 / 3 = 3.33"
```

### 4.4 Method String yang Sering Dipakai

```python
teks = "  Belajar Python Itu Menyenangkan!  "

# Bersihkan whitespace
teks.strip()             # "Belajar Python Itu Menyenangkan!" (hapus depan/belakang)
teks.lstrip()            # hapus kiri saja
teks.rstrip()            # hapus kanan saja

# Ubah huruf
teks.lower()             # semua huruf kecil
teks.upper()             # semua huruf besar
teks.capitalize()        # huruf pertama besar, sisanya kecil
teks.title()             # setiap kata: huruf pertama besar

# Cek isi string
"Belajar" in teks        # → True
"belajar" in teks        # → False (case-sensitive!)
"belajar" in teks.lower() # → True (cek dengan lower dulu)

# Ganti teks
teks.replace("Menyenangkan", "Seru")
# "Belajar Python Itu Seru!"

# Pecah string jadi list
kalimat = "apel,mangga,jeruk"
kalimat.split(",")       # → ['apel', 'mangga', 'jeruk']
kalimat.split()          # → pisah berdasarkan spasi

# Gabung list jadi string
buah = ['apel', 'mangga', 'jeruk']
",".join(buah)           # → "apel,mangga,jeruk"
" - ".join(buah)         # → "apel - mangga - jeruk"

# Hitung karakter
len("Rehan")             # → 5 (panjang string)
kalimat.count("a")       # → hitung berapa kali huruf 'a' muncul
kalimat.find("Python")   # → 8 (index pertama ditemukan)
kalimat.startswith("Bel") # → True
kalimat.endswith("!")     # → True
```

---

## 5. List — Koleksi yang Bisa Berubah

### 5.1 Membuat List

```python
# List kosong
kosong = []

# List dengan isi
angka = [1, 2, 3, 4, 5]
nama = ["Andi", "Budi", "Citra"]
campuran = [1, "dua", 3.0, True]  # ✓ boleh campur tipe data

# List dari range
deret = list(range(1, 11))   # → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap = list(range(0, 21, 2))  # → [0, 2, 4, ..., 20]
```

### 5.2 Mengakses Elemen List

```python
buah = ["apel", "mangga", "jeruk", "anggur", "pepaya"]

# Index positif — dari depan
buah[0]    # → 'apel'      (elemen pertama)
buah[1]    # → 'mangga'
buah[2]    # → 'jeruk'

# Index negatif — dari belakang
buah[-1]   # → 'pepaya'    (elemen terakhir)
buah[-2]   # → 'anggur'
buah[-3]   # → 'jeruk'

# Slicing
buah[1:4]  # → ['mangga', 'jeruk', 'anggur']
buah[:3]   # → ['apel', 'mangga', 'jeruk']
buah[2:]   # → ['jeruk', 'anggur', 'pepaya']
buah[::2]  # → ['apel', 'jeruk', 'pepaya']  (setiap 2)
buah[::-1] # → ['pepaya', 'anggur', 'jeruk', 'mangga', 'apel']  (reverse)
```

### 5.3 Memodifikasi List

```python
buah = ["apel", "mangga", "jeruk"]

# Tambah elemen
buah.append("anggur")   # → ["apel", "mangga", "jeruk", "anggur"] (di akhir)
buah.insert(1, "pepaya") # → ["apel", "pepaya", "mangga", "jeruk", "anggur"] (di index 1)

# Hapus elemen
buah.remove("mangga")   # → hapus berdasarkan NILAI ("mangga")
popped = buah.pop()     # → hapus elemen TERAKHIR, KEMBALIKAN nilainya
                          # buah sekarang ["apel", "pepaya"]
                          # popped = "jeruk"
buah.pop(0)             # → hapus index ke-0 ("apel"), return "apel"
buah.clear()            # → hapus semua → []

# Ubah elemen
buah[0] = "strawberry"  # → ["strawberry", ...] (ubah elemen di index tertentu)

# Urutkan
angka = [3, 1, 4, 1, 5]
angka.sort()            # → [1, 1, 3, 4, 5] (urut ascending, MODIFIKASI langsung)
sorted(angka)           # → [1, 1, 3, 4, 5] (return list baru, angka tidak berubah)

angka.sort(reverse=True) # → [5, 4, 3, 1, 1] (urut descending)
```

### 5.4 List Comprehension — Cara Pythonic Membuat List

List comprehension adalah cara paling ringkas dan cepat untuk membuat list baru dari list yang ada.

**Format:** `[ekspresi for item in iterable if kondisi]`

```python
# ════════════════════════════════════════
# BENTUK 1: Tanpa kondisi
# ════════════════════════════════════════
# [ekspresi for item in iterable]

# Kuadrat 1-10
kuadrat = [i**2 for i in range(1, 11)]
# i=1 → 1, i=2 → 4, ... i=10 → 100
# Result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Kapitalisasi nama
nama = ["budi", "ani", "citra"]
besar = [n.upper() for n in nama]
# Result: ["BUDI", "ANI", "CITRA"]

# ════════════════════════════════════════
# BENTUK 2: Dengan kondisi (if)
# ════════════════════════════════════════
# [ekspresi for item in iterable if kondisi]

# Bilangan genap 1-20
genap = [i for i in range(1, 21) if i % 2 == 0]
# Result: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# IPK di atas 3.5
mahasiswa = [{"nama": "Andi", "ipk": 3.8},
             {"nama": "Budi", "ipk": 3.2},
             {"nama": "Citra", "ipk": 3.9}]
cumlaude = [m["nama"] for m in mahasiswa if m["ipk"] >= 3.5]
# Result: ["Andi", "Citra"]

# ════════════════════════════════════════
# BENTUK 3: Dengan if-else (ternary di depan)
# ════════════════════════════════════════
# [hasil_if if kondisi else hasil_else for item in iterable]

ipk_list = [3.5, 2.8, 3.9, 3.2, 3.7]
predikat = ["Cum Laude" if ipk >= 3.5 else "Memuaskan" for ipk in ipk_list]
# Result: ["Cum Laude", "Memuaskan", "Cum Laude", "Memuaskan", "Cum Laude"]

# ════════════════════════════════════════
# BENTUK 4: Nested (bertingkat)
# ════════════════════════════════════════
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for row in matriks for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 5.5 List vs Tuple — Kapan Pakai Yang Mana

```python
# List — Mutable (bisa diubah)
list_mahasiswa = ["Andi", "Budi", "Citra"]
list_mahasiswa.append("Dewi")    # ✓ Legal — list bisa berubah
list_mahasiswa[0] = "Anggi"     # ✓ Legal — element bisa diubah

# Tuple — Immutable (tidak bisa diubah)
tuple_mahasiswa = ("Andi", "Budi", "Citra")
# tuple_mahasiswa.append("Dewi")  # ✗ AttributeError!
# tuple_mahasiswa[0] = "Anggi"   # ✗ TypeError!

# Kapan pakai List?
koordinat_x = []     # Jumlah data tidak fixed, mungkin bertambah
daftar_nilai = []     # Nilai bisa diubah/dihapus

# Kapan pakai Tuple?
koordinat = (10.5, 25.3, 8.1)  # Koordinat GPS fixed, tidak boleh berubah
nama_bulan = ("Jan", "Feb", "Mar", ... )  # Konstanta yang fixed

# Keunggulan Tuple vs List:
# 1. Lebih cepat (karena immutable, Python bisa optimisasi)
# 2. Bisa jadi dictionary key: d = {(0,0): "origin"}
# 3. Return multiple values dari fungsi
```

---

## 6. Dictionary — Key-Value Store

### 6.1 Membuat Dictionary

```python
# Cara 1: Kurung kurawal
mahasiswa = {
    "nama": "Rehan",
    "nim": "2021001",
    "ipk": 3.85,
    "aktif": True
}

# Cara 2: dict()
data = dict(nama="Rehan", nim="2021001")
# Result: {"nama": "Rehan", "nim": "2021001"}

# Kunci boleh string, angka, tuple
d1 = {"a": 1, "b": 2}
d2 = {0: "nol", 1: "satu"}
d3 = {(0, 0): "origin", (1, 1): "diagonal"}  # ✓ tuple sebagai key
```

### 6.2 Mengakses, Menambah, Mengubah

```python
mahasiswa = {"nama": "Rehan", "ipk": 3.85}

# Mengakses
print(mahasiswa["nama"])     # → "Rehan"
print(mahasiswa.get("alamat")) # → None (key tidak ada)
print(mahasiswa.get("alamat", "N/A"))  # → "N/A" (dengan default)

# Menambah
mahasiswa["semester"] = 5    # → {"nama": "Rehan", "ipk": 3.85, "semester": 5}
mahasiswa["jurusan"] = "IF"

# Mengubah
mahasiswa["ipk"] = 3.92      # → ubah nilai yang sudah ada
```

### 6.3 Iterasi Dictionary

```python
mahasiswa = {"nama": "Rehan", "ipk": 3.85, "jurusan": "IF"}

# Iterasi semua key-value
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
# Output:
# nama: Rehan
# ipk: 3.85
# jurusan: IF

# Iterasi semua key
for key in mahasiswa.keys():
    print(key)

# Iterasi semua value
for value in mahasiswa.values():
    print(value)

# Cek key ada atau tidak
if "nama" in mahasiswa:
    print(f"Nama: {mahasiswa['nama']}")
```

### 6.4 Nested Dictionary

```python
data = {
    "mhs1": {"nama": "Rehan", "ipk": 3.85},
    "mhs2": {"nama": "Ani", "ipk": 3.5}
}

# Akses bertingkat
print(data["mhs1"]["nama"])          # → "Rehan"
print(data["mhs2"]["ipk"])           # → 3.5

# Menambah nested
data["mhs3"] = {"nama": "Budi", "ipk": 3.2}

# Ubah nested
data["mhs1"]["ipk"] = 3.92
```

### 6.5 Dictionary Comprehension

```python
# {key: value for item in iterable if kondisi}

# Kuadrat 1-5
kuadrat = {i: i**2 for i in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter: siswa dengan ipk >= 3.5
mahasiswa = [
    {"nama": "Rehan", "ipk": 3.85},
    {"nama": "Ani", "ipk": 3.2},
    {"nama": "Budi", "ipk": 3.9}
]
cumlaude = {m["nama"]: m["ipk"] for m in mahasiswa if m["ipk"] >= 3.5}
# Result: {"Rehan": 3.85, "Budi": 3.9}
```

---

## 7. Kondisi (if / elif / else) — Alur Keputusan

### 7.1 Struktur Dasar

```python
# ════════════════════════════════════
# Format if / elif / else
# ════════════════════════════════════

nilai = 87

if nilai >= 90:          # Kondisi 1
    grade = "A"
elif nilai >= 80:         # Kondisi 2 (dicek HANYA jika kondisi 1 False)
    grade = "B"
elif nilai >= 70:         # Kondisi 3
    grade = "C"
else:                     # Dijalankan jika SEMUA kondisi di atas False
    grade = "D"

print(f"Grade: {grade}")   # → "Grade: B"
```

**Kenapa elif bukan else-if?**
- `elif` adalah singkatan dari "else if" — diciptakan untuk menghindari pengulangan
- `elif` CHAINED: kondisi 2 hanya dicek jika kondisi 1 `False`
- Pertama kali ada yang `True`, Python langsum masuk dan skip sisanya

### 7.2 Multiple Conditions

```python
# AND — semua harus True
umur = 25
gaji = 5000000

if umur >= 21 and gaji >= 3000000:
    print("Layak")          # ✓ — umur 25 >= 21 DAN gaji 5jt >= 3jt

# OR — salah satu harus True
hari = "Sabtu"
libur = True

if hari == "Minggu" or libur:
    print("Tidak masuk")    # ✓ — salah satu True

# NOT — membalik boolean
aktif = False
if not aktif:
    print("Akun nonaktif")  # ✓ — aktif = False → not False = True
```

### 7.3 Short-circuit Evaluation

```python
# Python tidak akan cek kondisi kedua jika tidak perlu
# karena AND → kalau pertama False, hasilnya pasti False
# karena OR → kalau pertama True, hasilnya pasti True

# Contoh:
x = 0
if x != 0 and 10 / x > 1:  # ← 10/x TIDAK dijalankan (x=0, x!=0 = False)
    print("terpenuhi")

# Kalau tidak ada short-circuit:
# if x != 0 and 10 / x > 1: → cek x != 0 → False → STOP
# Tapi kalau ditulis:
# if 10 / x > 1 and x != 0: → 10/0 = ERROR! (x=0, division by zero)
```

### 7.4 Ternary Operator — if/else satu baris

```python
# Format: hasil_if_true if kondisi else hasil_if_false

nilai = 85
status = "Lulus" if nilai >= 65 else "Tidak Lulus"
print(status)   # → "Lulus"

# Bersarang
grade = "A" if nilai >= 90 else "B" if nilai >= 80 else "C" if nilai >= 70 else "D"
```

### 7.5 Truthy dan Falsy — yang Sering Dibingungkan

**Falsy (dievaluasi sebagai False):**
```python
if False:      pass
if None:       pass
if 0:          pass      # angka nol
if 0.0:        pass      # float nol
if "":         pass      # string kosong
if []:         pass      # list kosong
if {}:         pass      # dict kosong
if ():         pass      # tuple kosong
```

**Truthy (dievaluasi sebagai True):**
```python
if True:       pass
if "halo":     pass      # string non-kosong
if 1:          pass      # angka non-nol
if -5:         pass      # angka non-nol
if [1, 2]:     pass      # list non-kosong
if {"a": 1}:   pass      # dict non-kosong
```

---

## 8. Loop (for / while) — Pengulangan

### 8.1 for loop dengan range()

```python
# range(stop) — 0 sampai stop-1
for i in range(5):
    print(i, end=" ")   # → 0 1 2 3 4

# range(start, stop) — start sampai stop-1
for i in range(2, 6):
    print(i, end=" ")   # → 2 3 4 5

# range(start, stop, step) — lompati step
for i in range(0, 10, 2):
    print(i, end=" ")   # → 0 2 4 6 8

# Reverse
for i in range(5, 0, -1):
    print(i, end=" ")   # → 5 4 3 2 1
```

### 8.2 for loop dengan iterable

```python
# Iterasi list
buah = ["apel", "mangga", "jeruk"]
for b in buah:
    print(b)
# → apel
# → mangga
# → jeruk

# Dengan index menggunakan enumerate
for i, b in enumerate(buah, start=1):
    print(f"{i}. {b}")
# → 1. apel
# → 2. mangga
# → 3. jeruk

# Iterasi string
for char in "Python":
    print(char, end=" ")  # → P y t h o n

# Iterasi dict
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
```

### 8.3 while loop

```python
# Format:
# while kondisi:
#     ... kode ...
#     WAJIB ada yang mengubah kondisi, kalau tidak → infinite loop

# Contoh 1: Hitung mundur
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1          # ← WAJIB — ubah kondisi agar eventually False
print("Go!")

# Contoh 2: Infinite loop (BERBAHAYA — jangan dijalankan!)
# while True:
#     print("This runs forever!")  # ← tidak ada kondisi berhenti

# Contoh 3: Input validation
password = ""
while password != "12345":
    password = input("Masukkan password: ")
    if password != "12345":
        print("Salah! Coba lagi.")
print("Berhasil login!")
```

### 8.4 break dan continue

```python
# break — keluar dari loop SEKETIKA
for i in range(10):
    if i == 5:
        break            # ← keluar loop TOTAL, tidak jalankan i=5 ke atas
    print(i, end=" ")    # → 0 1 2 3 4 (loop berhenti saat i=5)

print("\n--- setelah break ---")

# continue — skip ke iterasi berikutnya
for i in range(5):
    if i == 2:
        continue         # ← skip i=2, langsung ke i=3
    print(i, end=" ")    # → 0 1 3 4 (i=2 tidak di-print)
```

### 8.5 Nested Loop

```python
# Loop di dalam loop
for i in range(3):       # outer loop — 3 iterasi
    for j in range(4):   # inner loop — 4 iterasi per outer
        print(f"({i},{j})", end=" ")
    print()               # newline setelah setiap baris

# Output:
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)

# Contoh: Tabel perkalian
print("Tabel Perkalian 1-5:")
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        row += f"{i*j:4d}"   # :4d = 4 digit (rata kanan)
    print(row)

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

---

## 9. Fungsi — Kode yang Bisa Dipakai Ulang

### 9.1 Membuat Fungsi

```python
# ════════════════════════════════════
# Fungsi tanpa return
# ════════════════════════════════════
def sapa(nama):
    """Fungsi ini menyapa seseorang"""
    print(f"Halo, {nama}!")

sapa("Rehan")   # → "Halo, Rehan!"
sapa("Ani")     # → "Halo, Ani!"

# ════════════════════════════════════
# Fungsi dengan return
# ════════════════════════════════════
def kuadrat(x):
    return x ** 2

hasil = kuadrat(5)   # → 25
print(f"5 kuadrat = {hasil}")

# ════════════════════════════════════
# Fungsi dengan default argument
# ════════════════════════════════════
def pangkat(angka, p=2):
    """Pangkat default=2 (kuadrat)"""
    return angka ** p

print(pangkat(5))     # → 25 (default p=2)
print(pangkat(5, 3))  # → 125 (override p=3)
print(pangkat(2, 10)) # → 1024

# ════════════════════════════════════
# Multiple return
# ════════════════════════════════════
def stats(data):
    n = len(data)
    total = sum(data)
    mean = total / n
    return n, total, mean  # return tuple

jumlah, total, rata = stats([10, 20, 30])
print(f"Jumlah: {jumlah}, Total: {total}, Rata-rata: {rata}")
# → "Jumlah: 3, Total: 60, Rata-rata: 20.0"
```

### 9.2 *args dan **kwargs — Argumen Fleksibel

```python
# ════════════════════════════════════
# *args — terima banyak argumen positional
# ════════════════════════════════════
def total(*bilangan):
    """Terima jumlah argumen tidak terbatas"""
    print(f"Dapat {len(bilangan)} argumen: {bilangan}")
    return sum(bilangan)

print(total(1, 2, 3))           # → 6, args = (1, 2, 3)
print(total(10, 20, 30, 40))    # → 100, args = (10, 20, 30, 40)
print(total())                   # → 0, args = ()

# ════════════════════════════════════
# **kwargs — terima banyak argumen keyword
# ════════════════════════════════════
def info(**data):
    """Terima banyak pasangan key=value"""
    for key, value in data.items():
        print(f"{key}: {value}")

info(nama="Rehan", nim="2021001", ipk=3.85)
# Output:
# nama: Rehan
# nim: 2021001
# ipk: 3.85

# ════════════════════════════════════
# Kombinasi
# ════════════════════════════════════
def flex(nama, *scores, bonus=0, **detail):
    print(f"Nama: {nama}")
    print(f"Scores: {scores}")
    print(f"Bonus: {bonus}")
    print(f"Detail: {detail}")

flex("Rehan", 80, 85, 90, bonus=5, nim="2021001", ipk=3.85)
# Output:
# Nama: Rehan
# Scores: (80, 85, 90)
# Bonus: 5
# Detail: {'nim': '2021001', 'ipk': 3.85}
```

### 9.3 Lambda — Fungsi Tanpa Nama

Lambda adalah fungsi anonim (tanpa nama) yang biasa dipakai untuk operasi sederhana:

```python
# Format: lambda argumen: ekspresi

# Lambda biasa
kuadrat = lambda x: x ** 2
print(kuadrat(7))  # → 49

# Lambda dengan multiple args
jumlah = lambda a, b: a + b
print(jumlah(3, 4))  # → 7

# Lambda + map() — terapkan fungsi ke SETIAP elemen
angka = [1, 2, 3, 4, 5]
kuadrat_semua = list(map(lambda x: x ** 2, angka))
print(kuadrat_semua)  # → [1, 4, 9, 16, 25]

# Lambda + filter() — pilih elemen berdasarkan kondisi
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)  # → [2, 4]

# Lambda + sorted() — sorting dengan key kustom
mahasiswa = [{"nama": "Budi", "ipk": 3.2},
             {"nama": "Ani", "ipk": 3.9},
             {"nama": "Citra", "ipk": 3.5}]

# Sort berdasarkan IPK descending
terurut = sorted(mahasiswa, key=lambda m: m["ipk"], reverse=True)
print([m["nama"] for m in terurut])  # → ["Ani", "Citra", "Budi"]
```

---

## 10. Error Handling — try/except/finally

### 10.1 Struktur try/except

```python
# ════════════════════════════════════
# Basic try/except
# ════════════════════════════════════
def bagi(a, b):
    try:
        hasil = a / b
        print(f"{a} / {b} = {hasil}")
    except ZeroDivisionError:
        print("Error: tidak bisa bagi dengan 0!")
    except TypeError:
        print("Error: input harus angka!")
    except Exception as e:
        print(f"Error tidak terduga: {e}")

bagi(10, 2)    # → "10 / 2 = 5.0"
bagi(10, 0)   # → "Error: tidak bisa bagi dengan 0!"
bagi("10", 2)  # → "Error: input harus angka!"
```

### 10.2 try/except/else/finally

```python
# else → jalan jika TIDAK ada exception
# finally → SELALU jalan, baik ada error atau tidak

def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan!")
        data = None
    else:
        print("File berhasil dibaca!")  # ← hanya kalau tidak ada error
    finally:
        print("Selesai proses file")    # ← SELALU jalan
    return data
```

### 10.3 raise — Memunculkan Error Secara Manual

```python
# raise → untuk situasi di mana kamu mau Python "berteriak" ada yang salah

def validate_ipk(ipk):
    if not isinstance(ipk, (int, float)):
        raise TypeError("IPK harus berupa angka!")
    if ipk < 0 or ipk > 4.0:
        raise ValueError(f"IPK {ipk} tidak valid! Harus antara 0.0 - 4.0")

try:
    validate_ipk(3.85)   # ✓ — tidak ada error
    validate_ipk(-1)     # ✗ — ValueError
    validate_ipk("3.85") # ✗ — TypeError
except ValueError as e:
    print(f"Validasi gagal: {e}")
except TypeError as e:
    print(f"Tipe data salah: {e}")
```

---

## 11. Pola Kode yang Sering Dipakai di Level 1

### 11.1 Menukar Nilai Dua Variabel

```python
# Cara biasa (butuh variabel temporary)
a, b = 10, 20
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")   # → a = 20, b = 10

# Cara Pythonic (tuple unpacking)
a, b = 10, 20
a, b = b, a   # ← satu baris saja!
print(f"a = {a}, b = {b}")   # → a = 20, b = 10
```

### 11.2 flatten list

```python
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in matriks:
    for num in row:
        flat.append(num)
print(flat)  # → [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cara Pythonic
flat = [num for row in matriks for num in row]
```

### 11.3 Hitung frekuensi dengan Counter

```python
# Cara manual
nama = ["Andi", "Budi", "Andi", "Citra", "Budi", "Andi"]
frekuensi = {}
for n in nama:
    if n in frekuensi:
        frekuensi[n] += 1
    else:
        frekuensi[n] = 1
print(frekuensi)  # → {'Andi': 3, 'Budi': 2, 'Citra': 1}

# Pakai collections.Counter (lebih clean)
from collections import Counter
frekuensi = Counter(nama)
print(frekuensi.most_common())  # → [('Andi', 3), ('Budi', 2), ('Citra', 1)]
```

### 11.4 FizzBuzz — Klasik Pemrograman

```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Output:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...
```

---

## Ringkasan Pola Penulisan

| Pola | Penulisan | Kapan Dipakai |
|---|---|---|
| Variabel | `nama_var = nilai` | Selalu |
| Komentar | `# teks` atau `"""docstring"""` | Penjelasan non-obvious |
| If/elif/else | `if kondisi: ... elif: ... else: ...` | Decision branching |
| For loop | `for i in range(n):` atau `for x in list:` | Iterasi fixed/known count |
| While loop | `while kondisi:` | Iterasi tidak fixed, berbasis kondisi |
| Fungsi | `def nama(arg): return hasil` | Kode reusable |
| Lambda | `lambda x: x**2` | Fungsi anonim satu baris |
| List comprehension | `[x**2 for x in range(10)]` | Buat list baru dari iterasi |
| Try/except | `try: ... except Error: ...` | Handle anticipated errors |
| F-string | `f"nilai: {x}"` | String interpolation |

---

**Lanjut:** Buka `01_python_fundamental.ipynb` → jalankan cell pertama. Baca panduan ini bersamaan dengan kode yang kamu jalankan.
