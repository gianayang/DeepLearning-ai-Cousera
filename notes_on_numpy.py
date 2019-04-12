import numpy as np

#rank 1 array,not recommend
a =np.random.randn(5)
print(a)
#rank on the vector
print(a.shape)

#a.shape=(5,1)
a = np.random.randn(5,1)
print(a)
print(a.T)
#product
print(np.dot(a,a.T))

#to check the vector
assert(a.shape==(5,1))