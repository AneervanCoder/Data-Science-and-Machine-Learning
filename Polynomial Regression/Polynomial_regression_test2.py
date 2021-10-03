# Fitting Polynomial Regression to the dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # This line creates a matrix
y = dataset.iloc[:, 2].values

from sklearn.preprocessing import PolynomialFeatures
#hyper parameter pruning or Bias value trade off
poly_reg = PolynomialFeatures(degree = 5) #hyper-parameter
X_poly = poly_reg.fit_transform(X)

from sklearn.linear_model import LinearRegression
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Predicting a new result with Polynomial Regression
k=poly_reg.fit_transform([[8.3]])
salary = lin_reg_2.predict(k)
print("Predicted Salary:",salary)

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(X_poly),
         color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()




