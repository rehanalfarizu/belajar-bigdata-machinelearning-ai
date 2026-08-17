# Teori Mendalam — Level 06: MLOps dan Deployment

## 1. Mengapa model sulit dioperasikan?

Software biasa berubah ketika code berubah. Sistem ML berubah ketika code, data, label, feature, model, dependency, atau proses bisnis berubah. Prediction adalah kontrak antara producer data dan consumer keputusan. MLOps membuat kontrak tersebut observable, reproducible, dan dapat dipulihkan saat gagal.

Reproducibility mencakup source code/commit, environment, dependency lock, data version/hash, schema, split, seed, parameter, metric, artifact model, dan hardware bila relevan. Reproducibility sempurna tidak selalu mungkin pada GPU/distributed training, tetapi perbedaan harus diketahui dan dibatasi.

## 2. Training-serving consistency

Training feature dan serving feature harus memiliki definisi sama. Menyimpan `Pipeline` menggabungkan preprocessing dan model, tetapi tidak otomatis menyelesaikan perubahan upstream schema atau fitur yang dihitung dari database. Contract input, validation, feature version, dan test parity diperlukan. Offline feature yang memakai masa depan adalah leakage; online feature yang terlambat adalah serving failure.

## 3. API dan batch inference

Online API menuntut latency, availability, input validation, authentication, rate limiting, timeout, error handling, dan observability. Batch inference menuntut idempotency, partitioning, backfill, output version, serta data quality. Pilihan online/batch bukan teknis semata: pilih dari kapan keputusan dibutuhkan dan berapa biaya keterlambatan.

Model binary harus dimuat dari sumber tepercaya karena pickle/joblib dapat mengeksekusi code. API tidak boleh memaparkan traceback, path lokal, atau secret. Response harus menyertakan model version bila keputusan perlu diaudit.

## 4. Container, CI/CD, dan release

Container mengemas runtime, bukan menggantikan design yang baik. Build deterministic memakai base image yang ditinjau, dependency terpin, `.dockerignore`, non-root user, dan secret di luar image. CI menguji lint/type/test/security/build; CD mempromosikan artifact sama antar environment. Canary/shadow deployment mengurangi blast radius. Rollback harus dipraktikkan, bukan hanya ditulis.

## 5. Monitoring dan lifecycle

Operational metric: latency, throughput, error rate, resource, queue lag. Data metric: schema, missingness, range, category baru, freshness, distribution drift. Model metric: prediction distribution, calibration, quality saat ground truth datang, business outcome. Drift dapat berasal dari musim, bug, sensor, policy, atau populasi baru; retraining otomatis tanpa investigasi dapat memperkuat data rusak. Tetapkan owner, threshold, alert, dan runbook untuk setiap metric penting.
