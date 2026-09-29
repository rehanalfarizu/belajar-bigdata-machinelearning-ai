# Lesson 5 — TCP, HTTP, Request/Response, JSON, dan API

## Problem

Koneksi ke port server berhasil, tetapi application memberi `404`, `400`, atau JSON tidak dapat dibaca. Network path tersedia, tetapi percakapan application salah.

## Context dan why

Service modern bertukar request dan response. Memisahkan transport, protocol, representation, dan application contract membantu menemukan boundary yang benar saat gagal.

## Intuisi dan mental model

TCP seperti saluran telepon yang menjaga urutan bytes. HTTP adalah aturan giliran bicara dan format pesan. JSON adalah salah satu cara menulis isi pesan. API adalah kontrak layanan: operasi apa tersedia, input/output, error, dan version.

```text
API contract
  ↓ direpresentasikan sebagai JSON bytes
HTTP request/response
  ↓ dikirim lewat ordered TCP byte stream
IP packets
  ↓ melewati network
server parse → validate → execute → respond
```

## Definition dan internal mechanism

**TCP** menyediakan connection-oriented ordered byte stream; ia tidak memahami JSON atau business operation. **HTTP** mendefinisikan method, target, headers, body, status, dan response. **JSON** merepresentasikan object/array/string/number/boolean/null; JSON tidak menjamin schema, unit, timezone, atau semantic meaning. **API** adalah interface contract antarsoftware.

Client resolve/connect, mengirim HTTP bytes, server parse request, route berdasarkan method/path, validate input, menjalankan behavior, serialize response, dan menutup/menjaga connection. Timeout dan partial failure tetap mungkin; response yang hilang tidak membuktikan server tidak memproses request.

## Small manual example

```text
GET /health HTTP/1.1
Host: 127.0.0.1:8000

HTTP/1.1 200 OK
Content-Type: application/json

{"status":"ok"}
```

Status `200` adalah HTTP outcome; isi `{"status":"ok"}` adalah JSON representation; arti “healthy” tetap harus didefinisikan API.

## Hands-on experiment

Jalankan `04_LABS/local_json_server.py`, lalu:

```bash
curl -i http://127.0.0.1:8765/health
curl -i http://127.0.0.1:8765/missing
```

### Predict before run

Prediksi status, `Content-Type`, dan body kedua request. Apakah JSON valid selalu berarti request berhasil?

### Observe dan explain

Expected: `/health` memberi 200 JSON; route lain 404 JSON. Transport berhasil pada keduanya; application outcome berbeda.

## Workplace application

Digunakan pada data ingestion, model inference API, dashboard backend, cloud service, dan Digital Twin state service. Contract production mencakup auth, validation, idempotency, pagination/versioning, timeouts, errors, dan observability.

## Common failures dan debugging

- invalid JSON: lihat raw body dan posisi parse error; jangan menebak schema.
- `400`: request tidak memenuhi contract.
- `404`: route/resource tidak ditemukan, bukan otomatis server mati.
- `500`: server gagal; correlation ID/log membantu diagnosis.
- timeout: outcome mungkin unknown; retry hanya aman bila operation idempotent atau punya key.
- wrong `Content-Type`: bytes mungkin benar tetapi receiver memilih parser salah.

## Problem solving dan checkpoint

1. Bedakan network failure, HTTP error, JSON parse error, dan business validation error.
2. Mengapa retry POST dapat menggandakan transaksi?
3. Desain response error yang membantu client tanpa membocorkan secret.

## Penutup

**KAMU BARU BELAJAR:** TCP membawa bytes, HTTP membentuk pesan, JSON merepresentasikan data, API menetapkan kontrak.

**KENAPA INI PENTING:** layered diagnosis mencegah fix pada lapisan yang salah.

**DI DUNIA KERJA DIPAKAI UNTUK:** integration, inference, ingestion, service debugging, dan automation.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** source/config API berubah bersama tim; Lesson 6 menjelaskan bagaimana Git melacak dan menggabungkan perubahan.
