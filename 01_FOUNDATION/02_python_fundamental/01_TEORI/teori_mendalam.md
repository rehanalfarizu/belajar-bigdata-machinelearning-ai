# Teori Mendalam — Level 01: Python Fundamental

## 1. Dari source code ke eksekusi

Python adalah bahasa interpreted: source code diparse menjadi bytecode lalu dieksekusi virtual machine. Ini tidak berarti Python selalu membaca satu baris secara polos; function body, import, scope, dan object lifecycle mengikuti aturan bahasa yang jelas. Indentasi membentuk blok karena Python tidak memakai kurung kurawal. Satu level blok sebaiknya empat spasi konsisten; mencampur tab dan spasi menghasilkan error atau perilaku membingungkan.

Nama variabel di Python mengikat object. Assignment tidak selalu membuat salinan. `b = a` membuat nama kedua yang menunjuk object sama. Immutability berarti object tidak dapat diubah setelah dibuat; operasi yang terlihat “mengubah” string sebenarnya menghasilkan string baru. Mutability berguna untuk list/dict, tetapi membutuhkan perhatian pada aliasing, default argument mutable, dan copy dangkal versus dalam.

## 2. Tipe data dan truthiness

`int` presisi arbitrer, `float` mengikuti floating-point biner sehingga `0.1 + 0.2` tidak persis `0.3`, `str` adalah urutan Unicode immutable, dan `bool` adalah subclass `int`. Collection utama: list berurutan/mutable, tuple berurutan/immutable, dict memetakan key hashable ke nilai, set menyimpan anggota unik tanpa urutan terjamin. Pilih struktur dari operasi dominan: lookup key pada dict/set rata-rata cepat; akses indeks pada list; urutan tetap pada tuple.

Dalam kondisi, nilai kosong seperti `0`, `""`, `[]`, `{}`, `None`, dan `False` dianggap falsey. Namun gunakan `is None` untuk memeriksa ketiadaan nilai, bukan `== None`. Equality `==` membandingkan nilai; identity `is` membandingkan object yang sama. Kesalahan membedakannya sering muncul pada `None` dan object mutable.

## 3. Flow control dan kompleksitas

`if` memilih cabang, `for` mengiterasi iterable, dan `while` berulang hingga kondisi berubah. `range` menghasilkan urutan malas, bukan list besar. `enumerate` memberi index dan item; `zip` memasangkan iterable. Hindari memodifikasi collection yang sedang diiterasi kecuali kamu memahami konsekuensinya. Complexity kasar penting: mencari item dalam list umumnya O(n), sedangkan lookup set/dict rata-rata O(1). Optimisasi dimulai dari algoritme/data structure yang benar, bukan micro-optimization.

## 4. Function, scope, dan desain

Function menyatukan perilaku di balik nama, parameter, dan return value. Parameter adalah nama lokal; argument adalah nilai ketika dipanggil. Scope mengikuti LEGB: Local, Enclosing, Global, Built-in. Hindari global mutable karena membuat function sulit diuji. Function kecil dengan satu tanggung jawab, nama jelas, type hint, dan return eksplisit lebih mudah dikomposisi daripada script panjang.

Default argument dievaluasi sekali saat function didefinisikan. Karena itu jangan memakai `items=[]` sebagai default mutable; gunakan `None` lalu buat list di dalam function. `*args` mengumpulkan positional argument, `**kwargs` mengumpulkan keyword argument; gunakan bila API memang membutuhkan fleksibilitas, bukan untuk menyembunyikan kontrak function.

## 5. Error, testing, dan modul

Traceback dibaca dari bawah: exception terakhir memberi jenis error dan pesan, sedangkan frame di atasnya memberi jalur menuju masalah. Exception adalah bagian normal dari program: validasi input dan tangkap error yang dapat dipulihkan, tetapi jangan menangkap `Exception` luas tanpa tindakan. `assert` cocok untuk invariant internal, bukan validasi input pengguna di production.

Module adalah file Python yang dapat di-import; package adalah kumpulan module. Import menjalankan top-level code sekali per process lalu meng-cache module. Gunakan environment terisolasi agar dependency proyek tidak bercampur. Test unit memeriksa function kecil dengan input normal, batas, dan invalid; test integrasi memeriksa komponen bekerja bersama. Kode yang dapat diuji biasanya juga lebih mudah dipahami.
