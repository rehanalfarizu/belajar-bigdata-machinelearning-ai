# Claude Context — Materi Belajar Big Data / ML / AI

File ini adalah **sumber kebenaran** untuk proyek rewrite materi di folder `materi/`. Tujuannya: siapapun (termasuk Claude di session baru) bisa langsung paham konteks lengkap hanya dengan membaca 1 file ini.

Kalau Anda ingin Claude memulai sesi baru, cukup bilang: "Baca `_claude_context/CONTEXT.md` dulu, lalu lanjutkan dari status terbaru." Claude akan membaca file ini dan langsung paham apa yang harus dilakukan.

---

## Profil User

User adalah **pemula total** dalam Python dan programming. Target jangka panjangnya adalah **pindah karir menjadi data/ML engineer**. Cara belajar yang paling efektif untuk user adalah **analogi dunia nyata yang dikombinasikan dengan step-by-step eksekusi kode**. User bukan tipe yang cocok dengan teori panjang disusul kode panjang — user butuh pacing pelan: satu ide per cell, eksekusi, amati output, modifikasi, amati perubahan.

Format penjelasan yang user-friendly untuk user: **paragraf naratif utuh dalam bahasa Indonesia**, bukan bullet list panjang, bukan tabel besar, bukan emoji berlebihan. Namun **istilah teknis Python tetap dalam bahasa Inggris** karena itu adalah sintaksis — menerjemahkan "list comprehension" menjadi "pemahaman daftar" malah membuat bingung. Nada penulisan adalah menemani seperti teman yang sedang belajar bareng, bukan menggurui. Kalimat seperti "Anda harus ingat bahwa..." atau "Penting untuk diperhatikan..." harus dihindari, dan diganti dengan "Perhatikan bahwa...", "Coba amati...", "Apa yang terjadi kalau...".

User sering berhenti bekerja di tengah sesi karena kelelahan atau kantuk. Kebiasaan baik: selalu simpan progress ke task list sebelum berhenti, supaya sesi berikutnya bisa langsung lanjut tanpa mengulang dari awal.

---

## Status Proyek

Proyek ini adalah **rewrite total** folder `materi/` di repo ini. Versi lama materi menggunakan format yang tidak ramah pemula: cell kode langsung jadi tanpa breakdown, markdown penjelasan penuh dengan bullet dan tabel, dan struktur yang tidak konsisten antar chapter. Rewrite bertujuan mengubah semua materi menjadi format **naratif paragraf + step-by-step pacing**.

Progress saat ini:

- **Phase 0 selesai** — file `materi/TEMPLATE_CHAPTER.md` sudah dibuat sebagai acuan wajib semua chapter. File ini berisi pola 5-cell per section, checklist QA, template paragraf pembuka/penutup, dan daftar anti-pattern. Setiap chapter baru yang ditulis harus mengikuti acuan ini.
- **Phase 1 selesai 2026-06-02** — `materi/01_python_fundamental/` lengkap 5 file (utama 101 cell, praktikum 100 cell, typing_practice 31 cell, README naratif, PANDUAN_KODE 1196 baris). 8 section: variabel/tipe data, operator/string, struktur data, control flow, fungsi, error handling, modul/import, mini project to-do CLI.
- **Phase 2 selesai 2026-06-02** — `materi/02_data_analysis/` lengkap 5 file. 8 section: NumPy 1-4 (array, shape, vector, broadcasting), Pandas 5-7 (DataFrame, indexing, groupby/merge/missing), matplotlib 8 (visualisasi). Notebook 110 cell, praktikum ~82 cell, typing_practice 31 cell, README naratif, PANDUAN_KODE 453 baris.
- **Phase 3 selesai 2026-06-02** — `materi/03_ml_fundamental/` lengkap 5 file. 8 section: (1) Apa itu ML + supervised/unsupervised/reinforcement + X 2D/y 1D, (2) CRISP-DM + train/test split stratified, (3) Preprocessing scaling/encoding/pipeline, (4) Logistic Regression sigmoid+predict_proba, (5) KNN + pemilihan K dengan CV, (6) Decision Tree + Random Forest, (7) Regresi Linear/Ridge/Lasso, (8) Mini project end-to-end. Notebook utama 78 cell (49 md + 29 code), praktikum 48 cell (12 md + 36 code, 8 Latihan + Tantangan E2E + 3 Bonus), typing_practice 31 cell (10 soal bertingkat + referensi), README naratif ~50 baris, PANDUAN_KODE 11 bagian.
- **Phase 4 carry-over** — chapter 04 (ML Advanced: hyperparameter tuning, imbalanced data, time series, ensemble lanjutan) di `materi/04_ml_advanced/`. Format dan pola sama dengan chapter 01-03.
- **Phase 5 carry-over** — chapter 05 (Deep Learning) di `materi/05_deep_learning/`.
- **Phase 6 carry-over** — chapter 06 (MLOps/Deployment) di `materi/06_mlops/`. Mungkin perlu dipecah jadi 2 notebook (latihan/intro, deployment project) — lihat saat mulai.

