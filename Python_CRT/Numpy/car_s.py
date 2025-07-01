import numpy as np
milage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
for i in range(len(milage)):
    if milage[i]<15:
        print(i+1)