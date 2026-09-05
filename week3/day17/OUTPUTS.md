# Week 3 - Day 17: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D17-T1 - PASS

```text
Validation accuracy: 0.8
Validation F1: 0.605
Validation ROC-AUC: 0.861
```

## W3-D17-T2 - PASS

```text
Validation accuracy: 0.827
Validation F1: 0.675
Validation ROC-AUC: 0.857
```

## W3-D17-T3 - PASS

```text
Validation accuracy: 0.847
Validation F1: 0.676
Validation ROC-AUC: 0.897
```

## W3-D17-T4 - PASS

```text
First five labels: [1 1 0 1 0]
First five positive probabilities: [0.547 0.685 0.048 0.748 0.183]
              precision    recall  f1-score   support

           0       0.82      0.92      0.87       106
           1       0.72      0.52      0.61        44

    accuracy                           0.80       150
   macro avg       0.77      0.72      0.74       150
weighted avg       0.79      0.80      0.79       150
```

## W3-D17-T5 - PASS

```text
Feature 9 importance 0.261
Feature 3 importance 0.114
Feature 6 importance 0.109
Feature 7 importance 0.095
Feature 8 importance 0.093
Feature 5 importance 0.087
Feature 0 importance 0.073
Feature 1 importance 0.067
Feature 2 importance 0.055
Feature 4 importance 0.045
Impurity importance can favor high-cardinality features; it is not causation.
```

## W3-D17-T6 - PASS

```text
              model  accuracy    f1  roc_auc
      Random Forest     0.847 0.693    0.916
Logistic Regression     0.800 0.605    0.861
      Decision Tree     0.827 0.675    0.857
Validation comparison only. Do not call this an untouched final test.
```

## W3-D17-T7 - PASS

```text
Feature 9 AUC drop 0.26 +/- 0.038
Feature 7 AUC drop 0.043 +/- 0.008
Feature 3 AUC drop 0.033 +/- 0.008
Feature 6 AUC drop 0.03 +/- 0.011
Feature 8 AUC drop 0.018 +/- 0.007
Correlated features may share importance. These scores do not prove causality.
```
