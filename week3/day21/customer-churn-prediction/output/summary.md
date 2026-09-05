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
