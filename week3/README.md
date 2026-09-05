# Python for AI Engineers - Week 3

## ML with scikit-learn and XGBoost | Days 15-21

Final project: Customer Churn Prediction System.

50 numbered task files, plus one shared project module, one batch runner, and one test module. Every requested topic is mapped to a task. The naming format remains `w3-d15-t1-task-description.py`, with one folder per day and a separate Day 21 project folder. No ZIP archive is needed.

## Start here

1. Download week3 and preserve its folders. Place it beside week1 and week2 inside python-ai-90days.
2. Open a terminal in week3. Use Python 3.11 or 3.12.
3. Create an environment: `python -m venv .venv`.
4. Activate it: Windows Command Prompt `.venv\\Scripts\\activate.bat`; PowerShell `.venv\\Scripts\\Activate.ps1`; macOS/Linux `source .venv/bin/activate`.
5. Install dependencies: `python -m pip install -r requirements.txt`.
6. Check dependencies: `python -m pip check`.
7. Start with `python day15/w3-d15-t1-learning-types.py`.

Use Tab completion for long names. If your operating system uses python3, substitute that executable. Select the same environment in your editor. Missing packages raise import errors; these scripts do not silently install anything.

## Daily navigation

| Day | Focus | Task files | Instructions |
| --- | --- | ---: | --- |
| 15 | Machine Learning Foundations | 8 | [Day 15 instructions](day15/README.md) |
| 16 | Data Preprocessing for ML | 7 | [Day 16 instructions](day16/README.md) |
| 17 | Classical Models I | 7 | [Day 17 instructions](day17/README.md) |
| 18 | Classical Models II | 6 | [Day 18 instructions](day18/README.md) |
| 19 | Gradient Boosting and XGBoost | 6 | [Day 19 instructions](day19/README.md) |
| 20 | Model Evaluation and Hyperparameter Tuning | 7 | [Day 20 instructions](day20/README.md) |
| 21 | Customer Churn Prediction System | 9 | [Day 21 instructions](day21/README.md) |

## Full project and checks

Run from week3:

```bash
python day21/customer-churn-prediction/w3-d21-t9-customer-churn-prediction-system.py
python -m unittest discover -s tests -v
python run_all_tasks.py
```

The full runner executes all 50 tasks in numeric order and saves validation/task-results.json. It may take several minutes because each file is independent and Day 21 rebuilds prerequisites. CPU only; parallelism is limited to avoid overwhelming a laptop. Run one day or task at a time while learning.

## Explicit reduced mode

If XGBoost cannot be installed, use `requirements-sklearn-only.txt` instead, then run:

```bash
python run_all_tasks.py --sklearn-only
python day21/customer-churn-prediction/w3-d21-t9-customer-churn-prediction-system.py --sklearn-only
```

This intentionally skips five XGBoost-only lessons and omits XGBoost from the final model comparison. It does not count as completing all Week 3 tasks. LightGBM and CatBoost are optional conceptual overviews and are not required packages.

## Packages and why they are here

| Install name | Import | Role |
| --- | --- | --- |
| scikit-learn | sklearn | Preprocessing, estimators, CV, search, metrics |
| xgboost | xgboost | Boosted trees, CPU histogram training, early stopping |
| numpy | numpy | Arrays, random sample generation, numeric checks |
| pandas | pandas | Tables, CSV input/output, comparison results |
| matplotlib | matplotlib | ROC and learning-curve images, without a GUI |
| joblib | joblib | Serialize the full preprocessing/model pipeline |

pathlib, json, unittest, argparse, subprocess, and importlib belong to Python's standard library and need no pip install. Requirements use compatibility ranges rather than a lockfile; VALIDATION.md records what was actually tested.

## Added essential tasks

- Day 15 Task 8: dummy baseline and class imbalance.
- Day 16 Task 7: group-aware and time-ordered data splitting.
- Day 17 Task 7: permutation importance and interpretation limits.
- Day 20 Task 7: precision-recall evaluation and validation-only threshold selection.
- Day 21 Task 8: trusted pipeline loading and new-customer prediction.
- Day 21 Task 9: one-command complete project entry point.
- Project checks: missing columns, invalid values, duplicate IDs, one-class data, entirely missing features, train/validation/test separation, unseen categories, and save/load consistency.

## Data and output safety

All sample customer data are synthetic. No credentials or private records are included. Do not replace these samples with private customer data in a shared learning folder. The project generates data/sample-churn.csv only if absent. Outputs are overwritten on reruns; keep copies of experiments you want to retain.

The final project saves a ROC chart, classification report, metrics, comparison tables, a written summary, package metadata, and a local joblib pipeline. The binary pipeline is deliberately not distributed: regenerate it locally, and never load untrusted pickle/joblib files.

The current saved project outputs come from reduced scikit-learn-only mode. See day-specific OUTPUTS.md and VALIDATION.md. The code is educational and production-style in organization, not a deployed production system. XGBoost is not guaranteed to outperform Random Forest.
