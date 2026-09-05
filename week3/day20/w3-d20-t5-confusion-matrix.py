"""Week 3 | Day 20 | Task 5: Explain error types and costs.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.metrics import confusion_matrix

actual = [0, 0, 0, 1, 1, 1]
predicted = [0, 0, 1, 0, 1, 1]
matrix = confusion_matrix(actual, predicted, labels=[0, 1])
tn, fp, fn, tp = matrix.ravel()
print("Rows = actual; columns = predicted; order = [stay, churn]")
print(matrix)
print("True negatives:", tn, "False positives:", fp)
print("False negatives:", fn, "True positives:", tp)
# Assumed costs, not a measured commercial result.
cost = fp * 10 + fn * 100
print("Illustrative total error cost:", cost)
assert (tn, fp, fn, tp) == (2, 1, 1, 2)
