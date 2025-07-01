import numpy as np
import matplotlib.pyplot as plt
# y = np.array([35,25,12,15])
# plt.pie(y)
# plt.show()

# ------------
y = np.array([35,25,12,15])
mylabels=["Apples","Bananas","Oranges","Grapes"]
'''The `myexplode=[0,0,0,0]` line in the code snippet is setting the "explode" parameter for each slice
in the pie chart. The "explode" parameter is used to offset a slice from the rest of the pie chart.'''
myexplode=[0,0,0,0] 
plt.pie(y,labels=mylabels,explode=myexplode,startangle=0)
plt.legend(title="FRUITS")
plt.show()