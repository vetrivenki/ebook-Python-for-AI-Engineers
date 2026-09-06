"""Week 3 | Day 21 | Task 8: Added task: predict a new customer using the saved pipeline.

Keep churn_common.py beside this file. See its named functions for implementation.
For tasks 3-9, --sklearn-only explicitly omits XGBoost when unavailable.
"""

import joblib
import pandas as pd
from churn_common import (
    OUTPUT,
    fit_solution,
    parse_options,
    save_solution,
    validate_features,
)

options = parse_options()
solution = fit_solution(include_xgboost=not options.sklearn_only)
save_solution(solution)
# Load only the trusted artifact just created above, not a downloaded pickle.
bundle = joblib.load(OUTPUT / "churn-pipeline.joblib")
customer = pd.DataFrame(
    [
        {
            "tenure_months": 12,
            "monthly_charge": 80.0,
            "support_calls": 3,
            "contract": "monthly",
            "payment_method": "card",
        }
    ]
)
probability = bundle["pipeline"].predict_proba(validate_features(customer))[0, 1]
print("Estimated churn score:", round(probability, 3))
print("Decision threshold:", round(bundle["threshold"], 2))
print("Predicted churn:", bool(probability >= bundle["threshold"]))
print("This score is not guaranteed to be a calibrated real-world probability.")
