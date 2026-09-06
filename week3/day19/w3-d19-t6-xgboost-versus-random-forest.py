"""Week 3 | Day 19 | Task 6: Practice: compare XGBoost fairly.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Each model lesson uses the same data and validation split.
X, y = make_classification(
    n_samples=600,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    weights=[0.7, 0.3],
    class_sep=0.8,
    random_state=42,
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42,
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

models = {
    "Random Forest": RandomForestClassifier(n_estimators=80, random_state=42, n_jobs=1),
    "XGBoost": XGBClassifier(
        n_estimators=80,
        max_depth=3,
        learning_rate=0.08,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric="logloss",
        tree_method="hist",
        random_state=42,
        n_jobs=1,
    ),
}
scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    scores[name] = roc_auc_score(y_valid, model.predict_proba(X_valid)[:, 1])
    print(name, "validation AUC:", round(scores[name], 3))
print(
    "XGBoost minus Random Forest:",
    round(scores["XGBoost"] - scores["Random Forest"], 3),
)
print("Improvement is a goal, not a guarantee. Keep an honest negative result.")
