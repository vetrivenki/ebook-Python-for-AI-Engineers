"""Week 3 | Day 15 | Task 2: Keep three data partitions.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=600, random_state=42)
row_ids = np.arange(len(y))
train_ids, temporary_ids = train_test_split(
    row_ids,
    test_size=0.4,
    stratify=y,
    random_state=42,
)
valid_ids, test_ids = train_test_split(
    temporary_ids,
    test_size=0.5,
    stratify=y[temporary_ids],
    random_state=42,
)
# Train fits parameters. Validation guides choices. Test is the final check.
for name, ids in [("train", train_ids), ("validation", valid_ids), ("test", test_ids)]:
    print(name, "rows:", len(ids), "positive rate:", round(y[ids].mean(), 3))
assert not set(train_ids) & set(valid_ids)
assert not set(train_ids) & set(test_ids)
assert not set(valid_ids) & set(test_ids)
