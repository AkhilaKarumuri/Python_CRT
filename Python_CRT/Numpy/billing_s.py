import numpy as np
prices=np.array([50,20,30])
quantities=np.array([2,5,3])
mul=prices*quantities
print(mul)
bill=sum(mul)
print(bill)