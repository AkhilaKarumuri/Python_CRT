import numpy as np
#Array iterating 1D:
arr = np.array([1,2,3])
for x in arr:
    print(x)

#Array iterating 2D:
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

#Array iteration 3D:
arr=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for x in arr:
    print(x)

arr=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr[0,1:])