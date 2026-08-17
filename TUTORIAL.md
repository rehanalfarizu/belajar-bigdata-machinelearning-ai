# Tutorial Lengkap: Cara Menulis dan Menjalankan Python

> Panduan ini dibuat untuk mahasiswa Computer Science yang baru mulai belajar Python.
> Dibaca dari atas ke bawah — ini bukan dokumentasi, tapi langkah-langkah nyata yang bisa kamu ikuti.

---

## Tujuan

Setelah membaca panduan ini, kamu akan tahu:
- [ ] Cara menulis kode Python yang benar
- [ ] Cara menjalankan kode Python
- [ ] Cara membaca output hasil
- [ ] Cara debug (memperbaiki error)
- [ ] Cara organize proyek Python dengan benar

---

## 1. Cara Kerja Python — Apa yang Terjadi Saat Kamu Jalankan Kode?

### 1.1 Interpreter vs Compiler

Saat kamu jalankan kode Python, ada **interpreter** yang membaca kode kamu baris-demi-baris:

```python
# File: hello.py
nama = "Rehan"
print(f"Halo, {nama}!")
```

Saat kamu ketik `python3 hello.py`, yang terjadi:

```
Langkah 1: Interpreter baca "nama = "Rehan""
          → Python allocate memory, simpan string "Rehan", kasih label "nama"

Langkah 2: Interpreter baca "print(f"Halo, {nama}!")"
          → Python evaluasi f-string → "Halo, Rehan!"
          → Print ke layar

Langkah 3: Selesai — program exit
```

**Tidak ada tahap kompilasi.** Setiap baris langsung dijalankan saat dibaca.

### 1.2 Dua Jenis Error Python

| Jenis | Kapan terjadi | Bisa diperbaiki? |
|---|---|---|
| **SyntaxError** |Sebelum program jalan — typo syntax | Ya, perbaiki teksnya |
| **RuntimeError** |Saat program jalan — logical error | Ya, perbaiki logikanya |
| **Logic Error** | Program jalan tapi hasil salah | Ya, perbaiki algoritmanya |

**Contoh SyntaxError:**
```python
# SALAH:
if x = 5        # = adalah assignment, bukan comparison!
    print(x)

# BENAR:
if x == 5:      # == adalah comparison
    print(x)
```

**Contoh RuntimeError:**
```python
x = [1, 2, 3]
print(x[10])    # IndexError: list index out of range
```

**Contoh Logic Error (paling berbahaya — program jalan tapi salah):**
```python
# Mau rata-rata: 10 + 20 + 30 = 60/3 = 20
total = 10 + 20 + 30
jumlah = 3
rata = total / jumlah   # ← 60/3 = 20 ✓ (benar)
# Tapi kalau kamu tulis:
rata = total / 2        # ← 60/2 = 30 ✗ (salah! tapi tidak ada error message)
```

---

## 2. Tiga Cara Menjalankan Python

### 2.1 Cara 1: Jupyter Notebook (RECOMMENDED — untuk ML/Data Science)

**Kenapa Jupyter?**
- Kode ditulis per CELL, bisa jalan satu per satu
- Bisa tulis catatan (markdown) di antara kode
- Langsung lihat hasil di bawah kode
- Ini adalah standar industri untuk Data Science & ML

**Cara install & buka:**

```bash
# Install Jupyter
pip install jupyterlab

# Buka Jupyter (jalankan di terminal, arahkan ke folder proyek)
cd /Users/macbookpro/Documents/belajar-bigdata-machinelearning-ai
jupyter lab
```

Setelah Jupyter terbuka:
1. Klik `01_python_fundamental/01_python_fundamental.ipynb`
2. Klik cell pertama (berwarna biru di kiri)
3. Tekan `Shift + Enter` untuk menjalankan cell
4. Lihat output di bawah cell
5. Klik cell berikutnya, tekan `Shift + Enter` lagi — dan seterusnya

**Anatomi Jupyter Notebook:**

