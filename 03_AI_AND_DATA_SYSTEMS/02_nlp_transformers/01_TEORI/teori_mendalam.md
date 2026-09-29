# Teori Mendalam — Level 08: NLP, Transformer, dan Generative AI

## 1. Teks dan representasi

Teks adalah simbol yang context-dependent. Tokenization mengubah teks menjadi unit ID; pilihan token memengaruhi panjang sequence, vocabulary, bahasa, typo, dan biaya. Bag-of-words/TF-IDF mengabaikan banyak urutan/context tetapi tetap baseline kuat, interpretable, cepat, dan penting sebagai pembanding model besar. Embedding dense memetakan token/dokumen ke ruang vektor tempat kedekatan merepresentasikan pola training, bukan kebenaran semantik universal.

## 2. Attention dan Transformer

Setiap token membuat query, key, value. Similarity query-key menentukan bobot attention, lalu value digabung. Multi-head attention belajar beberapa jenis hubungan paralel. Positional encoding memberi informasi urutan karena attention sendiri permutation-invariant. Residual connection menjaga aliran informasi/gradient, layer normalization menstabilkan scale, feed-forward layer menambah transformasi non-linear per token.

Encoder menggunakan context dua arah dan cocok untuk representation/classification. Decoder memakai causal mask agar token tidak melihat masa depan dan cocok menghasilkan sequence. Encoder-decoder menghubungkan input-output untuk translation/summarization. Transformer memprediksi distribusi token berikutnya; output fasih tidak menjamin benar, aktual, atau bersumber.

## 3. Pretraining, fine-tuning, dan evaluasi

Pretraining belajar statistik corpus besar dengan objective seperti masked/next-token prediction. Fine-tuning mengadaptasi ke task khusus, tetapi dapat overfit data kecil atau memperkuat bias. Prompting, few-shot, PEFT, full fine-tuning, dan retrieval adalah pilihan berbeda dalam biaya, control, latency, dan data requirement. Evaluasi harus mencakup slice bahasa/domain, class imbalance, calibration, safety, serta example-level error—not just leaderboard aggregate.

## 4. Retrieval augmented generation

RAG menambahkan context eksternal: parse, clean, chunk, embed, index, retrieve, optional rerank, prompt, generate, cite. Chunk size/overlap, embedding model, metadata filter, index, query rewrite, dan prompt semuanya memengaruhi hasil. Ukur retrieval (recall@k, MRR, source coverage) terpisah dari generation (faithfulness, relevance, citation correctness). Jika source tidak ditemukan, generator sebaiknya abstain.

## 5. Safety dan governance

Prompt injection, malicious document, PII, copyright, hallucination, tool misuse, token cost, and data retention adalah risiko desain. Dokumen retrieved adalah untrusted data, bukan system instruction. Terapkan access control per dokumen, redaction, allowlist tools, structured output, sandbox, rate limit, human approval untuk aksi penting, serta audit yang tidak menyimpan teks sensitif lebih lama dari perlu.
