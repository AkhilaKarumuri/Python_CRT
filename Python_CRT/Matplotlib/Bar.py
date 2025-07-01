import numpy as np
import matplotlib.pyplot as plt
x=np.array(["A","B","C","D"])
y=np.array([5,7,4,2])
# `plt.bar(x,y)` is creating a vertical bar graph where the x-axis represents the categories or labels
# in the array `x` and the y-axis represents the values in the array `y`. Each category in `x` is
# associated with a bar whose height is determined by the corresponding value in `y`.
# plt.bar(x,y) 
# plt.barh(x,y) # For horizontal bar graph it is barh
plt.bar(x,y,color='blue',width=0.2)
plt.show()