```
┌──────────────────────────────────────────┐
│ [Cell 1: Markdown]                        │ ← Judul/penjelasan
│ # Level 1 — Python Fundamental            │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ [Cell 2: Code]                      [▶]  │ ← Kode Python
│ nama = "Rehan"                            │
│ print(f"Halo, {nama}")                    │
│                                          │
│ Output: Halo, Rehan!                     │ ← Hasil muncul di bawah
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ [Cell 3: Code]                      [▶]  │
│ x = 10                                   │
│ print(x * 2)                             │
│                                          │
│ Output: 20                               │
└──────────────────────────────────────────┘
```

**Navigasi keyboard penting:**
| Shortcut | Fungsi |
|---|---|
| `Shift + Enter` | Run cell + pilih cell berikutnya |
| `Ctrl + Enter` | Run cell + tetap di cell yang sama |
| `Esc` | Masuk mode command (warna biru) |
| `Enter` | Masuk mode edit (warna hijau) |
| `A` (esc mode) | Insert cell di atas |
| `B` (esc mode) | Insert cell di bawah |
| `D D` (double tap) | Delete cell |
| `Z` | Undo delete |
| `M` (esc mode) | Ubah cell jadi Markdown |
| `Y` (esc mode) | Ubah cell jadi Code |

### 2.2 Cara 2: Terminal / Command Line

Gunakan untuk script sederhana atau automation.

```bash
# Buat file baru
nano hello.py

# Atau pakai VS Code
code hello.py

# Jalankan
python3 hello.py
```

Contoh file `hello.py`:
```python
nama = "Rehan"
umur = 21
print(f"Halo, nama saya {nama}, umur {umur}")

# Aritmatika
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")     # 2 desimal
print(f"{a} // {b} = {a // b}")       # floor division
print(f"{a} % {b} = {a % b}")         # sisa bagi
print(f"{a} ** {b} = {a ** b}")       # pangkat
```

### 2.3 Cara 3: Google Colab (Tanpa Install Apapun)

Jika tidak mau install Jupyter, gunakan Google Colab (gratis, di cloud):

1. Buka https://colab.research.google.com
2. Klik "Upload" → upload file `.ipynb` dari folder materi
3. Atau klik "File" → "Open notebook" → upload file
4. Klik `Runtime` → `Run all` untuk jalan semua cell sekaligus

---

## 3. Sintaks Dasar Python — Aturan Penulisan

Python punya **5 aturan sintaks fundamental**. Jika satu saja dilanggar, program error.

### Aturan 1: Indentasi (Spasi di awal baris) — YANG PALING PENTING

Python pakai **indentasi (spasi/tab di awal baris)** untuk mendefinisikan blok kode. Ini BUKAN optional.

```python
# BENAR — 4 spasi untuk blok dalam if/for/def
if True:
    print("di dalam if")
    x = 5
    y = 10

# SALAH — tidak ada indentasi → IndentationError
# if True:
# print("di dalam if")   ← ERROR!
```

**Perbandingan dengan bahasa lain:**

```c
// C/Java — pakai kurung kurawal {}
if (x > 5) {
    printf("x lebih besar dari 5");
    x = x + 1;
}
```

```python
# Python — indentasi menggantikan {}
if x > 5:
    print("x lebih besar dari 5")
    x = x + 1
```

**Praktik terbaik:**
- Gunakan **4 spasi** (bukan tab) — ini konvensi resmi Python (PEP 8)
- Di Jupyter, tab otomatis jadi 4 spasi
- **Jangan campur tab dan spasi** — itu error

### Aturan 2: `=` adalah Assignment, bukan Persamaan Matematika

```python
# SALAH jika dibaca sebagai matematika:
x = 10
x = x + 5
# Dalam matematika: 10 = 10 + 5 → tidak masuk akal
# Dalam programming: "ambil nilai x, tambah 5, simpan ke x"

# BENAR dibaca sebagai:
# x = 10          → x sekarang sama dengan 10
# x = x + 5       → x sekarang sama dengan (nilai lama x + 5) = 15
```

### Aturan 3: Comparison menggunakan `==`, bukan `=`

```python
# Assignment (menyimpan nilai)
x = 10

# Comparison (membandingkan)
if x == 10:
    print("x sama dengan 10")

# Error jika pakai = dalam if:
# if x = 10:    ← SyntaxError!
```

### Aturan 4: String menggunakan kutip, bukan petik

