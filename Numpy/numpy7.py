import numpy as np
a=np.array([[1,2],[3,4]])
print(a)
print("###############")
print("Sum of all:",a.sum())
print("###############")
print("column wise sum:",a.sum(axis=0))
print("###############")
print("row wise sum:",a.sum(axis=1))
print("###############")
print(sum(a))
print("##################")
b=[[1,2],[3,4]]
k=np.array(b,dtype=complex)
print(k)
print("######################")
print(a)
print("Max element:",a.max())
print("column wise Max element:",a.max(axis=0))
print("row wise Max element:",a.max(axis=1))