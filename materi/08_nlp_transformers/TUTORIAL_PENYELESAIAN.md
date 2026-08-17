# Tutorial Penyelesaian — Level 08 NLP, Transformer, dan RAG

## Mulai dari baseline teks

Jangan langsung fine-tuning Transformer. Bersihkan duplikasi, pilih split yang mencegah dokumen serupa bocor, lalu buat TF-IDF + Logistic Regression. Baseline memberi pembanding biaya, latency, dan akurasi.

```python
model.fit(text_train, y_train)
pred = model.predict(text_test)
print(classification_report(y_test, pred))
```

Jika prediksi buruk, inspeksi teks salah, distribusi kelas, label ambigu, bahasa, panjang teks, dan contoh duplikat—bukan langsung menambah epoch.

## Embedding dan semantic search

Simpan `chunk_id`, teks, dokumen asal, halaman, dan embedding bersama-sama. Untuk query, embed query, hitung cosine similarity, ambil top-k, dan tampilkan sumber. Tambahkan threshold agar sistem dapat abstain bila tidak ada konteks relevan.

## RAG langkah demi langkah

1. Bersihkan dan chunk dokumen tanpa memotong konteks penting.
2. Buat index dan test query yang jawabannya diketahui.
3. Ukur `recall@k` sumber sebelum menggunakan LLM.
4. Kirim hanya context terambil dan instruksi untuk menyebut sumber.
5. Uji pertanyaan tanpa jawaban serta prompt injection dari dokumen.

Pisahkan error retrieval (sumber tidak ditemukan) dari error generation (sumber ada tetapi jawaban salah). Perbaikan keduanya berbeda.

## Keamanan

Jangan izinkan teks dokumen mengganti instruksi sistem. Redaksi PII sebelum indexing, batasi tool/action, dan log metadata aman tanpa isi percakapan sensitif.
