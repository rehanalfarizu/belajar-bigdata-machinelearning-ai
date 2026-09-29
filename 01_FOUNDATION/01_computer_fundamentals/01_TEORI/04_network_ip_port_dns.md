# Lesson 4 — Network, IP, Port, Localhost, dan DNS

## Problem

Browser berkata “connection refused” saat membuka `http://localhost:8000`. Apakah internet mati? Belum tentu. Kemungkinan tidak ada process yang mendengarkan port 8000, server memakai port lain, atau address binding berbeda.

## Context dan why

API, database, notebook server, message broker, dan dashboard berkomunikasi lewat network. Tanpa model IP/port, diagnosis sering berhenti pada “tidak bisa connect”.

## Intuisi dan mental model

IP seperti alamat gedung; port seperti nomor loket; protocol seperti aturan percakapan. DNS seperti buku kontak yang menerjemahkan nama menjadi address—bukan jalur pengiriman datanya.

```text
client process
  → resolve hostname lewat DNS (jika memakai nama)
  → destination IP + port
  → network stack/routing
  → host tujuan
  → listening socket pada port
  → server process
```

## Definition dan internal mechanism

**Network** menghubungkan endpoints yang bertukar packets/bytes. **IP address** mengidentifikasi network interface dalam suatu scope. **Port** mengidentifikasi transport endpoint pada host. **localhost** biasanya mengarah ke loopback milik komputer sendiri; traffic tidak pergi ke internet. **DNS** memetakan hostname ke record seperti IP.

Server membuat socket, bind ke address/port, lalu listen. `127.0.0.1` hanya dapat diakses lokal; `0.0.0.0` berarti menerima pada semua interface IPv4 yang sesuai, tetapi bukan address tujuan untuk client. Firewall dan container/VM boundaries tetap dapat membatasi akses.

## Small manual example

Host `127.0.0.1`, port `8000` berbeda endpoint dari host sama port `8001`. Dua server tidak dapat bind tuple address/port yang sama pada kondisi normal.

## Hands-on experiment

Terminal A:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Terminal B:

```bash
curl -I http://127.0.0.1:8000
```

### Predict before run

Prediksi hasil port 8000 saat server hidup, port 8001 tanpa server, dan apa yang terjadi bila server kedua mencoba port 8000.

### Observe dan explain

Expected: 8000 mengembalikan HTTP headers; 8001 gagal connect; server kedua mendapat “address already in use”. Network address harus berakhir pada listening process.

## Workplace application

Engineer memeriksa client address, DNS result, route, firewall, listening port, service health, dan protocol—berurutan. “Ping berhasil” tidak membuktikan application port atau HTTP route sehat.

## Common failures dan debugging

- connection refused: host reachable tetapi tidak ada listener/ditolak.
- timeout: packets/response tidak kembali dalam batas waktu; penyebab bisa routing, firewall, overload, atau server hang.
- wrong host: `localhost` dari container menunjuk container itu sendiri.
- DNS failure: nama tidak resolve; menguji IP dapat membantu membedakan, tetapi bukan fix final.
- port conflict: identifikasi owner process sebelum menghentikannya.

## Problem solving dan checkpoint

1. Mengapa `localhost` di laptop dan container tidak selalu menunjuk process yang sama?
2. Susun langkah diagnosis dari URL sampai server process.
3. Jelaskan mengapa DNS sukses belum membuktikan port terbuka.

## Penutup

**KAMU BARU BELAJAR:** hostname/IP menemukan host; port menemukan service endpoint; localhost adalah loopback lokal.

**KENAPA INI PENTING:** semua service data/AI memakai network boundary.

**DI DUNIA KERJA DIPAKAI UNTUK:** API, database, broker, dashboards, dan distributed jobs.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** setelah endpoint ditemukan, client dan server masih butuh protocol; Lesson 5 menjelaskan TCP, HTTP, JSON, dan API.
