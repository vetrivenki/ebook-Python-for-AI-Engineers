"""Week 4, Day 22, Task 2: create tensors in common ways."""

import numpy as np
import torch

print("List:", torch.tensor([[1, 2], [3, 4]]))
print("NumPy:", torch.from_numpy(np.array([1.5, 2.5], dtype=np.float32)))
print("Random:", torch.rand(2, 3))
print("Zeros:", torch.zeros(2, 2))
print("Ones:", torch.ones(2, 2))
