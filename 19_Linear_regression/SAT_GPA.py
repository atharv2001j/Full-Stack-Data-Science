# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:04:06 2024

@author: Atharv Joshi
"""
'''
Problem Statement :
    A certain university wants to understand the relationship between 
    students’ SAT scores and their GPA. Build a Simple Linear Regression
    model with GPA as the target variable and record the RMSE and correlation
    coefficient values for different models.

'''
'''
Business Objective :

Maximize : The GPA of the students so the progress of the student will be monitored
and require action plan will be taken

Minimize : The Bad Performance of the studen score

Business Contraints : The correct data to predict the GPA and the SAT score

'''
##################################### EDA ########################################
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf

sat = pd.read_csv('SAT_GPA.csv')
sat.head()

# Five number summary
sat.describe()
'''
       SAT_Scores         GPA
count  200.000000  200.000000
mean   491.810000    2.849500
std    174.893834    0.541076
min    202.000000    2.000000
25%    349.750000    2.400000
50%    480.500000    2.800000
75%    641.500000    3.400000
max    797.000000    3.900000
'''
# There is slightly diffrence in mean and meadian also the S.D is 
# Not good 

# Dataset information
sat.info()
'''
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   SAT_Scores  200 non-null    int64  
 1   GPA         200 non-null    float64
dtypes: float64(1), int64(1)
'''
# The Two columns of the dataset are numeric and also the dataset 
# not contain any null value so no need of null handling

sat.columns
# Index(['SAT_Scores', 'GPA'], dtype='object')

# Visualize the data
# Check for the outliers 
sns.boxplot(sat)
# No outlier is present 

# Cjeck whether the data is normally distributed or not
sns.distplot(sat['SAT_Scores'])
# Data is somwhat bi-modal

sns.distplot(sat['GPA'])
# Data is Bi-modal

# Check the data is co-related or not 
sat.corr()
'''
            SAT_Scores       GPA
SAT_Scores    1.000000  0.293538
GPA           0.293538  1.000000
'''
# The data value is 1 which means the data is co-related with each
# other and their is relation among them

sns.heatmap(sat)
# Heatmap also shows they are co-related to each other

sns.regplot(x=sat['SAT_Scores'],y=sat['GPA'])
# It shows the data is in scatter format 

# Build a model
model=smf.ols("SAT_Scores ~ GPA",data=sat).fit()
# Test the model
# Find the coefficient parameters
model.params
'''
Intercept    221.445677
GPA           94.881321
dtype: float64
'''
# Finding tvalues and pvalues
model.tvalues , model.pvalues

# Finding Rsquared Values
model.rsquared , model.rsquared_adj
# (0.0861647191695093, 0.08154938946834522)
# R-Squared value is 0.086 so the modelis ready to predict
model.predict(sat['GPA'])
'''
0      439.672714
1      449.160846
2      553.530299
3      487.113375
4      468.137110
   
195    515.577771
196    458.648978
197    553.530299
198    591.482827
199    449.160846
'''

model.summary()
# The summary shows the R-squared value is 0.086 which in the range 0 to 1
# from this we cansay that our model will predict 86% correctly
