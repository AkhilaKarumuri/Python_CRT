'''WAPP to create a 1D array with 15 elements and reshape it into 2D array with 3 rows and 5 columns
5 rows and 3 columns and print the dimension of it 
Reshape the same array into a 3D array with 5 rows 3 columns with 1 element in each column '''
import numpy as np
Array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(Array)
newarr=Array.reshape(3,5)
print(newarr)
newarr1=Array.reshape(5,3,1)
print(newarr1)