# Lesson 5 — Iterator dan Generator

## Problem, context, why

File jutaan lines tidak muat memory. Kita ingin menghasilkan satu event, memprosesnya, lalu lanjut—tanpa membuat list lengkap.

## Intuisi dan mental model

Iterable adalah buku yang bisa dimulai; iterator adalah penanda halaman yang maju; generator adalah cara menulis iterator sebagai function yang dapat pause pada `yield`.

## Definition dan internal mechanism

`iter(obj)` menghasilkan iterator; `next` meminta item dan akhirnya `StopIteration`. Generator menyimpan frame/state di antara yields, lazy, dan sekali habis. Lazy berarti error juga dapat tertunda sampai item diminta.

## Small example

```python
def valid_numbers(lines):
    for line in lines:
        text = line.strip()
        if text:
            yield float(text)
```

### Predict/run/observe/explain

Buat generator, tetapi jangan iterate. Prediksi kapan `float` dijalankan dan kapan invalid line gagal. Observe saat `next` dipanggil.

## Hands-on experiment

Bandingkan list comprehension dengan generator expression untuk jumlah besar; ukur behavior, bukan mengklaim semua generator selalu lebih cepat.

## Workplace application

Digunakan untuk stream/file/batch pagination dan pipelines. Resource lifetime harus jelas bila generator membaca file.

## Common failure dan debugging

Iterator habis dipakai dua kali, error tertunda, generator tidak dikonsumsi, side effect order tersembunyi, dan file sudah tertutup. Inspect creation vs consumption boundary.

## Mini exercise/checkpoint

Buat generator JSONL yang yield valid events dan menghitung quarantine melalui object/context terpisah. Lulus bila dapat menjelaskan lazy execution.

## Penutup

**KAMU BARU BELAJAR:** iterator membawa state traversal; generator pause/resume secara lazy.

**KENAPA INI PENTING:** streams besar membutuhkan bounded memory.

**DI DUNIA KERJA DIPAKAI UNTUK:** ingestion, pagination, ETL, dan batch processing.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** behavior lintas function kadang dibungkus dengan decorator; gunakan dengan hati-hati di Lesson 6.
