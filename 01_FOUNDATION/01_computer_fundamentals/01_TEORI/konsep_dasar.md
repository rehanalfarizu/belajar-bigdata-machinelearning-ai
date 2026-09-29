# Konsep Dasar Komputer untuk Engineer

Program berjalan sebagai **process** dengan ruang memory dan resource sendiri. **Thread** adalah alur eksekusi di dalam process; concurrency tidak otomatis berarti parallel. Sistem operasi menjembatani program dengan CPU, memory, filesystem, network, clock, dan device.

Path absolut dimulai dari root sistem; path relatif ditafsirkan dari working directory. Nama file yang benar belum cukup bila process tidak punya permission atau working directory berbeda. Environment variable adalah input proses, bukan tempat menyimpan secret di source control.

Network stack mengirim bytes antar-host. DNS menerjemahkan nama, TCP menyediakan ordered byte stream, sedangkan HTTP memberi struktur request/response di atas transport. JSON adalah serialization format; ia tidak menjamin schema, unit, timezone, atau semantic meaning. Timeout, retry, idempotency, dan partial failure harus dianggap normal.

Git menyimpan snapshot dan graph commit. Working tree, staging area, local history, dan remote adalah state berbeda. `status`, `diff`, dan `log` harus dibaca sebelum perubahan besar. Konflik bukan error Git; itu permintaan keputusan manusia tentang intent yang bertabrakan.

Mental model debugging: observasi gejala → buat hipotesis → ukur state → ubah satu variabel → verifikasi. Hindari mengganti dependency atau path secara acak sebelum mengetahui process, environment, dan file yang sebenarnya dipakai.
