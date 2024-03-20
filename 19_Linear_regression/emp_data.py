# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:22:09 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    A certain organization wants an early estimate of their employee churn out rate. 
    So the HR department gathered the data regarding the employee’s salary hike and 
    the churn out rate in a financial year. The analytics team will have to perform 
    an analysis and predict an estimate of employee churn based on the salary hike. 
    Build a Simple Linear Regression model with churn out rate as the target variable.
    Apply necessary transformations and record the RMSE and correlation coefficient 
    values for different models.

'''
'''
Business Objective :
    
Maximize : The correct prediction of the hike given to the emplyee so that the 
company value and the employee trust should be maintain in the company.

Minimize : The unneccesary salary and hike given to the employee and also the 
overall churn in the financialyear

Business Contraints ; The employee satisfaction towards the salary and also the the record
of the employee .

'''
########################################### EDA ###########################################
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


emp=pd.read_csv('emp_data.csv')
emp.head()


# Five Number summary
emp.describe()
'''
       Salary_hike  Churn_out_rate
count    10.000000       10.000000
mean   1688.600000       72.900000
std      92.096809       10.257247
min    1580.000000       60.000000
25%    1617.500000       65.750000
50%    1675.000000       71.000000
75%    1724.000000       78.750000
max    1870.000000       92.000000
'''
# the mean and median shows slight diffrence in there values so the central tendancy and
# the scatterness of datapoints are somewhat away from meadian

# Information of the dataset
emp.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 2 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Salary_hike     10 non-null     int64
 1   Churn_out_rate  10 non-null     int64
dtypes: int64(2)
memory usage: 292.0 bytes
'''
# There is no null value present
# All the datapoints are numeric in nature

# Visualize the data
# Check for he outliers
sns.boxplot(emp)
# No outlier is present

emp.corr()
'''
              Salary_hike  Churn_out_rate
Salary_hike        1.000000       -0.911722
Churn_out_rate    -0.911722        1.000000
'''
# There is corelation are in the column

# Plot the Scatter plot
sns.scatterplot(x='Salary_hike', y='Churn_out_rate', data=emp)
plt.title('Churn Out Rate vs. Salary Hike')
plt.show()

# Most of the datapoints are lies in the range 1600-1750
# Datapoints are shows some curve like structure

# Preparing the data
X = emp[['Salary_hike']]
y = emp['Churn_out_rate']

# Splitting the empset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the base model
base_model = LinearRegression()
base_model.fit(X_train, y_train)

# Making predictions
base_predictions = base_model.predict(X_test)
base_predictions
# Evaluating the base model
base_rmse = np.sqrt(mean_squared_error(y_test, base_predictions))
base_r2 = r2_score(y_test, base_predictions)
print(f"Base Model RMSE: {base_rmse}") # 2.7570866858265246
print(f"Base Model R^2: {base_r2}") # 0.9425215350233506

# As the rmse value is more we can apply the log transformation to check whether the
# rmse and r2 value is reduce or not

# Log transformation of the target variable
y_log = np.log(y)

# Splitting the transformed dataset
X_train, X_test, y_log_train, y_log_test = train_test_split(X, y_log, test_size=0.2, random_state=42)

# Rebuilding the model with the transformed target
log_model = LinearRegression()
log_model.fit(X_train, y_log_train)

# Making predictions and transforming back
log_predictions = np.exp(log_model.predict(X_test))
log_predictions
# Evaluating the log model
log_rmse = np.sqrt(mean_squared_error(y_test, log_predictions))
log_r2 = r2_score(y_test, log_predictions)
print(f"Log Model RMSE: {log_rmse}") # 2.8309474076209207
print(f"Log Model R^2: {log_r2}") # 0.9394006561458177
# We can obseved that there is slight change in r^2 value

# Now we can try for the polynomial one
from sklearn.preprocessing import PolynomialFeatures

# Generating polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Splitting the dataset
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Rebuilding the model with polynomial features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

# Making predictions
poly_predictions = poly_model.predict(X_test_poly)

# Evaluating the polynomial model
poly_rmse = np.sqrt(mean_squared_error(y_test, poly_predictions))
poly_r2 = r2_score(y_test, poly_predictions)
print(f"Polynomial Model RMSE: {poly_rmse}") # 1.65436787453
print(f"Polynomial Model R^2: {poly_r2}") # 0.654832563
# As we can see that the polynomial will give the best result so we will use same one

