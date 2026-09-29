# INCIDENT-001 — Recommendation Stale Setelah Outage

## Situation

Model service outage 17 menit. Setelah recovery, 240 recommendation lama diproses sekaligus; 18 sudah tidak relevan dan empat operator melaporkan action membingungkan. Tidak ada physical harm.

## Task

1. Tulis aksi mitigasi 30 menit pertama dan komunikasi stakeholder.
2. Bangun timeline dari data yang perlu dikumpulkan.
3. Tentukan expiry, queue policy, state precondition, backpressure, dan reconciliation.
4. Tulis root-cause hypotheses tanpa menyalahkan individu.
5. Buat follow-up dengan owner, priority, verification, dan rollback.

Constraints: audit record tidak boleh dihapus; operasi harus tetap tersedia dalam read-only/degraded mode.
