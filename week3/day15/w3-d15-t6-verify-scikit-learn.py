"""Week 3 | Day 15 | Task 6: Verify the package installation.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import sys
import sklearn

# Install from your terminal: python -m pip install scikit-learn
# The distribution is scikit-learn; its import name is sklearn.
print("Python executable:", sys.executable)
print("scikit-learn version:", sklearn.__version__)
print("Import succeeded. This script does not install packages.")
