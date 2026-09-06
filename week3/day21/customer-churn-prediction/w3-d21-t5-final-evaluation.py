"""Week 3 | Day 21 | Task 5: Evaluate a frozen model and threshold on the held-out test.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import evaluate_solution, fit_solution, parse_options

options = parse_options()
solution = fit_solution(include_xgboost=not options.sklearn_only)
metrics = evaluate_solution(solution)
print("Frozen validation-selected threshold:", round(solution["threshold"], 2))
print("Test metrics:", metrics)
print("The ROC chart and classification report were saved in output/.")
