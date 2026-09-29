# Programming Problem-Solving Ladder — Phase 1

Gunakan decomposition, state tracing, assumptions, tests, dan explanation. Jangan lompat ke Level 5 sebelum Level 1–3 dapat dikerjakan tanpa menyalin.

## LEVEL 1 — Recall

1. Hitung rata-rata tiga angka dan jelaskan tiap variable.
2. Tentukan output lima expressions sebelum run.
3. Pilih list, tuple, set, atau dict untuk empat kebutuhan sederhana.

## LEVEL 2 — Apply

1. Hitung mean readings sambil mengabaikan input invalid sesuai rule eksplisit.
2. Parse `sensor_id,value,unit` dan laporkan error field.
3. Baca JSON kecil, validasi keys/type/range, lalu buat summary.

## LEVEL 3 — Analyze

1. Jelaskan crash pada list kosong dan bandingkan tiga contract no-data.
2. Temukan aliasing mutable yang mengubah state caller.
3. Bedakan wrong cwd, missing file, invalid JSON, wrong schema, dan import environment.
4. Trace condition/loop/function/exception pada satu bad event.

## LEVEL 4 — Design

1. Rancang pemrosesan file besar dengan streaming, quarantine, metrics, dan bounded memory.
2. Rancang package parser dengan domain/io/cli boundaries, config, logs, tests, dan pyproject.
3. Rancang CLI contract dan failure/exit-code matrix.

## LEVEL 5 — Debug / Workplace

Process crash di tengah file besar dan harus resume tanpa menggandakan effect. Diberikan: checkpoint terakhir mungkin tertulis tetapi acknowledgment hilang; satu line corrupt; output downstream tidak transactional. Susun symptom→reproduce→observations→hypotheses→tests→root cause→safe design→verification→prevention. Bahas idempotency key, checkpoint ownership, reconciliation, dan limitations tanpa langsung memilih teknologi baru.
