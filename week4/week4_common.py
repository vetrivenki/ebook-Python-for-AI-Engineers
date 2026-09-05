"""Shared, beginner-friendly helpers for Week 4 examples."""
from __future__ import annotations

import random
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def seed_everything(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def best_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def classification_loaders(samples: int = 240, features: int = 4, batch_size: int = 32):
    seed_everything()
    x = torch.randn(samples, features)
    y = (x[:, 0] + 0.7 * x[:, 1] > 0).long()
    split = int(samples * 0.8)
    train = DataLoader(TensorDataset(x[:split], y[:split]), batch_size=batch_size, shuffle=True)
    valid = DataLoader(TensorDataset(x[split:], y[split:]), batch_size=batch_size)
    return train, valid


def image_loaders(samples: int = 256, batch_size: int = 32, classes: int = 10):
    seed_everything()
    images = torch.rand(samples, 3, 32, 32)
    labels = torch.arange(samples) % classes
    split = int(samples * 0.8)
    train = DataLoader(TensorDataset(images[:split], labels[:split]), batch_size=batch_size, shuffle=True)
    valid = DataLoader(TensorDataset(images[split:], labels[split:]), batch_size=batch_size)
    return train, valid


class TinyMLP(nn.Module):
    def __init__(self, inputs: int = 4, classes: int = 2):
        super().__init__()
        self.layers = nn.Sequential(nn.Linear(inputs, 16), nn.ReLU(), nn.Linear(16, classes))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layers(x)


class TinyCNN(nn.Module):
    def __init__(self, classes: int = 10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.AdaptiveAvgPool2d((1, 1)),
        )
        self.classifier = nn.Linear(32, classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.classifier(self.features(x).flatten(1))


def run_epoch(model, loader, loss_fn, optimizer=None, device=None):
    # Follow the model's current device; never move only the batch to a GPU.
    model_device = next(model.parameters()).device
    device = torch.device(device) if device is not None else model_device
    if device.type == model_device.type and device.index is None:
        device = model_device
    if device != model_device:
        raise ValueError("Move the model to the requested device before creating the optimizer.")
    training = optimizer is not None
    model.train(training)
    total_loss = correct = total = 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        if training:
            optimizer.zero_grad()
        with torch.set_grad_enabled(training):
            logits = model(x)
            loss = loss_fn(logits, y)
            if training:
                loss.backward()
                optimizer.step()
        total_loss += loss.item() * y.size(0)
        correct += (logits.argmax(1) == y).sum().item()
        total += y.size(0)
    if total == 0:
        raise ValueError("The loader must contain at least one sample.")
    return total_loss / total, correct / total


def save_state(model: nn.Module, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), path)
