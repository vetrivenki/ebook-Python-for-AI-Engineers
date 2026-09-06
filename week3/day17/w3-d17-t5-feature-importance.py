"""Week 3 | Day 17 | Task 5: Inspect tree feature importance.

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

model = RandomForestClassifier(n_estimators=80, random_state=42, n_jobs=1)
model.fit(X_train, y_train)
ranking = sorted(
    enumerate(model.feature_importances_), key=lambda item: item[1], reverse=True
)
for feature, importance in ranking:
    print("Feature", feature, "importance", round(importance, 3))
print("Impurity importance can favor high-cardinality features; it is not causation.")
