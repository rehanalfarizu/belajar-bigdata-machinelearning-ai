# Guided Refactor — Dari Script ke Package

Gunakan script Sensor Log CLI dari chapter sebelumnya. Jangan menyalin hasil final; lakukan satu perubahan dan jalankan behavior check setiap langkah.

## Step 1 — Freeze behavior

Catat sample input, stdout, stderr, exit code, dan tiga failures. Ini baseline; refactor tidak boleh diam-diam mengubahnya.

## Step 2 — Extract domain functions

Pisahkan parse/validate/summarize dari arguments, file open, print, dan exit. Prediksi dependency direction: CLI boleh memakai domain; domain tidak mengetahui CLI.

## Step 3 — Introduce data model

Ganti dictionary internal dengan dataclass hanya bila fields/invariant menjadi lebih jelas. Tambah type hints; jangan menganggap hints memvalidasi JSON.

## Step 4 — Make boundaries explicit

Gunakan generator untuk lines, context manager untuk file, exception taxonomy kecil, validated config object, dan named logger.

## Step 5 — Add tests

Test domain success/boundaries lebih dulu, lalu satu integration test file→summary. Inject temporary path/data; jangan memakai production file.

## Step 6 — Package

Susun `src/sensor_tool`, `tests`, dan `pyproject.toml`. Uji import dan CLI dari clean environment, bukan hanya cwd source.

## Review questions

- Behavior apa yang sengaja berubah dan mengapa?
- Dependency mana yang kini eksplisit?
- Failure mana yang diterjemahkan dan mana yang dibiarkan naik?
- Evidence apa membuktikan refactor tidak merusak contract?
