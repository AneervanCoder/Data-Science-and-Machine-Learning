import numpy as np
import pandas as pd 
# Importing the dataset
dataset = pd.read_csv('Employee_Data.csv')

X = dataset.iloc[:, :4].values
y = dataset.iloc[:, 4].values
print("#########Features#######################")
print(X)
print("####################Output#######################")
print(y)
print("###########################################")

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
print("##########After Label Encoding###########")
print(X)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X, y, 
                    test_size = .25, random_state = 42) 


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred=regressor.predict(X_test)
'''Return the coefficient of determination R^2 
of the prediction. The coefficient R^2 is defined
 as (1 - u/v), where u is the residual sum of 
 squares ((y_test - y_pred) ** 2).sum() and v is 
 the total sum of squares
 ((y_test - y_test.mean()) ** 2).sum(). 
 The best possible score is 1.0 and it can be
 negative (because the model can be arbitrarily worse).
 A constant model that always predicts the expected
 value of y, disregarding the input features, 
 would get a R^2 score of 0.0.'''
accuracy = (regressor.score(X_test,y_pred))
print("Accuracy=",accuracy)
from sklearn import metrics
print("Error:",np.sqrt(metrics.mean_squared_error
                       (y_test,y_pred)))

print("result",
      regressor.predict(np.array([0, 2300, 0, 1.1]).reshape(1,4)))

print("result2",
      regressor.predict([[1, 2300, 0, 1.1]]))











