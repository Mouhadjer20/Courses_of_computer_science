import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

import os

startups = pd.read_excel("50_StartUp.xlsx")
df = startups.copy()

#df.info()
"""
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 50 entries, 0 to 49
    Data columns (total 5 columns):
    #   Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
    0   R&D Spend        50 non-null     float64
    1   Administration   50 non-null     float64
    2   Marketing Spend  50 non-null     float64
    3   State            50 non-null     object 
    4   Profit           50 non-null     float64
    dtypes: float64(4), object(1)
    memory usage: 2.1+ KB
    None
"""

#df.shape #(50, 5)

##Method to Find what is the column are efecte to cost
#df = df.drop(["State"], axis=1)
#corr = df.corr()
#corr
"""
                 R&D Spend  Administration  Marketing Spend    Profit
R&D Spend         1.000000        0.241955         0.724248  0.972900
Administration    0.241955        1.000000        -0.032154  0.200717
Marketing Spend   0.724248       -0.032154         1.000000  0.747766
Profit            0.972900        0.200717         0.747766  1.000000
"""

#df["State"].unique() #['New York' 'California' 'Florida']

dfDummies = pd.get_dummies(df["State"], prefix="State")
df = pd.concat([df,dfDummies], axis=1)
df = df.drop(["State_Florida"], axis=1)
df = df.drop(["State"], axis=1)
#df.head()
"""
   R&D Spend  Administration  Marketing Spend     Profit  State_California  State_New York
0  165349.20       136897.80        471784.10  192261.83             False            True
1  162597.70       151377.59        443898.53  191792.06              True           False
2  153441.51       101145.55        407934.54  191050.39             False           False
3  144372.41       118671.85        383199.62  182901.99             False            True
4  142107.34        91391.77        366168.42  166187.94             False           False
"""

x = df.drop("Profit", axis= 1)
y = df["Profit"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 35)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
model = lm.fit(X_train, y_train)
y_pred = model.predict(X_test)
df = pd.DataFrame({"y_test" : y_test, "y_pred" 
                   : y_pred, "diff between y_pred and y_test" :abs(y_pred-y_test)})

from sklearn.metrics import mean_absolute_error
MSE =mean_absolute_error(y_test, y_pred)
#MSE #6657.417321576705

RMSE = np.sqrt(MSE)
#RMSE #81.59299799355766

model.score(X_train, y_train) #0.956142267350216
df1 = startups.head(10)
df1.plot(kind="bar", figsize=(16,10))
plt.grid(which="major",linestyle="-", linewidth="0.5",color="green")

plt.show()

print('Intercept of the model:\n',lm.intercept_)
print("="*50)
print('Coefficient of the line:\n',lm.coef_)


#######Other methode to choose what is the column are efecte on value of cost
import statsmodels.api as sm
stmodel=sm.OLS(y,x).fit()
stmodel.summary()

"""
Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[3] The condition number is large, 8.02e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
x=sm.add_constant(x)
model=sm.OLS(y,x).fit()
model.summary()

"""
Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.56e+06. This might indicate that there are
strong multicollinearity or other numerical problems. 
"""
x=x.drop(['State_California'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

"""
Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.43e+06. This might indicate that there are
strong multicollinearity or other numerical problems. 
"""
x=x.drop(['State_New York'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

"""
Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.4e+06. This might indicate that there are
strong multicollinearity or other numerical problems. 
"""
x=x.drop(['Administration'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

"""
Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.32e+05. This might indicate that there are
strong multicollinearity or other numerical problems. 
"""
x=x.drop(['Marketing Spend'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

"""
Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.65e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
from sklearn.preprocessing import StandardScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = StandardScaler()
s.fit_transform(data)

"""
array([[-1.        , -1.34164079],
       [-1.        , -0.4472136 ],
       [ 1.        ,  0.4472136 ],
       [ 1.        ,  1.34164079]])
"""
from sklearn.preprocessing import MinMaxScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = MinMaxScaler()
s.fit_transform(data)

""""
array([[0.        , 0.        ],
       [0.        , 0.33333333],
       [1.        , 0.66666667],
       [1.        , 1.        ]])
"""

from sklearn.preprocessing import RobustScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = RobustScaler()
s.fit_transform(data)
"""
array([[-0.5       , -1.        ],
       [-0.5       , -0.33333333],
       [ 0.5       ,  0.33333333],
       [ 0.5       ,  1.        ]])
"""

from sklearn.preprocessing import Normalizer
data = [[0,61],[0,62],[1,63],[1,64]]
s = Normalizer()
s.fit_transform(data)
"""
array([[0.        , 1.        ],
       [0.        , 1.        ],
       [0.01587102, 0.99987405],
       [0.01562309, 0.99987795]])
"""