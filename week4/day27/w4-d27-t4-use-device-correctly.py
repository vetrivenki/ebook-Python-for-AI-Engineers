import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 4: keep model and batch on the same device."""
import torch
from week4_common import TinyCNN, best_device

device = best_device()
model = TinyCNN().to(device)
images = torch.rand(8, 3, 32, 32, device=device)
with torch.inference_mode():
    predictions = model(images).argmax(1)
print("Device:", device, "predictions:", predictions.cpu().tolist())
