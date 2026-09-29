# Teori Mendalam — Level 09: AI Systems, Cloud, dan Governance

## 1. Sistem adalah lebih dari model

Produk AI terdiri dari user/client, identity, network, input validation, data service, model, cache/queue, observability, storage, dan operator. Latency end-to-end adalah gabungan semua komponen; accuracy model tidak mengatasi request timeout atau schema salah. Rancang dari non-functional requirement: throughput, latency, availability, cost, privacy, compliance, recovery objective, dan blast radius.

## 2. Reliability engineering

SLI adalah pengukuran seperti success rate/latency; SLO adalah target; error budget adalah toleransi kegagalan. Timeout membatasi penantian, retry dengan backoff+jitter menangani kegagalan sementara, circuit breaker mencegah cascade, bulkhead mengisolasi resource, queue memisahkan kerja asynchronous, dan idempotency mencegah duplicate effect. Health check mengatakan process hidup; readiness mengatakan ia siap menerima traffic. Keduanya berbeda.

## 3. Cloud primitives dan biaya

Object storage murah/durable untuk artefak dan data, database menyimpan state/query, container/VM menjalankan service, Kubernetes mengatur workload cluster, IAM mengatur identity, VPC/network policy membatasi jalur komunikasi. Managed service mengurangi operasi tetapi dapat menambah lock-in/cost. Cost dipengaruhi compute time, storage, request, data scan, egress, GPU idle, autoscaling, dan log volume. Gunakan budget, quota, tagging, dan observability sejak awal.

## 4. Security by design

Threat model menyebut asset, actor, trust boundary, attack path, mitigasi, dan residual risk. Least privilege memberi akses minimum; secret manager mencegah credential di source/image; encryption in transit/at rest melindungi data tetapi tidak menggantikan authorization; audit log membantu investigasi. Dependency, container, model artifact, prompt/tool, dan data pipeline masing-masing merupakan supply-chain/attack surface.

## 5. Governance dan operasi AI

Governance mendokumentasikan tujuan, user, prohibited use, data provenance, metric, limitations, fairness/privacy assessment, review/approval, retention, owner, dan incident response. Human-in-the-loop diperlukan bila impact tinggi atau uncertainty besar. Monitoring harus menghasilkan keputusan: investigate, rollback, disable, communicate, or retrain after root cause. Postmortem mencari perbaikan sistem, bukan kambing hitam.
