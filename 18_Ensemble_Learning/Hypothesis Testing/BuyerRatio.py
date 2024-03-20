# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:46:51 2024

@author: Atharv Joshi
"""

'''
of products in four different regions is tabulated for males and females. Find if male-female buyer rations 
are similar across regions.
'''

'''
Business Objective

maximize : The Male female Buyer relation 

Minimize : The Un co-relation betweeen the male and female relation

Business Contraints : The values provided are either correct or incorrect

'''
########################################## EDA ###################################
import scipy.stats as stats
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


buyer = pd.read_csv('BuyerRatio.csv', index_col = 0)
buyer 

table = [[50,142,131,70],
        [435,1523,1356,750]]

# Plot the Data Points
sns.distplot(buyer['East'])
sns.distplot(buyer['West'])
sns.distplot(buyer['North'])
sns.distplot(buyer['South'])
plt.legend(['East','West','North','South'])

# Plot the Boxplot
sns.boxplot(data=[buyer['East'],buyer['West'],buyer['North'],buyer['South']],notch=True)
plt.legend(['East','West','North','South'])
# There is no outlier present in the dataset 

# Applying Chi-Square contingency table to convert observed value into expected value

stat, p, dof, exp = stats.chi2_contingency(buyer) 
print(stat,"\n", p,"\n", dof,"\n", exp)
'''
1.595945538661058 
 0.6603094907091882 
 3 
 [[  42.76531299  146.81287862  131.11756787   72.30424052]
 [ 442.23468701 1518.18712138 1355.88243213  747.69575948]]
'''

stats.chi2_contingency(table) 
# pvalue=0.6603094907091882

observed = np.array([50, 142, 131, 70, 435, 1523, 1356, 750])
expected = np.array([42.76531299,  146.81287862,  131.11756787, 72.30424052, 442.23468701, 1518.18712138, 1355.88243213, 747.69575948])


# Comparing Evidence with Hypothesis
statistics, p_value = stats.chisquare(observed, expected, ddof = 3)
print("Statistics = ",statistics,"\n",'P_Value = ', p_value)

'''
Statistics =  1.5959455390914483 
 P_Value =  0.8095206646905712
'''

# We fail to reject Null Hypothesis because of lack evidence. Therefore, 
# there is no association or dependency between male-female buyers rations 
# and are similar across regions. Hence, Independent samples