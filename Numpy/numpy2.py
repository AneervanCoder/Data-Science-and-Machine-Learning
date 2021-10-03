import numpy as np
k=np.arange(12)
print("Values :",k)
print("Data type of k:",type(k))
print("Data type of each element:",k.dtype)
print("data of any:",type(k[1]))
print("Dimension of k:",k.ndim)
print("Shape of k:",k.shape)
print("No of elements:",len(k))
print("#####################")
k1=k.reshape((3,4))
print(k1)
print("Dimension of k1:",k1.ndim)
print("Shape of k1:",k1.shape)
print("No of rows:",len(k1))
print("No of rows:",k1.shape[0])
print("No of columns:",k1.shape[1])
m=np.arange(2,10)
print("#############")
print(m)
print("#############")
m1=np.arange(2,20,3)
print(m1)
print("#############")
m2=np.arange(1,2,.3)
print(m2)
print("#############")
m2=np.arange(1,2,.01)
print(m2)











