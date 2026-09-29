# ARCH-001 — Fleet Digital Twin Architecture

## Context

5.000 vehicles × 40 signals × rata-rata 0,2 Hz; burst 5×. Operations membutuhkan latest state <10 detik, historical analysis 2 tahun, geofence alert, simulation what-if, dan read-only partner access.

## Constraints

Intermittent connectivity, multi-region users, privacy restrictions, cost ceiling, schema evolution, replay, dan no direct cloud-to-actuator path.

## Task

Buat requirement/non-goal, capacity estimate, data/control plane, storage/partition choices, event contract, consistency, security, SLO/observability, backpressure, degraded mode, DR, migration, cost drivers, alternatives, dan failure-injection plan. Pertahankan kapan graph/spatial store diperlukan dan kapan tidak.
