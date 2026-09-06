"""Week 4, Day 22, Task 8: inspect shape/dtype and safely detach."""

import torch

x = torch.randn(2, 3, requires_grad=True)
y = (x * 2).sum()
y.backward()
print("Shape:", x.shape, "dtype:", x.dtype)
print("Gradient shape:", x.grad.shape)
print("Detached NumPy shape:", x.detach().cpu().numpy().shape)
