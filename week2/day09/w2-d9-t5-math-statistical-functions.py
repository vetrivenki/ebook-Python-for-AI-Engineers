import numpy as np

a = np.array([1.0, 4.0, 9.0, 16.0])
print("sqrt", np.sqrt(a))
print("log", np.log(a))
print("median", np.median(a))
print("variance", np.var(a))
print("75 percentile", np.percentile(a, 75))
