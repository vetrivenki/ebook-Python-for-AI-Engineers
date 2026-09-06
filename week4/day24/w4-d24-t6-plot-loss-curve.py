import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 6: train an MLP and save its loss curve."""
import matplotlib.pyplot as plt
import torch
from torch import nn
from week4_common import TinyMLP, classification_loaders, run_epoch

train, _ = classification_loaders()
model = TinyMLP()
opt = torch.optim.Adam(model.parameters(), lr=0.02)
losses = [run_epoch(model, train, nn.CrossEntropyLoss(), opt)[0] for _ in range(8)]
out = Path(__file__).with_name("output") / "mlp-loss.png"
out.parent.mkdir(exist_ok=True)
plt.plot(losses, marker="o")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("MLP training loss")
plt.tight_layout()
plt.savefig(out)
print("Saved:", out)
