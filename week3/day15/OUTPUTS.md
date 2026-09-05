# Week 3 - Day 15: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D15-T1 - PASS

```text
Predicted score for 5 hours: 80.0
Cluster IDs (names are arbitrary): [0 0 1 1]
Learned action values: {'study': 0.75, 'skip': 0.0}
```

## W3-D15-T2 - PASS

```text
train rows: 360 positive rate: 0.497
validation rows: 120 positive rate: 0.5
test rows: 120 positive rate: 0.5
```

## W3-D15-T3 - PASS

```text
Depth: 1 train accuracy: 0.773 validation accuracy: 0.773
Depth: 4 train accuracy: 0.902 validation accuracy: 0.827
Depth: None train accuracy: 1.0 validation accuracy: 0.813
A large train/validation gap suggests overfitting; one split is not proof.
```

## W3-D15-T4 - PASS

```text
Degree: 1 bias squared: 0.1736 variance: 0.0123
Degree: 4 bias squared: 0.0044 variance: 0.0165
Degree: 12 bias squared: 0.0084 variance: 0.2875
Empirical estimates against a known function, not exact generalization error.
```

## W3-D15-T5 - PASS

```text
Accuracy 0.667
Precision 0.667
Recall 0.667
F1 0.667
ROC-AUC 0.889
MAE 20.0
RMSE 21.602
```

## W3-D15-T6 - PASS

```text
Python executable: /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
scikit-learn version: 1.8.0
Import succeeded. This script does not install packages.
```

## W3-D15-T7 - PASS

```text
Training row IDs: [11, 10, 7, 18, 3, 17, 0, 16, 15, 9, 4, 1, 2, 14]
Held-out row IDs: [8, 19, 6, 13, 5, 12]
TP, TN, FP, FN: 2 2 1 1
Accuracy: 0.6666666666666666
Precision, recall, F1: 0.6666666666666666 0.6666666666666666 0.6666666666666666
```

## W3-D15-T8 - PASS

```text
Accuracy: 0.9
Positive-class recall: 0.0
Balanced accuracy: 0.5
90% accuracy can hide complete failure to identify the minority class.
```
