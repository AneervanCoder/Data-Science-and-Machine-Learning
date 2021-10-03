#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array((11.8,12,13,14))
s1 = pd.Series(data,index=[101,102,103,104])
print( s1)