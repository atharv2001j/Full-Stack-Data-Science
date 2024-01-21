# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:02:14 2023

@author: Atharv
"""
import pandas as pd
df=pd.read_csv('ethnic_diversity.csv')
df
################
df.columns
df.shape
df.head
df.tail
######################
df.dtypes
###############
df2=df.convert_dtypes()
df2.dtypes
####################
df3=df.astype(str)
df3.dtypes
####################
df4=df.astype({'Sex':str},errors='ignore')
df4.dtypes
######################
df5=df.astype({'Sex':str},errors='raised')
df5.dtypes
####################
df6=df.rename({'Sex':'SEX'},axis=1)
df6
###################
df.describe()
######################
df.columns
df.columns.values
df.index
df.dtypes
#####################
df['Sex']
######################
df[['Sex','EmpID']]
######################
df7=df.drop([1,3])
df7
####################
df8=df.drop(df.index[2:])
df8
####################
df9=df.drop(['Sex'],axis=1)
df9
####################
df['Sex'][5]
##############
import random
row_label=['r0','r1','r2','r3','r4','r5']
df10=pd.DataFrame(df,[random.choice(row_label) for i in range(310)])
df10
##############
#different ways to access row by index
df.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]    
####################
df10.loc['r1']
df10.loc[['r1','r2','r3']]
#######################
df11=df.query('Zip==1450')
df11
######################
df12=df.query('Zip!=1450')
df12
########################
def add_4(x):
   return x+4
df["Zip"] = df["Zip"].apply(add_4)
df["Zip"]
####################
df['Zip'] = df['Zip'].map(lambda A: A/2.)
print(df)
#####################
def add_2(x):
    return x+2
df['Zip'] = df['Zip'].transform(add_2)
print(df)
######################
#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df13=df['age'].apply(np.square)
df13
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df14=np.square(df['age'])
df14

#groupby() function
df15=df.groupby(['age']).sum()
df15
##########################################3

#group by multiple columns
df16=df.groupby(['Zip','age']).sum()
df16
######################################
#add index to the groupby data
#add row index to the group by result
df17=df.groupby(['Zip','age']).sum().reset_index()
df17
################################



#get the list of all column names from header
columns_header=list(df.columns.values)
print("The column Header:",columns_header)

#####################################
#using list(df) to get the column headers as a list
column_headers=list(df.columns)
column_headers

#using list(df) to get the list of all column names
column_headers=list(df)
column_headers
###################################

#pandas shuffle Dataframe rows
#shuffle the DataFrame rows and return all rows

df18= df.sample(frac=1)
df18
#######################################

#create a new index starting from zero
df19=df.sample(frac=1).reset_index()
df19
#########################

#Drof shuffle index
df20=df.sample(frac=1).reset_index(drop=True)
df20
























