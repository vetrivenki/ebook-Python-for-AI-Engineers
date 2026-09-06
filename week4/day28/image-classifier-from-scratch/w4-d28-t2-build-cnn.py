import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 2: build the project CNN from scratch."""
import torch
from project_common import ImageCNN

model = ImageCNN()
output = model(torch.randn(4, 3, 32, 32))
print(model)
print("Output shape:", output.shape)
print("Parameters:", sum(p.numel() for p in model.parameters()))
