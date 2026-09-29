# Konsep Dasar Time Series

Time series memiliki order. Definisikan event time, ingestion time, timezone, sampling interval, forecast origin, horizon, dan unit sebelum membuat feature. Resampling membutuhkan aggregation yang sesuai makna fisik: flow dapat dijumlah, state biasanya dirata atau diambil pada boundary dengan aturan jelas.

Lag dan rolling feature hanya boleh memakai informasi yang tersedia pada forecast origin. Random split merusak simulasi penggunaan bila masa depan bocor ke train. Gunakan expanding atau rolling-window validation dan laporkan kinerja per horizon/regime.

Baseline wajib: last value, seasonal naive, atau simple average sesuai proses. Trend dan seasonality bukan alasan otomatis untuk decomposition tertentu. Stationarity adalah sifat distribusi/proses pada asumsi model, bukan tombol preprocessing universal.

Forecast adalah distribusi, bukan satu angka. Evaluasi point error bersama interval coverage dan width. MAPE gagal pada target nol/dekat nol; metric dipilih dari cost dan scale. Concept drift dapat muncul pada input, relationship, atau target; retraining bukan respons otomatis tanpa diagnosis.
