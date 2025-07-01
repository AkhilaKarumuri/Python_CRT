import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
#Array reshape -->1D to 2D
arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
#Array reshape -->1D to 3D
newarr2=arr.reshape(2,3,2)
print(newarr2)