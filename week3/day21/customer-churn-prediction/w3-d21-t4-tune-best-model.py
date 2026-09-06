"""Week 3 | Day 21 | Task 4: Tune the strongest CV candidate.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import (
    compare_models,
    load_data,
    parse_options,
    split_data,
    tune_model,
)

options = parse_options()
parts = split_data(load_data())
comparison = compare_models(parts, include_xgboost=not options.sklearn_only)
name, search = tune_model(parts, comparison, include_xgboost=not options.sklearn_only)
print("Selected model:", name)
print("Best parameters:", search.best_params_)
print("Selected training-CV AUC:", round(search.best_score_, 3))
