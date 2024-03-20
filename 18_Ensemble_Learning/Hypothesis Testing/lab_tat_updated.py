# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:57:39 2024

@author: Atharv Joshi
"""
'''
A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT)
 of reports of the laboratories on their preferred list. They collected a random sample and recorded 
 TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch. 

Analyze the data and determine whether there is any difference in average TAT among the 
different laboratories at 5% significance level. 

'''
'''
Business Objective :

Maximize : The Arrangement of the result according to the preffered list

Minimize : The total Turn Around Time of the Reports which is getting from the 
            laboratory
            
business Contraints : The accuracy of the data received from the labpratory

'''
################################### EDA ##########################################
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from PIL import ImageGrab
import matplotlib.pyplot as plt
import seaborn as sns


labtat = pd.read_csv('lab_tat_updated.csv')
labtat.head()

# Five Number Summary
labtat.describe()
'''
       Laboratory_1  Laboratory_2  Laboratory_3  Laboratory_4
count    120.000000    120.000000    120.000000     120.00000
mean     178.257333    178.902917    200.210167     163.68275
std       13.919668     14.957114     15.794801      15.08508
min      140.250000    140.550000    170.580000     124.06000
25%      170.267500    168.025000    190.182500     154.05000
50%      179.055000    178.870000    198.610000     164.42500
75%      187.222500    189.112500    211.197500     172.88250
max      216.390000    217.860000    238.700000     205.18000
'''
# There is slight difference between the all the columns and also median is 
# Not same 

# Check if there is any null value or not
labtat.isnull().sum()
'''
Laboratory_1    0
Laboratory_2    0
Laboratory_3    0
Laboratory_4    0
dtype: int64
'''
# There is no null value in the dataset

# Check the null values
labtat[labtat.duplicated()].shape
#  (0, 4)

labtat.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 120 entries, 0 to 119
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Laboratory_1  120 non-null    float64
 1   Laboratory_2  120 non-null    float64
 2   Laboratory_3  120 non-null    float64
 3   Laboratory_4  120 non-null    float64
dtypes: float64(4)
memory usage: 3.9 KB
'''

# Plotting the data

sns.boxplot(labtat['Laboratory_1'])
# There is outlier in column

sns.boxplot(labtat['Laboratory_2'])
# There is no outlier

sns.boxplot(labtat['Laboratory_3'])
# There is no outlier

sns.boxplot(labtat['Laboratory_4'])
# There is a outlier

# Plot the Bar Graph
plt.subplots(figsize = (9,6))
plt.subplot(221)
plt.hist(labtat['Laboratory_1'])
plt.title('Laboratory 1')
plt.subplot(222)
plt.hist(labtat['Laboratory_2'])
plt.title('Laboratory 2')
plt.subplot(223)
plt.hist(labtat['Laboratory_3'])
plt.title('Laboratory 3')
plt.subplot(224)
plt.hist(labtat['Laboratory_4'])
plt.title('Laboratory 4')
plt.show()

# The Data is Bimodal and Normally distributes 

plt.figure(figsize = (8,6))
labels = ['Lab 1', 'Lab 2','Lab 3', 'Lab 4']
sns.distplot(labtat['Laboratory_1'], kde = True)
sns.distplot(labtat['Laboratory_2'],hist = True)
sns.distplot(labtat['Laboratory_3'],hist = True)
sns.distplot(labtat['Laboratory_4'],hist = True)
plt.legend(labels)

# Here you can visualize the All aspects of the data

# Plotting Q-Q plot to check whether the distribution follows normal distribution or not

sm.qqplot(labtat['Laboratory_1'], line = 'q')
plt.title('Laboratory 1')
sm.qqplot(labtat['Laboratory_2'], line = 'q')
plt.title('Laboratory 2')
sm.qqplot(labtat['Laboratory_3'], line = 'q')
plt.title('Laboratory 3')
sm.qqplot(labtat['Laboratory_4'], line = 'q')
plt.title('Laboratory 4')
plt.show()

# The line is almost covered all the data Points so the datapoints are normally distributed

test_statistic , p_value = stats.f_oneway(labtat.iloc[:,0],labtat.iloc[:,1],labtat.iloc[:,2],labtat.iloc[:,3])
print('p_value =',p_value)
# p_value = 2.143740909435053e-58
# Hence, We fail to reject Null Hypothesis because of lack evidence, there is no significant difference between the samples


