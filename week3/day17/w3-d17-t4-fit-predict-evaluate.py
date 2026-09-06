"""Week 3 | Day 17 | Task 4: Understand the model lifecycle.

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

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)  # Learn from training rows.
labels = model.predict(X_valid)  # Return a class per validation row.
probabilities = model.predict_proba(X_valid)[:, 1]  # Continuous positive-class score.
print("First five labels:", labels[:5])
print("First five positive probabilities:", probabilities[:5].round(3))
print(classification_report(y_valid, labels, zero_division=0))
