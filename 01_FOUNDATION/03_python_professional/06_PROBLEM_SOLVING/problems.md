# Problem-Solving Ladder — Python Professional

## Level 1 — Recall

Pilih function, dataclass, atau stateful class untuk tiga kebutuhan: conversion, immutable reading, dan estimator state. Jelaskan alasan.

## Level 2 — Apply

Ubah parser eager menjadi generator tanpa mengubah accepted/rejected semantics.

## Level 3 — Analyze

Package memiliki flaky tests karena config global dan shared mutable cache. Bangun hypothesis tree dan minimal reproduction.

## Level 4 — Design

Rancang package CLI yang dapat diinstall: public API, config, logs, exceptions, tests, build metadata, dan dependency direction.

## Level 5 — Debug / Workplace

Async ingestion kadang kehilangan task exception saat shutdown. Rancang observability, bounded task ownership, cancellation, draining, timeout, dan verification—tanpa menganggap `gather` saja menyelesaikan lifecycle.
