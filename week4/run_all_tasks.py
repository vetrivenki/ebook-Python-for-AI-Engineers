"""List or run every Week 4 task in filename order."""
import argparse, subprocess, sys
import re
from pathlib import Path
root=Path(__file__).resolve().parent
tasks=sorted(root.glob("day*/**/w4-d*-t*.py"),
             key=lambda p: tuple(map(int, re.findall(r"\d+", p.name)[:3])))
parser=argparse.ArgumentParser(); parser.add_argument("--run", action="store_true", help="execute every task"); args=parser.parse_args()
for task in tasks:
    print(task.relative_to(root))
    if args.run: subprocess.run([sys.executable, str(task)], check=True, cwd=root)
print(f"Total task files: {len(tasks)}")
