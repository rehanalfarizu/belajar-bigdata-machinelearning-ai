# Broken Cases — Python Fundamental

Gunakan flow debugging Phase 1 dan simpan minimal reproduction.

## Case 1 — Wrong type

```text
total = "10" + 5
```

Prediksi exception, cari boundary yang menghasilkan text, dan tentukan validation/conversion policy. Jangan sekadar membungkus semuanya dengan `str`.

## Case 2 — Mutable alias

```python
a = [1, 2]
b = a
b.append(3)
```

Jelaskan state dan perbaiki sesuai intent: shared mutation atau independent copy.

## Case 3 — List kosong

```python
average = sum(values) / len(values)
```

Definisikan contract no-data sebelum memilih return `None`, exception, atau domain result.

## Case 4 — Infinite loop

```text
count = 3
while count > 0:
    print(count)
```

Temukan missing progress, hentikan process secara aman, dan tambah termination test.

## Case 5 — Shadowed built-in

```python
list = [1, 2]
values = list("abc")
```

Gunakan traceback dan scope model untuk menjelaskan failure.

## Case 6 — Invalid JSON versus invalid schema

Bandingkan `{"value": 2.5}`, `{"value": "hot"}`, dan text dengan trailing comma. Tentukan parser layer dan validation layer.

## Case 7 — Import error

Module lokal dapat diimport dari satu cwd tetapi tidak yang lain. Inspect interpreter, cwd, project structure, `sys.path`, dan module `__file__`; jangan menambah random path permanen.

## Case 8 — Exception tertelan

```python
try:
    value = float(raw)
except Exception:
    value = 0
```

Jelaskan silent corruption dan desain error/quarantine contract.
