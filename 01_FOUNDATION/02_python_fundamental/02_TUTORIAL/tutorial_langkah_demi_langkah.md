# Tutorial Penyelesaian — Level 01 Python Fundamental

Kerjakan `typing_practice.ipynb` dahulu. Untuk setiap soal, ketik kode tanpa melihat solusi, jalankan, bandingkan output, lalu jelaskan fungsi setiap baris.

## Pola menyelesaikan program kecil

Pisahkan **input → proses → output**. Contoh program luas persegi panjang:

```python
panjang = 7
lebar = 5
luas = panjang * lebar
print(f"Luas: {luas}")
```

Jangan menaruh perhitungan, input, dan format output dalam satu baris pada awal belajar. Variabel bernama jelas memudahkan debugging.

## If, loop, dan function

Untuk kondisi, tulis semua cabang yang mungkin. Untuk loop, tulis koleksi yang diiterasi dan apa yang berubah tiap iterasi. Untuk function, tentukan parameter, return value, dan contoh input sebelum menulis badan function.

```python
def status_nilai(nilai: float) -> str:
    if nilai >= 75:
        return "lulus"
    return "belum lulus"

assert status_nilai(75) == "lulus"
assert status_nilai(74) == "belum lulus"
```

## Saat muncul error

- `NameError`: variabel belum dibuat atau typo.
- `TypeError`: cek `type()` setiap nilai yang dioperasikan.
- `IndexError`: cek `len(data)`; indeks terakhir adalah `len(data) - 1`.
- `KeyError`: pakai `dict.get()` bila key mungkin tidak ada.
- `ValueError`: tipe benar, tetapi isi tidak dapat diterima; validasi input.

Untuk soal input umur, letakkan konversi di dalam `try/except ValueError`; jangan menangkap `Exception` secara luas karena itu menyembunyikan bug lain.

## Cara menilai jawaban sendiri

Uji input normal, batas, dan salah: umur `20`, `0`, `-1`, dan `"dua puluh"`. Program yang hanya berhasil untuk satu input contoh belum selesai.
