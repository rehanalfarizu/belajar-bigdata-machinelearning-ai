# Lesson 6 — Git Mental Model

## Problem

Kamu mengedit file, menjalankan `git commit`, tetapi perubahan tertentu tidak masuk. Atau file muncul “modified” setelah commit. Penyebabnya biasanya bukan Git acak—perubahan berada pada state berbeda.

## Context dan why

Git dipakai untuk eksperimen aman, collaboration, code review, rollback, dan evidence. Menghafal command tanpa model working tree/index/commit membuat conflict terasa menakutkan.

## Intuisi dan mental model

Bayangkan meja kerja, baki pilihan, album snapshot, dan perpustakaan bersama.

```text
working tree          staging area/index       local commits        remote refs
file yang diedit  →   perubahan dipilih    →   snapshot graph   →   dibagikan/fetch
       git add                  git commit               push/fetch

branch = nama/reference yang bergerak ke commit
commit = snapshot + parent + metadata
merge = membuat history yang menggabungkan ancestry/content
```

## Definition dan internal mechanism

Working tree adalah file yang sedang kamu lihat. Staging area menyimpan kandidat snapshot berikutnya. Commit adalah immutable snapshot dengan parent. Branch bukan salinan folder; ia reference ke commit. Remote adalah repository/reference lain, bukan backup otomatis dari perubahan belum dipush.

Git membandingkan snapshots dan ancestry. Conflict muncul ketika Git tidak dapat menentukan intent gabungan secara aman. Marker conflict adalah permintaan keputusan; hapus marker setelah memilih/menggabungkan isi dan menguji hasil.

## Small manual example

Jika file A dan B berubah tetapi hanya A di-`git add`, commit berisi state staged A; B tetap modified di working tree. `git diff` menunjukkan unstaged; `git diff --staged` menunjukkan kandidat commit.

## Hands-on experiment

Buat repository temporary sesuai [Lab 6](../04_LABS/06_git.md). Buat dua branch yang mengubah baris sama, merge, baca marker, pilih hasil yang memenuhi intent, test, lalu commit resolution.

### Predict before run

Prediksi output `git status` setelah edit, setelah add, setelah commit, dan saat conflict.

### Observe dan explain

Expected: status berubah sesuai state. Conflict tidak selesai hanya dengan menghapus marker; kamu harus menentukan content benar dan stage resolution.

## Workplace application

Branch/commit mendukung review, bisect, release, audit, dan rollback. Commit kecil dan pesan yang menjelaskan intent memudahkan rekan memahami perubahan. Jangan commit secrets, generated cache, atau data sensitif.

## Common failures dan debugging

- “nothing to commit”: cek repo/cwd, ignored file, dan actual diff.
- perubahan tidak masuk: cek `git diff --staged` sebelum commit.
- branch tertinggal: fetch lalu pahami history sebelum merge/rebase.
- conflict: baca kedua intent dan tests; jangan selalu memilih “ours/theirs”.
- detached HEAD: pahami commit aktif sebelum membuat perubahan lanjutan.

## Problem solving dan checkpoint

1. Di state mana perubahan berada sebelum dan sesudah `git add`?
2. Mengapa branch murah dibuat?
3. Apa evidence bahwa conflict resolution benar selain command merge selesai?

## Penutup

**KAMU BARU BELAJAR:** Git melacak snapshot melalui working tree, index, commits, branches, dan remotes.

**KENAPA INI PENTING:** collaboration aman membutuhkan history dan intent yang dapat ditinjau.

**DI DUNIA KERJA DIPAKAI UNTUK:** pull request, review, release, audit, rollback, dan incident analysis.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Git memberi evidence perubahan; Lesson 7 menyatukan semua layer menjadi debugging berbasis hypothesis.
