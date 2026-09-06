import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 23, Task 7: run an MLP forward pass."""
import torch
from week4_common import TinyMLP, seed_everything

seed_everything()
model = TinyMLP()
features = torch.randn(6, 4)
logits = model(features)
print("Logits shape:", logits.shape)
print("Predicted classes:", logits.argmax(dim=1).tolist())