---

## Keputusan yang Sudah Disetujui User

Ada 4 keputusan arsitektur besar yang sudah disetujui user. Keputusan pertama adalah **pemisahan peran file menjadi 3 kategori tegas**. `README.md` per chapter berfungsi sebagai navigasi tipis (150-200 baris), isinya cuma daftar isi, prasyarat, dan link ke file lain — BUKAN textbook. Notebook `.ipynb` adalah pengalaman belajar utama dengan format naratif. `PANDUAN_KODE.md` adalah referensi pattern + anti-pattern, BUKAN duplikat notebook. `praktikum.md` adalah latihan terstruktur + tantangan akhir. Tidak boleh ada duplikasi konsep antar file.

Keputusan kedua adalah **jumlah section di chapter 01 dikurangi dari 10 menjadi 8**. Section-section itu adalah: variabel dan tipe data, operator dan string, struktur data (List, Dict, Tuple, Set), control flow (if/elif/else, for, while), fungsi, error handling, modul, dan mini project. Versi lama yang 10 section terlalu tersebar.

Keputusan ketiga adalah **1 chapter = 1 notebook**, kecuali chapter 05 (Deep Learning) atau chapter 06 (MLOps) mungkin perlu dipecah kalau cell-nya melebihi 100. Standarnya tetap 1 chapter 1 notebook untuk konsistensi.

Keputusan keempat adalah **bahasa penjelasan**. Naratif dan analogi pakai bahasa Indonesia. Istilah teknis Python (function, loop, list, dict, tuple, set, lambda, comprehension, dan lain-lain) tetap bahasa Inggris. Pesan error Python juga jangan diterjemahkan — tampilkan apa adanya.

---

## Pola 5-Cell Per Section (Ringkas)

Setiap section di notebook mengikuti pola 5 cell. Cell pertama adalah **markdown naratif** sepanjang 1-3 paragraf berisi pengenalan konsep dengan analogi dunia nyata. Cell kedua adalah **markdown ajakan** yang eksplisit meminta pembaca mengetik kode. Cell ketiga adalah **code cell** berisi kode mini 3-8 baris yang bisa langsung dijalankan. Cell keempat adalah **markdown breakdown** yang menjelaskan apa yang terjadi di balik layar. Cell kelima adalah **code cell modifikasi** yang mengajak pembaca mengubah kode di cell ketiga dan mengamati perubahannya. Section ditutup dengan **mini-check refleksi** 1-2 pertanyaan terbuka.

Detail lengkap ada di `materi/TEMPLATE_CHAPTER.md`. File itu wajib dibaca sebelum menulis atau mengedit chapter baru.

---

## Daftar File yang Akan Dimodifikasi (Phase 1)

Phase 1 mengerjakan 5 file di `materi/01_python_fundamental/`. Daftar file dalam urutan eksekusi: pertama `README.md` (rewrite tipis jadi navigasi), kedua `QUICKSTART.md` (rewrite setup environment step-by-step), ketiga `01_python_fundamental.ipynb` (rewrite total jadi 8 section × 5 cell = sekitar 40 cell), keempat `PANDUAN_KODE.md` (rewrite jadi referensi pattern + anti-pattern), kelima `praktikum.md` (rewrite jadi latihan bertingkat + tantangan mini project). Setelah kelimanya selesai, user akan review dan konfirmasi sebelum lanjut ke Phase 2.

---

## File Pendukung yang Bisa Diabaikan

Ada 2 file yang tidak perlu di-rewrite untuk Phase 1 karena isinya masih relevan: `materi/_claude_context/CONTEXT.md` (file ini) dan `materi/TEMPLATE_CHAPTER.md` (sudah selesai). File plan di `/Users/macbookpro/.claude/plans/golden-soaring-token.md` adalah rencana eksternal yang tidak masuk repo — abaikan saja.

---

## Catatan Tambahan

User lebih nyaman dengan **paragraf naratif** dalam bahasa percakapan. Kalau di tengah kerja Claude mulai menulis bullet list atau tabel untuk penjelasan, user biasanya minta diubah. Selalu ingat: ini materi untuk **pemula total**, jadi setiap konsep harus terasa "ditemani" — tidak menggurui, tidak menghakimi, tidak menggurui berlebihan.

Estimasi total rewrite: Phase 0 butuh 1-2 jam (selesai), Phase 1 butuh 8-12 jam, Phase 2-6 butuh 6-8 jam per chapter. Total 40-55 jam kerja, dilakukan bertahap dengan review user di setiap phase.

Kalau Claude di session baru membaca file ini dan status di atas mengatakan "Phase 1 carry-over", maka langsung mulai dari `01_python_fundamental/README.md` dan kerjakan 5 file secara berurutan. Setelah selesai, tanyakan ke user apakah formatnya cocok sebelum lanjut ke chapter 02.
