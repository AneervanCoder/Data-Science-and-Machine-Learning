#import the pandas library and aliasing as pd
import pandas as pd

data = {'a' : 9.9, 'b' : 1.4, 'c' : 2.0,'d':11,'e':12}
s = pd.Series(data,index=['b','a','e','d','c','k'])
print (s)
