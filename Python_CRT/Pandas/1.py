#checking version
import pandas as pd
print(pd.__version__)
Num=['List of Num' ,1,2,3,4,5,6,7,8,9,10]
print(pd.Series(Num))

num=[10,20,30,40,50,60,70,80,90,100]
num_series=pd.Series(num,index=['i','ii','iii','iv','v','vi','vii','viii','ix','x'])
print(num_series)