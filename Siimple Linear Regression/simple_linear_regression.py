import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
# Importing the dataset
dataset=pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x, y, 
                     test_size = .25, random_state = 42)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()# create model
regressor.fit(x_train, y_train)#train model

y_pred=regressor.predict(x_test)#predict y 

from sklearn import metrics
print("Error=",np.sqrt(metrics.mean_squared_error
                       (y_test, y_pred)))

# predict salary for 2.3 year experience
print("Salary :",regressor.predict([[3.3]]))

plt.plot(x_train,y_train,'r*')#visualise actual training data
#plt.plot(X_train,y_train,'g')
y_pred_train=regressor.predict(x_train)#predict y value for training data
plt.plot(x_train,y_pred_train)#draw solution line
#plt.plot([[2.3]],regressor.predict(np.array([[2.3]])),'g^')
plt.title("Employee data")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
print("Intercept:",regressor.intercept_)
print("Co-efficient:",regressor.coef_)








 





