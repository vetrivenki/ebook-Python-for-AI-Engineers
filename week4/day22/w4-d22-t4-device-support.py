from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 22, Task 4: select CUDA, MPS, or CPU."""
import torch
from week4_common import best_device

device = best_device()
tensor = torch.arange(5, dtype=torch.float32).to(device)
print("Device:", device)
print("Tensor:", tensor)
print("Back on CPU:", tensor.cpu())

