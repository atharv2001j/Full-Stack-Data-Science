# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:53:23 2023

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv('Computer_data.csv')
df
df.dtypes
df2=df.convert_dtypes()
df2.dtypes
######
df3=df.astype(str)
df3.dtypes
############
df.columns
df3=df.rename({'price':'PRICE','speed':'SPEED'},axis=1)
df3
#################
cols=['speed','hd','ram','cd']
df4=df[cols].astype(str)
df4
#####################
df5=df.astype({'speed':'float'},errors='ignore')
df5
###################
df6=df.astype({'speed':'float'},errors='raised')
df6
####################
df.columns
df.columns.values
df.index
df.dtypes
#################
df['speed']
#################
df[['speed','hd']]
################
df7=df.drop([1,3])
df7
##############
df8=df.drop(df.index[[2,4]])
df8
##############
df8=df.drop(df.index[2:])
df8
#################
df9=df.drop(['hd'],axis=1)
df9
###############
df.drop(df.columns[[2]],axis=1,inplace=True)
df
##############
import pandas as pd
import numpy as np
df.columns
df.loc[:,'hd':]
###############
import random
row_label=['r0','r1','r2','r3','r4','r5']
df8=pd.DataFrame(df,[random.choice(row_label) for i in range(405)])
df8
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
df8.loc['r1']
df8.loc[['r1','r2','r3']]
###################
df.dtypes
df9=df.query('hd==80')
df9
#################3
df9=df.query('hd!=80')
df9
################3


#using apply function single column
df=pd.read_csv('Computer_Data.csv')
df
def add_4(x):
    return x+4
df10=df["speed"].apply(add_4)
df10

#apply to multiple columns
def add_10(x):
    return x+10
df11=df[['speed','price']].apply(add_10)
df11

#apply lambda fun to single column
df12=df["speed"].apply(lambda x:x-2)
df12

#using DataFrame.transform()
def add_2(x):
    return x+2
df13=df['speed'].transform(add_2)
df13

#using pandas>dataframe.map() to single column

df14=df['speed'].map(lambda Sales: Sales/2.)
df14

df
def add_4(x):
    return x+4
df15=df["speed"].apply(add_4)
df15


#apply lambda fun to single column
df16=df["speed"].apply(lambda x:x-2)
df16

####################################

#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df17=df['speed'].apply(np.square)
df17
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df18=np.square(df['speed'])
df18

#groupby() function
#for single column
df=pd.read_csv('Computer_Data.csv')
df19=df.groupby(['speed']).sum()
df19
##########################################3

#group by multiple columns
df20=df.groupby(['speed','price']).sum()
df20
######################################
#add index to the groupby data
#add row index to the group by result
df21=df.groupby(['speed','price']).sum().reset_index()
df21
################################

df=pd.read_csv('Computer_Data.csv')
df.columns

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

df22= df.sample(frac=1)
df22
#######################################

#create a new index starting from zero
df23=df.sample(frac=1).reset_index()
df23
#########################

#Drof shuffle index
df24=df.sample(frac=1).reset_index(drop=True)
df24















