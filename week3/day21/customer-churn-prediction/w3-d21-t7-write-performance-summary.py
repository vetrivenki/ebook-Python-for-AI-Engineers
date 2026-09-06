"""Week 3 | Day 21 | Task 7: Write an honest model-performance summary.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import evaluate_solution, fit_solution, parse_options, write_summary

options = parse_options()
solution = fit_solution(include_xgboost=not options.sklearn_only)
metrics = evaluate_solution(solution)
write_summary(solution, metrics)
