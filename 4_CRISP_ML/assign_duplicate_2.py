# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:39:48 2023
#Blue Eyes
@author: Atharv
"""

import pandas as pd
import numpy as np
import seaborn as sns

df=pd.read_csv('OnlineRetail.csv',encoding='unicode_escape')
df

#shape
df.shape

#columns
df.columns

#datatypes
df.dtypes


#######################################################################3
#1. Finding duplicates

df_duplicate=df.duplicated()
df_duplicate
sum(df_duplicate)

# so there are 5268 duplicates are availabel

#drop duplicates

df_drop=df.drop_duplicates()
df_drop.shape

######################################################################3
# 2. Outlier Analysis

sns.boxplot(df)

sns.boxplot(df['Quantity'])

#Lets calculate IQR
IQR=df.Quantity.quantile(0.75)-df.Quantity.quantile(0.25)
IQR

#Calculate upper_limit and lower_limit

lower_limit=df.Quantity.quantile(0.25)-1.5 * IQR
lower_limit

upper_limit=df.Quantity.quantile(0.75) + 1.5 * IQR
upper_limit

######################################################################
# 3. trimming

df_outliers=np.where(df.Quantity>upper_limit,True,np.where(df.Quantity<lower_limit,True,False))
df_outliers

df_trimmed=df.loc[~df_outliers]
df_trimmed.shape

####################################################################33
#Replacement Technique

df_replace=pd.DataFrame(np.where(df.Quantity>upper_limit,upper_limit,np.where(df.Quantity<lower_limit,lower_limit,df.Quantity)))
df_replace

sns.boxplot(df_replace[0])
#No outloier is remain


###################################################################3
