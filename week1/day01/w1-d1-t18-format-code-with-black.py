"""Format all Week 1 Python files with Black."""

import subprocess
import sys
from pathlib import Path

week1 = Path(__file__).parents[1]
subprocess.run([sys.executable, "-m", "black", str(week1)], check=True)
print("Black formatting completed.")
