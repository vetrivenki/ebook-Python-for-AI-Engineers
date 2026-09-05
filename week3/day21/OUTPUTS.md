# Week 3 - Day 21: captured output

These are real outputs from the supplied samples. Floating-point rounding and timing can differ by environment. Day 21 tasks 3-9 used --sklearn-only; XGBoost-only tasks were skipped, not passed.

## W3-D21-T1 - PASS

```text
customer_id  tenure_months  monthly_charge  support_calls contract payment_method  churn
  DEMO-0000            7.0           24.24            3.0  monthly         manual      0
  DEMO-0001           56.0          108.41            1.0  monthly  bank_transfer      1
  DEMO-0002           48.0           90.96            3.0   annual           card      1
  DEMO-0003           32.0           37.31            3.0   annual           card      0
  DEMO-0004           32.0           29.17            2.0  monthly  bank_transfer      1
Rows and columns: (900, 7)
Missing values:
 customer_id        0
tenure_months      0
monthly_charge    25
support_calls      0
contract           0
payment_method    15
churn              0
dtype: int64
Churn counts:
 churn
0    501
1    399
Name: count, dtype: int64
train rows: 540
valid rows: 180
test rows: 180
```

## W3-D21-T2 - PASS

```text
Training shape: (540, 8)
Validation shape: (180, 8)
Output names: ['numeric__tenure_months' 'numeric__monthly_charge'
 'numeric__support_calls' 'categorical__contract_annual'
 'categorical__contract_monthly'
 'categorical__payment_method_bank_transfer'
 'categorical__payment_method_card' 'categorical__payment_method_manual']
```

## W3-D21-T3 - PASS

```text
              model  cv_auc  cv_std
Logistic Regression   0.784   0.026
      Random Forest   0.733   0.009
     Dummy baseline   0.500   0.000
Reduced scikit-learn-only mode: True
```

## W3-D21-T4 - PASS

```text
Selected model: Logistic Regression
Best parameters: {'model__C': 1.0}
Selected training-CV AUC: 0.784
```

## W3-D21-T5 - PASS

```text
              precision    recall  f1-score   support

        stay       0.90      0.46      0.61       100
       churn       0.58      0.94      0.72        80

    accuracy                           0.67       180
   macro avg       0.74      0.70      0.66       180
weighted avg       0.76      0.67      0.66       180

Confusion matrix [stay, churn]:
 [[46 54]
 [ 5 75]]
Frozen validation-selected threshold: 0.25
Test metrics: {'accuracy': 0.6722222222222223, 'precision': 0.5813953488372093, 'recall': 0.9375, 'f1': 0.7177033492822966, 'roc_auc': 0.828625, 'average_precision': 0.7955452921706309}
The ROC chart and classification report were saved in output/.
```

## W3-D21-T6 - PASS

```text
Saved trusted local pipeline: week3/day21/customer-churn-prediction/output/churn-pipeline.joblib
Saved feature names: ['tenure_months', 'monthly_charge', 'support_calls', 'contract', 'payment_method']
Saved package versions: {'scikit-learn': '1.8.0', 'numpy': '2.3.5', 'pandas': '2.2.3', 'joblib': '1.5.3'}
Round-trip probabilities verified for the locally created artifact.
Never load a joblib/pickle artifact from an untrusted source.
```

## W3-D21-T7 - PASS

```text
              precision    recall  f1-score   support

        stay       0.90      0.46      0.61       100
       churn       0.58      0.94      0.72        80

    accuracy                           0.67       180
   macro avg       0.74      0.70      0.66       180
weighted avg       0.76      0.67      0.66       180

Confusion matrix [stay, churn]:
 [[46 54]
 [ 5 75]]
# Customer Churn Prediction - Learning Report

Data: 900 synthetic customers by default; not a real business dataset.

Selected model: Logistic Regression

XGBoost included: False

Selected parameters: {'model__C': 1.0}

Training-CV ROC-AUC: 0.784

Validation-selected decision threshold: 0.25

Final test metrics: {
  "accuracy": 0.6722222222222223,
  "precision": 0.5813953488372093,
  "recall": 0.9375,
  "f1": 0.7177033492822966,
  "roc_auc": 0.828625,
  "average_precision": 0.7955452921706309
}

Selection uses 3-fold CV on the 60% training partition; threshold selection uses the 20% validation partition. The remaining 20% is held out until final evaluation. Do not iterate on this test result. CV rankings have selection bias; the final test is an estimate from a small synthetic sample, not an operational guarantee.

The synthetic label generator uses tenure, contract, charge, support calls, and payment method. This is by construction, not an empirical causal insight about real customers. No deployment, authentication, privacy review, or drift monitoring is implemented.

Never load an untrusted joblib/pickle file. Reuse the recorded package versions.
```

## W3-D21-T8 - PASS

```text
Saved trusted local pipeline: week3/day21/customer-churn-prediction/output/churn-pipeline.joblib
Estimated churn score: 0.851
Decision threshold: 0.25
Predicted churn: True
This score is not guaranteed to be a calibrated real-world probability.
```

## W3-D21-T9 - PASS

```text
              precision    recall  f1-score   support

        stay       0.90      0.46      0.61       100
       churn       0.58      0.94      0.72        80

    accuracy                           0.67       180
   macro avg       0.74      0.70      0.66       180
weighted avg       0.76      0.67      0.66       180

Confusion matrix [stay, churn]:
 [[46 54]
 [ 5 75]]
Saved trusted local pipeline: week3/day21/customer-churn-prediction/output/churn-pipeline.joblib
# Customer Churn Prediction - Learning Report

Data: 900 synthetic customers by default; not a real business dataset.

Selected model: Logistic Regression

XGBoost included: False

Selected parameters: {'model__C': 1.0}

Training-CV ROC-AUC: 0.784

Validation-selected decision threshold: 0.25

Final test metrics: {
  "accuracy": 0.6722222222222223,
  "precision": 0.5813953488372093,
  "recall": 0.9375,
  "f1": 0.7177033492822966,
  "roc_auc": 0.828625,
  "average_precision": 0.7955452921706309
}

Selection uses 3-fold CV on the 60% training partition; threshold selection uses the 20% validation partition. The remaining 20% is held out until final evaluation. Do not iterate on this test result. CV rankings have selection bias; the final test is an estimate from a small synthetic sample, not an operational guarantee.

The synthetic label generator uses tenure, contract, charge, support calls, and payment method. This is by construction, not an empirical causal insight about real customers. No deployment, authentication, privacy review, or drift monitoring is implemented.

Never load an untrusted joblib/pickle file. Reuse the recorded package versions.
```
