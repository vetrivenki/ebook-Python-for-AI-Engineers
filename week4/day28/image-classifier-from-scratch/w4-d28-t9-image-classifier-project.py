from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 9: run the complete image-classifier project."""
from project_common import OUTPUT, train
if __name__ == "__main__":
    _, history=train(epochs=2, samples=500)
    best=max(row["validation"]["accuracy"] for row in history)
    print(f"Project complete. Best validation accuracy: {best:.1%}")
    print("Outputs:", OUTPUT)
    import runpy
    for task in ["w4-d28-t4-evaluate-performance.py", "w4-d28-t6-write-project-summary.py"]:
        runpy.run_path(str(Path(__file__).with_name(task)), run_name="__main__")
