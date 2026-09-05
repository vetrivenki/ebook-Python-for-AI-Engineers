# Week 4 review

Fixed model/batch device mismatches, changing validation splits and evaluation overlap, hidden training during model loading, and task-runner relative paths. Day 26 now generates and batches image-folder data. Day 28 inference accepts --image PATH. The final task now generates evaluation and a written summary.

The final project now uses learnable synthetic color classes, not FakeData or real-world objects. Training uses seed 42; fixed 100-image validation uses seed 43; held-out test uses seed 44. Do not tune on the test results. Old checkpoints must be retrained. Missing checkpoints raise an error instead of silently training.

56 Python files pass syntax checks. PyTorch and torchvision are absent: runtime, GPU behavior and accuracy are NOT verified. Run python run_all_tasks.py --run after installing requirements.txt. Concept-only short examples are still educational demonstrations, not production implementations.

Only load trusted checkpoints. Reference: https://docs.pytorch.org/docs/stable/generated/torch.load.html

