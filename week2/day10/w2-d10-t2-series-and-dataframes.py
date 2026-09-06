import pandas as pd

s = pd.Series([1200, 1500, 900], index=["Jan", "Feb", "Mar"])
df = pd.DataFrame(
    {"product": ["Laptop", "Mouse"], "units": [5, 20], "price": [900.0, 25.0]}
)
print(s)
print(df)
