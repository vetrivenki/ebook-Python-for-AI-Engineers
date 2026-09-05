import numpy as np
a=np.array([55,72,91,68,84,43])
print("mask",a>=70)
print("passing",a[a>=70])
print("60-90",a[(a>=60)&(a<=90)])
