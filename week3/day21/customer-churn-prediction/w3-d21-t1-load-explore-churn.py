"""Week 3 | Day 21 | Task 1: Load and explore the synthetic dataset.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import load_data, split_data

frame = load_data()
print(frame.head().to_string(index=False))
print("Rows and columns:", frame.shape)
print("Missing values:\n", frame.isna().sum())
print("Churn counts:\n", frame["churn"].value_counts())
parts = split_data(frame)
for name in ["train", "valid", "test"]:
    print(name, "rows:", len(parts["y_" + name]))
