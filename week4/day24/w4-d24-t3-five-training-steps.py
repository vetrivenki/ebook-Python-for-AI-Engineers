import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 3: zero grad, forward, loss, backward, step."""
import torch
from torch import nn
from week4_common import TinyMLP

model = TinyMLP()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
x = torch.randn(16, 4)
y = (x[:, 0] > 0).long()
optimizer.zero_grad()
logits = model(x)
loss = nn.CrossEntropyLoss()(logits, y)
loss.backward()
optimizer.step()
print("One training-step loss:", loss.item())
