# Week 3 - Day 21: Customer Churn Prediction System

Follow a complete educational pipeline over synthetic customer records. Preprocessing is inside every candidate Pipeline. Select a candidate using training-only CV, tune it, select an F1 threshold on validation, then evaluate the untouched final test.

## Before running

Install Week 3 requirements using the root README. Run each file from a terminal, in numeric task order. Each lesson generates or uses local sample data. No API keys or downloads are needed after package installation.

## Small tasks

### Week 3 - Day 21 - Task 1: Load and explore the synthetic dataset

- File: [customer-churn-prediction/w3-d21-t1-load-explore-churn.py](customer-churn-prediction/w3-d21-t1-load-explore-churn.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t1-load-explore-churn.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 2: Prepare mixed customer features

- File: [customer-churn-prediction/w3-d21-t2-preprocessing-pipeline.py](customer-churn-prediction/w3-d21-t2-preprocessing-pipeline.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t2-preprocessing-pipeline.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 3: Compare candidate pipelines using training-only CV

- File: [customer-churn-prediction/w3-d21-t3-train-compare-models.py](customer-churn-prediction/w3-d21-t3-train-compare-models.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t3-train-compare-models.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 4: Tune the strongest CV candidate

- File: [customer-churn-prediction/w3-d21-t4-tune-best-model.py](customer-churn-prediction/w3-d21-t4-tune-best-model.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t4-tune-best-model.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 5: Evaluate a frozen model and threshold on the held-out test

- File: [customer-churn-prediction/w3-d21-t5-final-evaluation.py](customer-churn-prediction/w3-d21-t5-final-evaluation.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t5-final-evaluation.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 6: Save the complete fitted pipeline

- File: [customer-churn-prediction/w3-d21-t6-save-pipeline-joblib.py](customer-churn-prediction/w3-d21-t6-save-pipeline-joblib.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t6-save-pipeline-joblib.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 7: Write an honest model-performance summary

- File: [customer-churn-prediction/w3-d21-t7-write-performance-summary.py](customer-churn-prediction/w3-d21-t7-write-performance-summary.py)
- Requested task or mini practice.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t7-write-performance-summary.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 8: Added task: predict a new customer using the saved pipeline

- File: [customer-churn-prediction/w3-d21-t8-predict-new-customer.py](customer-churn-prediction/w3-d21-t8-predict-new-customer.py)
- Added essential task.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t8-predict-new-customer.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 21 - Task 9: Run the complete Week 3 project

- File: [customer-churn-prediction/w3-d21-t9-customer-churn-prediction-system.py](customer-churn-prediction/w3-d21-t9-customer-churn-prediction-system.py)
- Added essential task.
- Run from this day folder: `python customer-churn-prediction/w3-d21-t9-customer-churn-prediction-system.py`
- Review status: Passed in explicit --sklearn-only mode; full XGBoost mode not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

## Project organization

- The numbered entry points live in customer-churn-prediction/ beside churn_common.py.
- Tasks 1-2 cover data and preprocessing. Tasks 3-9 require XGBoost by default.
- Explicit reduced mode: append `--sklearn-only` to a task 3-9 command. This omits XGBoost and is not the complete comparison.
- Each numbered task can run independently; training tasks rebuild prerequisites, so there is no hidden dependence on a previous interpreter session.
- The shared helper contains named functions for loading, validation, splitting, preprocessing, comparison, tuning, threshold selection, evaluation, saving, and report writing.
- Training uses 540 rows; validation uses 180; test uses 180 for the 900-row sample. Customer ID and churn are excluded from features.
- Model selection and tuning use only the training partition. Validation chooses the threshold. Do not revise choices after reading final-test results.
- The selected pipeline remains fitted on the training partition rather than being silently refitted after threshold selection.
- Default data are generated only if missing. The script does not overwrite an existing input CSV. Generated files in output/ are replaced on reruns.
- joblib loading can execute arbitrary code. Task 8 loads only an artifact it just created. Do not load a downloaded model from an untrusted source.
- No API service, cloud deployment, authentication, or monitoring is implemented.

## Success criteria

Run the final project, open its report and ROC chart, and verify saved-pipeline predictions. Explain that synthetic scores are not proof of production readiness.
