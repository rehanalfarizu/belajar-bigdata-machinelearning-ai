# Praktikum Level 08

## Latihan 1 — TF-IDF

Buat dataset sentiment minimal 30 dokumen. Split stratified, latih baseline, tampilkan confusion matrix, dan inspeksi fitur dengan bobot terbesar per kelas.

## Latihan 2 — Leakage teks

Tambahkan duplikasi dokumen ke train dan test. Bandingkan skor sebelum dan sesudah deduplication. Jelaskan mengapa skor tinggi akibat duplikasi bukan generalisasi.

## Latihan 3 — Semantic search

Buat 20 dokumen pendek, hitung embedding dengan model sentence-transformers, cari top-k menggunakan cosine similarity, dan tampilkan metadata sumber. Tambahkan query di luar domain dan buat threshold abstain.

## Latihan 4 — RAG

Buat lima pertanyaan dengan sumber jawaban. Implementasikan chunk-retrieve-prompt. Ukur recall sumber pada k=1,3,5, lalu dokumentasikan pertanyaan yang gagal.

## Tantangan

Tambahkan prompt injection di salah satu dokumen. Rancang instruksi dan filter sehingga isi dokumen tidak dapat mengubah kebijakan sistem.
