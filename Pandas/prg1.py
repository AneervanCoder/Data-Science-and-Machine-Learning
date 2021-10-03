import pandas as pd
data=pd.read_csv('Income_data.csv')
print(data)
data2=data.set_index("State")
'''data2.iloc[start row index:end row index,
start column index:end column index]'''

data3=data2.iloc[1:3,2:4]
data4=data2.iloc[:,2:4]
data5=data2.iloc[:,2]
print("Average sales:",data5.mean())
data6=data2.iloc[:,[1,3,5]]
data61=data6.mean(axis=0)
data62=data6.mean(axis=1)

df1=data2.loc["Alabama":"Arizona","2007":"2009"]
df2=data2.loc["California",:]
df3=data2.loc["California","2013"]
print("California sales in 2013:",df3)
df4=data2.mean()
df5=data2.mean(axis=1)