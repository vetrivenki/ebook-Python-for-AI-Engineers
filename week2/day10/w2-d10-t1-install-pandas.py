try:
    import pandas as pd

    print("Pandas version:", pd.__version__)
except ImportError:
    print("Run: python -m pip install pandas openpyxl")
