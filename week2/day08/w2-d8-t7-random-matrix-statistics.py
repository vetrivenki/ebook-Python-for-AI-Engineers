import numpy as np

rng = np.random.default_rng(42)
a = rng.integers(1, 101, (5, 5))
print(a)
print("row means", a.mean(axis=1))
print("column means", a.mean(axis=0))
print("row max", a.max(axis=1))
print("column min", a.min(axis=0))
