# Lab 01 — Profile Messy Data
## 1. TUJUAN
Menentukan grain, schema, key, dan quality failures sebelum cleaning.
## 2. PREREQUISITE
Lesson 01–03; Python; raw CSV lokal.
## 3. SETUP
Salin data raw ke workspace lab; raw tidak boleh ditimpa.
## 4. PREDICTION BEFORE RUN
Prediksi row count, unique event, missing, category, unit, dan timestamp failures.
## 5. LANGKAH PRAKTIKUM
Ketik profiler dengan `csv`/Pandas: shape, type candidates, null, duplicate key, category/unit counts, time parse.
## 6. OBSERVATION
Catat prediksi vs hasil serta rule yang dilanggar setiap row.
## 7. WHY
Profiling memvalidasi asumsi sebelum transformasi menghapus bukti.
## 8. MODIFICATION
Tambahkan satu row valid dan satu category baru; prediksi perubahan report.
## 9. FAILURE EXPERIMENT
Biarkan inference type menerima mixed column dan gunakan whole-row duplicate saja.
## 10. DEBUGGING
Bandingkan raw text, grain key, parsing result, dan rejected reasons.
## 11. WORKPLACE CONNECTION
Muncul pada source onboarding, data contract, incident, dan analytics request.
## 12. CHECKPOINT
Serahkan profile, grain/key/schema, tujuh issue, serta rule/evidence tanpa melihat langkah.
