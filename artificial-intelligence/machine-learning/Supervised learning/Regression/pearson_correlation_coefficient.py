"""
Pearson correlation Coefficient
Y = n * x + b
m (slope) = r. Sy/Sx
Sx = sqt((x- x_) ** 2 / M - 1), M: ( عدد الصفوف في data)
Sy = sqt((y- y_) ** 2 / M - 1)

(x_, y_): متوسط
b = y_ - m * x_

Cost func: 1/2M * sum( ( (y_i - yi) **2) )

---
"""

"""
### Question 1: Data Import and Exploration
1. Import the required libraries for data manipulation, visualization, and modeling.
2. Load the dataset "Salary_Dataa.csv" and display its structure.
3. Explore the data using methods like `.info()` and `.describe()`.

---
"""
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Salary_Data.csv')
#print(data)

#print(data.info())
#print(data.describe())

"""
### Question 2: Data Visualization
1. Create a scatter plot to visualize the relationship between 'YearsExperience' and 'Salary'.
2. Label the axes and add a title to the plot.

---
"""
plt.figure(figsize=(12,6))
sns.pairplot(data, x_vars=["YearsExperience"], y_vars=["Salary"], height=7, kind="scatter")
plt.xlabel("years")
plt.ylabel("salary")
plt.title("salary prediction")
#plt.show()

"""
### Question 3: Data Preparation
1. Split the dataset into input (X) and output (y) variables.
2. Display the first few rows of both X and y.
3. Split the data into training and testing sets using an 80-20 ratio.

---
"""
from sklearn.model_selection import train_test_split

X = data.iloc[:,:-1]
y = data.iloc[:,1]

X.head()
y.head()

X_train , X_test , y_train , y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

"""
### Question 4: Model Training
1. Train a **Linear Regression** model using the training data.

---
"""
from sklearn.linear_model import LinearRegression

my_model = LinearRegression().fit(X_train,y_train)

"""
### Question 5: Training Set Visualization
1. Plot the training data points as red dots.
2. Add the regression line in blue.

---
"""
plt.scatter(X_train, y_train, color = 'blue')
y_result = my_model.predict(X_train)
plt.plot(X_train, y_result, color = 'orange')

"""
### Question 6: Testing Set Visualization
1. Predict values for the test set.
2. Plot the test data points as red dots.

---
"""
plt.scatter(X_test, y_test, color = 'red')

"""
### Question 7: Actual vs Predicted Values
1. Plot the actual and predicted values to compare them.
2. Use different colors for actual (red) and predicted (blue) values.

---
"""

y_pred = my_model.predict(X_test)
count = [i for i in range(1,len(y_test)+1)]
#plt.plot(c, y_test, color='r', linestyle='-')
#plt.plot(c, y_pred, color='b', linestyle='-')

"""
### Question 8: Error Plotting
1. Plot the error values (differences between actual and predicted values).
---
"""
#plt.plot(count, y_test - y_pred, color='r', linestyle='-')

"""
### Question 9: Model Evaluation
1. Calculate and display the **Mean Squared Error (MSE)**.
2. Calculate and display the **R-squared (R²)** value.

---
"""
from sklearn.metrics import mean_squared_error, r2_score

print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Coefficient of determination: {r2_score(y_test, y_pred):.2f}")

plt.show()

"""
### Question 10: Model Coefficients and Predictions
1. Display the intercept and coefficient of the model.
2. Use the model to predict the salary for 4.5 years of experience.

---
"""

print('Intercept of the model:',my_model.intercept_)
print('Coefficient of the line:',my_model.coef_)

y_hat = my_model.coef_ * 4.5 + my_model.intercept_
print(y_hat)