#import creste pandas series from dictionary
import pandas as pd
calories={"day1": 420, "day2": 380, "day3":400}
myvar=pd.Series(calories,index=["day1","day2"])
print(myvar)
print(myvar.loc["day1"])
print(myvar.loc["day2"])