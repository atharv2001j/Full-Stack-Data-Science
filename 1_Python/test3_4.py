# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:28:20 2023

@author: Atharv Joshi
"""
import pandas as pd
df=pd.read_csv('Diabetes.csv')
df
######################3
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
######################
df4=df.astype({'Number_of_times_pregnant':str},errors='ignore')
df4.dtypes
###########################
df5=df.astype({'Number_of_times_pregnant':int},errors='raised')
df5
###########################
df6=df.rename({'Number_of_times_pregnant':'Pregnant_count'},axis=1)
df6
#########################
df7=df.rename({'Number_of_times_pregnant':'Pregnant_count'},axis='columns')
df7
########################
df.describe()
######################
df.columns
df.columns.values
df.index
df.dtypes
##########################
df.dtypes
df[' Body mass index']
#############################
df[[' Body mass index',' Class variable']]
##############################
df7=df.drop([1,3])
df7
####################
df8=df.drop(df.index[2:])
df8
#################
df9=df.drop([' Number_of_times_pregnant'],axis=1)
df9
################
df[' Number_of_times_pregnant'][1]
##################
df.drop(df.columns[[1]],axis=1,inplace=True)
df
####################
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
#######################
df.dtypes
df10=df.query('Number_of_times_pregnant==6')
df10
#################3
df11=df.query('Number_of_times_pregnant!=1')
df11
#########################
def add_4(x):
   return x+4
df[" Number_of_times_pregnant"] = df[" Number_of_times_pregnant"].apply(add_4)
df[" Number_of_times_pregnant"]
##############################
df[' Number_of_times_pregnant'] = df[' Number_of_times_pregnant'].map(lambda A: A/2.)
print(df)
#############################
def add_2(x):
    return x+2
df[' Number_of_times_pregnant'] = df[' Number_of_times_pregnant'].transform(add_2)
print(df)
################################
#apply lambda fun to single column
df3=df[" Number_of_times_pregnant"].apply(lambda x:x-2)
df3

####################################

#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df4=df[' Number_of_times_pregnant'].apply(np.square)
df4
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df5=np.square(df[' Number_of_times_pregnant'])
df5

#groupby() function
df6=df.groupby([' Number_of_times_pregnant']).sum()
df6
##########################################3

#group by multiple columns
df7=df.groupby([' Number_of_times_pregnant',' Plasma_glucose_concentration']).sum()
df7
######################################
#add index to the groupby data
#add row index to the group by result
df7=df.groupby([' Number_of_times_pregnant',' Plasma_glucose_concentration']).sum().reset_index()
df7
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

df10= df.sample(frac=1)
df10
#######################################

#create a new index starting from zero
df11=df.sample(frac=1).reset_index()
df11
#########################

#Drof shuffle index
df12=df.sample(frac=1).reset_index(drop=True)
df12




