# Lab 03 — Dot Product dan Similarity

## 1. TUJUAN
Menghubungkan dot product dengan weighted sum, alignment, dan similarity.

## 2. PREREQUISITE
Baca lesson 02.

## 3. SETUP
Pilih `a=[1,2]` dan `b=[3,4]`; gambar arah keduanya.

## 4. PREDICTION BEFORE RUN
Hitung manual `1×3 + 2×4` dan prediksi tanda untuk vector searah, tegak lurus, berlawanan.

## 5. LANGKAH PRAKTIKUM
Panggil `dot` untuk tiga pasangan; buat bar ASCII positif/negatif terhadap nol.

## 6. OBSERVATION
Bandingkan manual, kode, arah gambar, dan tanda dot.

## 7. WHY
Dot menjumlah kontribusi pasangan komponen; besar mentah juga dipengaruhi norm.

## 8. MODIFICATION
Skalakan satu vector dan bandingkan dot dengan cosine `dot/(norm(a)norm(b))`.

## 9. FAILURE EXPERIMENT
Berikan panjang vector berbeda atau simpulkan similarity hanya dari dot besar.

## 10. DEBUGGING
Periksa shape dan normalisasi; pisahkan pertanyaan magnitude dari direction.

## 11. WORKPLACE CONNECTION
Di dunia kerja ini muncul pada scoring linear, rekomendasi, attention, dan similarity embedding.

## 12. CHECKPOINT
Buat pasangan vector, jelaskan intuisi, hitung, kodekan, visualisasikan, ubah skala, dan interpretasikan.
