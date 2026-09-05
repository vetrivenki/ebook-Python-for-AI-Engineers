from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 25, Task 4: build a simple CNN."""
import torch
from week4_common import TinyCNN
model = TinyCNN(classes=10)
print(model)
print("Output shape:", model(torch.randn(4, 3, 32, 32)).shape)

