# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:34:04 2024

@author: Atharv Joshi 
"""
'''
Problem Statement :
    A logistics company recorded the time taken for delivery and the time taken
    for the sorting of the items for delivery. Build a Simple Linear Regression 
    model to find the relationship between delivery time and sorting time with 
    delivery time as the target variable. Apply necessary transformations and 
    record the RMSE and correlation coefficient values for different models.

'''
'''
Business Objective :

Maximize : The number of deliveries by reducing the time for packaging . For that 
we have to analyze the relationship between the delicvery time and sorting time

Minimize : The delivery time and the sorting time

Business Contraints : The number of workers required to increase the number od delivery
and also the buget for this also important.

'''

##################################### EDA #####################################
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf

delivery=pd.read_csv('delivery_time.csv')
delivery.head()

# Five Number summary
delivery.describe()
'''
       delivery_time  sorting_time
count      21.000000     21.000000
mean       16.790952      6.190476
std         5.074901      2.542028
min         8.000000      2.000000
25%        13.500000      4.000000
50%        17.830000      6.000000
75%        19.750000      8.000000
max        29.000000     10.000000
'''
# The mean and median are showing some difference so we can say that there is relation
# in between them .

# Check the information of the dataset
delivery.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21 entries, 0 to 20
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Delivery Time  21 non-null     float64
 1   Sorting Time   21 non-null     int64  
dtypes: float64(1), int64(1)
memory usage: 468.0 bytes
'''
# All the data are numeric in nature as well as the there is no null value present 
# in the dataset

# Visualize the datapoints
# Check for the Outliers
sns.boxplot(delivery)
# No outlier is present in the dataset

sns.distplot(delivery['Delivery Time'])
# The data is Normally distributed

sns.distplot(delivery['Sorting Time'])
# The data is normally distributted

# Renaming Columns
delivery=delivery.rename({'Delivery Time':'delivery_time', 'Sorting Time':'sorting_time'},axis=1)
delivery

delivery.corr()
'''
               delivery_time  sorting_time
delivery_time       1.000000      0.825997
sorting_time        0.825997      1.000000

'''
# The Data are co-related toeach other for more we will plot the heatmap
sns.heatmap(delivery)
# As the heatmap also shows that the datapoints are co-relatedto each other

sns.regplot(x=delivery['sorting_time'],y=delivery['delivery_time'])
# As we see that the datapoints are passes through the line so we can sure that the
# the datapoints are co-related to each other 
# So we can move to build our model

model=smf.ols("delivery_time~sorting_time",data=delivery).fit()
# Test the model
# Find the coefficient parameters
model.params
'''
Intercept       6.582734
sorting_time    1.649020
dtype: float64
'''
# Finding tvalues and pvalues
model.tvalues , model.pvalues

# Finding Rsquared Values
model.rsquared , model.rsquared_adj
#  (0.6822714748417231, 0.6655489208860244)
# The modeel rsqaured value is 0.6822 which is less than the 0.85 
# So our model can predict the 68% datapoints correctly

# Manual prediction for say sorting time 5
delivery_time = (6.582734) + (1.649020)*(5)
delivery_time
#  14.827834

# Automatic Prediction for say sorting time 5, 8
new_data=pd.Series([5,8])
new_data
'''
0    5
1    8
'''

data_pred=pd.DataFrame(new_data,columns=['sorting_time'])
data_pred
# The preducted data by model and the automatic predicted data are same
model.predict(data_pred)
'''
0    14.827833
1    19.774893
'''
# The manually calculated delivery time and the delivery time predicted by our model is
# same so wecan say that the model isfit for the prediction

