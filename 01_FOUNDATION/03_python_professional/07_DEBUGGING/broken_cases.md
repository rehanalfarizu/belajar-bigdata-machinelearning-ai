# Broken Cases — Python Professional

## Case 1 — Circular import

`domain` mengimpor `cli` untuk config, sedangkan `cli` mengimpor `domain`. Temukan dependency yang salah dan pindahkan contract ke boundary netral/lebih dalam.

## Case 2 — Mutable dataclass default

Beberapa instances berbagi list. Reproduce dan gunakan `default_factory`; jelaskan mengapa fix bekerja.

## Case 3 — Type hint dianggap validation

External JSON string masuk ke field `float` tanpa conversion. Buktikan annotation tidak menolak runtime input.

## Case 4 — Generator sudah habis

Count pertama benar, pass kedua kosong. Tentukan apakah contract harus single-pass, factory iterable, atau materialization.

## Case 5 — Decorator menelan exception

Wrapper mengembalikan `None` pada semua failure. Pertahankan cause dan definisikan retry/translation pada owner boundary.

## Case 6 — Context cleanup gagal

Resource kedua gagal acquire setelah resource pertama didapat. Rancang partial-cleanup path dan test failure injection.

## Case 7 — Duplicate logs

Handler ditambahkan setiap import/call. Inspect logger propagation dan pindahkan configuration ke entrypoint.

## Case 8 — Config boolean

`bool("false")` menghasilkan True. Buat parser accepted values dan error untuk ambiguity.

## Case 9 — Test flaky waktu

Test memakai real sleep dan exact duration. Ganti claim menjadi behavior/tolerance atau injectable clock sesuai scope.

## Case 10 — Coroutine never awaited

Function async dipanggil seperti function biasa. Identifikasi coroutine object, task ownership, event loop boundary, dan exception observation.
