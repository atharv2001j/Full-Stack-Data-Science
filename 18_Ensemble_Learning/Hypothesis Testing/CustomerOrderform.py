# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:01:40 2024

@author: Atharv Joshi
"""

'''
Telecall uses 4 centers around the globe to process customer order forms. 
They audit a certain % of the customer order forms. Any error in order form 
renders it defective and must be reworked before processing. 
The manager wants to check whether the defective % varies by center. 
Please analyze the data at 5% significance level and help the manager draw 
appropriate inferences.

'''

'''
Business Objective :
    
Maximize : The analysis of the defective form and providing the best service,
on time service to the customer

Minimize : The Count of the errror forms should be minimize so the data
will be process further

Business contraints : The accuracy of the data fill by the customer and te
security of the data

'''
################################# EDA ###################################

import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from PIL import ImageGrab
import matplotlib.pyplot as plt
import seaborn as sns

centers = pd.read_csv('CustomerOrderForm.csv')
centers.head(10)

# Five Number Summary
centers.describe()
'''

       Phillippines   Indonesia       Malta       India
count           300         300         300         300
unique            2           2           2           2
top      Error Free  Error Free  Error Free  Error Free
freq            271         267         269         280

'''
# Checking for the Null values
centers.isnull().sum()
'''
Phillippines    15
Indonesia       15
Malta           15
India           15
dtype: int64
'''
# There is null value present in each column
centers.dropna()

centers.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 315 entries, 0 to 314
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Phillippines  300 non-null    object
 1   Indonesia     300 non-null    object
 2   Malta         300 non-null    object
 3   India         300 non-null    object
dtypes: object(4)
memory usage: 10.0+ KB
'''
# So there is no null value is present
# Check the data is balanced or imbalanced
print(centers['Phillippines'].value_counts(),'\n',centers['Indonesia'].value_counts(),'\n',centers['Malta'].value_counts(),'\n',centers['India'].value_counts())

# Calculate the Contingeny table
contingency_table = [[271,267,269,280],
                    [29,33,31,20]]
print(contingency_table)

# Calculating Expected Values for Observed data
stat, p, df, exp = stats.chi2_contingency(contingency_table)
print("Statistics = ",stat,"\n",'P_Value = ', p,'\n', 'degree of freedom =', df,'\n', 'Expected Values = ', exp)

'''
Statistics =  3.858960685820355 
 P_Value =  0.2771020991233135 
 degree of freedom = 3 
 Expected Values =  [[271.75 271.75 271.75 271.75]
 [ 28.25  28.25  28.25  28.25]]
'''
# Defining Expected values and observed values
observed = np.array([271, 267, 269, 280, 29, 33, 31, 20])
expected = np.array([271.75, 271.75, 271.75, 271.75, 28.25, 28.25, 28.25, 28.25])

# Compare Evidences with Hypothesis using t-statictic

test_statistic , p_value = stats.chisquare(observed, expected, ddof = df)
print("Test Statistic = ",test_statistic,'\n', 'p_value =',p_value)

# Test Statistic =  3.858960685820355 
# p_value = 0.4254298144535761

# We fail to reject Null Hypothesis because of lack of evidence.