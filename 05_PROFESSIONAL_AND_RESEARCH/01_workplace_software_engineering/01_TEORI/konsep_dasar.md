# Workplace Software Engineering

Pekerjaan engineer dimulai dari outcome dan constraints, bukan dari coding. Klarifikasi actor, current behavior, desired behavior, acceptance criteria, non-goals, compatibility, security/privacy, operability, dan rollback.

Perubahan kecil mempercepat feedback dan review. Sebelum coding, baca sistem dan test, reproduksi masalah, tulis hypothesis, lalu tentukan minimal safe change. Commit/PR menjelaskan masalah, keputusan, alternatif, evidence test, risk, deployment, dan rollback. Review menilai correctness, maintainability, security, operability, dan test gaps—bukan style pribadi.

Debugging produksi memisahkan symptom dari cause. Gunakan logs, metrics, traces, events, config/version, dan timeline. Jangan menambah retry sebelum memahami idempotency/backpressure. Incident response memprioritaskan mitigasi dan komunikasi; root-cause analysis dilakukan setelah stabil. Postmortem membahas conditions dan system improvements, bukan menyalahkan individu.

Definition of done meliputi code, tests, docs, observability, migration/backward compatibility, rollout, ownership, dan cleanup. Software selesai bukan ketika merge, tetapi ketika outcome berfungsi dan dapat dioperasikan.
