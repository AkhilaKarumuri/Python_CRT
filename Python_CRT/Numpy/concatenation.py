#Joining two arrays
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)
#Joining two 2D arrays
arr1=np.array([[1,2],[3,4]])
arr2= np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1) # 1-Horizontal concatenation
print(arr)
#Joining two 2D arrays
arr1=np.array([[1,2],[3,4]])
arr2= np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=0) # 0- Vertical concatenation
print(arr)