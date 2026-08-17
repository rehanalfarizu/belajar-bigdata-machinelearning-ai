# Tutorial Penyelesaian — Level 10 Digital Twin

## Urutan membangun twin yang benar

Mulai dari satu aset dan satu state yang penting. Contoh terbaik untuk belajar adalah tangki: state-nya tinggi air, input-nya inflow pompa, dan observasi-nya sensor level. Jangan mulai dari arsitektur cloud/3D dashboard sebelum model dan data dasar dapat diverifikasi.

1. Definisikan state, unit, batas fisik, input, output, dan frekuensi update.
2. Buat plant simulator terpisah agar ada “ground truth” saat belajar.
3. Tambahkan sensor dengan noise/dropout; jangan biarkan twin membaca ground truth.
4. Buat prediksi model dari state sebelumnya dan input.
5. Koreksi prediksi dengan observasi yang lolos quality check.
6. Simpan residual dan analisis sebelum membuat alarm.
7. Jalankan what-if tanpa menyentuh plant fisik.

## Cara mengecek solusi

Plant level tidak boleh negatif. Sensor boleh `NaN` saat dropout. Twin harus tetap menghasilkan estimasi saat sensor hilang, tetapi uncertainty seharusnya meningkat di sistem nyata. Setelah memasukkan fault, residual seharusnya berubah; jika tidak, fault tidak benar-benar memengaruhi observasi/model.

## Debugging yang sering terjadi

- Plot tampak datar: cek `dt`, area, dan unit inflow/outflow.
- Level langsung negatif: lakukan clamp `max(0, level)` dan cek stabilitas timestep.
- Alarm selalu menyala: threshold dihitung dari data fault atau satuan salah.
- Alarm tidak pernah menyala: fault terlalu kecil, residual memakai state yang sama, atau sensor langsung menimpa twin tanpa menyimpan prediksi.
- Waktu kacau: bedakan event time, process time, dan timezone.

## Setelah notebook

Kerjakan praktikum berurutan. Baru setelah hasil simulasi stabil, coba ganti generator sensor dengan CSV atau broker MQTT lokal. Jangan hubungkan controller ke perangkat nyata selama safety/review manusia belum tersedia.
