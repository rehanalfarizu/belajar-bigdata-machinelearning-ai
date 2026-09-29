# Mini-Project — Trusted Sensor Analysis

Bangun pipeline tiga tabel lokal.

1. Nyatakan question, grain, schema, keys.
2. Profile raw dan tulis quality report.
3. Curate tanpa mengubah raw; quarantine rejected.
4. Reconcile input=accepted+rejected.
5. Jalankan SQL join/group/window yang cardinality-safe.
6. Buat tiga EDA insight dengan evidence/limitation.
7. Tambahkan test untuk duplicate, unit, timezone, join.

Definition of done: satu documented command mengulang pipeline; output tidak berubah saat rerun; tidak ada silent drop; insight menunjuk query/code.
