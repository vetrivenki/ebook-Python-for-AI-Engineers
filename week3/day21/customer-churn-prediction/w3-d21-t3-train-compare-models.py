"""Week 3 | Day 21 | Task 3: Compare candidate pipelines using training-only CV.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import compare_models, load_data, parse_options, split_data

options = parse_options()
parts = split_data(load_data())
comparison = compare_models(parts, include_xgboost=not options.sklearn_only)
print(comparison.round(3).to_string(index=False))
print("Reduced scikit-learn-only mode:", options.sklearn_only)
