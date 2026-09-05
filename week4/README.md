# Week 4 — Deep Learning with PyTorch

Review update: see REVIEW.md. Day 28 now uses learnable synthetic color classes
and independent validation/test datasets. Retrain old checkpoints. PyTorch
runtime and GPU behavior remain unverified; syntax checks alone do not prove execution.

**Days 22–28** | **Final project:** Image Classifier from Scratch

Every learning task is a small runnable Python file named `w4-d<day>-t<task>-<description>.py`.
The examples default to small synthetic datasets, so no dataset download is required.

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run one task

```bash
python day22/w4-d22-t2-create-tensors.py
```

## Run the final project

```bash
python day28/image-classifier-from-scratch/w4-d28-t9-image-classifier-project.py
```

Outputs are written below each day's `output/` folder. Generated model files are not included; run the training task to create them.

## Added engineering coverage

- Deterministic seeds and device selection
- Tensor shape validation
- Train/validation data isolation
- Safe `state_dict` checkpoints
- Early stopping and structured logging
- Confusion matrix and per-class accuracy
- Single-image inference
- Smoke tests
