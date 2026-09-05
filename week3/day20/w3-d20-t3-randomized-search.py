"""Week 3 | Day 20 | Task 3: Sample hyperparameter combinations.

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

from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42, n_jobs=1),
    {"n_estimators": [40, 80, 120], "max_depth": [3, 5, None], "min_samples_leaf": [1, 3, 6]},
    n_iter=5, cv=StratifiedKFold(3, shuffle=True, random_state=42),
    scoring="roc_auc", random_state=42, n_jobs=1,
)
search.fit(X_train, y_train)
print("Best parameters:", search.best_params_)
print("Best cross-validation AUC:", round(search.best_score_, 3))
