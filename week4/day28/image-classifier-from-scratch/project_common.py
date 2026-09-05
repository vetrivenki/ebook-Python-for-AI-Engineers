"""Reusable components for the Day 28 image-classifier project."""
from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms

CLASSES = [f"class-{i}" for i in range(10)]
OUTPUT = Path(__file__).with_name("output")


def seed_all(seed=42):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)


def device():
    if torch.cuda.is_available(): return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available(): return torch.device("mps")
    return torch.device("cpu")


def loaders(samples=500, batch_size=32):
    """Independent synthetic color-pattern sets; validation never changes with train size."""
    if samples < 50 or batch_size < 1:
        raise ValueError("Use at least 50 samples and a positive batch size.")
    train = pattern_data(int(samples * 0.8), seed=42)
    valid = pattern_data(100, seed=43)
    return DataLoader(train, batch_size=batch_size, shuffle=True, num_workers=0), DataLoader(valid, batch_size=batch_size, num_workers=0)


def pattern_data(count, seed):
    """Ten learnable color classes with independent noise; not real-world images."""
    generator = torch.Generator().manual_seed(seed)
    labels = torch.arange(count) % 10
    palette = torch.tensor([[0.1 + 0.8 * ((i >> bit) & 1) for bit in range(3)] for i in range(8)]
                           + [[0.5, 0.5, 0.5], [0.9, 0.5, 0.1]])
    noise = torch.randn(count, 3, 32, 32, generator=generator) * 0.08
    images = (palette[labels, :, None, None] + noise).clamp(0, 1)
    return TensorDataset(images * 2 - 1, labels.long())


def test_loader():
    """Held-out seed, used only after architecture and training decisions are frozen."""
    return DataLoader(pattern_data(100, seed=44), batch_size=32)


class ImageCNN(nn.Module):
    def __init__(self, classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.AdaptiveAvgPool2d(1),
        )
        self.classifier = nn.Sequential(nn.Flatten(), nn.Dropout(0.2), nn.Linear(128, classes))
    def forward(self, x): return self.classifier(self.features(x))


def one_epoch(model, loader, loss_fn, optimizer=None, on_device=None):
    on_device = on_device or next(model.parameters()).device
    training = optimizer is not None; model.train(training)
    total_loss = correct = count = 0
    for images, labels in loader:
        images, labels = images.to(on_device), labels.to(on_device)
        if training: optimizer.zero_grad()
        with torch.set_grad_enabled(training):
            logits = model(images); loss = loss_fn(logits, labels)
            if training: loss.backward(); optimizer.step()
        total_loss += loss.item() * labels.size(0); correct += (logits.argmax(1) == labels).sum().item(); count += labels.size(0)
    return {"loss": total_loss/count, "accuracy": correct/count}


def train(epochs=2, samples=500):
    if epochs < 1:
        raise ValueError("epochs must be positive")
    seed_all(); on_device = device(); train_loader, valid_loader = loaders(samples=samples)
    model = ImageCNN().to(on_device); optimizer = torch.optim.Adam(model.parameters(), lr=0.001); loss_fn = nn.CrossEntropyLoss()
    OUTPUT.mkdir(exist_ok=True); best = -1.0; history = []
    for epoch in range(1, epochs+1):
        train_metrics = one_epoch(model, train_loader, loss_fn, optimizer, on_device)
        valid_metrics = one_epoch(model, valid_loader, loss_fn, on_device=on_device)
        row = {"epoch":epoch, "train":train_metrics, "validation":valid_metrics}; history.append(row); print(json.dumps(row))
        if valid_metrics["accuracy"] > best:
            best = valid_metrics["accuracy"]
            torch.save({"model_state":model.state_dict(), "classes":CLASSES,
                        "architecture":"ImageCNN", "dataset_version":"color-patterns-v1",
                        "normalization":"x * 2 - 1"}, OUTPUT/"best-model.pt")
    (OUTPUT/"metrics.json").write_text(json.dumps(history, indent=2))
    return model, history


def load_model(path=OUTPUT/"best-model.pt"):
    if not Path(path).exists():
        raise FileNotFoundError("Run Day 28 task 3 or task 9 to train a model first.")
    checkpoint = torch.load(path, map_location="cpu", weights_only=True)
    if checkpoint.get("dataset_version") != "color-patterns-v1":
        raise ValueError("Old or incompatible checkpoint: retrain with the reviewed code.")
    model = ImageCNN(classes=len(checkpoint["classes"])); model.load_state_dict(checkpoint["model_state"]); model.eval()
    return model, checkpoint["classes"]
