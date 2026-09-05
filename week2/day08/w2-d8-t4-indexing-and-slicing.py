import numpy as np
a=np.arange(1,17).reshape(4,4)
print(a)
print("cell",a[0,0])
print("row",a[1])
print("slice\n",a[1:3,1:3])
print("advanced\n",a[[0,2]])
