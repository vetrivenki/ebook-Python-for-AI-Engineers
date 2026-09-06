"""Week 3 | Day 21 | Task 2: Prepare mixed customer features.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

import numpy as np
from churn_common import load_data, make_preprocessor, split_data

parts = split_data(load_data())
preprocessor = make_preprocessor()
train = preprocessor.fit_transform(parts["X_train"])
valid = preprocessor.transform(parts["X_valid"])
print("Training shape:", train.shape)
print("Validation shape:", valid.shape)
print("Output names:", preprocessor.get_feature_names_out())
assert np.isfinite(train).all() and np.isfinite(valid).all()
