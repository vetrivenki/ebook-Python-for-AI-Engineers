"""Week 4, Day 22, Task 3: tensor operations and broadcasting."""

import torch

matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
offset = torch.tensor([10.0, 20.0])
print("Broadcast addition:\n", matrix + offset)
print("Matrix product:\n", matrix @ matrix.T)
print("Mean:", matrix.mean().item())
