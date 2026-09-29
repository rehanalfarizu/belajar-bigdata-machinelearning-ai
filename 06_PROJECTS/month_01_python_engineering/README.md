# Month 1 — Python Engineering: Sensor Simulator

## Context

Bangun simulator sensor sebagai evolusi kecil yang selalu runnable. Setiap milestone menambah satu capability dan evidence; tidak ada full solution yang diberikan.

## Product outcome

Package dan CLI menyimulasikan readings dengan stable sensor ID, UTC timestamp, sequence number, value, unit, quality, dan schema version. User dapat mengatur seed/rate/noise/missing/output; tests membuktikan behavior penting.

## Milestone ladder

### Milestone 1 — Generate satu nilai

Buat value numeric plausible. Tentukan range dan arti value. **Done:** run menghasilkan satu value dan kamu dapat menjelaskan source/randomness.

### Milestone 2 — Tambahkan timestamp

Gunakan timestamp timezone-aware UTC. **Done:** format, timezone, dan kapan timestamp dibuat terdokumentasi.

### Milestone 3 — Tambahkan identity dan unit

Tambahkan `sensor_id`, `sequence`, `unit`, dan `quality`. **Done:** event contract kecil serta example valid/invalid tersedia.

### Milestone 4 — Pisahkan functions

Pisahkan generation, validation, dan formatting. **Done:** domain function tidak membaca terminal atau menulis file.

### Milestone 5 — Ubah menjadi package

Buat package dengan public API dan dependency direction jelas. **Done:** package dapat diimport tanpa menjalankan simulation.

### Milestone 6 — Configuration

Tambahkan seed, count/rate, noise, dropout, sensor ID, unit, dan output config dengan precedence/validation. **Done:** invalid config fail-fast.

### Milestone 7 — Logging

Catat lifecycle dan rejection/error dengan context; jangan log secret/payload berlebihan. **Done:** level dan fields mempunyai alasan.

### Milestone 8 — Tests

Test determinism untuk seed sama, schema/range, sequence/timestamp, dropout/fault, invalid config, dan empty count. **Done:** failure case benar-benar gagal sebelum fix/regression test.

### Milestone 9 — CLI

Tambahkan `--help`, arguments, stdout/stderr, dan exit codes. **Done:** automation dapat membedakan success/failure dan domain dapat dites tanpa CLI.

### Milestone 10 — Documentation dan release rehearsal

Tulis setup/run/test, event schema, examples, architecture, assumptions, limitations, dan troubleshooting. Test install/run dari clean environment. **Done:** rekan dapat mengulang tanpa penjelasan lisan tambahan.

## Acceptance criteria

- seed sama menghasilkan sequence sama di environment yang didukung;
- timestamp UTC, identity, unit, quality, dan schema valid;
- dropout/fault mode reproducible dan jelas simulated;
- generator dapat stream tanpa menampung seluruh output;
- domain, config, logging, CLI, dan tests terpisah secara masuk akal;
- no secrets/generated caches committed;
- error/failure mempunyai message dan exit behavior actionable.

## Evidence dan checkpoint

Sertakan milestone log, test transcript, sample output, one debugging narrative, reasoning trade-off, clean-run instructions, dan limitations. Tunjukkan demo dari kosong, lalu jawab Phase 1 gate tanpa membaca materi.
