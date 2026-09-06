"""Week 3 | Day 20 | Task 7: Added task: select a decision threshold.

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

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
probability = model.predict_proba(X_valid)[:, 1]
print(
    "Average precision (PR summary):",
    round(average_precision_score(y_valid, probability), 3),
)
rows = []
for threshold in [0.2, 0.35, 0.5, 0.65, 0.8]:
    labels = (probability >= threshold).astype(int)
    result = (
        threshold,
        precision_score(y_valid, labels, zero_division=0),
        recall_score(y_valid, labels, zero_division=0),
        f1_score(y_valid, labels, zero_division=0),
    )
    rows.append(result)
    print("Threshold, precision, recall, F1:", np.round(result, 3))
print("Selected validation F1 threshold:", max(rows, key=lambda row: row[3])[0])
print(
    "Freeze this choice before a final test. Average precision is not trapezoidal PR-AUC."
)
