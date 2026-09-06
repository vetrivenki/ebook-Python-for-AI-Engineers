"""Week 3 | Day 17 | Task 7: Added task: inspect held-out permutation importance.

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
from sklearn.inspection import permutation_importance

model = RandomForestClassifier(n_estimators=60, random_state=42, n_jobs=1)
model.fit(X_train, y_train)
result = permutation_importance(
    model,
    X_valid,
    y_valid,
    scoring="roc_auc",
    n_repeats=5,
    random_state=42,
    n_jobs=1,
)
for feature in result.importances_mean.argsort()[::-1][:5]:
    print(
        "Feature",
        feature,
        "AUC drop",
        round(result.importances_mean[feature], 3),
        "+/-",
        round(result.importances_std[feature], 3),
    )
print("Correlated features may share importance. These scores do not prove causality.")
