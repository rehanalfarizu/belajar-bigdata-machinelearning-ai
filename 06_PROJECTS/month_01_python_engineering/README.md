# Month 1 — Python Engineering: Sensor Simulator

## Context

Buat package dan CLI yang menyimulasikan temperature sensor. Output event harus punya stable sensor ID, UTC event time, sequence number, value, unit, quality, dan schema version.

## Deliverables

- package terstruktur dengan domain model terpisah dari CLI/I/O;
- configuration tervalidasi untuk seed, rate, noise, missing, dan output;
- JSON Lines/CSV output dan summary report;
- structured logging, README run commands, dan tests;
- experiment note tentang random seed, floating point, dan failure behavior.

## Acceptance criteria

Input invalid ditolak jelas; seed sama menghasilkan sequence sama; timestamp/unit/schema valid; dropout/fault mode dapat direproduksi; generator tidak memuat seluruh stream ke memory; test mencakup empty/invalid/boundary cases.

## Evidence

Sertakan test transcript, sample output, coverage rationale, satu debugging narrative, dan link journal. Tidak ada solution starter; desain interface adalah bagian penilaian.
