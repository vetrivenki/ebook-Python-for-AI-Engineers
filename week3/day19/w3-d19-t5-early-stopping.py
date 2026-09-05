"""Week 3 | Day 19 | Task 5: Stop boosting using validation data.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Each model lesson uses the same data and validation split.
X, y = make_classification(
    n_samples=600, n_features=10, n_informative=6, n_redundant=2,
    weights=[0.7, 0.3], class_sep=0.8, random_state=42,
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42,
)

from xgboost import XGBClassifier

from sklearn.metrics import roc_auc_score

# early_stopping_rounds belongs in the constructor in modern XGBoost.
model = XGBClassifier(
    n_estimators=500, max_depth=3, learning_rate=0.08, early_stopping_rounds=20,
    eval_metric="logloss", tree_method="hist", random_state=42, n_jobs=1,
)
model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
print("Best iteration (zero-based):", model.best_iteration)
print("Validation AUC:", round(roc_auc_score(y_valid, model.predict_proba(X_valid)[:, 1]), 3))
print("Early stopping used validation data. Do not use the final test as eval_set.")
