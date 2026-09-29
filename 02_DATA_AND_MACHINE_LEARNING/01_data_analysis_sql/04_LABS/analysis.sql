-- Run with DuckDB from this directory after creating views over the raw CSV files.
CREATE OR REPLACE VIEW readings AS
SELECT * FROM read_csv_auto('data/raw/readings.csv');

CREATE OR REPLACE VIEW assets AS
SELECT * FROM read_csv_auto('data/raw/assets.csv');

CREATE OR REPLACE VIEW maintenance AS
SELECT * FROM read_csv_auto('data/raw/maintenance.csv');

-- Grain and key checks must precede analysis.
SELECT COUNT(*) AS rows, COUNT(DISTINCT event_id) AS distinct_event_ids FROM readings;

-- LEFT JOIN exposes unknown foreign keys without silently dropping them.
SELECT r.event_id, r.asset_id, a.site
FROM readings AS r
LEFT JOIN assets AS a USING (asset_id)
WHERE a.asset_id IS NULL;

-- Aggregate each fact table before combining to prevent many-to-many multiplication.
WITH reading_summary AS (
    SELECT asset_id, COUNT(*) AS reading_count
    FROM readings
    GROUP BY asset_id
),
maintenance_summary AS (
    SELECT asset_id, SUM(cost) AS maintenance_cost
    FROM maintenance
    GROUP BY asset_id
)
SELECT a.asset_id, r.reading_count, m.maintenance_cost
FROM assets AS a
LEFT JOIN reading_summary AS r USING (asset_id)
LEFT JOIN maintenance_summary AS m USING (asset_id);

-- A window keeps event grain while adding within-asset order.
SELECT
    event_id,
    asset_id,
    event_time,
    ROW_NUMBER() OVER (PARTITION BY asset_id ORDER BY event_time) AS event_order
FROM readings;
