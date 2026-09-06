"""Week 3 | Day 19 | Task 4: Change a few parameters deliberately.

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

from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

# A small validation experiment, not an exhaustive tuning strategy.
for depth, rate, trees in [(2, 0.05, 50), (3, 0.1, 80), (5, 0.05, 100)]:
    model = XGBClassifier(
        max_depth=depth,
        learning_rate=rate,
        n_estimators=trees,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        tree_method="hist",
        random_state=42,
        n_jobs=1,
    )
    model.fit(X_train, y_train)
    auc = roc_auc_score(y_valid, model.predict_proba(X_valid)[:, 1])
    print("Depth/rate/trees:", depth, rate, trees, "validation AUC:", round(auc, 3))
print("Lower learning rates usually need more trees; deeper trees increase capacity.")
