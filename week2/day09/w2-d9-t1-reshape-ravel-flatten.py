import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a)
print("ravel",a.ravel())
print("flatten",a.flatten())
print("ravel shares memory",np.shares_memory(a,a.ravel()))
