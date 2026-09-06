"""Week 4, Day 22, Task 5: build an autograd computation graph."""

import torch

x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2 * x + 1
print("Result:", y.item())
print("Graph operation:", y.grad_fn)
