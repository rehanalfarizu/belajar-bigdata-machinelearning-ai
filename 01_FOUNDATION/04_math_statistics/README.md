# Mulai dari sini — Math & Statistics

## Saya sedang belajar apa?

Kamu akan memakai matematika sebagai bahasa untuk empat kebutuhan: merepresentasikan banyak quantities (linear algebra), memahami perubahan (calculus), memodelkan uncertainty (probability), dan menarik kesimpulan dari sample (statistics).

## Kenapa penting?

ML, forecasting, state estimation, simulation, dan eksperimen memakai konsep ini. Tujuan chapter bukan menghafal rumus, tetapi dapat menjelaskan asumsi, menghitung contoh kecil manual, memverifikasi dengan Python, dan menginterpretasikan hasil.

## Prerequisite dan effort

Lulus Python Fundamental; Python Professional dapat dipelajari sebelum atau paralel pada bagian akhir. Estimasi 24–32 jam untuk 13 lesson, 11 lab, exercises, debugging, project, dan checkpoint.

## Lesson map

### Linear Algebra

1. [Scalar dan vector](01_TEORI/01_scalar_vector.md)
2. [Matrix, dot product, norm, transformation](01_TEORI/02_matrix_dot_norm_transformation.md)
3. [Eigen concept, SVD, dan PCA](01_TEORI/03_eigen_svd_pca.md)

### Calculus dan Optimization

4. [Function, slope, dan derivative](01_TEORI/04_function_slope_derivative.md)
5. [Gradient dan chain rule](01_TEORI/05_gradient_chain_rule.md)
6. [Gradient descent](01_TEORI/06_gradient_descent.md)

### Probability

7. [Random variable dan probability](01_TEORI/07_random_variable_probability.md)
8. [Conditional probability dan Bayes](01_TEORI/08_conditional_bayes.md)
9. [Expectation dan variance](01_TEORI/09_expectation_variance.md)

### Statistics

10. [Population, sample, mean, variance](01_TEORI/10_population_sample_mean_variance.md)
11. [Sampling, CLT, confidence interval](01_TEORI/11_sampling_clt_confidence_interval.md)
12. [Hypothesis testing](01_TEORI/12_hypothesis_testing.md)
13. [Correlation dan regression interpretation](01_TEORI/13_correlation_regression.md)

## Urutan praktik

```text
problem → visual intuition → manual calculation → formula
→ Python → visualization → application → failure/debugging
→ exercises → reasoning problems → mini-project → checkpoint
```

- [Tutorial perhitungan](02_TUTORIAL/tutorial_langkah_demi_langkah.md)
- Praktikum: [vector](04_LABS/01_vector_visualization.md),
  [matrix transform](04_LABS/02_matrix_transform.md),
  [dot product](04_LABS/03_dot_product.md),
  [numeric derivative](04_LABS/04_numeric_derivative.md),
  [gradient descent](04_LABS/05_manual_gradient_descent.md),
  [probability simulation](04_LABS/06_probability_simulation.md),
  [Bayes update](04_LABS/07_bayes_update.md),
  [sampling distribution](04_LABS/08_sampling_distribution.md),
  [confidence interval](04_LABS/09_confidence_interval.md),
  [hypothesis test](04_LABS/10_hypothesis_test.md), dan
  [bootstrap](04_LABS/11_bootstrap.md).
- [Cara menjalankan lab numerik](04_LABS/README.md)
- [Exercises](05_EXERCISES/exercises.md)
- [Problem-solving ladder](06_PROBLEM_SOLVING/problems.md)
- [Broken cases](07_DEBUGGING/broken_cases.md)
- [Mini-project — Sensor Uncertainty Report](08_PROJECT/README.md)
- [Checkpoint](09_CHECKPOINT/CHECKPOINT.md)

Gunakan [teori mendalam](01_TEORI/teori_mendalam.md) sebagai synthesis setelah lesson, bukan sebagai entrypoint. Jangan buka [solutions](99_SOLUTIONS/solusi_dan_teori_lengkap.md) sebelum mencoba 20–30 menit.

## Dunia kerja

Vector/matrix merepresentasikan features/transforms; derivative/gradient melatih models; probability menyatakan uncertainty; statistics menilai sample, experiment, alarms, dan claims.

## Navigasi

- Previous: [03 Python Professional](../03_python_professional/README.md)
- Current: **04 Math & Statistics**
- Next: [01 Data Analysis & SQL](../../02_DATA_AND_MACHINE_LEARNING/01_data_analysis_sql/README.md)
