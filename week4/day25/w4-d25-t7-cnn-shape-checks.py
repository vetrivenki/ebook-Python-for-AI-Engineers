from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 25, Task 7: catch wrong CNN input shapes."""
import torch
from week4_common import TinyCNN
model = TinyCNN()
correct = torch.randn(4, 3, 32, 32)
assert model(correct).shape == (4, 10)
wrong = torch.randn(4, 32, 32)
try:
    model(wrong)
except RuntimeError as error:
    print("Caught expected shape error:", str(error).splitlines()[0])
print("Correct NCHW shape passed.")

