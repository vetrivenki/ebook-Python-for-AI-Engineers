"""Week 3 | Day 15 | Task 7: Calculate classification metrics manually.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.model_selection import train_test_split

rows = list(range(20))
labels = [0, 1] * 10
train, test = train_test_split(rows, test_size=0.3, stratify=labels, random_state=42)
print("Training row IDs:", train)
print("Held-out row IDs:", test)

actual = [0, 1, 1, 0, 1, 0]
predicted = [0, 1, 0, 1, 1, 0]  # Fixed practice predictions, not a trained model.
tp = sum(a == 1 and p == 1 for a, p in zip(actual, predicted))
tn = sum(a == 0 and p == 0 for a, p in zip(actual, predicted))
fp = sum(a == 0 and p == 1 for a, p in zip(actual, predicted))
fn = sum(a == 1 and p == 0 for a, p in zip(actual, predicted))
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
print("TP, TN, FP, FN:", tp, tn, fp, fn)
print("Accuracy:", (tp + tn) / len(actual))
print("Precision, recall, F1:", precision, recall, f1)
assert tp == 2 and tn == 2 and fp == 1 and fn == 1
