# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:25:23 2024

@author: Atharv Joshi 
"""

'''
Problem Statement : A F&B manager wants to determine whether there is any 
significant difference in the diameter of the cutlet between two units. 
A randomly selected sample of cutlets was collected from both units and 
measured? Analyze the data and draw inferences at 5% significance level. 
Please state the assumptions and tests that you carried out to check validity
 of the assumptions. 
'''
'''
Business Objective :
    
maximize : The exact prediction and measurement of the diameter of the cutlets between
            two unnits
            
Minimize : The False measures of the diameter and the wrong prediction.

Business Contraints : The accuracy of the Data Provided to us as well as the 
                    required parameters to measure the diameter
                    
'''
#################################### EDA #########################################
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from PIL import ImageGrab
import matplotlib.pyplot as plt
import seaborn as sns

# We are going to conduct a 2 tailed t-Test on 2 Independent samples with Numerical Data
# We need to check whether the mean of both samples are different and
# Is there any significance difference between the two samples?

cutlets = pd.read_csv('Cutlets.csv')
cutlets.head(10)

# The Five Number summary
cutlets.describe()
'''
          Unit A     Unit B
count  35.000000  35.000000
mean    7.019091   6.964297
std     0.288408   0.343401
min     6.437600   6.038000
25%     6.831500   6.753600
50%     6.943800   6.939900
75%     7.280550   7.195000
max     7.516900   7.545900
'''
# The mean of both samples are slightly diffrenet and also there is slight change in the median
# also so we will check if there is any duplicate or null values 

cutlets.isnull().sum()
'''
Unit A    16
Unit B    16
dtype: int64
'''
# Drop rows with missing values
cutlets.dropna(inplace=True)
# As we see there are 16 null values in both the samples
cutlets[cutlets.duplicated()].shape
# (0, 2)
cutlets[cutlets.duplicated()]

# Check the overall information about the datasets
cutlets.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 51 entries, 0 to 50
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Unit A  35 non-null     float64
 1   Unit B  35 non-null     float64
dtypes: float64(2)
memory usage: 948.0 bytes
'''
# As we will remove all null values and present there is no null value in the 
# Dataset

# Plot the Unit A and Unit B for hecking an outlier
sns.boxplot(cutlets['Unit A'])
# No outlier is present in the column

sns.boxplot(cutlets['Unit B'])
# One outlier is present in the Columns

# Plot the bar graph to know about the skewness and nature of the data
plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.hist(cutlets['Unit A'], bins = 15)
plt.title('Unit A')
plt.subplot(122)
plt.hist(cutlets['Unit B'], bins = 15)
plt.title('Unit B')
plt.show()

# The data shows somewhat skewnwess and there is an outlier

plt.figure(figsize = (8,6))
labels = ['Unit A', 'Unit B']
sns.distplot(cutlets['Unit A'], kde = True)
sns.distplot(cutlets['Unit B'],hist = True)
plt.legend(labels)

# Here it will clearly shows that the data is left skewed

# Plotting Q-Q plot to check whether the distribution follows normal distribution or not

sm.qqplot(cutlets["Unit A"], line = 'q')
plt.title('Unit A')
sm.qqplot(cutlets["Unit B"], line = 'q')
plt.title('Unit B')
plt.show()

# The data somewhat is normally distributted and the the line almost crosses the
# maximum points

# Compare Evidences with Hypothesis using t-statistics
statistic , p_value = stats.ttest_ind(cutlets['Unit A'],cutlets['Unit B'], alternative = 'two-sided')
print('p_value=',p_value)

# p_value= 0.4722394724599501

# The P-value is below 0.5 so we will failed to reject the NULL Hypothesis 
# because of lack of evidence, there is no significant difference between the two samples
