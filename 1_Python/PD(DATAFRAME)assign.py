# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:06:58 2023

@author: Atharv
Introduction to pandas dataframe
"""
import pandas as pd
import random
df=pd.read_csv("bank_data.csv")
#Size of the file
df.shape
#Calculate size
df.size
#Accessing first row
df.head()
#Accessing last five 
df.tail()
#no.of columns
df.columns
#values of columns
df.columns.values
#Accessing one column
df['age']
#accessing more than one column
df[['age','balance']]
#select certain rows and assign it to another dataframe
df2=df[3:] 
df2
#Accessing certain cell from column
df3=df['age'][3]
df3
#Describe dataframe
df.describe()
#Rename pandas dataframe column rename()
df=pd.read_csv("bank_data.csv")
df4=df.rename({'age':'AGE','default':'DEFAULT'},axis=1)
df4
#Drop dataframe columns
df5=df.drop(['age'],axis=1)
df5
df6=df.drop(['default','balance'],axis=1)
df6
#giving name to rows
row_label=['r0','r1','r2','r3','r4','r5']
df8=pd.DataFrame(df,[random.choice(row_label) for i in range(45212)])
df8
#delete row by label
df9=df8.drop('r2')
df9
#select row by label
df10=df8.loc['r5']
df10
#select multiple label rows
df11=df8.loc[['r3','r1']]
df11
##############################################################
#Checking data type 
print(df.dtypes)
#convert all type to best possible types
df12=df.convert_dtypes()
df12.dtypes
#change the data type of all the columns
df13=df.astype(float)
df13.dtypes
#changing data type of particular column
df14=df.astype({'age':float,'default':str})
df14.dtypes
#convert data type for all columns in the list
cols=['age','default','balance']
df[cols]=df[cols].astype(float)
df[cols].dtypes
#Ignore error
df15=df.astype({'age':str},errors='ignore')
#Generate error
df=df.astype({'age':int},errors='raise')
df.dtypes
#Convert feed column into numeric
df['age']=pd.to_numeric(df['age'])
df.dtypes
#delete row by index/position range
df
df15=df.drop(df.index[2:])
df15
#delete row by index
df
df16=df.drop(df.index[[1,3]])
df16
#When you have default index for rows
df=pd.read_csv("bank_data.csv")
df
df17=df.drop(0)
df17
#delete  using range function
df
df18=df.drop(range(0,3))
df18
#to delete multiple row without using index
df
df19=df.drop([1,3])
df19
#

