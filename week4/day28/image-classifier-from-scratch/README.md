# Day 28 Project — Image Classifier from Scratch

This project trains a CNN on ten learnable synthetic RGB color classes, not natural objects. Training, validation and final test use independent seeds 42, 43 and 44. Validation and test each contain 100 images, independent of training sample count. See ../../REVIEW.md for fixes and validation limits. Retrain old checkpoints before running inference. Runtime accuracy has not been measured here.

## Run

```bash
python w4-d28-t9-image-classifier-project.py
python w4-d28-t4-evaluate-performance.py
python w4-d28-t7-single-image-inference.py
```

## Outputs

- `output/best-model.pt` — safe state-dictionary checkpoint
- `output/metrics.json` — epoch metrics
- `output/confusion-matrix.csv` — evaluation counts
- `output/project-summary.md` — architecture and results summary

Model binaries are generated locally and excluded from the uploaded source files.
