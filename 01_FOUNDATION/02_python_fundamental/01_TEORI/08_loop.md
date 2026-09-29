# Lesson 8 — Loop dan Iteration

## Problem, context, why

Kamu mempunyai seribu readings. Menulis statement seribu kali tidak mungkin. Loop menerapkan behavior berulang sambil menjaga state dan termination.

## Intuisi dan mental model

`for` meminta item berikutnya dari iterable sampai habis. `while` mengulang selama condition True; programmer bertanggung jawab memastikan progress menuju stop.

```text
iterable → iterator → next item → body → state update → next ...
while: condition → body → state update → condition ...
```

## Definition dan internal mechanism

`for` bekerja melalui iteration protocol. `range` menghasilkan sequence angka secara lazy-like object. `enumerate` memberi index+item. `break` berhenti, `continue` melompat ke iteration berikutnya. Loop variable tetap name biasa setelah loop.

## Small manual example

```python
values = [10, None, 20]
total = 0
count = 0
for value in values:
    if value is None:
        continue
    total += value
    count += 1
```

### Predict → run → observe → explain

Trace `value,total,count` per iteration. Expected average valid adalah 15, tetapi code belum menghitung bila count zero—itu case berikutnya.

## Hands-on experiment

Uji empty list, semua `None`, dan input besar. Bandingkan loop yang membuat list baru dengan aggregation incremental.

## Workplace application

Loop memproses rows/events/files, melakukan retries terbatas, polling dengan timeout, dan batch aggregation. Untuk data sangat besar, streaming/generator mencegah memory penuh.

## Common failure dan debugging

Infinite `while`, off-by-one range, denominator zero, mutate collection saat iterasi, nested loop mahal, atau state tidak direset. Trace satu iteration kecil dan nyatakan loop invariant.

## Mini exercise dan checkpoint

Hitung min/max/mean valid tanpa `min/max/sum` dan tangani empty-valid case secara eksplisit. Lulus bila dapat menjelaskan termination dan state update.

## Penutup

**KAMU BARU BELAJAR:** loop mengulang behavior atas iterable atau condition dengan state/termination.

**KENAPA INI PENTING:** data dan events diproses sebagai collections/streams.

**DI DUNIA KERJA DIPAKAI UNTUK:** ETL, validation, aggregation, batching, dan polling.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** behavior loop perlu diberi nama dan contract agar reusable; Lesson 9 membahas function.
