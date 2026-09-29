# Python sebagai Engineering Tool

Kode profesional bukan kode yang memakai banyak pattern; kode profesional membuat behavior, dependency, state, dan failure mudah dilihat serta diuji.

- Type hints menyatakan kontrak untuk manusia dan tooling, tetapi tidak otomatis memvalidasi runtime input.
- `dataclass` cocok untuk value/state object yang jelas; entity dengan lifecycle tetap membutuhkan invariant dan identity.
- Exception harus muncul pada boundary yang memahami kegagalan. Tangkap exception hanya jika dapat menambah konteks, melakukan recovery, atau menerjemahkan kontrak.
- Iterator/generator memproses stream secara incremental; pahami bahwa generator bersifat lazy dan dapat habis.
- Context manager memastikan acquire/release resource walau operasi gagal.
- Decorator mengubah behavior function; gunakan untuk concern yang benar-benar cross-cutting dan tetap jaga observability.
- Async cocok untuk banyak pekerjaan menunggu I/O, bukan jalan pintas untuk kerja CPU-bound.

Struktur package memisahkan public API dari detail. Configuration berasal dari input eksplisit atau environment dan divalidasi saat startup. Logging merekam event dengan konteks, bukan menggantikan test. Unit test mengisolasi domain behavior; integration test memeriksa boundary nyata. Mock hanya pada boundary yang mahal/tidak deterministik, bukan setiap object.
