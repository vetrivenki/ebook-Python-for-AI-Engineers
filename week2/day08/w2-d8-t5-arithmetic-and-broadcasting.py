import numpy as np

prices = np.array([100.0, 150.0, 200.0])
qty = np.array([2, 3, 1])
print("revenue", prices * qty)
a = np.array([[10, 20, 30], [40, 50, 60]])
print("scalar broadcast\n", a + 5)
print("column broadcast\n", a + np.array([1, 2, 3]))