```python
nama = "Rehan"     # ✓ — double quote
nama = 'Rehan'     # ✓ — single quote (sama saja)
nama = "Rehan'      # ✗ — quote tidak match

kalimat = "It's a great day"    # ✓ — ada apostrophe di dalam
kalimat = 'It\'s a great day'   # ✓ — escape apostrophe
kalimat = "It's a great day"    # ✓ — lebih clean
```

### Aturan 5: `print()` untuk melihat hasil

**DI Jupyter, setiap cell yang runs最后一行会自动显示为 output.**

```python
# Langsung lihat hasil
x = 10
x + 5        # Di Jupyter: output otomatis = 15 ✓

# Tapi untuk AMAN, selalu pakai print():
x = 10
print(x + 5)  # Output: 15 ✓

# Kenapa harus print()? Karena:
# - Di terminal, tanpa print() tidak ada output
# - print() lebih jelas saat ada banyak operasi
```

---

## 4. Cara Membaca Output Python

### 4.1 Output Angka

```python
x = 7 / 2
print(x)           # → 3.5  (desimal / float)

x = 7 // 2
print(x)           # → 3    (floor division — dibulatkan ke bawah)

x = 7 % 2
print(x)           # → 1    (modulo — sisa bagi)
```

### 4.2 Output String

```python
# f-string (paling umum di Python modern)
nama = "Rehan"
ipk = 3.85

print(f"IPK {nama} adalah {ipk:.2f}")
# → "IPK Rehan adalah 3.85"
# {ipk:.2f} → 2 desimal, dibulatkan

# Format angka besar
juta = 1500000
print(f"{juta:,}".replace(",", "."))
# → "1.500.000"
```

### 4.3 Output List

```python
angka = [3, 1, 4, 1, 5]
print(angka)          # → [3, 1, 4, 1, 5] (keseluruhan)
print(angka[0])      # → 3 (elemen pertama)
print(angka[-1])     # → 5 (elemen terakhir)
print(len(angka))    # → 5 (jumlah elemen)
print(sum(angka))    # → 14 (total)
print(sorted(angka)) # → [1, 1, 3, 4, 5] (sorted baru, tidak ubah aslinya)
```

### 4.4 Output Boolean

```python
x = 10
print(x > 5)    # → True (x lebih besar dari 5, ya)
print(x == 10)   # → True (x sama dengan 10, ya)
print(x != 10)   # → False (x tidak sama dengan 10, tidak)
print(x < 5)    # → False (x lebih kecil dari 5, tidak)
```

### 4.5 Output None

```python
def tanpa_return(x):
    print(x)

hasil = tanpa_return(5)  # print(5) jalan, tapi fungsi tidak return apa-apa
print(hasil)               # → None (karena tidak ada return statement)
```

---

## 5. Debugging — Cara Memperbaiki Error

### 5.1 Jenis Error yang Paling Sering

```python
# ══════════════════════════════════════════════
# ERROR 1: IndentationError
# ══════════════════════════════════════════════
# Penyebab: Spasi/tab tidak konsisten

if True:
print("halo")    # ← ERROR: inconsistent indentation

# Solusi: Tambahkan 4 spasi di awal baris
if True:
    print("halo")  # ✓
```

```python
# ══════════════════════════════════════════════
# ERROR 2: SyntaxError
# ══════════════════════════════════════════════
# Penyebab: Salah ketik keyword atau tanda

if x = 5:          # ← ERROR: = bukan ==
    print(x)

# Solusi: Pakai == untuk comparison
if x == 5:
    print(x)        # ✓
```

```python
# ══════════════════════════════════════════════
# ERROR 3: NameError
# ══════════════════════════════════════════════
# Penyebab: Variabel belum didefinisikan

print(nama)    # ← ERROR: name 'nama' is not defined

# Solusi: Definisikan variabel dulu
nama = "Rehan"
print(nama)    # ✓ → "Rehan"
```

```python
# ══════════════════════════════════════════════
# ERROR 4: TypeError
# ══════════════════════════════════════════════
# Penyebab: Operasi dengan tipe yang salah

umur = 21
kalimat = "Umur saya " + umur   # ← ERROR: can only concatenate str (not "int") to str

# Solusi: Konversi int ke str
kalimat = "Umur saya " + str(umur)  # ✓ → "Umur saya 21"
```

