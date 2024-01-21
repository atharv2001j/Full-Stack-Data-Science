# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:14:21 2023
# desi kalakar
@author: Atharv
"""

#Exercise 1
import pandas as pd
import numpy as np
import seaborn as sns

df=pd.read_csv('Boston.csv')
df
####################################################
#shape
df.shape
#####################################################
#columns 
df.columns
######################################################3
#datatypes
df.dtypes
#Unnamed: 0      int64
#crim          float64
#zn            float64
#indus         float64
#chas            int64
#nox           float64
#rm            float64
#age           float64
#dis           float64
#rad             int64
#tax             int64
#ptratio       float64
#black         float64
#lstat         float64
#medv          float64
##################################################################3
#five number summary
df.describe()

###################################################################
# mean
df.mean()

###############################################################3
#Pairplot
sns.pairplot(df)

######################################################################
# ploting histplot
sns.histplot(df['black'],kde=True)
#data is left-skew and the not normallly distributed
sns.histplot(df,kde=True)
#The data is showing the skewness 

# ploting histplot
sns.histplot(df['tax'],kde=True)
#data is bi-modal ormallly distributed



############################################################3
# boxplot
sns.boxplot(df)
#There is an outlier for the column black,Crim,zn,istate and also the columns like
#age tax having no outlier in there columns but they posesses skewness

##################################################################

df.median()

df.mean()

df.std()
# as the standard deviation of the tax  and black are more so the datapoints
# of these two columns are deviated from the median 
########################################################################
#1. Finding duplicates

df_duplicate=df.duplicated()
df_duplicate
sum(df_duplicate)

#No duplicates are found

#######################################################################
#2. Outlier Analysis

sns.boxplot(df)

#Perform  operation on black column
sns.boxplot(df['black'])

#let us find the  IQR
IQR=df.black.quantile(0.75)-df.black.quantile(0.25)
IQR

#Calculate lower and upper limit
lower_limit=df.black.quantile(0.25)- 1.5*IQR
lower_limit

upper_limit=df.black.quantile(0.75)+1.5 * IQR
upper_limit



######################################################################
# 3. Trimming
outlier_df=np.where(df.black>upper_limit,True,np.where(df.black<lower_limit,True,False))
outlier_df

df_trimmed=df.loc[~outlier_df]
df_trimmed.shape

########################################################################
# 4. replacement / Winsorization

df_replacement=pd.DataFrame(np.where(df.black>upper_limit,upper_limit,np.where(df.black<lower_limit,lower_limit,df.black)))
df_replacement

sns.boxplot(df_replacement[0])

#########################################################################
# 5. Winerization

from feature_engine.outliers import Winsorizer

winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['black'])

df_t=winsor.fit_transform(df[['black']])
sns.boxplot(df['black'])

sns.boxplot(df_t['black'])


