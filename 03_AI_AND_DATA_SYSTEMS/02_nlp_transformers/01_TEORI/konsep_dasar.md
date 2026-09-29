# Level 08 — NLP, Transformer, dan Generative AI

## 1. Representasi teks

Tokenisasi memecah teks menjadi unit yang dapat diproses model. Bag-of-words/TF-IDF adalah baseline sparse yang kuat dan mudah dijelaskan. Embedding dense memetakan token atau dokumen ke ruang vektor; cosine similarity membandingkan arah, bukan besaran.

## 2. Supervised NLP

Pisahkan dokumen berdasarkan sumber/penulis/waktu bila ada dependensi; random split dapat menyebabkan duplikasi bocor. Mulai dari TF-IDF + Logistic Regression, lalu bandingkan model pretrained. Metrik harus melihat kelas minoritas dan calibration.

## 3. Attention dan Transformer

Self-attention menghitung `softmax(QKᵀ / sqrt(d_k))V`. Query mencari informasi, key mencocokkan, value membawa isi. Multi-head attention mempelajari relasi dari beberapa subruang. Residual connection dan normalization membantu optimisasi. Encoder cocok untuk representasi/klasifikasi; decoder autoregressive menghasilkan token berikutnya; encoder-decoder cocok untuk sequence-to-sequence.

## 4. Pretraining dan fine-tuning

Pretraining belajar pola umum dari data besar; fine-tuning menyesuaikan tugas. Bedakan full fine-tuning, parameter-efficient tuning, prompting, dan retrieval. Catat tokenizer, max length, truncation, padding, label mapping, dan versi model.

## 5. RAG

RAG memisahkan pengetahuan dari parameter model: ingest → cleaning → chunking → embedding → index → retrieval → optional reranking → prompt → generation. Evaluasi retrieval recall/precision dan jawaban (faithfulness, relevance, citation) secara terpisah. Jangan menganggap jawaban fasih sebagai jawaban benar.

## 6. Keamanan dan biaya

Tangani prompt injection, data poisoning, PII, secret leakage, jailbreak, copyright, hallucination, context overflow, latency, dan biaya token. Terapkan allowlist tools, sandbox, redaction, access control, rate limit, audit log, dan human review untuk aksi berisiko.

## Proyek

Buat sentiment classifier baseline, semantic search atas dokumen lokal, lalu RAG yang mengembalikan kutipan sumber. Laporan wajib membandingkan baseline, retrieval hit-rate, latency, dan failure cases.
