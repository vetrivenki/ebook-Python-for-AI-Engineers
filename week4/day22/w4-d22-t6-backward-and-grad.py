"""Week 4, Day 22, Task 6: call backward and inspect gradients."""

import torch

weight = torch.tensor(2.0, requires_grad=True)
loss = (weight * 3 - 10) ** 2
loss.backward()
print("Loss:", loss.item())
print("dLoss/dWeight:", weight.grad.item())
