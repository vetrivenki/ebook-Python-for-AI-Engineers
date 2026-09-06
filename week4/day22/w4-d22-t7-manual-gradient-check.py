"""Week 4, Day 22, Task 7: compare a manual derivative with autograd."""

import torch

x = torch.tensor(4.0, requires_grad=True)
y = x**3 + 2 * x
y.backward()
manual = 3 * x.item() ** 2 + 2
print("Manual gradient:", manual)
print("Autograd gradient:", x.grad.item())
print("Match:", abs(manual - x.grad.item()) < 1e-6)
