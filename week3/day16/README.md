# Week 3 - Day 16: Data Preprocessing for ML

Learn feature scaling, target versus feature encoding, missing-value imputation, and mixed-column pipelines. Fit preprocessing only on training rows. During cross-validation, place preprocessing inside the Pipeline so it is re-fitted separately in each fold.

## Before running

Install Week 3 requirements using the root README. Run each file from a terminal, in numeric task order. Each lesson generates or uses local sample data. No API keys or downloads are needed after package installation.

## Small tasks

### Week 3 - Day 16 - Task 1: Fit scalers only on training data

- File: [w3-d16-t1-feature-scaling.py](w3-d16-t1-feature-scaling.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t1-feature-scaling.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 2: Use the right categorical encoder

- File: [w3-d16-t2-categorical-encoding.py](w3-d16-t2-categorical-encoding.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t2-categorical-encoding.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 3: Impute missing values inside a pipeline

- File: [w3-d16-t3-missing-values-pipeline.py](w3-d16-t3-missing-values-pipeline.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t3-missing-values-pipeline.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 4: Route different columns through different steps

- File: [w3-d16-t4-column-transformer.py](w3-d16-t4-column-transformer.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t4-column-transformer.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 5: Recognize preprocessing leakage

- File: [w3-d16-t5-prevent-data-leakage.py](w3-d16-t5-prevent-data-leakage.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t5-prevent-data-leakage.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 6: Train a complete mixed-data pipeline

- File: [w3-d16-t6-mixed-data-pipeline-practice.py](w3-d16-t6-mixed-data-pipeline-practice.py)
- Requested task or mini practice.
- Run from this day folder: `python w3-d16-t6-mixed-data-pipeline-practice.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

### Week 3 - Day 16 - Task 7: Added task: split according to how data is collected

- File: [w3-d16-t7-group-and-time-splits.py](w3-d16-t7-group-and-time-splits.py)
- Added essential task.
- Run from this day folder: `python w3-d16-t7-group-and-time-splits.py`
- Review status: Executed successfully with the supplied sample.
- Practice: predict the output, run the file, change one input or parameter, and explain the difference. See OUTPUTS.md for the captured reference run.

## Success criteria

Build a mixed-data pipeline, transform an unseen category, and explain when group/time splitting is safer than random row splitting.
