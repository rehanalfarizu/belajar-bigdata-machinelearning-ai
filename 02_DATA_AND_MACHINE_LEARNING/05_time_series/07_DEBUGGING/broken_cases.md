# Broken Cases — Time Series

1. Timestamp naive/timezone shift.
2. Duplicate/out-of-order event.
3. Centered rolling memakai future.
4. Backfill future ke past.
5. Random split.
6. Scaler fit seluruh timeline.
7. Model tidak mengalahkan seasonal naive.
8. Interval coverage buruk setelah drift.

Evidence: source-time assertion, rolling metric by horizon/period, and fixed baseline comparison.
