# Broken Cases — Data Analysis & SQL

Untuk tiap kasus: predict symptom, reproduce, isolate, fix, regression test, prevention.

1. Numeric column terbaca string karena token `N/A?`.
2. `event_id` duplicate tetapi whole-row duplicate check lolos.
3. Many-to-many join menggandakan total.
4. Timestamp naive diasumsikan UTC padahal local.
5. 75°F diperlakukan sebagai 75°C.
6. Missing di-drop sehingga failure assets hilang dari report.
7. Aggregation berubah grain tetapi label chart masih “per event”.

Evidence minimum: failing row/query, invariant yang dilanggar, before/after count, dan test.
