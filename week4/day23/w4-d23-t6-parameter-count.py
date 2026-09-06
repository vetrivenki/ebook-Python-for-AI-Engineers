import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 23, Task 6: inspect trainable parameters."""
from week4_common import TinyMLP

model = TinyMLP()
for name, parameter in model.named_parameters():
    print(name, tuple(parameter.shape))
print(
    "Trainable parameters:",
    sum(p.numel() for p in model.parameters() if p.requires_grad),
)
