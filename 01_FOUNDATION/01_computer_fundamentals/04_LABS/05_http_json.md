# Lab 05 — HTTP Request/Response dan JSON

## 1. TUJUAN

Mengamati status, header, body, serta memisahkan kegagalan HTTP dari kegagalan parsing JSON.

## 2. PREREQUISITE

Baca lesson 05. Gunakan `local_json_server.py` di folder lab dan dua terminal.

## 3. SETUP

Jalankan `python local_json_server.py`. Baca output untuk mengetahui port, tetapi jangan membuka kode server dahulu.

## 4. PREDICTION BEFORE RUN

Prediksi status dan bentuk body untuk `/health` serta `/missing`. Apakah respons 404 masih dapat berisi JSON valid?

## 5. LANGKAH PRAKTIKUM

Tulis client kecil dengan `urllib.request.urlopen` untuk `/health`; cetak status, content type, bytes mentah, lalu hasil `json.loads`. Tangani `urllib.error.HTTPError` untuk membaca body `/missing`.

## 6. OBSERVATION

Catat request path, status, content type, body mentah, dan object Python setelah parsing.

## 7. WHY

HTTP mengatur pertukaran pesan; JSON hanya format representasi body. Status gagal tidak otomatis berarti JSON tidak valid.

## 8. MODIFICATION

Tambahkan endpoint `/sensor` pada server yang mengembalikan name dan value. Prediksi Content-Length lalu bandingkan hasil aktual.

## 9. FAILURE EXPERIMENT

Sengaja kirim body bukan JSON tetapi header `application/json`, kemudian jalankan parser.

## 10. DEBUGGING

Pisahkan pemeriksaan transport, status, header, bytes, decoding UTF-8, dan parsing. Perbaiki layer yang salah lalu ulangi client.

## 11. WORKPLACE CONNECTION

Di dunia kerja ini muncul pada API data/ML, webhook, health endpoint, service integration, dan observability.

## 12. CHECKPOINT

Buat endpoint dan client baru; tunjukkan satu respons sukses, satu 404 JSON, dan satu kegagalan parsing beserta diagnosis layer-nya.
