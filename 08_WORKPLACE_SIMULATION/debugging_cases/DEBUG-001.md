# DEBUG-001 — State Melompat Mundur

## Report

Twin state motor kadang kembali ke temperature lebih lama selama 2–5 detik setelah network pulih.

## Evidence

```text
12:00:03 ingest seq=104 event_time=11:59:59 value=71.2
12:00:03 state  version=880 value=71.2
12:00:04 ingest seq=103 event_time=11:59:58 value=69.8
12:00:04 state  version=881 value=69.8
12:00:05 ingest seq=105 event_time=12:00:04 value=71.9
```

Consumer retry count naik, tidak ada error. Device sequence reset saat reboot tetapi tidak ada boot ID.

## Task

Susun hypothesis tree, data tambahan yang diperlukan, minimal reproduction, invariant, fix options beserta trade-off, tests, migration, dan monitoring. Bedakan ingestion order, event time, sequence, dan state version.
