# Template Penulisan Chapter

File ini adalah acuan internal untuk chapter di delapan kelompok kompetensi repository. Tujuannya menjaga konsistensi tanpa memaksa semua topik ke bentuk yang sama. Struktur topik pemula, sistem terdistribusi, simulation, dan research boleh berbeda selama learning outcome, assumptions, experiment, test, dan gate-nya jelas.

Setiap topik idealnya menjawab: sejarah/konteks, masalah, alasan muncul, mental model, teori/matematika, cara kerja internal, implementasi minimal, implementasi library, contoh, eksperimen, kesalahan/anti-pattern, best practice, debugging, latihan/challenge/project, checkpoint, serta hubungan ke Digital Twin. Jangan membuat file hanya untuk memenuhi nama; satu README yang utuh lebih baik daripada enam placeholder.

## Prinsip Dasar

Penulisan materi di repo ini mengikuti tiga prinsip. Setiap chapter yang ditulis harus menghormati ketiganya. Prinsip pertama adalah **naratif, bukan daftar**. Penjelasan ditulis dalam bentuk paragraf utuh, bukan bullet point atau tabel. Bullet dan tabel hanya dipakai untuk data yang memang tidak cocok dituangkan dalam kalimat (misalnya daftar library, atau signature fungsi). Prinsip kedua adalah **bertahap, bukan sekaligus**. Satu cell notebook hanya menyampaikan satu ide. Kalau ada tiga konsep yang harus dikenalkan, pecah jadi tiga cell markdown, bukan satu cell besar berisi ketiganya. Prinsip ketiga adalah **eksperimentasi, bukan demonstrasi**. Tujuan utama notebook bukan menunjukkan kode yang jalan, tapi mengajak pembaca memodifikasi kode dan mengamati sendiri apa yang berubah.

## Struktur Per Section (Pola 5-Cell)

Untuk notebook beginner, pola 5 cell berikut adalah default, bukan syarat mekanis. Section advanced boleh memakai derivasi→implementation→experiment→visualization→evaluation selama urutannya jelas dan cell tetap dapat dijalankan berurutan.

Cell pertama adalah **markdown naratif**. Panjangnya 1-3 paragraf. Isinya pengenalan konsep dengan analogi dunia nyata, penjelasan "kenapa" konsep itu ada, dan apa masalah yang dipecahkan. Tidak boleh ada kode di cell ini. Cell kedua adalah **markdown ajakan**. Satu paragraf pendek yang mengajak pembaca mengetik kode tertentu di cell berikutnya. Ajakan ini harus eksplisit ("Sekarang coba ketik ini"), bukan pasif ("Berikut adalah contoh"). Cell ketiga adalah **code cell**. Kode di sini harus mini, idealnya 3-8 baris, dan harus bisa dijalankan tanpa error ketika cell dieksekusi. Output dari cell ini akan dipakai di cell breakdown, jadi pastikan outputnya informatif. Cell keempat adalah **markdown breakdown**. Satu paragraf yang menjelaskan apa yang terjadi di balik layar ketika kode di cell tiga dijalankan. Cell ini menjawab pertanyaan "kenapa outputnya begitu" dan "apa yang sebenarnya dilakukan Python saat eksekusi baris itu". Cell kelima adalah **code cell modifikasi**. Berisi 1-3 baris kode yang merupakan modifikasi dari kode di cell tiga. Ajakan sebelumnya di cell dua sudah menyebutkan modifikasi ini, jadi cell lima tinggal menjalankan. Setelah cell modifikasi, section ditutup dengan **mini-check refleksi** — 1-2 pertanyaan terbuka (bukan pilihan ganda) yang memancing pembaca berpikir.

## Anjuran Bahasa dan Nada

Penjelasan naratif ditulis dalam bahasa Indonesia. Namun istilah teknis Python dipertahankan dalam bahasa Inggris. Ini bukan konsistensi yang setengah hati — ini disengaja. Alasannya, istilah seperti "list comprehension", "f-string", "lambda function" adalah konsep Python yang kalau diterjemahkan malah rancu (terjemahan "list comprehension" jadi "pemahaman daftar" tidak membantu). Pembaca yang sudah pernah lihat dokumentasi Python akan langsung mengenali istilah ini, dan pembaca pemula akan cepat terbiasa karena melihatnya berulang. Nada penulisan adalah **menemani**, bukan **menggurui**. Hindari kalimat seperti "Anda harus ingat bahwa..." atau "Penting untuk diperhatikan...". Ganti dengan nada percakapan: "Perhatikan bahwa...", "Coba amati...", "Apa yang terjadi kalau...". Pembaca diperlakukan sebagai teman yang sedang belajar bareng, bukan murid yang harus patuh.

## Checklist QA Per Section

Sebelum sebuah section dianggap selesai, harus lolos checklist berikut. Pertama, ada minimal satu analogi dunia nyata. Analogi boleh datang dari kehidupan sehari-hari (dapur, jalan raya, kantor pos) atau dari bidang lain (ekonomi, biologi). Yang penting pembaca bisa "merasakan" konsepnya, bukan hanya memahaminya secara abstrak. Kedua, kode mini di cell tiga maksimal 8 baris. Kalau lebih dari 8 baris, pecah jadi dua section atau dua sub-langkah. Ketiga, cell breakdown menjelaskan minimal satu hal yang tidak langsung terlihat dari kode (misalnya kenapa list indexing mulai dari 0, atau kenapa `==` berbeda dari `=`). Keempat, cell modifikasi benar-benar mengajak perubahan yang observable. Jangan cuma minta mengubah string statis — minta pembaca mengubah logika, seperti membalik kondisi, atau mengganti operator, supaya output berubah dengan cara yang bermakna. Kelima, mini-check refleksi benar-benar terbuka, bukan "apakah kamu paham?" yang jawabannya ya/tidak. Contoh refleksi yang baik: "Menurut kamu, kapan lebih tepat pakai tuple dibanding list? Coba pikirkan satu skenario selain koordinat GPS."

