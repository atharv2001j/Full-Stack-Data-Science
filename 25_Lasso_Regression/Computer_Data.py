# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:07:29 2024

@author: Atharv Joshi
"""
'''
Problem Statement:
    1.	Officeworks is a leading retail store in Australia, with 
    numerous outlets around the country. The manager would like to
    improve the customer experience by providing them online predictive
    prices for their laptops if they want to sell them. To improve this
    experience the manager would like us to build a model which is 
    sustainable and accurate enough. Apply Lasso and Ridge Regression model
    on the dataset and predict the price, given other attributes. Tabulate
    R squared, RMSE, and correlation values.
'''

'''
Business Objective :
    
Maximize : The production as well as the quality of the computer

Minimize : The price of the computer as well the production cost of the 
Computer.

Business Cotraints : The overll budget of the company and the data required
for the computer should be secuure.The maintainance of the computer.

'''
#################################### EDA #####################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Computer_Data.csv')

df.info()
'''
#   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Unnamed: 0  6259 non-null   int64
 1   price       6259 non-null   int64
 2   speed       6259 non-null   int64
 3   hd          6259 non-null   int64
 4   ram         6259 non-null   int64
 5   screen      6259 non-null   int64
 6   cd          6259 non-null   int32
 7   multi       6259 non-null   int32
 8   premium     6259 non-null   int32
 9   ads         6259 non-null   int64
 10  trend       6259 non-null   int64
dtypes: int32(3), int64(8)
'''
# All the datapoints are numeric in nature as well as there is no null value
# Is present in the dataset
df.columns
'''
Index(['Unnamed: 0', 'price', 'speed', 'hd', 'ram', 'screen', 'cd', 'multi',
       'premium', 'ads', 'trend'],
      dtype='object')
'''
df.dtypes
'''
Unnamed: 0     int64
price          int64
speed          int64
hd             int64
ram            int64
screen         int64
cd            object
multi         object
premium       object
ads            int64
trend          int64
dtype: object
'''
df.info()
'''
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Unnamed: 0  6259 non-null   int64 
 1   price       6259 non-null   int64 
 2   speed       6259 non-null   int64 
 3   hd          6259 non-null   int64 
 4   ram         6259 non-null   int64 
 5   screen      6259 non-null   int64 
 6   cd          6259 non-null   object
 7   multi       6259 non-null   object
 8   premium     6259 non-null   object
 9   ads         6259 non-null   int64 
 10  trend       6259 non-null   int64 
dtypes: int64(8), object(3)
memory usage: 538.0+ KB
'''
# Data Visualization
import seaborn as sns
sns.boxplot(df)
# There is outlier present in some columns
sns.pairplot(df)
#here colinearity is high between hd & ram but scatter plot shows no any linearity.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import r2_score, mean_squared_error

# Summary statistics
summary_stats = df.describe()
summary_stats
'''
        Unnamed: 0        price  ...          ads        trend
count  6259.000000  6259.000000  ...  6259.000000  6259.000000
mean   3130.000000  2219.576610  ...   221.301007    15.926985
std    1806.961999   580.803956  ...    74.835284     7.873984
min       1.000000   949.000000  ...    39.000000     1.000000
25%    1565.500000  1794.000000  ...   162.500000    10.000000
50%    3130.000000  2144.000000  ...   246.000000    16.000000
75%    4694.500000  2595.000000  ...   275.000000    21.500000
max    6259.000000  5399.000000  ...   339.000000    35.000000
'''
# there is slight difference in the mean and median .So the datapoints are spread
# from the median
# Convert categorical columns to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['cd', 'multi', 'premium'])

# Correlation matrix
corr_matrix = df.corr()
corr_matrix
# They shows the co-relation among themselves
# Check for missing values
missing_values = df.isnull().sum()
missing_values
'''
Unnamed: 0     0
price          0
speed          0
hd             0
ram            0
screen         0
ads            0
trend          0
cd_no          0
cd_yes         0
multi_no       0
multi_yes      0
premium_no     0
premium_yes    0
dtype: int64
'''
# There is no null value present in this
# Split the data into train and test sets
X = df.drop(['Unnamed: 0', 'price'], axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Apply Lasso Regression
lasso_model = Lasso(alpha=0.1)  # You can adjust the alpha value as needed
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)
lasso_predictions
# Calculate R squared and RMSE for Lasso Regression
lasso_r2 = r2_score(y_test, lasso_predictions)
lasso_rmse = np.sqrt(mean_squared_error(y_test, lasso_predictions))
lasso_rmse
# 283.37996428996655 
# Apply Ridge Regression
ridge_model = Ridge(alpha=0.1)  # You can adjust the alpha value as needed
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Calculate R squared and RMSE for Ridge Regression
ridge_r2 = r2_score(y_test, ridge_predictions)
ridge_rmse = np.sqrt(mean_squared_error(y_test, ridge_predictions))

# Tabulate the results
results = pd.DataFrame({
    'Model': ['Lasso Regression', 'Ridge Regression'],
    'R squared': [lasso_r2, ridge_r2],
    'RMSE': [lasso_rmse, ridge_rmse]
})

# Print the results
print("Summary Statistics:")
print(summary_stats)
print("\nCorrelation Matrix:")
print(corr_matrix)
print("\nMissing Values:")
print(missing_values)
print("\nModel Evaluation:")
print(results)

'''
              Model  R squared        RMSE
0  Lasso Regression   0.754176  283.379964
1  Ridge Regression   0.754090  283.429914
'''
