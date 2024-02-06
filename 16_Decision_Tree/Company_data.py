# -*- coding: utf-8 -*-
"""
Created on Fri Feb 2 22:38:08 2024
@author: Atharv Joshi
"""

'''
Business objective:
    
Maximize: The overall sales of the company. We aim to maximize the accuracy of the model.

Minimize: The loss of the company and factors affecting profit should be minimized.

Business Constraints: The accuracy of the data and fault prediction of the data.
'''
'''
DataFrame:
    
The Sales column will be the target column, and the remaining columns will be features contributing to sales.
'''

###################### EDA ######################################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('Company_data.csv')

# Display the dataset
print(df)

# Check the info about the dataset
print(df.info())

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Sales        400 non-null    float64
 1   CompPrice    400 non-null    int64  
 2   Income       400 non-null    int64  
 3   Advertising  400 non-null    int64  
 4   Population   400 non-null    int64  
 5   Price        400 non-null    int64  
 6   ShelveLoc    400 non-null    object 
 7   Age          400 non-null    int64  
 8   Education    400 non-null    int64  
 9   Urban        400 non-null    object 
 10  US           400 non-null    object 
dtypes: float64(1), int64(7), object(3)
memory usage: 34.5+ KB
None
'''

# The Five number summary
print(df.describe())
'''
           Sales   CompPrice      Income  ...       Price         Age   Education
count  400.000000  400.000000  400.000000  ...  400.000000  400.000000  400.000000
mean     7.496325  124.975000   68.657500  ...  115.795000   53.322500   13.900000
std      2.824115   15.334512   27.986037  ...   23.676664   16.200297    2.620528
min      0.000000   77.000000   21.000000  ...   24.000000   25.000000   10.000000
25%      5.390000  115.000000   42.750000  ...  100.000000   39.750000   12.000000
50%      7.490000  125.000000   69.000000  ...  117.000000   54.500000   14.000000
75%      9.320000  135.000000   91.000000  ...  131.000000   66.000000   16.000000
max     16.270000  175.000000  120.000000  ...  191.000000   80.000000   18.000000
'''


# Display the dataset
print(df)

# Check the DataType of the dataframe
df.dtypes
'''
Sales          float64
CompPrice        int64
Income           int64
Advertising      int64
Population       int64
Price            int64
ShelveLoc       object
Age              int64
Education        int64
Urban           object
US              object
dtype: object
'''

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
# Define predictors and target
colnames = list(df.columns)
predictors = colnames[1:]
target = colnames[0]

# Split the data into training and testing sets
train, test = train_test_split(df, test_size=0.3, random_state=42)

# Create a Decision Tree model for regression
model = DecisionTreeRegressor()

# Train the model
model.fit(train[predictors], train[target])

# Make predictions on the test set
preds = model.predict(test[predictors])
preds
# Evaluate the model on the test set
np.mean(preds==test[target])

mse = mean_squared_error(test[target], preds)
print(f"Mean Squared Error on test set: {mse}")
# The Model showing the 83% accuracy 