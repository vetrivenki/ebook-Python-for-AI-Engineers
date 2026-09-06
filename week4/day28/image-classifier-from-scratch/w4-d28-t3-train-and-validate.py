import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 3: run full training and validation."""
from project_common import train

if __name__ == "__main__":
    _, history = train(epochs=2, samples=500)
    print("Completed epochs:", len(history))
