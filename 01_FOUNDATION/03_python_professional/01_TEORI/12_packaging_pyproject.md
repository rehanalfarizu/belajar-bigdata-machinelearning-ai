# Lesson 12 — Packaging dan `pyproject.toml`

## Problem, context, why

Project hanya berjalan setelah `sys.path` diubah manual atau dari cwd tertentu. Rekan tidak tahu dependency, package name, atau command install.

## Intuisi dan mental model

Source tree adalah bahan; build metadata adalah resep; distribution artifact adalah paket kirim; environment install adalah tempat artifact digunakan.

## Definition dan internal mechanism

`pyproject.toml` menyatakan build system dan project metadata/dependencies. Source layout memisahkan importable package dari project files. Installer membangun/menginstal distribution ke environment; editable install menghubungkan development source tetapi bukan substitute build test.

## Small example

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "sensor-tool"
version = "0.1.0"
requires-python = ">=3.11"
```

### Predict/run/observe/explain

Prediksi perbedaan import dari source cwd, editable install, dan wheel install. Inspect package `__file__` dan environment.

## Workplace application

Packaging memberi version, dependency contract, CLI entrypoint, artifact untuk CI/release, dan reproducible installation. Lock/environment strategy tetap perlu untuk applications.

## Common failure dan debugging

Package name vs import name bingung, files tidak masuk distribution, build isolation failure, dependency tidak dinyatakan, atau hanya editable install diuji. Bangun artifact dan test install di clean environment.

## Mini exercise/checkpoint

Buat `pyproject.toml` Sensor Package dengan metadata minimal dan test import dari environment baru. Jangan publish.

## Penutup

**KAMU BARU BELAJAR:** packaging mengubah source menjadi versioned installable artifact.

**KENAPA INI PENTING:** “works on my machine” sering berasal dari environment/path implisit.

**DI DUNIA KERJA DIPAKAI UNTUK:** internal libraries, CLI delivery, CI artifacts, dan releases.

**HUBUNGANNYA DENGAN MATERI BERIKUTNYA:** package/service sering melakukan banyak I/O; Lesson 13 menjelaskan async secara proporsional.
