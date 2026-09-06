"""Week 4, Day 25, Task 3: compare max and average pooling."""

import torch
from torch import nn

x = torch.tensor(
    [
        [
            [
                [1.0, 2.0, 3.0, 4.0],
                [5.0, 6.0, 7.0, 8.0],
                [9.0, 10.0, 11.0, 12.0],
                [13.0, 14.0, 15.0, 16.0],
            ]
        ]
    ]
)
print("Max pool:\n", nn.MaxPool2d(2)(x).squeeze())
print("Average pool:\n", nn.AvgPool2d(2)(x).squeeze())
