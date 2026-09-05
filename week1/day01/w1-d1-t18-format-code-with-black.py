"""Format all Week 1 Python files with Black."""

from pathlib import Path
import subprocess
import sys

week1 = Path(__file__).parents[1]
subprocess.run([sys.executable, "-m", "black", str(week1)], check=True)
print("Black formatting completed.")
