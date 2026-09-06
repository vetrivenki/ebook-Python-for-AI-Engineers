"""Week 3 | Day 18 | Task 3: Train Naive Bayes.

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

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

model.fit(X_train, y_train)
prediction = model.predict(X_valid)
probability = model.predict_proba(X_valid)[:, 1]
print("Validation accuracy:", round(accuracy_score(y_valid, prediction), 3))
print("Validation F1:", round(f1_score(y_valid, prediction), 3))
print("Validation ROC-AUC:", round(roc_auc_score(y_valid, probability), 3))
