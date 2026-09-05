# Week 3 validation report

- Numbered task files: 50.
- Syntax parsed successfully: 53 Python files (50 tasks, shared helper, runner, tests).
- Executed task files: 45 passed, 0 failed.
- Skipped runtime checks: Day 19 Tasks 2, 4, 5, 6 and Day 20 Task 6; XGBoost installation was blocked in this environment.
- Day 21 Tasks 3-9 passed in explicit --sklearn-only mode. Their full XGBoost path has not been runtime-validated here.
- Unit checks: 14 passed. Run `python -m unittest discover -s tests -v`.
- Full execution transcript: validation/task-results.json and per-day OUTPUTS.md.

## Tested environment

Python 3.12; scikit-learn 1.8.0; NumPy 2.3.5; Pandas 2.2.3; Matplotlib 3.10.8; joblib 1.5.3. XGBoost was unavailable. No runtime results are claimed for LightGBM or CatBoost, which are overview-only.

## Reduced-mode project result on synthetic data

Logistic Regression ranked highest among the reduced-mode candidates by training-only cross-validation. Frozen-threshold final-test results: accuracy 0.6722, precision 0.5814, recall 0.9375, F1 0.7177, ROC-AUC 0.8286, average precision 0.7955. These describe one deterministic 900-row synthetic example, not real-world churn performance.

These checks verify execution and important invariants, not all possible inputs or production readiness. The final test must not become another tuning set. Future changes should be evaluated with a properly reserved test or nested validation design.
