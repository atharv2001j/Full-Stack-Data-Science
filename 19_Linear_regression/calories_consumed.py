# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:12:06 2024

@author: Atharv Joshi
"""
'''
Problem statement :
    
A certain food-based company conducted a survey with the help of a fitness 
company to find the relationship between a person’s weight gain and the 
number of calories they consumed in order to come up with diet plans for 
these individuals. Build a Simple Linear Regression model with calories 
consumed as the target variable. Apply necessary transformations and record
the RMSE and correlation coefficient values for different models. 

'''
'''
Business Objective :

Maximize : The accuracy of the diet plan for the person by calculating the calories
burn and the relationship between the weight and the calories burn

Minimize : The weight of the customer by giving the proper diet plan so it can
easy to trainer for advice the proper diet

Business contraints : The suitable diet plan and exercise suggestion to the customer.

'''
###################################### EDA #####################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from math import sqrt


wg_cc = pd.read_csv("calories_consumed.csv")

# View the first few rows of the dataset
print(wg_cc.head())

# Summary of data/EDA
print(wg_cc.describe())
'''
count              14.000000          14.000000
mean              357.714286        2340.714286
std               333.692495         752.109488
min                62.000000        1400.000000
25%               114.500000        1727.500000
50%               200.000000        2250.000000
75%               537.500000        2775.000000
max              1100.000000        3900.000000
'''
# As there is slight difference in the mean and median so the centraltendancy
# might get disturb due to the diffrence

# Scatterplot of input vs output
plt.scatter(wg_cc['Calories Consumed'], wg_cc['Weight gained (grams)'])
plt.xlabel('Calories Consumed')
plt.ylabel('Weight gained (grams)')
plt.title('Scatterplot of Calories Consumed vs Weight Gained')
plt.show()

# The scatter plot shows that the most of the datapoints are lies in the range
# 1500-2700 . So our prediction is more sffected in this range

# Correlation between output and input
print("Correlation coefficient:", wg_cc.corr().iloc[0, 1])
# Correlation coefficient: 0.9469910088554457

# Outlier analysis
sns.boxplot(wg_cc)
# No outlier is present so there is no need of othere techniques

####################### Model Building #################################
# Simple Linear Regression model
X = wg_cc[['Calories Consumed']]  # Predictor
y = wg_cc['Weight gained (grams)']  # Response
X = sm.add_constant(X)  # Adds a constant term to the predictor
model = sm.OLS(y, X).fit()

# Summary of regression model
print(model.summary())

# R-square value is 0.897 which is greater than the 0.85 
# The Durbin-Watso value is also greater than 1 i.e 2.537
# So our model is ready for furthre process

# Check fitted values(predicted) and residuals
wg_cc['fitted_values'] = model.fittedvalues
wg_cc['residuals'] = model.resid

# Check for predicted values 
predictions = model.predict(X)
predictions
'''
0        4.482599
1      340.607908
2      802.780209
3      298.592245
4      424.639236
5       46.498263
6      -37.533065
7      172.545254
8      550.686227
9     1012.858527
10      75.909227
11     172.545254
12     508.670563
13     634.717554
dtype: float64
'''

# Check for associated errors
print("Sum of residuals:", sum(model.resid))
# Sum of residuals: -2.9132252166164108e-12
# Check for mean of sum of errors is equal to 0
print("Mean of residuals:", np.mean(model.resid))
# Mean of residuals: -2.0808751547260076e-13
# The mean of residual is almost zero 
# Check errors are normally distributed or not
plt.hist(model.resid, bins=10)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()
# Erros are normally , Bi-modal distributed
# Check for RMSE value
rmse = sqrt(mean_squared_error(y, predictions))
print("RMSE:", rmse)
# RMSE: 103.30250194726932

# Interval for 95% confidence
print("Confidence Intervals for the model parameters:")
print(model.conf_int(0.05))
'''
                            0           1
const             -845.426655 -406.078057
Calories Consumed    0.330506    0.509807
'''

# Visualizing model
sns.regplot(x='Calories Consumed', y='Weight gained (grams)', data=wg_cc, color='blue', line_kws={'color': 'green'})
plt.show()
# As the best fit line is passes through the most of the points and also the error
# Is also less as comapared to the previous model 
# From all above  value or correlatio coe.r is 0.94 which is good ,
# function is linear in nature i.e. lm(WG ~ CC), 
# Coe. are significant and coe.of Determination value is R^2 is 0.89 which is also good
# sum of errors is 6.750156e-14 which is almost 0 ans errors are alost normally distributed.
# RMSE value is 103.30 which is nearest to lower range value of weight gain
# so model is best fit