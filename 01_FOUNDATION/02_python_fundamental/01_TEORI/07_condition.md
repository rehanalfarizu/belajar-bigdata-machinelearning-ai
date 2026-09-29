# Lesson 7 — Condition dan Branching

## Problem, context, why

Sensor value harus diterima, dikarantina, atau ditolak. Program memerlukan decision rule yang eksplisit, dapat ditelusuri, dan mencakup boundary.

## Intuisi dan mental model

Condition seperti persimpangan: satu expression boolean memilih branch. Urutan `if/elif` penting karena branch pertama yang True dijalankan.

```text
input
  ↓ valid type?
 no → reject
 yes ↓ in range?
 no → quarantine
 yes → accept
```

## Definition dan internal mechanism

`if/elif/else` mengontrol statement mana dijalankan. Python memakai truthiness: empty collection/string, zero, `None`, dan `False` adalah falsy. Tetapi “missing” tidak selalu sama dengan zero/empty; gunakan rule domain yang jelas.

## Small manual example

```python
value = 150
if value < -50 or value > 150:
    status = "reject"
elif value > 100:
    status = "review"
else:
    status = "accept"
```

### Predict → run → observe → explain

Prediksi status tepat pada -50, 100, dan 150. Tulis decision table agar operator `<` vs `<=` terlihat.

## Hands-on experiment

Ubah urutan branches dan amati unreachable/misclassified case. Buat test table sebelum code, lalu cocokkan semua rows.

## Workplace application

Condition membentuk validation, access policy, routing, alert threshold, dan fallback. Decision table membantu reviewer menemukan gap/overlap.

## Common failure dan debugging

Boundary off-by-one, branch terlalu umum di atas, truthiness menggantikan missing rule, dan nested condition terlalu dalam. Trace condition values dan sederhanakan dengan guard clauses bila sesuai.

## Mini exercise dan checkpoint

Rancang decision table untuk status battery: invalid, critical, low, normal, overvoltage. Sertakan exact boundaries dan `None`.

## Penutup

**KAMU BARU BELAJAR:** branch dipilih oleh boolean expression dan urutan/range matters.

**KENAPA INI PENTING:** decision rule yang ambigu menghasilkan behavior tidak konsisten.

**DI DUNIA KERJA DIPAKAI UNTUK:** validation, alerts, routing, permissions, dan fallbacks.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** keputusan sering diterapkan berulang pada banyak item; Lesson 8 membahas loop.
