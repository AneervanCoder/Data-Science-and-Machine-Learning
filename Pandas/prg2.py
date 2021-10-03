
import pandas as pd
data=pd.read_csv('Income_data.csv')
print(data.isnull().sum())
data1=data.fillna(33000)
data2=data.dropna()