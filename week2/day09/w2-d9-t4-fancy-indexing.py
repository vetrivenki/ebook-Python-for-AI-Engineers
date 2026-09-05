import numpy as np
products=np.array(["Laptop","Mouse","Keyboard","Monitor"])
sales=np.array([12,45,30,18])
positions=np.array([1,3,0])
print(products[positions])
print(sales[positions])
print(products[np.argsort(sales)[::-1]])
