# Tutorial Penyelesaian — Level 06 MLOps dan Deployment

## Urutan menyimpan model dengan benar

Simpan pipeline lengkap, bukan classifier dan scaler terpisah bila tidak perlu. Catat versi package, data, seed, metric, waktu training, dan schema input.

```python
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "artifacts/models/iris_pipeline.joblib")
loaded = joblib.load("artifacts/models/iris_pipeline.joblib")
assert (pipeline.predict(X_test) == loaded.predict(X_test)).all()
```

File pickle/joblib hanya boleh dimuat dari sumber tepercaya karena deserialisasi dapat menjalankan kode berbahaya.

## API FastAPI: cek sebelum container

1. Definisikan Pydantic request schema.
2. Load model sekali saat startup.
3. Validasi bentuk/range input.
4. Sediakan `/health` dan `/predict`.
5. Uji happy path, input salah, dan model error.

Gunakan array dua dimensi untuk satu prediksi: `np.array([[...]], dtype=float)`. Return nilai JSON-native dengan `int()`/`float()`, bukan NumPy scalar.

## Docker debugging

Build setelah test lokal lulus. Jika container langsung keluar, lihat `docker logs`. Jika health check gagal, panggil endpoint dari dalam container dan pastikan command health check memang tersedia di base image. Jangan copy `.env`, cache, atau model rahasia ke image.

## Monitoring

Pantau input/schema drift, latency, error rate, volume, dan outcome label bila feedback tersedia. Drift bukan otomatis alasan retraining; investigasi perubahan data, bug upstream, dan dampak bisnis lebih dulu.
