"""Week 3 | Day 19 | Task 1: Train trees that correct previous errors.

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

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss

model = GradientBoostingClassifier(n_estimators=60, learning_rate=0.05, random_state=42)
model.fit(X_train, y_train)
for stage, probability in enumerate(model.staged_predict_proba(X_valid), start=1):
    if stage in [1, 10, 30, 60]:
        print(
            "Stage",
            stage,
            "validation log loss:",
            round(log_loss(y_valid, probability), 4),
        )
print("Boosting adds trees sequentially; more trees can also overfit.")
