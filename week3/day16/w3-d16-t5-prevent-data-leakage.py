"""Week 3 | Day 16 | Task 5: Recognize preprocessing leakage.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler

train = np.array([[10.0], [20.0], [30.0]])
held_out = np.array([[1000.0]])
safe_scaler = StandardScaler().fit(train)
print("Correct training-only mean:", safe_scaler.mean_)
# Deliberately bad example: DO NOT use this fitted scaler for evaluation.
leaky_scaler = StandardScaler().fit(np.vstack([train, held_out]))
print("Leaky mean that saw held-out data:", leaky_scaler.mean_)
print("Use a Pipeline inside cross-validation so every fold fits its own scaler.")
assert safe_scaler.mean_[0] == 20.0
