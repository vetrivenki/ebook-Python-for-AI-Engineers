from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 2: create SGD and Adam optimizers."""
import torch
from week4_common import TinyMLP
model = TinyMLP()
sgd = torch.optim.SGD(model.parameters(), lr=0.05, momentum=0.9)
adam = torch.optim.Adam(model.parameters(), lr=0.001)
print(sgd)
print(adam)

