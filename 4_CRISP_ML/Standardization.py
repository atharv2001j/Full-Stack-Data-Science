# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:21:28 2023

@author:Atharv Joshi
"""
# 12 Standardization

# we convert the numerical value in he range 0 and 1 called Normaliztion and Normalization
# it is used to contribute alll the features equally in output

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

d=pd.read_csv('mtcars.csv')
d.describe()

a=d.describe()

# initialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(a)
dataset=pd.DataFrame(df)
res=dataset.describe()
# in the resvariable we will see that the mean value is almost value 
#Standard deviation is zero
######################################################################
#Example 2

d=pd.read_csv('Seeds_data.csv')
a=d.describe()

# initialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(a)
dataset=pd.DataFrame(df)
res=dataset.describe()

# in the resvariable we will see that the mean value is almost value 
# and standard deviation is zero 

###################################################################
#13. Normalization

ethnic=pd.read_csv('ethnic diversity.csv')

ethnic.describe()

ethnic.columns

ethnic.drop(['Employee_Name','EmpID','Zip'],axis=1,inplace=True)

a1=ethnic.describe()
#here in a1 dataframe we see that thhere is huge difference beween min and max so
# we will normalize it
# so first we will convert the non-numeric data to numeric data
ethnic=pd.get_dummies(ethnic,drop_first=True)

#Normalization Function
def norm_function(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_function(ethnic)
b=df_norm.describe()

#we will see that the dimension of the b dataframe ids 8,81 
# earlier it was 8,11 because it contain non-numeric dataframe

df_norm.shape

























