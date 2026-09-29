# Teori Mendalam — Level 02: Data Analysis

## 1. Data sebagai bukti, bukan sekadar tabel

Sebelum operasi apa pun, tentukan grain: satu baris mewakili apa? Satu transaksi, satu pelanggan per hari, satu sensor per menit, atau satu produk per gudang? Tanpa grain, join dan agregasi dapat menghasilkan angka salah tetapi tampak masuk akal. Buat data dictionary: nama kolom, arti bisnis, tipe, unit, allowed range, missing meaning, owner, dan waktu pembaruan.

Data mentah tidak netral. Ia dapat kehilangan baris, memiliki duplikasi, representasi kategori tidak konsisten, timestamp berbeda timezone, atau bias pengukuran. Cleaning adalah keputusan analitis yang harus dicatat: aturan apa, berapa baris berubah, dan mengapa aturan itu tepat.

## 2. NumPy: array, memory, dan vectorization

NumPy `ndarray` menyimpan elemen satu dtype dalam blok memori kontigu/berstrides sehingga operasi vektor dapat dieksekusi di C. Ini alasan ia lebih cepat daripada loop Python untuk operasi numerik besar. View berbagi memory dengan array asal, sedangkan copy independen; slicing sering menghasilkan view, advanced indexing sering menghasilkan copy. Perubahan tidak sengaja pada view adalah bug umum.

Broadcasting membandingkan shape dari dimensi terakhir: ukuran sama atau salah satunya 1 dapat diperluas. Ia membuat normalisasi matriks atau penambahan bias sangat ringkas. Tetapi selalu cek shape karena broadcasting dapat memperluas ke matriks besar atau menghasilkan operasi yang tidak dimaksud tanpa exception.

## 3. Pandas: index, Series, dan DataFrame

Series adalah data satu dimensi berlabel; DataFrame adalah collection Series dengan index bersama. Index membantu alignment: Pandas menyesuaikan label saat operasi, bukan sekadar posisi. Alignment mencegah sebagian kesalahan tetapi dapat menciptakan `NaN` bila label tidak cocok. `.loc` mengakses berdasarkan label, `.iloc` berdasarkan posisi. Chained indexing dapat menghasilkan view/copy ambigu; gunakan `.loc[mask, column] = value` untuk assignment eksplisit.

Tipe data menentukan perilaku. Angka yang tersimpan sebagai `object` tidak aman untuk agregasi; timestamp harus diparse dengan timezone/format yang diketahui; category dapat hemat memori dan mendefinisikan domain. Missing `NaN` menyebar melalui banyak operasi dan berbeda dari `0` atau string kosong. Putuskan apakah nilai hilang harus diimputasi, dibiarkan, dihapus, atau menjadi kategori sendiri berdasarkan makna prosesnya.

## 4. EDA dan visualisasi

EDA adalah proses membangun dan menguji hipotesis. Mulai dari shape, sample, schema, missing, duplicate, summary statistik, distribusi, segment, hubungan, dan waktu. Histogram memeriksa distribusi; boxplot memeriksa spread/outlier antar kelompok; scatterplot memeriksa hubungan; line chart memeriksa tren/seasonality. Pilih visualisasi dari pertanyaan, bukan sebaliknya.

Grafik harus memiliki judul informatif, label sumbu, unit, baseline bila relevan, dan tidak memanipulasi skala untuk membuat perbedaan kecil tampak ekstrem. Outlier bukan otomatis kesalahan: ia dapat berupa kasus bisnis penting, masalah instrumentasi, atau sinyal fraud. Investigasi sebelum menghapus.

## 5. Agregasi, join, dan reproducibility

`groupby` membagi data ke group lalu menerapkan agregasi. Tentukan denominator: `size` menghitung baris, `count` menghitung non-null, `nunique` menghitung identitas unik. Join membutuhkan key dengan uniqueness/cardinality yang diketahui. One-to-many normal; many-to-many dapat menggandakan nilai agregat. Selalu validasi row count dan sample setelah merge.

Analisis yang dapat diulang memisahkan raw data dari cleaned data, memakai function/configuration, menyimpan seed dan versi source, serta menghasilkan artefak yang dapat diperiksa. Notebook yang bergantung urutan cell tersembunyi tidak reproducible.
