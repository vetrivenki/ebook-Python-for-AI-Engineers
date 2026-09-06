import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 8: reusable end-to-end training function."""
import torch
from torch import nn
from week4_common import TinyCNN, best_device, image_loaders, run_epoch


def train_model(epochs=2):
    train, valid = image_loaders(samples=192)
    device = best_device()
    model = TinyCNN().to(device)
    opt = torch.optim.Adam(model.parameters(), lr=0.003)
    for epoch in range(1, epochs + 1):
        run_epoch(model, train, nn.CrossEntropyLoss(), opt, device)
        loss, accuracy = run_epoch(model, valid, nn.CrossEntropyLoss(), device=device)
        print(f"epoch={epoch} valid_loss={loss:.3f} valid_accuracy={accuracy:.1%}")
    return model


if __name__ == "__main__":
    train_model()
