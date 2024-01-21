# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:05:19 2023

@author: Atharv
"""
import pandas as pd
import random
df=pd.read_csv("boston_data.csv")
df
#display first 5 rows
df.head()
#display last 5 rows
df.tail()
#size
df.shape
df.size
df.columns
#Accessing one column
df['crim']
#Accessing multiple columns
df[['crim','zn','indus']]
#select certain row and assign to new dataframe
df1=df[3:]
df1
#accessing certain cell from column
df['crim'][3]
#Describe 
df.describe()
#rename pandas dataframe column
df=pd.read_csv("boston_data.csv")
df2=df.rename({'crim':'CRIM','zn':'ZN'},axis=1)
df2
#drop dataframe columns
df3=df.drop(['crim'],axis=1)
df3
#drop multiple columns
df4=df.drop(['crim','zn'],axis=1)
df4
#Checking data type
df.dtypes
#converting it into all possible datatitypes
df5=df.convert_dtypes()
df5.dtypes
#Change all colums to same data type
df6=df.astype(str)
df6.dtypes
#Change datatype of one or more columns
df7=df.astype({'crim':int,'zn':str})
df7.dtypes
#convert datatype for all columns in a list
col=['crim','zn','indus','chas']
df[col]=df[col].astype(str)
df[col].dtypes
#ignore error
df=df.astype({'crim':float},errors='ignore')
#generate error
df=df.astype({'crim':int},errors='raise')
#convert feed column to numeric
df['crim']=pd.to_numeric(df['crim'])
df.dtypes
#giving labels to the row
row_label=['r0','r1','r2','r3','r4','r5']
df8=pd.DataFrame(df,[random.choice(row_label) for i in range(405)])
df8
#delete row by label
df9=df8.drop(['r0','r1'])
df9
#delete row by index
df10=df.drop(df.index[[1,3]])
df10
#delete row by index range
df11=df.drop(df.index[3:])
df11
#when you have default indexes for rows
df12=df.drop(0)
df12
#range() function to delete rows
df13=df.drop(range(0,210))
df13
#To delete muliple rows
df14=df.drop([1,3])
df14
#delete column by name
df15=df.drop(['crim'],axis=1)
df15
#Explicitly using name labels
df16=df.drop(labels=['crim'],axis=1)
df16
#using columns\
df17=df.drop(columns=['crim'],axis=1)
df17
#Drop column by index
df18=df.drop(df.columns[2],axis=1)#it will delete indus
df18
#Using inplace true 
df.drop(df.columns[1],axis=1,inplace=True)
df
#Drop two or more columns by label name
df19=df.drop(['crim','indus'],axis=1)
df19
#drop two or more columns by index
df20=df.drop(df.columns[[0,1]],axis=1)
df20
#drop column from the list of column
df=pd.read_csv("boston_data.csv")
lcol=['crim','indus','chas','nox']
df21=df.drop(lcol,axis=1)
df21
#different ways to access row by index
df.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]            #select alternate row
#different ways to access rows by label
row_label=['r0','r1','r2','r3','r4','r5']
df22=pd.DataFrame(df,[random.choice(row_label) for i in range(405)])
df22
df22.loc['r1']
df22.loc[['r1','r2','r3']]
#here below two are not work because we use random function
df22.loc['r1':'r4']
df22.loc['r0':'r4':2] #alernatte row
#Select multiple columns 
df23=df.loc[:,['crim','indus']]
df23
#Select column between two column
df24=df.loc[:,'crim':'indus']
df24
#Select columns by range
df25=df.loc[:,'indus':]
df25

df26=df.loc[:,:'chas']
df26
#To display all rows containing paricular value query()
df27=df.query("crim==0.01501")
df27
#To display all rows not containing paricular value query()
df28=df.query("crim!=0.01501")
df28
#select multiple columns
df29=df[['crim','indus']]
df29
