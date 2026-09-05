"""Week 3 | Day 16 | Task 7: Added task: split according to how data is collected.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.model_selection import GroupShuffleSplit, TimeSeriesSplit

X = np.arange(24).reshape(-1, 1)
customers = np.repeat(np.arange(8), 3)
splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
train, valid = next(splitter.split(X, groups=customers))
print("Training customers:", np.unique(customers[train]))
print("Validation customers:", np.unique(customers[valid]))
assert not set(customers[train]) & set(customers[valid])

# Here row order represents time. Train on past rows, validate on future rows.
for train, valid in TimeSeriesSplit(n_splits=3).split(X):
    print("Latest training row:", train[-1], "first validation row:", valid[0])
    assert train[-1] < valid[0]
print("Choose group/time splits for repeated customers or future forecasting.")
