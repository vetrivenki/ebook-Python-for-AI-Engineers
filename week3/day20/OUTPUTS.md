# Week 3 - Day 20: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D20-T1 - PASS

```text
Fold AUC: [0.879 0.864 0.855 0.862 0.823]
Mean and standard deviation: 0.856 0.019
The pipeline refits its scaler within every training fold.
```

## W3-D20-T2 - PASS

```text
Best parameters: {'logisticregression__C': 1.0}
Best cross-validation AUC: 0.857
The best CV score is selected optimistically; final evaluation needs unseen data.
```

## W3-D20-T3 - PASS

```text
Best parameters: {'n_estimators': 40, 'min_samples_leaf': 3, 'max_depth': None}
Best cross-validation AUC: 0.892
```

## W3-D20-T4 - PASS

```text
Training sizes: [ 90 180 300]
Validation AUC: [0.855 0.854 0.881]
Saved: week3/day20/output/learning-curve.png
```

## W3-D20-T5 - PASS

```text
Rows = actual; columns = predicted; order = [stay, churn]
[[2 1]
 [1 2]]
True negatives: 2 False positives: 1
False negatives: 1 True positives: 2
Illustrative total error cost: 110
```

## W3-D20-T6 - SKIPPED

Not executed: XGBoost installation was unavailable. No fabricated output is supplied.

## W3-D20-T7 - PASS

```text
Average precision (PR summary): 0.737
Threshold, precision, recall, F1: [0.2   0.522 0.818 0.637]
Threshold, precision, recall, F1: [0.35  0.667 0.682 0.674]
Threshold, precision, recall, F1: [0.5   0.719 0.523 0.605]
Threshold, precision, recall, F1: [0.65  0.739 0.386 0.507]
Threshold, precision, recall, F1: [0.8   0.846 0.25  0.386]
Selected validation F1 threshold: 0.35
Freeze this choice before a final test. Average precision is not trapezoidal PR-AUC.
```
