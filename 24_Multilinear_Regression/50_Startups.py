# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:33:57 2024

@author: Atharv Joshi
"""
'''
Problem Statement:
    1.	An analytics company has been tasked with the crucial job of finding
    out what factors affect a startup company and if it will be profitable or 
    not. For this, they have collected some historical data and would like to
    apply multilinear regression to derive brief insights into their data. 
    Predict profit, given different attributes for various startup companies.
    
'''

'''
Business Objective :

Maximize : The profit of the startup companies which will help them to
grow in wise manner.

Minimize : The factor which are affecting the growth of the startups 

Business contraints : the data collected to calculate the profit or not should 
be safe .

'''

######################################### EDA ###########################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import influence_plot

data=pd.read_csv("50_Startups.csv")
data

# Five number summary
data.describe()
'''
           R&D Spend  Administration  Marketing Spend         Profit
count      50.000000       50.000000        50.000000      50.000000
mean    73721.615600   121344.639600    211025.097800  112012.639200
std     45902.256482    28017.802755    122290.310726   40306.180338
min         0.000000    51283.140000         0.000000   14681.400000
25%     39936.370000   103730.875000    129300.132500   90138.902500
50%     73051.080000   122699.795000    212716.240000  107978.190000
75%    101602.800000   144842.180000    299469.085000  139765.977500
max    165349.200000   182645.560000    471784.100000  192261.830000
'''
# The mean and median is very less so we can assume that the datapoints
# are scatter in the median 

# Information of the datasets
data.info()
'''
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   R&D Spend        50 non-null     float64
 1   Administration   50 non-null     float64
 2   Marketing Spend  50 non-null     float64
 3   State            50 non-null     object 
 4   Profit           50 non-null     float64
'''
# Except the State column the all the columns are numeric in range

# Rename some columns for better understand
data1=data.rename({'R&D Spend':'RDS','Administration':'ADMS','Marketing Spend':'MKTS'},axis=1)
data1

# Check for duplicates
data1[data1.duplicated()]
# No duplicates are available
data1.describe()
'''
                 RDS           ADMS           MKTS         Profit
count      50.000000      50.000000      50.000000      50.000000
mean    73721.615600  121344.639600  211025.097800  112012.639200
std     45902.256482   28017.802755  122290.310726   40306.180338
min         0.000000   51283.140000       0.000000   14681.400000
25%     39936.370000  103730.875000  129300.132500   90138.902500
50%     73051.080000  122699.795000  212716.240000  107978.190000
75%    101602.800000  144842.180000  299469.085000  139765.977500
max    165349.200000  182645.560000  471784.100000  192261.830000
'''
# same observation as above summary

# Find the correlation 
data1.drop(['State'],axis=1,inplace=True)
data1.corr()
'''
        RDS      ADMS      MKTS    Profit
RDS     1.000000  0.241955  0.724248  0.972900
ADMS    0.241955  1.000000 -0.032154  0.200717
MKTS    0.724248 -0.032154  1.000000  0.747766
Profit  0.972900  0.200717  0.747766  1.000000
'''
# The datapoints are co-related to each other

# Plot the pairplot
sns.set_style(style='darkgrid')
sns.pairplot(data1)
# The columns shows the co-relation 

# Check for outliers
sns.boxplot(data1)
# No outlier is present in the dataset

# Model Building
model=smf.ols("Profit~RDS+ADMS+MKTS",data=data1).fit()
#  Test the model
# Finding Coefficient parameters
model.params
'''
Intercept    50122.192990
RDS              0.805715
ADMS            -0.026816
MKTS             0.027228
dtype: float64
'''
# Finding tvalues and pvalues
model.tvalues , np.round(model.pvalues,5)
'''
(Intercept     7.626218
 RDS          17.846374
 ADMS         -0.525507
 MKTS          1.655077
 dtype: float64,
 Intercept    0.00000
 RDS          0.00000
 ADMS         0.60176
 MKTS         0.10472
 dtype: float64)
'''
# Finding rsquared values

model.rsquared , model.rsquared_adj  # Model accuracy is 94.75%
# Build SLR and MLR models for insignificant variables 'ADMS' and 'MKTS'
# Also find their tvalues and pvalues
slr_a=smf.ols("Profit~ADMS",data=data1).fit()
slr_a.tvalues , slr_a.pvalues  # ADMS has in-significant pvalue
'''
(Intercept    3.040044
 ADMS         1.419493
 dtype: float64,
 Intercept    0.003824
 ADMS         0.162217
 dtype: float64)
'''
slr_m=smf.ols("Profit~MKTS",data=data1).fit()
slr_m.tvalues , slr_m.pvalues  # MKTS has significant pvalue
'''
(Intercept    7.808356
 MKTS         7.802657
 dtype: float64,
 Intercept    4.294735e-10
 MKTS         4.381073e-10
 dtype: float64)
'''
mlr_am=smf.ols("Profit~ADMS+MKTS",data=data1).fit()
mlr_am.tvalues , mlr_am.pvalues  # varaibles have significant pvalues

# Model Validation
# Residual analysis
# Test for Normality of Residuals (Q-Q Plot) using residual model (model.resid)

sm.qqplot(model.resid,line='q')
plt.title("Normal Q-Q plot of residuals")
plt.show()
# The lines almost covers maximum points

# Checking the influencer
# Leverage Value using High Influence Points : Points beyond Leverage_cutoff value are influencers
influence_plot(model)
plt.show()

