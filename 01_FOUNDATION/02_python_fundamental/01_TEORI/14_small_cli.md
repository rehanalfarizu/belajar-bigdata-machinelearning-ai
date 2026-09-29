# Lesson 14 — Small CLI

## Problem, context, why

Script dengan `input()` dan path hard-coded sulit diulang oleh scheduler atau rekan. CLI memberi contract eksplisit melalui arguments, stdout/stderr, dan exit code.

## Intuisi dan mental model

CLI adalah API untuk manusia/shell.

```text
arguments + stdin/environment/files
          ↓ parse & validate boundary
domain function (tanpa print/input)
          ↓ result/error
format stdout/stderr + exit code
```

## Definition dan internal mechanism

Shell membentuk argument vector. `argparse` mengubah text arguments menjadi names/values dan menghasilkan help/error. Exit code 0 berarti success secara konvensi; nonzero berarti failure category. Stdout untuk result yang dapat dipipe; stderr untuk diagnostics.

## Small manual example

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--value", type=float, required=True)
args = parser.parse_args()
print(args.value * 2)
```

### Predict → run → observe → explain

Prediksi behavior tanpa argument, dengan `--help`, valid number, dan invalid text. Observe output channel dan exit code.

## Hands-on experiment

Pisahkan `double(value)` dari parser/print. Test function langsung, lalu test CLI manually. Tambahkan unit option dan explicit validation.

## Workplace application

CLI dipakai untuk ETL jobs, migrations, admin tools, experiment runners, model evaluation, dan automation CI.

## Common failure dan debugging

Parsing tercampur domain logic, error selalu exit 0, secrets menjadi command arguments/history, relative path tersembunyi, dan output manusia sulit diparse automation. Definisikan interface dan audience.

## Mini exercise dan checkpoint

Buat CLI yang menerima input JSONL, menghasilkan summary, mempunyai `--help`, exit code, dan actionable errors. Ini menjadi [mini-project chapter](../08_PROJECT/README.md).

## Penutup

**KAMU BARU BELAJAR:** CLI adalah boundary input→validation→domain→output→exit status.

**KENAPA INI PENTING:** program yang dapat diulang membutuhkan interface eksplisit.

**DI DUNIA KERJA DIPAKAI UNTUK:** jobs, automation, developer tools, dan reproducible experiments.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** Python Professional mengubah modules/CLI ini menjadi package bertipe, bertest, terkonfigurasi, dan observable.
