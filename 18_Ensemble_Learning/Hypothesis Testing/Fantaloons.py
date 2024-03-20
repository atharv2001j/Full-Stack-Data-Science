# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:52:08 2024

@author: Atharv Joshi
"""
'''
Fantaloons Sales managers commented that % of males versus 
females walking into the store differ based on day of the 
week. Analyze the data and determine whether there is
evidence at 5 % significance level to support this hypothesis

'''
'''
Business Objective :

Maximize : To equilize the working hours of the male and female in the store

Minimize : The difference between the working hours in Female and male
workers.

Business Contraints : The data of working hours given by the company workers should
be in proper and True

'''

###################################### EDA ##########################
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


Fantaloons=pd.read_csv('Fantaloons.csv')
Fantaloons.head()

# Five number summary
Fantaloons.describe()
'''
Fantaloons=pd.read_csv('Faltoons.csv')
Fantaloons.head()
'''
# Checked whether the data is balanced or imbalanced
Weekdays_value=Fantaloons['Weekdays'].value_counts()
Weekend_value=Fantaloons['Weekend'].value_counts()
print(Weekdays_value,Weekend_value)
'''
Weekdays
Female    287
Male      113
Name: count, dtype: int64 Weekend
Female    233
Male      167
Name: count, dtype: int64
'''
#The given data is imbalanced 
Fantaloons.isnull().sum()
'''
Weekdays    25
Weekend     25
dtype: int64
'''
# This many null values are preent in the dataset
# Drop that rows and columns
Fantaloons.dropna()

# Check the Overall information,datatypes of thedataset
Fantaloons.info()
#we do the cross table 
'''

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 425 entries, 0 to 424
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Weekdays  400 non-null    object
 1   Weekend   400 non-null    object
dtypes: object(2)
memory usage: 6.8+ KB

'''
# Here we can see there is no null value is present in the dataset
# The Datatypes is also a String one

tab = Fantaloons.groupby(['Weekdays', 'Weekend']).size()
count = np.array([280, 520]) #How many Male and Female
nobs = np.array([400, 400]) #Total number of Male and Female are there 

stat, pval = proportions_ztest(count, nobs,alternative='two-sided') 
#Alternative The alternative hypothesis can be either two-sided or one of the one- sided tests
#smaller means that the alternative hypothesis is prop < value
#larger means prop > value.
print('{0:0.3f}'.format(pval))
# two. sided -> means checking for equal proportions of Male and Female 
# p-value < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 

stat, pval = proportions_ztest(count, nobs,alternative='larger')
print('{0:0.3f}'.format(pval))
# p_value is 1.00
# Ha -> Proportions of Male > Proportions of Female
# Ho -> Proportions of Female > Proportions of Male
# p-value >0.05 accept null hypothesis 
# so proportion of Female > proportion of Male

