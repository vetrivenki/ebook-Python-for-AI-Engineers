"""Week 4, Day 22, Task 1: verify the PyTorch installation."""

try:
    import torch
except ImportError as error:
    raise SystemExit(
        "Install first: python -m pip install -r requirements.txt"
    ) from error
print("PyTorch:", torch.__version__)
print("Installation is ready.")
