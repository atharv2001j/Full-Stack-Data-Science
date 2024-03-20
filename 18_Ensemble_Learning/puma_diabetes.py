# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:23:09 2024

@author: Atharv Joshi
"""

import pandas as pd
df=pd.read_csv('puma_diabetes.csv')
df.head()
df.isnull().sum()
# No null value is present

df.describe()
'''
      Pregnancies     Glucose  ...         Age     Outcome
count   768.000000  768.000000  ...  768.000000  768.000000
mean      3.845052  120.894531  ...   33.240885    0.348958
std       3.369578   31.972618  ...   11.760232    0.476951
min       0.000000    0.000000  ...   21.000000    0.000000
25%       1.000000   99.000000  ...   24.000000    0.000000
50%       3.000000  117.000000  ...   29.000000    0.000000
75%       6.000000  140.250000  ...   41.000000    1.000000
max      17.000000  199.000000  ...   81.000000    1.000000
'''
# The data somehow not normalize as the difference between the mean and median
# is vary

############################################################################
df.Outcome.value_counts()
'''
0    500
1    268
Name: Outcome, dtype: int64
'''
# there is slightly imbalance in our dataset .But since it is not major so not worry about it

##########################################################################
# Train test split
X=df.drop('Outcome',axis='columns')
y=df.Outcome

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
X_scaled[:3]

# In order to make our datasetbalanced while splittting ,you can use stratify

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,stratify=y,random_state=42)

X_train.shape
X_test.shape
y_train.value_counts()
