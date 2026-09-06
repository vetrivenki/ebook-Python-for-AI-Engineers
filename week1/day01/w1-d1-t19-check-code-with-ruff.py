"""Check all Week 1 Python files with Ruff."""

import subprocess
import sys
from pathlib import Path

week1 = Path(__file__).parents[1]
subprocess.run([sys.executable, "-m", "ruff", "check", str(week1)], check=True)
print("Ruff check completed.")
