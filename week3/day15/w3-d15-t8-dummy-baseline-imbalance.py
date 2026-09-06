"""Week 3 | Day 15 | Task 8: Added task: establish a baseline.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, recall_score

X = [[i] for i in range(100)]
y = [0] * 90 + [1] * 10
model = DummyClassifier(strategy="most_frequent").fit(X, y)
prediction = model.predict(X)  # Illustrates a metric trap, not test performance.
print("Accuracy:", accuracy_score(y, prediction))
print("Positive-class recall:", recall_score(y, prediction))
print("Balanced accuracy:", balanced_accuracy_score(y, prediction))
print("90% accuracy can hide complete failure to identify the minority class.")
