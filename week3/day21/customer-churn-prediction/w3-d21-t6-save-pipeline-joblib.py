"""Week 3 | Day 21 | Task 6: Save the complete fitted pipeline.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

from churn_common import fit_solution, parse_options, save_solution

options = parse_options()
solution = fit_solution(include_xgboost=not options.sklearn_only)
bundle = save_solution(solution)
print("Saved feature names:", bundle["features"])
print("Saved package versions:", bundle["versions"])
print("Round-trip probabilities verified for the locally created artifact.")
print("Never load a joblib/pickle artifact from an untrusted source.")
