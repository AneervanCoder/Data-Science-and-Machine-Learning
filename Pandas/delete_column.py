import pandas as pd

mydict = {'names': ['Somu', 'Kiku', 'Amol', 'Lini'],
	      'physics': [68, 74, 77, 78],
	      'chemistry': [84, 56, 73, 69],
	        'algebra': [78, 88, 82, 87]  }

s=pd.Series(mydict)
print(s)
print("#########################")
#create dataframe
df_marks = pd.DataFrame(mydict)
print('Original DataFrame\n--------------')
print(df_marks)
print("########after pop###############")
df1=df_marks
#delete column
df1.pop("algebra")
print('\n\nDataFrame after deleting column\n--------------')
print(df1)
print("########last###############")
print(df_marks)








