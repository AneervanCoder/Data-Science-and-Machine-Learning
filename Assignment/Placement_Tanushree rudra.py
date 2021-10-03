# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('F:\Certificates\ML\DataPlacement.csv')
df2 = pd.DataFrame(df.values)
column_names = df2[0:1].values[0]
df3 = df2[1:]
df3.columns = df2[0:1].values[0]
df3.head()

for i in range(3,10):
    df3[column_names[i]] = list(map(lambda x: x[:-1], df3[column_names[i]].values))
    df3[column_names[i]] = [float(x) for x in df3[column_names[i]].values]

X = df3.iloc[:, 2:10].values
Y = df3.iloc[:, 10].values

from sklearn.preprocessing import StandardScaler, LabelEncoder
labelencoder=LabelEncoder()
Y=labelencoder.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 42)
# Feature Scaling


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Decision Tree Classifier to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',
                                    random_state = 0)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)

'''from sklearn.metrics import confusion_matrix
print("My Confusion Matrix:",
      confusion_matrix(y_test, y_pred))'''

from sklearn.metrics import accuracy_score
print("Accuracy: ",accuracy_score(y_test, y_pred))


#new customer prediction age=28 salry=119000
k=classifier.predict(sc.transform([[240, 0, 20, 24, 0, 0, 24, 0]]))
print("New customer class:",k)
if k[0]==0:
    print("Placed")
else:
    print("Not placed")






 





 











