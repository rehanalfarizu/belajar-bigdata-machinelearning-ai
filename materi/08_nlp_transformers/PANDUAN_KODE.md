# Panduan Kode Level 08

## Baseline TF-IDF

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
    ("clf", LogisticRegression(max_iter=1000)),
])
model.fit(text_train, y_train)
```

Fit vectorizer hanya pada train melalui pipeline. Periksa stopword, bahasa, negasi, panjang teks, dan duplikasi sebelum menyimpulkan model.

## Embedding dan retrieval

Normalisasi embedding membuat dot product setara cosine similarity. Simpan ID dokumen dan metadata di samping vector index agar jawaban dapat menyertakan sumber. Uji query yang tidak memiliki jawaban; sistem seharusnya dapat mengatakan “tidak ditemukan”.

## Evaluasi generatif

Buat dataset pertanyaan dengan expected source. Ukur retrieval recall@k, answer relevance, groundedness, citation correctness, refusal correctness, latency p50/p95, dan biaya per request. Evaluasi manusia tetap diperlukan untuk kualitas yang tidak tertangkap metrik otomatis.
