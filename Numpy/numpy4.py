import numpy as np
k=[11,22]
k1=np.array(k)
print("Dimension of k1:", k1.ndim)
m=[[11,22],[33,44]]
m1=np.array(m)
print("Dimension of m1:",m1.ndim)
print("################")
n=np.arange(12).reshape(3,4)
print(n)
print("################")
n=np.arange(12).reshape(3,4,1,1)
print(n)