"""Run numbered lessons in numeric order; collect stdout, errors, and exit codes."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
XGBOOST_TASKS = {"w3-d19-t2", "w3-d19-t4", "w3-d19-t5", "w3-d19-t6", "w3-d20-t6"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sklearn-only", action="store_true", help="Skip XGBoost-only tasks; reduce the final project.")
    options = parser.parse_args()
    if not options.sklearn_only and importlib.util.find_spec("xgboost") is None:
        raise SystemExit("Install requirements.txt first, or explicitly use --sklearn-only for a PARTIAL run.")
    files = sorted(BASE.glob("day*/**/w3-*.py"), key=lambda p: tuple(map(int, re.findall(r"\d+", p.name)[:3])))
    results = []
    environment = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    for path in files:
        task_id = "-".join(path.stem.split("-")[:3])
        if options.sklearn_only and task_id in XGBOOST_TASKS:
            results.append({"task": task_id, "file": str(path.relative_to(BASE)), "status": "SKIPPED", "reason": "XGBoost not enabled"})
            print(task_id, "SKIPPED (not validated)")
            continue
        command = [sys.executable, str(path)]
        if options.sklearn_only and "day21" in path.parts and int(task_id.split("-t")[1]) >= 3:
            command.append("--sklearn-only")
        try:
            run = subprocess.run(command, capture_output=True, text=True, timeout=180, env=environment)
            status = "PASS" if run.returncode == 0 else "FAIL"
            result = {"task": task_id, "file": str(path.relative_to(BASE)), "status": status,
                      "returncode": run.returncode, "stdout": run.stdout, "stderr": run.stderr}
        except subprocess.TimeoutExpired:
            status = "FAIL"
            result = {"task": task_id, "file": str(path.relative_to(BASE)), "status": status, "reason": "180-second timeout"}
        results.append(result)
        print(task_id, status)
    output = BASE / "validation"
    output.mkdir(exist_ok=True)
    (output / "task-results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("PASS:", sum(r["status"] == "PASS" for r in results),
          "SKIPPED:", sum(r["status"] == "SKIPPED" for r in results),
          "FAIL:", sum(r["status"] == "FAIL" for r in results))
    if any(r["status"] == "FAIL" for r in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
