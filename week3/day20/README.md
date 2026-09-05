# Week 3 - Day 20: Model Evaluation and Hyperparameter Tuning

Use stratified CV, grid and randomized search, learning curves, and confusion-matrix costs. Keep threshold selection on validation data. The XGBoost search tunes tree counts without sharing one eval_set across CV folds.

## Before running

Install Week 3 requirements using the root README. Run each file from a terminal, in numeric task order. Each lesson generates or uses local sample data. No API keys or downloads are needed after package installation.

## Small tasks

### Week 3 - Day 20 - Task 1: Use identical stratified folds

- File: [w3-d20-t1-stratified-cross-validation.py](w3-d20-t1-stratified-cross-validation.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t1-stratified-cross-validation.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 2: Search a small parameter grid

- File: [w3-d20-t2-grid-search.py](w3-d20-t2-grid-search.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t2-grid-search.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 3: Sample hyperparameter combinations

- File: [w3-d20-t3-randomized-search.py](w3-d20-t3-randomized-search.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t3-randomized-search.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 4: Plot performance versus training-set size

- File: [w3-d20-t4-learning-curves.py](w3-d20-t4-learning-curves.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t4-learning-curves.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 5: Explain error types and costs

- File: [w3-d20-t5-confusion-matrix.py](w3-d20-t5-confusion-matrix.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t5-confusion-matrix.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 6: Practice: tune XGBoost on training folds

- File: [w3-d20-t6-xgboost-search-practice.py](w3-d20-t6-xgboost-search-practice.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d20-t6-xgboost-search-practice.py`
- Review status: Syntax checked; XGBoost runtime not tested.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 20 - Task 7: Added task: select a decision threshold

- File: [w3-d20-t7-precision-recall-and-thresholds.py](w3-d20-t7-precision-recall-and-thresholds.py)
- Added essential task.
- Run from this day folder: `python w3-d20-t7-precision-recall-and-thresholds.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

## Success criteria

Explain how the pipeline prevents leakage, report CV variation, select a threshold using validation data, and reserve a final test.
