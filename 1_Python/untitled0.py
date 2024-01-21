# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:31:03 2023

@author: Atharv
"""
import pandas as pd

df=pd.read_csv('ethnic diversity.csv')

df


#check shape
df.shape

#check columns
df.columns

# check  datatype
df.dtypes

# pairplot
import seaborn as sns

sns.pairplot(df)

# Five nummber summary
df.describe()

# finding null value
df.isna()
