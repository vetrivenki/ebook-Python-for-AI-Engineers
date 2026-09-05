"""Week 3 | Day 20 | Task 6: Practice: tune XGBoost on training folds.

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

from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.metrics import roc_auc_score

baseline = XGBClassifier(n_estimators=80, max_depth=3, learning_rate=0.08, subsample=0.9, colsample_bytree=0.9, eval_metric="logloss", tree_method="hist", random_state=42, n_jobs=1)
baseline.fit(X_train, y_train)
search = RandomizedSearchCV(
    XGBClassifier(n_estimators=80, max_depth=3, learning_rate=0.08, subsample=0.9, colsample_bytree=0.9, eval_metric="logloss", tree_method="hist", random_state=42, n_jobs=1),
    {"n_estimators": [40, 80, 120], "max_depth": [2, 3, 5],
     "learning_rate": [0.03, 0.08, 0.15], "subsample": [0.7, 1.0]},
    n_iter=5, cv=StratifiedKFold(3, shuffle=True, random_state=42),
    scoring="roc_auc", random_state=42, n_jobs=1,
)
search.fit(X_train, y_train)
print("Best parameters:", search.best_params_)
print("Baseline validation AUC:", round(roc_auc_score(y_valid, baseline.predict_proba(X_valid)[:, 1]), 3))
print("Tuned validation AUC:", round(roc_auc_score(y_valid, search.predict_proba(X_valid)[:, 1]), 3))
print("No shared eval_set is used across folds; tree counts are tuned instead.")
