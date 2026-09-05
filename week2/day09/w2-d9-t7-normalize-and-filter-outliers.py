import numpy as np
rng=np.random.default_rng(42)
data=rng.normal([50,100,150,200],[10,20,30,40],(1000,4))
z=(data-data.mean(axis=0))/data.std(axis=0)
clean=z[(np.abs(z)<=3).all(axis=1)]
print("original",data.shape)
print("means",z.mean(axis=0).round(3))
print("std",z.std(axis=0).round(3))
print("clean",clean.shape)
