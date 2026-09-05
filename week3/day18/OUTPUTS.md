# Week 3 - Day 18: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D18-T1 - PASS

```text
Validation accuracy: 0.88
Validation F1: 0.743
Validation ROC-AUC: 0.945
```

## W3-D18-T2 - PASS

```text
Validation accuracy: 0.893
Validation F1: 0.778
Validation ROC-AUC: 0.937
```

## W3-D18-T3 - PASS

```text
Validation accuracy: 0.773
Validation F1: 0.564
Validation ROC-AUC: 0.823
```

## W3-D18-T4 - PASS

```text
              model  accuracy    f1  roc_auc
                SVM     0.880 0.743    0.945
                KNN     0.893 0.778    0.937
      Random Forest     0.847 0.693    0.916
Logistic Regression     0.800 0.605    0.861
      Decision Tree     0.827 0.675    0.857
        Naive Bayes     0.773 0.564    0.823
Validation comparison only. Do not call this an untouched final test.
```

## W3-D18-T5 - PASS

```text
Logistic Regression: Strong fast baseline; linear decision boundary; scale features.
Decision Tree: Readable rules at shallow depth; deep trees can overfit.
Random Forest: Nonlinear tabular baseline; larger and less transparent.
SVM: Useful for medium-sized data; scale inputs; prediction can be costly.
KNN: Simple distance baseline; scale inputs; costly on large training sets.
Naive Bayes: Fast baseline; independence assumption may be unrealistic.
Measure validation quality, training time, inference time, and model size.
Use MultinomialNB for suitable count features; this week uses GaussianNB.
```

## W3-D18-T6 - PASS

```text
              model  accuracy    f1  roc_auc
                SVM     0.880 0.743    0.945
                KNN     0.893 0.778    0.937
      Random Forest     0.847 0.693    0.916
Logistic Regression     0.800 0.605    0.861
      Decision Tree     0.827 0.675    0.857
        Naive Bayes     0.773 0.564    0.823
Validation comparison only. Do not call this an untouched final test.
Saved: week3/day18/output/model-comparison.csv
```