## Daftar Anti-Pattern

Berikut adalah hal-hal yang harus dihindari. Pertama, **jangan copy-paste teori dari dokumentasi resmi**. Materi di repo ini bukan terjemahan dokumentasi. Kalau pembaca butuh dokumentasi resmi, mereka bisa ke docs.python.org. Materi di sini harus terasa "manusiawi" dan kontekstual. Kedua, **jangan masukkan kode 20+ baris dalam satu cell**. Kode panjang harus dipecah. Setiap chunk kode yang melakukan satu hal harus jadi cell sendiri. Ketiga, **jangan pakai emoji atau ikon berlebihan** di markdown naratif. Emoji hanya dipakai untuk penanda struktural (misalnya "Catatan" atau "Peringatan"), bukan untuk mempermanis kalimat. Keempat, **jangan ada duplikasi konsep antar file**. Kalau notebook sudah menjelaskan list comprehension, PANDUAN_KODE.md cukup merujuk dan menunjukkan variasi, tidak mengulang penjelasan dari awal. Kelima, **jangan pakai bahasa yang menggurui atau menghakimi** seperti "pemula yang benar-benar bodoh akan...", atau "kesalahan yang memalukan". Ganti dengan nada netral: "kesalahan yang umum terjadi" atau "jebakan yang sering ditemui".

## Template Paragraf Pembuka Section

Gunakan template ini sebagai titik mulai, lalu sesuaikan. Pembuka section yang baik dimulai dengan **menghubungkan ke konsep sebelumnya**. Contoh: "Di section sebelumnya kita sudah lihat bagaimana variabel bekerja sebagai label untuk data. Sekarang kita perlu cara untuk **mengorganisir banyak data sekaligus** — dan di sinilah list berperan." Lalu lanjutkan ke analogi. Setelah analogi, **transisi ke kode**: "Mari kita coba sendiri. Ketik kode berikut di cell bawah...". Penutup section harus berupa **jembatan ke section berikutnya**: "Sekarang kamu sudah bisa menyimpan banyak data dalam satu variabel. Tapi bagaimana kalau kita ingin **melakukan operasi pada setiap elemen** list itu? Itu akan kita pelajari di section berikut."

## Template untuk README.md (Per Chapter)

README selalu menjadi entrypoint dan bagian paling atas memakai “Mulai dari sini”. README menjawab mengapa chapter penting, prasyarat, outcome, urutan material, gate, project, serta Previous/Current/Next. Materi mengikuti `01_TEORI` sampai `09_CHECKPOINT` hanya bila ada isi nyata; solution ditempatkan di `99_SOLUTIONS`. Setiap klaim standard/protocol yang dapat berubah harus merujuk sumber authoritative serta menyatakan scope-nya.

## Template untuk praktikum.md (Per Chapter)

Praktikum berisi latihan dan tantangan. Format latihan: paragraf naratif yang menjelaskan konteks (misalnya, "Bayangkan Anda sedang membuat sistem penilaian untuk sekolah..."), lalu soal yang diminta. Tiap section punya 3-5 soal bertingkat. Level 1 adalah modifikasi kode (ubah angka, ubah string). Level 2 adalah menerjemahkan soal cerita ke kode. Level 3 adalah bikin dari nol dengan guidance. Tantangan akhir chapter adalah mini project yang menggabungkan semua section. Tantangan tidak boleh memberikan kode sample — siswa harus bangun sendiri.

## Template untuk PANDUAN_KODE.md (Per Chapter)

PANDUAN_KODE adalah **referensi ringkas**, bukan duplikat notebook. Isinya adalah pattern Pythonic (idiom) yang umum dipakai di chapter itu, plus anti-pattern yang harus dihindari. Untuk setiap pattern: paragraf pendek "kenapa ini ada", kode minimal 3-5 baris yang mengilustrasikan, dan paragraf "kapan dipakai" atau "kapan hindari". Daftar pattern yang masuk PANDUAN_KODE diputuskan per chapter — tidak semua pattern Pythonic relevan untuk chapter pemula, dan tidak semua yang dipakai di chapter lanjut perlu ada di PANDUAN_KODE.

## Quality gate teknis

- Semua code fence berlabel `python` harus valid syntax; contoh yang sengaja salah diberi label `text` dan dijelaskan.
- Notebook valid JSON, memiliki tujuan/teori/implementasi/eksperimen/visualisasi/latihan/checkpoint, dan dapat dijalankan berurutan setelah dependency resmi dipasang.
- Domain logic penting dipindahkan ke `src/` dan diuji; notebook menjadi experiment/interface, bukan satu-satunya source of truth.
- Gunakan relative path, timezone-aware timestamp, explicit unit, seeded randomness, dan temporal split bila relevan.
- Jangan commit `.DS_Store`, credentials, cache, atau generated model artifact tanpa alasan/versioning yang jelas.
- Laporkan batas verifikasi: parse statis berbeda dari execution test; simulator berbeda dari validasi aset nyata.
