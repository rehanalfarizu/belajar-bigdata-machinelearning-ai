# Lesson 02 — Data Quality sebagai Contract

## Problem dan why

Pipeline dapat selesai tanpa error sambil menghasilkan keputusan salah. “File berhasil dibaca” bukan bukti data dapat dipercaya.

## Mental model

Quality mempunyai dimensi: completeness, uniqueness, validity, consistency, timeliness, dan referential integrity. Contract mengubah harapan menjadi pemeriksaan executable: type, range, category, unit, key, dan freshness.

Missing tidak selalu error: sensor offline, “tidak berlaku”, dan belum diukur memiliki makna berbeda. Duplicate juga harus dinilai terhadap grain, bukan seluruh row.

## Manual example

Untuk event temperature: `event_id` unik, `asset_id` harus dikenal, unit ∈ {C,F}, value setelah konversi berada pada operating range, timestamp timezone-aware, dan status termasuk vocabulary resmi.

## Kenapa tidak langsung drop/fill?

Drop mengurangi sample dan dapat menimbulkan bias. Mean imputation mengecilkan variance. Forward fill mengasumsikan state bertahan. Interpolation mengasumsikan perubahan halus. Pilih dari mekanisme data, bukan kenyamanan API.

## Failure dan debugging

Pisahkan raw immutable dari curated. Simpan rejected row dengan reason. Periksa count masuk = accepted + rejected; jangan diam-diam menghapus bukti.

## Evidence, workplace, checkpoint

Di pekerjaan, contract melindungi dashboard, feature pipeline, billing, dan model. Tulis enam rule untuk dataset lab, satu alternatif handling per rule, serta consequence bila rule dilewati.
