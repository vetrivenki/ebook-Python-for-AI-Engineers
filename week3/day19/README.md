# Week 3 - Day 19: Gradient Boosting and XGBoost

Watch boosting improve successive stages, train XGBoost, vary core parameters, and use validation-only early stopping. LightGBM/CatBoost are overview-only optional libraries, not implementations claimed as tested. The comparison reports the measured difference, including losses.

## Before running

Install Week 3 requirements using the root README. Run each file from a terminal, in numeric task order. Each lesson generates or uses local sample data. No API keys or downloads are needed after package installation.

## Small tasks

### Week 3 - Day 19 - Task 1: Train trees that correct previous errors

- File: [w3-d19-t1-gradient-boosting.py](w3-d19-t1-gradient-boosting.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t1-gradient-boosting.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 19 - Task 2: Install and train XGBoost

- File: [w3-d19-t2-xgboost-training.py](w3-d19-t2-xgboost-training.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t2-xgboost-training.py`
- Review status: Syntax checked; XGBoost runtime not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 19 - Task 3: Compare boosting libraries conceptually

- File: [w3-d19-t3-lightgbm-catboost-overview.py](w3-d19-t3-lightgbm-catboost-overview.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t3-lightgbm-catboost-overview.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 19 - Task 4: Change a few parameters deliberately

- File: [w3-d19-t4-xgboost-hyperparameters.py](w3-d19-t4-xgboost-hyperparameters.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t4-xgboost-hyperparameters.py`
- Review status: Syntax checked; XGBoost runtime not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 19 - Task 5: Stop boosting using validation data

- File: [w3-d19-t5-early-stopping.py](w3-d19-t5-early-stopping.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t5-early-stopping.py`
- Review status: Syntax checked; XGBoost runtime not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 19 - Task 6: Practice: compare XGBoost fairly

- File: [w3-d19-t6-xgboost-versus-random-forest.py](w3-d19-t6-xgboost-versus-random-forest.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d19-t6-xgboost-versus-random-forest.py`
- Review status: Syntax checked; XGBoost runtime not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

## XGBoost compatibility

Use XGBoost 2.1 or newer within the supplied range. early_stopping_rounds is passed to XGBClassifier, not fit. A feature-preprocessing pipeline does not automatically transform a raw eval_set; the standalone early-stopping task intentionally uses already-numeric input. Do not use the test partition for early stopping.

## Success criteria

Train XGBoost after installing the package. Compare against Random Forest honestly; improvement is a practice goal, never a promised outcome.
