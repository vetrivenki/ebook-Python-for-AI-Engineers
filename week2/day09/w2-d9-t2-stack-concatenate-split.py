import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("vstack\n", np.vstack((a, b)))
print("hstack\n", np.hstack((a, b)))
c = np.concatenate((a, b), axis=0)
print("concatenate\n", c)
print("split", np.split(c, 2))
