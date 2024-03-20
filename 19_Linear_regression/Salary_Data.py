# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:44:36 2024

@author: Atharv Joshi
"""
'''
Problem Statement : 
    The head of HR of a certain organization wants to automate their salary
    hike estimation. The organization consulted an analytics service provider
    and asked them to build a basic prediction model by providing them with
    a dataset that contains the data about the number of years of experience
    and the salary hike given accordingly. Build a Simple Linear Regression
    model with salary as the target variable. Apply necessary transformations
    and record the RMSE and correlation coefficient values for different 
    models.

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

################################## EDA ########################################

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

Salary= pd.read_csv('Salary_Data.csv')
Salary.head()


# Five Number summary
Salary.describe()
'''
       YearsExperience         Salary
count        30.000000      30.000000
mean          5.313333   76003.000000
std           2.837888   27414.429785
min           1.100000   37731.000000
25%           3.200000   56720.750000
50%           4.700000   65237.000000
75%           7.700000  100544.750000
max          10.500000  122391.000000
'''
# There is slight difference in the value of the mean and median so the 
# Central tendancy property may vary

#  Information of the dataset
Salary.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 2 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   YearsExperience  30 non-null     float64
 1   Salary           30 non-null     float64
dtypes: float64(2)
memory usage: 612.0 bytes
'''
# The dataset is of numeric type
# There is no any null value present in the dataset

Salary.columns
# Index(['YearsExperience', 'Salary'], dtype='object')

# Visualize the data
# Check for the outliers
sns.boxplot(Salary)
# There is no outlier is present in the dataset

Salary.corr()
'''
                 YearsExperience    Salary
YearsExperience         1.000000  0.978242
Salary                  0.978242  1.000000
'''
# The values in the co-relation says that the datapoints are co-related to each other and
# the prediction is depends onn each other

# Plot the Scatter plot
sns.scatterplot(x='YearsExperience', y='Salary', data=Salary)
plt.title('YearsExperience Vs Salary')
plt.show()

# The more datapoints are in the range of 1-7


# Preparing the data
X = Salary[['YearsExperience']]
y = Salary['Salary']

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
print(f"Base Model RMSE: {base_rmse}") # 7059.04362190151
print(f"Base Model R^2: {base_r2}") # 0.9024461774180497

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
print(f"Log Model RMSE: {log_rmse}") # 9215.847672114533
print(f"Log Model R^2: {log_r2}") # 0.8337264628223056
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
print(f"Polynomial Model RMSE: {poly_rmse}") # 7247.6145295383185
print(f"Polynomial Model R^2: {poly_r2}") # 7247.6145295383185
# As we can see that the log transformation  will give the best result so we will use same one

