"""Check all Week 1 Python files with Ruff."""

from pathlib import Path
import subprocess
import sys

week1 = Path(__file__).parents[1]
subprocess.run([sys.executable, "-m", "ruff", "check", str(week1)], check=True)
print("Ruff check completed.")