```python
# ══════════════════════════════════════════════
# ERROR 5: IndexError
# ══════════════════════════════════════════════
# Penyebab: Akses index di luar range

buah = ["apel", "mangga", "jeruk"]
print(buah[10])   # ← ERROR: list index out of range

# Solusi: Cek panjang list dulu
if len(buah) > 10:
    print(buah[10])
else:
    print("Index tidak ada")  # ✓ → akan tampil
```

```python
# ══════════════════════════════════════════════
# ERROR 6: ZeroDivisionError
# ══════════════════════════════════════════════
# Penyebab: Bagi dengan 0

x = 10 / 0           # ← ERROR: division by zero

# Solusi: Cek penyebut dulu
if b != 0:
    hasil = a / b
else:
    print("Tidak bisa bagi dengan 0")
```

### 5.2 Cara Baca Traceback Error (Pesan Error Python)

```python
# Contoh error:
Traceback (most recent call last):
  File "script.py", line 5, in <module>
    print(x[10])
IndexError: list index out of range
```

**Cara baca:**
1. `File "script.py"` → Nama file yang error
2. `line 5` → Baris ke-5 yang menyebabkan error
3. `IndexError` → Jenis errornya
4. `list index out of range` → Penjelasan errornya

**Artinya:** Kamu mencoba akses index ke-10 dari list yang jumlah elementnya kurang dari 11.

### 5.3 Teknik Debugging Tambahan

```python
# Pakai print() untuk cek nilai variabel di tengah-tengah proses
def hitung(a, b):
    print(f"Input: a={a}, b={b}")  # ← Debugging: lihat nilai a dan b
    hasil = a + b
    print(f"Proses: {a} + {b} = {hasil}")  # ← Debugging: lihat proses
    return hasil

# Pakai assert untuk verify asumsi
x = 10
assert x > 0, "x harus positif!"  # ✓ — lanjut jika True
# assert x > 100, "x harus > 100!"  # ✗ — Error: AssertionError: x harus > 100!

# Pakai type() untuk cek tipe data
print(type(10))       # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("halo"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

---

## 6. Best Practices Penulisan Kode Python

### 6.1 Naming Convention (Cara Menamai Variabel)

```python
# ══════════════════════════════
# BENAR: snake_case untuk variabel dan fungsi
# ══════════════════════════════
nama_lengkap = "Rehan"
ipk_mahasiswa = 3.85
hitung_rata_rata = ...

# ══════════════════════════════
# BENAR: PascalCase untuk class
# ══════════════════════════════
class DataMahasiswa:
    pass

# ══════════════════════════════
# BENAR: SCREAMING_SNAKE untuk konstanta
# ══════════════════════════════
MAX_RETRY = 3
PASSWORD = "12345"

# ══════════════════════════════
# SALAH: tidak informatif
# ══════════════════════════════
x = 10          # ← x apa? Tidak jelas
data = [...]    # ← data apa? Tidak jelas

# BENAR: self-documenting code
jumlah_mahasiswa = 10
daftar_nilai_mahasiswa = [...]
```

### 6.2 Comment (Komentar)

```python
# ════════════════════════════════════════════
# Kapan pakai comment? Hanya untuk alasan non-obvious
# ════════════════════════════════════════════

# BAD — comment yang tidak perlu (kode sudah jelas)
x = 10          # assign 10 to x

# GOOD — comment untuk alasan non-obvious
# Menggunakan nilai seed agar hasil random konsisten saat diuji ulang
random.seed(42)

# GOOD — comment untuk workaround sementara
# TODO(human): Ganti dengan implementasi yang lebih efisien
x = x + 1       # workaround karena API belum ready
```

### 6.3 Mengorganisir Kode

```python
# ════════════════════════════════════════════
# GOOD: Pisahkan bagian dengan comment
# ════════════════════════════════════════════

# ─── Input ───
nama = "Rehan"
uts = 85
uas = 90

# ─── Proses ───
rerata = (uts + uas) / 2
lulus = rerata >= 65

