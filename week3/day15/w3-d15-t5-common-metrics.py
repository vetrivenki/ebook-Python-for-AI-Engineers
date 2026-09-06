"""Week 3 | Day 15 | Task 5: Calculate classification and regression metrics.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    recall_score,
    roc_auc_score,
)

actual = [0, 1, 1, 0, 1, 0]
probability = np.array([0.1, 0.8, 0.4, 0.7, 0.9, 0.2])
predicted = (probability >= 0.5).astype(int)
for name, metric in [
    ("Accuracy", accuracy_score),
    ("Precision", precision_score),
    ("Recall", recall_score),
    ("F1", f1_score),
]:
    print(name, round(metric(actual, predicted), 3))
# ROC-AUC needs continuous scores, not the thresholded labels.
print("ROC-AUC", round(roc_auc_score(actual, probability), 3))
actual_amount = [100, 200, 300]
predicted_amount = [110, 180, 330]
print("MAE", round(mean_absolute_error(actual_amount, predicted_amount), 3))
print("RMSE", round(np.sqrt(mean_squared_error(actual_amount, predicted_amount)), 3))
