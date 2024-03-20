# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:26:36 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    	With the growing consumption of avocados in the USA, a freelance
        company would like to do some analysis on the patterns of consumption
        in different cities and would like to come up with a prediction
        model for the price of avocados. For this to be implemented, build 
        a prediction model using multilinear regression and provide your 
        insights on it.

'''
'''
Business Objective :

Maximize : The consumption and supply of the Avacado and the custommor satisfaction
should be increase .

Minimize : The loss of Avacado and all other material .Also the cost of
the ravelling

Business contraints : The Availability of the Avacado and the workers 
for the delivery purpose.

'''
######################################### EDA ###############################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Avacado = pd.read_csv('Avacado_Price.csv')
Avacado.head()

# Columns of the dataset
Avacado.columns
'''
Index(['AveragePrice', 'Total_Volume', 'tot_ava1', 'tot_ava2', 'tot_ava3',
       'Total_Bags', 'Small_Bags', 'Large_Bags', 'XLarge Bags', 'type', 'year',
       'region'],
      dtype='object')
'''

# Check the datatype of the all columns
Avacado.dtypes
'''
AveragePrice    float64
Total_Volume    float64
tot_ava1        float64
tot_ava2        float64
tot_ava3        float64
Total_Bags      float64
Small_Bags      float64
Large_Bags      float64
XLarge Bags     float64
type             object
year              int64
region           object
dtype: object
'''
# Except the type columns all are the numeric in nature

# Check the five number summary
Avacado.describe()
'''
       AveragePrice  Total_Volume  ...    XLarge Bags          year
count  18249.000000  1.824900e+04  ...   18249.000000  18249.000000
mean       1.405978  8.506440e+05  ...    3106.426507   2016.147899
std        0.402677  3.453545e+06  ...   17692.894652      0.939938
min        0.440000  8.456000e+01  ...       0.000000   2015.000000
25%        1.100000  1.083858e+04  ...       0.000000   2015.000000
50%        1.370000  1.073768e+05  ...       0.000000   2016.000000
75%        1.660000  4.329623e+05  ...     132.500000   2017.000000
max        3.250000  6.250565e+07  ...  551693.650000   2018.000000
'''
# As we see there are mixed kind of nature in the summary 

# Check the info of the dataset
Avacado.info()
'''
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   AveragePrice  18249 non-null  float64
 1   Total_Volume  18249 non-null  float64
 2   tot_ava1      18249 non-null  float64
 3   tot_ava2      18249 non-null  float64
 4   tot_ava3      18249 non-null  float64
 5   Total_Bags    18249 non-null  float64
 6   Small_Bags    18249 non-null  float64
 7   Large_Bags    18249 non-null  float64
 8   XLarge Bags   18249 non-null  float64
 9   type          18249 non-null  object 
 10  year          18249 non-null  int64  
 11  region        18249 non-null  object 
dtypes: float64(9), int64(1), object(2)
'''
# We see that there is no null value present in any columns
# Visualize the data
sns.boxplot(Avacado)
# As we see there are outliers in the dataset

sns.distplot(Avacado['AveragePrice'])
# As we see the data is normally right skewed

sns.distplot(Avacado['Total_Volume'])
# The Data is right skewed

sns.distplot(Avacado['tot_ava1'])
# The data is right skewed

sns.distplot(Avacado['tot_ava2'])
# the data is right skewed

sns.distplot(Avacado['tot_ava3'])
# The data is right skewed

sns.distplot(Avacado['Total_Bags'])
# The data is right skewed

# As we observed that the most of the data is right skewed

# fing the corelation
Avacado.drop(['type'],inplace=True,axis=1)
Avacado.drop(['region'],inplace=True,axis=1)

Avacado.corr()
# As we see the points shows the co-relationnamong themselves
# Now we can Build our model

import statsmodels.formula.api as smf
Avacado['year'] = Avacado['year'].astype('category')
# Let us build a formula for building our model
formula = 'AveragePrice ~ Total_Volume + tot_ava1 + tot_ava2 + tot_ava3 + Total_Bags + Small_Bags + Large_Bags + Q("XLarge Bags") + C(type) + C(year) + C(region)'

# Fit the model
model = smf.ols(formula=formula, data=Avacado).fit()
# Print the summary of the model to get detailed results
print(model.summary())
# The R-Squared value is 0.584 which is less than the 0.85
# The Durbin-Watson value is also 0.447 which is in the range of
# 0-1 . So we can say that the model may predict the correct output
X = Avacado.drop('AveragePrice', axis=1)
y = Avacado['AveragePrice']
from sklearn.model_selection import train_test_split
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Predict on the test set
y_pred = model.predict(X_test)

# Calculate RMSE
rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
print(f'RMSE: {rmse}')
# RMSE: 0.258605232525816
# As our RMSE value is in the range of 0-1 , so our model
# is relatively significant.