# ─── Output ───
print(f"Nama: {nama}")
print(f"Rata-rata: {rerata:.1f}")
print(f"Status: {'Lulus' if lulus else 'Tidak Lulus'}")
```

---

## 7. Struktur Proyek Python yang Baik

### 7.1 Folder Structure (untuk proyek ini)

```
belajar-bigdata-machinelearning-ai/
├── materi/
│   ├── 01_python_fundamental/
│   │   ├── README.md           ← Teori lengkap (baca dulu)
│   │   ├── praktikum.md         ← Soal latihan
│   │   └── 01_python_fundamental.ipynb  ← Notebook untuk dijalankan
│   ├── 02_data_analysis/
│   └── ...
├── TUTORIAL.md                  ← File ini (panduan cara kerja Python)
└── ROADMAP_TRACKER.txt
```

### 7.2 Cara Kerja Per Level

```
1. Baca materi/README.md     → Pahami teori dan konsep
2. Buka notebook .ipynb      → Jalankan kode per cell
3. Kerjakan praktikum.md     → Tantangan tambahan
4. Review & experiment        → Ubah nilai, lihat apa yang berubah
```

---

## 8. Checklist Sebelum Kode Kamu Dijalankan

Gunakan checklist ini sebelum kamu jalankan setiap cell di Jupyter:

```
□ Variabel sudah di-assign?         (nama = "Rehan")
□ Tipe data sudah benar?            (str + int → str(int))
□ Indentasi sudah 4 spasi?          (di dalam if/for/def)
□ Tidak ada typo keyword?            (== bukan =, if bukan iif)
□ Index dalam range?                (list[0] sampai list[len-1])
□ Penyebut tidak nol?               (a / 0 → error)
□ String quote sudah match?         ("halo" bukan "halo)
```

---

## 9. Cara Lain untuk Belajar dari Notebook Ini

### 9.1 Ubah Nilai dan Lihat Hasilnya

Di setiap cell, **jangan hanya run — ubah nilainya**:

```python
# Cell asli:
nama = "Rehan"
ipk = 3.85

# Ubah jadi:
nama = "Ani"
ipk = 2.5

# Lihat apa yang berubah — ini belajar paling efektif
print(f"{nama} - IPK: {ipk}")
```

### 9.2 Tambahkan Cell Debug Sendiri

Setelah cell berjalan, klik `+` untuk tambah cell baru. Coba experiment:

```python
# Experiment di cell baru:
# 1. Apa yang terjadi kalau x = -1?
# 2. Apa yang terjadi kalau list kosong []?
# 3. Apa yang terjadi kalau string berisi angka "123"?

# Contoh experiment:
x = -5
if x > 0:
    print("Positif")
elif x < 0:
    print("Negatif")  # ← Apakah ini yang akan jalan?
else:
    print("Nol")
```

### 9.3 Buat Journal — Catat Apa yang Kamu Pelajari

Setelah setiap level, catat dalam file `journal.md`:

```
# Journal - Level 1
Tanggal: 2026-05-31

HAL YANG SAYA PELAJARI:
1. Variabel di Python = label, bukan slot memori
2. == adalah comparison, = adalah assignment
3. List comprehension itu cepat dan pythonic
4. LEGB scope — Local, Enclosing, Global, Built-in

HAL YANG MASIH MEMBINGUNGKAN:
1. Kapan pakai tuple vs list — masih belajar
2. closure di lambda — perlu lebih banyak contoh

CODE FAVORIT:
- FizzBuzz karena menunjukkan logika jelas
```

---

## Ringkasan

| Yang Harus Kamu Tahu | Detail |
|---|---|
| Python itu interpreter | Dijalankan baris-demi-baris, tidak dikompilasi |
| Indentasi WAJIB 4 spasi | Tidak boleh campur tab dan spasi |
| `=` adalah assignment | "x = 10" → x menunjuk ke objek 10 |
| `==` adalah comparison | "x == 10" → cek apakah x sama dengan 10 |
| `print()` untuk output | Di Jupyter output otomatis, di terminal wajib print |
| Error dibaca dari bawah | Traceback → file, line, jenis error |
| Naming: snake_case | `nama_lengkap`, `ipk_mahasiswa` |
| Selalu experiment | Ubah nilai, lihat hasil, jangan hanya run |

---

**Lanjut**: Buka `materi/01_python_fundamental/01_python_fundamental.ipynb` — jalankan cell pertama dengan `Shift + Enter`.