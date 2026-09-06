"""Run every non-interactive Day 1 learning script."""

import subprocess
import sys
from pathlib import Path

current_file = Path(__file__).name
skip_files = {current_file, "w1-d1-t10-read-user-input.py"}

for script in sorted(Path(__file__).parent.glob("w1-d1-*.py")):
    if script.name in skip_files or "t18-" in script.name or "t19-" in script.name:
        continue
    print(f"\n--- Running {script.name} ---")
    subprocess.run([sys.executable, str(script)], check=True)
