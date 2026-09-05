# Week 3 - Day 16: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D16-T1 - PASS

```text
StandardScaler
Scaled training data: [[-1.22474487 -1.22474487]
 [ 0.          0.        ]
 [ 1.22474487  1.22474487]]
Future data using training statistics: [[2.44948974 2.44948974]]
MinMaxScaler
Scaled training data: [[0.  0. ]
 [0.5 0.5]
 [1.  1. ]]
Future data using training statistics: [[1.5 1.5]]
MinMaxScaler can return values outside [0, 1] for new data.
```

## W3-D16-T2 - PASS

```text
One-hot names: ['x0_annual' 'x0_monthly']
Unseen category: [[0. 0.]]
Ordered priorities: [[2.]
 [0.]
 [1.]]
Encoded targets: [1 0 1]
Class mapping: ['churn' 'stay']
```

## W3-D16-T3 - PASS

```text
Transformed train: [-1.22474487  0.          1.22474487]
Transformed future: [0.         9.79795897]
Training median: [20.]
```

## W3-D16-T4 - PASS

```text
Train shape: (90, 4)
Validation shape: (30, 4)
Feature names: ['numeric__tenure' 'numeric__monthly_fee' 'category__contract_annual'
 'category__contract_monthly']
```

## W3-D16-T5 - PASS

```text
Correct training-only mean: [20.]
Leaky mean that saw held-out data: [265.]
Use a Pipeline inside cross-validation so every fold fits its own scaler.
```

## W3-D16-T6 - PASS

```text
              precision    recall  f1-score   support

           0       0.73      1.00      0.85        22
           1       0.00      0.00      0.00         8

    accuracy                           0.73        30
   macro avg       0.37      0.50      0.42        30
weighted avg       0.54      0.73      0.62        30

New-category churn probability: 0.3266363361840824
```

## W3-D16-T7 - PASS

```text
Training customers: [0 2 3 4 6 7]
Validation customers: [1 5]
Latest training row: 5 first validation row: 6
Latest training row: 11 first validation row: 12
Latest training row: 17 first validation row: 18
Choose group/time splits for repeated customers or future forecasting.
```
