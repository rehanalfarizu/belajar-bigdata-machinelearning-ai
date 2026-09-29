# Lesson 01 — Time Index, Ordering, dan Frequency

Time series bukan tabel biasa: order membawa informasi. Bedakan event time, ingestion time, dan processing time. Timestamp naive tidak aman lintas zona.

Sampling frequency menyatakan kapan observation diharapkan. Resampling mengubah grain waktu dan membutuhkan aggregation/handling gap. Upsampling tidak menciptakan informasi baru.

Precondition: timezone, duplicate timestamp, ordering, unit, dan expected cadence jelas. Postcondition: index monoton per entity dan gap terukur.

Failure: sort global bukan per asset, DST, device clock reset, dan duplicate retry. Debug count per interval dan delta-time distribution.
